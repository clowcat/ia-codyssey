
# B1-1: 시스템 관제 자동화 스크립트 개발 리포트

## 1. 프로젝트 개요

본 프로젝트는 리눅스 서버의 보안을 강화하고, 시스템 리소스(CPU, 메모리, 디스크) 및 애플리케이션의 상태를 실시간으로 관제하여 로그로 기록하는 **자동화 시스템 구축**을 목표로 합니다.

## 2. 시스템 보안 및 네트워크 설정

안전한 서버 운영을 위해 외부 접근을 최소화하고 보안 정책을 수립하였습니다.

### 2.1. SSH 설정 변경

* **포트 변경**: 기본 22번 포트에서 **20022**번 포트로 변경하여 무작위 대입 공격 리스크를 감소시켰습니다.
* **Root 접속 차단**: `PermitRootLogin no` 설정을 통해 Root 계정으로의 직접 원격 접속을 금지하였습니다.
* **검증 명령어**: `ss -tulnp | grep 20022`

![Dockerfile Screenshot](https://github.com/clowcat/ia-codyssey/blob/main/B1-1/screenshot/ssh_config_after.png)

<img src="https://github.com/clowcat/ia-codyssey/blob/main/B1-1/screenshot/ssh_config_after.png" width="300">

```bash
cyanc01125000@c4r6s7 ia-codyssey % docker rm -f ssh-test 
cyanc01125000@c4r6s7 ia-codyssey % docker run -d --privileged -p 20022:20022 --name ssh-test ubuntu:22.04 sleep infinity
cyanc01125000@c4r6s7 ia-codyssey % docker exec -it ssh-test bash
cyanc01125000@c4r6s7 ia-codyssey % apt install -y vim
root@02032ddf5c6f:/# apt update
root@02032ddf5c6f:/# apt install -y vim
root@02032ddf5c6f:/# apt update && apt install -y openssh-server vim sudo
root@02032ddf5c6f:/# apt install -y iproute2
root@02032ddf5c6f:/# vi /etc/ssh/sshd_config
root@02032ddf5c6f:/# service ssh start


root@c836e7b852cc:/# ss -tulnp | grep 20022      
tcp   LISTEN 0      128          0.0.0.0:20022      0.0.0.0:*    users:(("sshd",pid=4728,fd=3))
tcp   LISTEN 0      128             [::]:20022         [::]:*    users:(("sshd",pid=4728,fd=4))
```

### 2.2. 방화벽(UFW) 정책

* **기본 정책**: 모든 인바운드 트래픽 차단 (Default Deny)
* **허용 포트**:
* `20022/tcp` (SSH)
* `15034/tcp` (Application)

* UFW 설치
```bash
docker run -d --privileged -p 20022:20022 --name ssh-test ubuntu:22.04 sleep infinity
docker exec -it ssh-test bash
apt update && apt install -y ufw
```

* UFW 활성화 및 20022/tcp, 15034/tcp 만 허용
```bash
ufw allow 20022/tcp
ufw allow 15034/tcp
ufw enable
```


* **검증 결과**:
```bash
# ufw status 결과 예시
Status: active

To                         Action      From
--                         ------      ----
20022/tcp                  ALLOW       Anywhere                  
15034/tcp                  ALLOW       Anywhere                  
20022/tcp (v6)             ALLOW       Anywhere (v6)             
15034/tcp (v6)             ALLOW       Anywhere (v6) 

```



## 3. 계정 및 권한 관리 (RBAC & ACL)

직무 분리(SoD)를 위해 역할 기반 계정을 생성하고 파일 시스템 접근 권한을 세분화하였습니다.

### 3.1. 계정 및 그룹 구성

| 구분 | 이름 | 소속 그룹 | 역할 |
| --- | --- | --- | --- |
| **운영 계정** | `agent-admin` | `agent-core` | 시스템 관리 및 크론 등록 |
| **개발 계정** | `agent-dev` | `agent-common` | 앱 배포 및 스크립트 수정 |
| **테스트 계정** | `agent-test` | `agent-common` | QA 및 관제 결과 확인 |

### 3.2. 디렉토리 보안 및 ACL 설정

* **보안 디렉토리**: `/var/log/agent-app`, `$AGENT_HOME/api_keys`
* `agent-core` 그룹에만 읽기/쓰기 권한 부여 (`770`)


* **공유 디렉토리**: `$AGENT_HOME/upload_files`
* `agent-common` 그룹 전체에 공유 권한 부여


* **검증 명령어**: `getfacl [디렉토리 경로]`

## 4. 애플리케이션 실행 환경

환경 변수를 통해 실행 환경을 표준화하고 앱의 안정성을 확보하였습니다.

| 환경 변수명 | 설정값 | 용도 |
| --- | --- | --- |
| `AGENT_HOME` | `/home/agent-admin/app` | 애플리케이션 루트 경로 |
| `AGENT_PORT` | `15034` | 서비스 리슨 포트 |
| `AGENT_KEY_PATH` | `$AGENT_HOME/api_keys/t_secret.key` | 인증 키 파일 경로 |

## 5. 시스템 관제 스크립트 (`monitor.sh`)

애플리케이션과 시스템의 상태를 주기적으로 수집하는 Bash 스크립트를 개발하였습니다.

### 5.1. 주요 기능

1. **Health Check**: 프로세스 생존(PID) 및 포트(15034) 활성 상태 확인
2. **리소스 모니터링**: CPU, 메모리, 디스크 사용률 수집
3. **임계값 경고**: CPU > 20%, MEM > 10%, DISK > 80% 발생 시 로그에 `[WARNING]` 태그 삽입
4. **로그 관리**: 10MB 초과 시 로그 로테이션 수행 (비우기/압축)

### 5.2. 스크립트 권한

* **소유자**: `agent-dev` (수정 가능)
* **그룹**: `agent-core` (실행 가능)
* **권한**: `750` (`-rwxr-x---`)

## 6. 자동화 및 모니터링 결과

### 6.1. Crontab 설정

* **주기**: 매 분(1분)마다 실행
* **설정 내용**: `* * * * * /home/agent-admin/app/monitor.sh`

### 6.2. 관제 로그 출력 예시 (`monitor.log`)

```text
[2026-05-11 14:01:01] INFO: PID:48291 CPU:15.2% MEM:8.1% DISK:23%
[2026-05-11 14:02:01] INFO: PID:48291 CPU:25.3% MEM:12.4% DISK:23% [CPU Warning: 25.3%] [MEM Warning: 12.4%]

```

## 7. 고찰 및 결론

* **보안 강화**: SSH 포트 변경과 방화벽 정책을 통해 공격 표면을 획기적으로 줄였습니다.
* **가시성 확보**: 쉘 스크립트 자동화를 통해 시스템 장애 발생 시 로그를 통한 사후 추적성(Audit Trail)을 확보하였습니다.
* **향후 과제**: 로그 파일의 단순 비우기 방식에서 일자별 압축 저장 방식으로 고도화가 필요합니다.

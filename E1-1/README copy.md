## 1) 실행 환경
- OS: macOS 15.7.4
- Shell: zsh 5.9
- Docker: 28.5.2
- Git: 2.53.0

## 2) 수행 체크리스트
- [o] 터미널 기본 조작 및 폴더 구성
- [o] 권한 변경 실습
- [o] Docker 설치/점검
- [o] hello-world 실행
- [o] Dockerfile 빌드/실행
- [o] 포트 매핑 접속(2회)
- [o] 바인드 마운트 반영
- [o] 볼륨 영속성
- [o] Git 설정 + VSCode GitHub 연동

## 2-1) 보너스 과제 체크리스트
- [o] Docker Compose 기초
- [o] Docker Compose 멀티 컨테이너
- [o] Compose 운영 명령어 습득
- [o] 환경변수 활용
- [o] GitHub SSH 키 설정

 ## 3) 수행 로그(발췌)
- 터미널 기본 조작 및 폴더 구성
cyanc01125000@c4r4s3 ~ % pwd
/Users/cyanc01125000
cyanc01125000@c4r4s3 ~ % ls -al
total 24
drwxr-x---+ 21 cyanc01125000  cyanc01125000   672 Apr  3 19:27 .
drwxr-xr-x  10 root           admin           320 Apr  3 18:25 ..
-r--------   1 cyanc01125000  cyanc01125000     7 Apr  3 18:25 .CFUserTextEncoding
drwx------   3 cyanc01125000  cyanc01125000    96 Apr  3 18:36 .copilot
drwxr-xr-x   8 cyanc01125000  cyanc01125000   256 Apr  3 18:57 .docker
drwxr-xr-x  10 cyanc01125000  cyanc01125000   320 Apr  3 18:26 .orbstack
drwxr-xr-x   3 cyanc01125000  cyanc01125000    96 Apr  3 18:26 .ssh
drwx------+  4 cyanc01125000  cyanc01125000   128 Apr  3 19:14 .Trash
-rw-------   1 cyanc01125000  cyanc01125000  1378 Apr  3 19:27 .viminfo
drwxr-xr-x   5 cyanc01125000  cyanc01125000   160 Apr  3 18:33 .vscode
-rw-------   1 cyanc01125000  cyanc01125000    42 Apr  3 18:41 .zsh_history
drwxr-xr-x   4 cyanc01125000  cyanc01125000   128 Apr  3 18:43 codyssey
drwx------+  4 cyanc01125000  cyanc01125000   128 Apr  3 19:14 Desktop
drwx------+  3 cyanc01125000  cyanc01125000    96 Apr  3 18:25 Documents
drwx------+  3 cyanc01125000  cyanc01125000    96 Apr  3 18:25 Downloads
drwx------@ 78 cyanc01125000  cyanc01125000  2496 Apr  3 19:16 Library
drwx------   3 cyanc01125000  cyanc01125000    96 Apr  3 18:25 Movies
drwx------+  3 cyanc01125000  cyanc01125000    96 Apr  3 18:25 Music
drwx------   4 cyanc01125000  cyanc01125000   160 Apr  3 18:26 OrbStack
drwx------+  4 cyanc01125000  cyanc01125000   128 Apr  3 18:25 Pictures
drwxr-xr-x+  4 cyanc01125000  cyanc01125000   128 Apr  3 18:25 Public
cyanc01125000@c4r4s3 ~ % 
cyanc01125000@c4r4s3 ~ % mkdir mi1     
cyanc01125000@c4r4s3 ~ % cd mi1
cyanc01125000@c4r4s3 mi1 % touch sample.txt
cyanc01125000@c4r4s3 mi1 % echo "Hello, Docker
dquote> " >sample.txt
cyanc01125000@c4r4s3 mi1 % cat sample.txt 
Hello, Docker

cyanc01125000@c4r4s3 mi1 % cp sample.txt ../    
cyanc01125000@c4r4s3 mi1 % cd ..
cyanc01125000@c4r4s3 ~ % ls -l
total 8
drwxr-xr-x   4 cyanc01125000  cyanc01125000   128 Apr  3 18:43 codyssey
drwx------+  4 cyanc01125000  cyanc01125000   128 Apr  3 19:14 Desktop
drwx------+  3 cyanc01125000  cyanc01125000    96 Apr  3 18:25 Documents
drwx------+  3 cyanc01125000  cyanc01125000    96 Apr  3 18:25 Downloads
drwx------@ 78 cyanc01125000  cyanc01125000  2496 Apr  3 19:16 Library
drwxr-xr-x   3 cyanc01125000  cyanc01125000    96 Apr  3 20:10 mi1
drwx------   3 cyanc01125000  cyanc01125000    96 Apr  3 18:25 Movies
drwx------+  3 cyanc01125000  cyanc01125000    96 Apr  3 18:25 Music
drwx------   4 cyanc01125000  cyanc01125000   160 Apr  3 18:26 OrbStack
drwx------+  4 cyanc01125000  cyanc01125000   128 Apr  3 18:25 Pictures
drwxr-xr-x+  4 cyanc01125000  cyanc01125000   128 Apr  3 18:25 Public
-rw-r--r--   1 cyanc01125000  cyanc01125000    15 Apr  3 20:12 sample.txt
cyanc01125000@c4r4s3 ~ % cd mi1
cyanc01125000@c4r4s3 mi1 % cd ..
cyanc01125000@c4r4s3 ~ % rename sample.txt sample_copy.txt
zsh: command not found: rename
cyanc01125000@c4r4s3 ~ % mv -i sample.txt sample_copy.txt
cyanc01125000@c4r4s3 ~ % ls -l
total 8
drwxr-xr-x   4 cyanc01125000  cyanc01125000   128 Apr  3 18:43 codyssey
drwx------+  4 cyanc01125000  cyanc01125000   128 Apr  3 19:14 Desktop
drwx------+  3 cyanc01125000  cyanc01125000    96 Apr  3 18:25 Documents
drwx------+  3 cyanc01125000  cyanc01125000    96 Apr  3 18:25 Downloads
drwx------@ 78 cyanc01125000  cyanc01125000  2496 Apr  3 19:16 Library
drwxr-xr-x   3 cyanc01125000  cyanc01125000    96 Apr  3 20:10 mi1
drwx------   3 cyanc01125000  cyanc01125000    96 Apr  3 18:25 Movies
drwx------+  3 cyanc01125000  cyanc01125000    96 Apr  3 18:25 Music
drwx------   4 cyanc01125000  cyanc01125000   160 Apr  3 18:26 OrbStack
drwx------+  4 cyanc01125000  cyanc01125000   128 Apr  3 18:25 Pictures
drwxr-xr-x+  4 cyanc01125000  cyanc01125000   128 Apr  3 18:25 Public
-rw-r--r--   1 cyanc01125000  cyanc01125000    15 Apr  3 20:12 sample_copy.txt
cyanc01125000@c4r4s3 ~ % mv -i sample_copy.txt ./mi1/
cyanc01125000@c4r4s3 ~ % cd mi1
cyanc01125000@c4r4s3 mi1 % ls -l
total 16
-rw-r--r--  1 cyanc01125000  cyanc01125000  15 Apr  3 20:12 sample_copy.txt
-rw-r--r--  1 cyanc01125000  cyanc01125000  15 Apr  3 20:11 sample.txt
cyanc01125000@c4r4s3 mi1 % rm sample_copy.txt 
cyanc01125000@c4r4s3 mi1 % ls -l
total 8
-rw-r--r--  1 cyanc01125000  cyanc01125000  15 Apr  3 20:11 sample.txt




- 권한 변경 실습
  . sample.txt 파일의 권한을 644에서 755로 변경
  . test 디렉토리의 권한을 755에서 744로 변경
cyanc01125000@c4r4s3 mission1 % touch sample.txt
cyanc01125000@c4r4s3 mission1 % echo "Hello, Docker" >sample.txt 
cyanc01125000@c4r4s3 mission1 % cat sample.txt 
Hello, Docker
cyanc01125000@c4r4s3 mission1 % ls -l sample.txt 
-rw-r--r--  1 cyanc01125000  cyanc01125000  14 Apr  3 18:43 sample.txt
cyanc01125000@c4r4s3 mission1 % chmod 755 sample.txt 
cyanc01125000@c4r4s3 mission1 % ls -l sample.txt 
-rwxr-xr-x  1 cyanc01125000  cyanc01125000  14 Apr  3 18:43 sample.txt

cyanc01125000@c4r4s3 mi1 % mkdir test
cyanc01125000@c4r4s3 mi1 % ls -l
total 8
-rw-r--r--  1 cyanc01125000  cyanc01125000  15 Apr  3 20:11 sample.txt
drwxr-xr-x  2 cyanc01125000  cyanc01125000  64 Apr  3 20:19 test
cyanc01125000@c4r4s3 mi1 % chmod 744 test
cyanc01125000@c4r4s3 mi1 % ls -l
total 8
-rw-r--r--  1 cyanc01125000  cyanc01125000  15 Apr  3 20:11 sample.txt
drwxr--r--  2 cyanc01125000  cyanc01125000  64 Apr  3 20:19 test



- Docker 설치/점검
  . docker --version
  . docker info
  . docker images
  . docker ps, docker ps -a
  . docker logs web-container
  . docker stats

cyanc01125000@c4r4s3 mi1 % docker --version
Docker version 28.5.2, build ecc6942
cyanc01125000@c4r4s3 mi1 % docker info
Client:
 Version:    28.5.2
 Context:    orbstack
 Debug Mode: false
 Plugins:
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.29.1
    Path:     /Users/cyanc01125000/.docker/cli-plugins/docker-buildx
  compose: Docker Compose (Docker Inc.)
    Version:  v2.40.3
    Path:     /Users/cyanc01125000/.docker/cli-plugins/docker-compose

Server:
 Containers: 5
  Running: 2
  Paused: 0
  Stopped: 3
 Images: 3
 Server Version: 28.5.2
 Storage Driver: overlay2
  Backing Filesystem: btrfs
  Supports d_type: true
  Using metacopy: false
  Native Overlay Diff: true
  userxattr: false
 Logging Driver: json-file
 Cgroup Driver: cgroupfs
 Cgroup Version: 2
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local splunk syslog
 CDI spec directories:
  /etc/cdi
  /var/run/cdi
 Swarm: inactive
 Runtimes: io.containerd.runc.v2 runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: 1c4457e00facac03ce1d75f7b6777a7a851e5c41
 runc version: d842d7719497cc3b774fd71620278ac9e17710e0
 init version: de40ad0
 Security Options:
  seccomp
   Profile: builtin
  cgroupns
 Kernel Version: 6.17.8-orbstack-00308-g8f9c941121b1
 Operating System: OrbStack
 OSType: linux
 Architecture: x86_64
 CPUs: 6
 Total Memory: 15.67GiB
 Name: orbstack
 ID: 9d14e252-fafe-4d0c-b045-60572636f69b
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Experimental: false
 Insecure Registries:
  ::1/128
  127.0.0.0/8
 Live Restore Enabled: false
 Product License: Community Engine
 Default Address Pools:
   Base: 192.168.97.0/24, Size: 24
   Base: 192.168.107.0/24, Size: 24
   Base: 192.168.117.0/24, Size: 24
   Base: 192.168.147.0/24, Size: 24
   Base: 192.168.148.0/24, Size: 24
   Base: 192.168.155.0/24, Size: 24
   Base: 192.168.156.0/24, Size: 24
   Base: 192.168.158.0/24, Size: 24
   Base: 192.168.163.0/24, Size: 24
   Base: 192.168.164.0/24, Size: 24
   Base: 192.168.165.0/24, Size: 24
   Base: 192.168.166.0/24, Size: 24
   Base: 192.168.167.0/24, Size: 24
   Base: 192.168.171.0/24, Size: 24
   Base: 192.168.172.0/24, Size: 24
   Base: 192.168.181.0/24, Size: 24
   Base: 192.168.183.0/24, Size: 24
   Base: 192.168.186.0/24, Size: 24
   Base: 192.168.207.0/24, Size: 24
   Base: 192.168.214.0/24, Size: 24
   Base: 192.168.215.0/24, Size: 24
   Base: 192.168.216.0/24, Size: 24
   Base: 192.168.223.0/24, Size: 24
   Base: 192.168.227.0/24, Size: 24
   Base: 192.168.228.0/24, Size: 24
   Base: 192.168.229.0/24, Size: 24
   Base: 192.168.237.0/24, Size: 24
   Base: 192.168.239.0/24, Size: 24
   Base: 192.168.242.0/24, Size: 24
   Base: 192.168.247.0/24, Size: 24
   Base: fd07:b51a:cc66:d000::/56, Size: 64

WARNING: DOCKER_INSECURE_NO_IPTABLES_RAW is set
cyanc01125000@c4r4s3 mi1 % docker images         
REPOSITORY    TAG       IMAGE ID       CREATED       SIZE
my-web        1.0       9539304791a0   2 hours ago   62.2MB
hello-world   latest    e2ac70e7319a   10 days ago   10.1kB
ubuntu        latest    f794f40ddfff   5 weeks ago   78.1MB
cyanc01125000@c4r4s3 mi1 % docker ps
CONTAINER ID   IMAGE        COMMAND                  CREATED             STATUS             PORTS                                     NAMES
73afd6a50d2a   ubuntu       "sleep infinity"         About an hour ago   Up About an hour                                             vol-test
b892f997cb26   my-web:1.0   "/docker-entrypoint.…"   About an hour ago   Up About an hour   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   web-container
cyanc01125000@c4r4s3 mi1 % docker ps -a
CONTAINER ID   IMAGE         COMMAND                  CREATED             STATUS                         PORTS                                     NAMES
e655d38ba068   ubuntu        "cat /app/my-data_te…"   About an hour ago   Exited (0) About an hour ago                                             priceless_gauss
bdd791cdf453   ubuntu        "cat /app/my-data_te…"   About an hour ago   Exited (1) About an hour ago                                             quirky_williams
73afd6a50d2a   ubuntu        "sleep infinity"         About an hour ago   Up About an hour                                                         vol-test
b892f997cb26   my-web:1.0    "/docker-entrypoint.…"   About an hour ago   Up About an hour               0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   web-container
5b72b6582bd1   hello-world   "/hello"                 2 hours ago         Exited (0) 2 hours ago                                                   clever_antonelli
cyanc01125000@c4r4s3 mi1 % docker logs
docker: 'docker logs' requires 1 argument

Usage:  docker logs [OPTIONS] CONTAINER

Run 'docker logs --help' for more information
cyanc01125000@c4r4s3 mi1 % docker logs --help
Usage:  docker logs [OPTIONS] CONTAINER

Fetch the logs of a container

Aliases:
  docker container logs, docker logs
CONTAINER ID   NAME            CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS 
73afd6a50d2a   vol-test        --        -- / --             --        --        --          -- 
b892f997cb26   web-container   --        -- / --             --        --        --          -- 
 
cyanc01125000@c4r4s3 mi1 % docker logs web-container
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2026/04/03 09:58:40 [notice] 1#1: using the "epoll" event method
2026/04/03 09:58:40 [notice] 1#1: nginx/1.29.7
2026/04/03 09:58:40 [notice] 1#1: built by gcc 15.2.0 (Alpine 15.2.0) 
2026/04/03 09:58:40 [notice] 1#1: OS: Linux 6.17.8-orbstack-00308-g8f9c941121b1
2026/04/03 09:58:40 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 20480:1048576
2026/04/03 09:58:40 [notice] 1#1: start worker processes
2026/04/03 09:58:40 [notice] 1#1: start worker process 30
2026/04/03 09:58:40 [notice] 1#1: start worker process 31
2026/04/03 09:58:40 [notice] 1#1: start worker process 32
2026/04/03 09:58:40 [notice] 1#1: start worker process 33
2026/04/03 09:58:40 [notice] 1#1: start worker process 34
2026/04/03 09:58:40 [notice] 1#1: start worker process 35
192.168.215.1 - - [03/Apr/2026:09:59:26 +0000] "GET / HTTP/1.1" 200 23 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.6 Safari/605.1.15" "-"
2026/04/03 09:59:26 [error] 30#30: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 192.168.215.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:8080", referrer: "http://localhost:8080/"
192.168.215.1 - - [03/Apr/2026:09:59:26 +0000] "GET /favicon.ico HTTP/1.1" 404 153 "http://localhost:8080/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.6 Safari/605.1.15" "-"



  . 아래는 docker stats 실행 흔적
Aliases:
  docker container logs, docker logs
CONTAINER ID   NAME            CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O         PIDS 
73afd6a50d2a   vol-test        0.00%     148KiB / 15.67GiB     0.00%     956B / 126B       4.24MB / 4.1kB    1 
b892f997cb26   web-container   0.00%     4.957MiB / 15.67GiB   0.03%     2.98kB / 1.22kB   10.2MB / 8.19kB   7 
 



- hello-world 실행
  . attach : 컨테이너가 실행 중이 메인 터미널에 직접 연결되므로, attach상태에서 exit를 하면 컨테이너 자체가 종료된다. 
  . exec : 이미 실행중인 컨테이너에 별도 통로를 하나 더 열어서 들어가므로, exec로 들어갔다가 exit를 해도 컨테이는 여전히 running 중이다.

cyanc01125000@c4r4s3 mission1 % docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
4f55086f7dd0: Pull complete 
Digest: sha256:452a468a4bf985040037cb6d5392410206e47db9bf5b7278d281f94d1c2d0931
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/


cyanc01125000@c4r4s3 mi1 % docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

cyanc01125000@c4r4s3 mi1 % docker run -it --name my-ubuntu ubuntu /bin/bash
root@1bc9ee69c957:/# ls -l
total 16
lrwxrwxrwx   1 root root   7 Apr 22  2024 bin -> usr/bin
drwxr-xr-x   1 root root   0 Apr 22  2024 boot
drwxr-xr-x   5 root root 340 Apr  3 11:43 dev



- Dockerfile 빌드/실행
  . 베이스 이미지 : nginx:alpine (웹서버를 구동하기 위해 가장 가볍고 보안이 강화된 이미지이기 때문)
  . 로컬의 html/index.html파일을 복사하여 웹 페이지를 띄우도록 함
  . LABEL을 통해 작성자 정보를 메타데이터로 추가함
  . 아래는 Dockerfile 내용
![Dockerfile Screenshot](https://github.com/clowcat/ia-codyssey/blob/main/screenshot/Dockerfile.png)

  . 아래는 포트 매핑 및 접속 증거
![Web Page Screenshot](https://github.com/clowcat/ia-codyssey/blob/main/screenshot/Web%20page.png)


cyanc01125000@c4r4s3 mission1 % vi Dockerfile
cyanc01125000@c4r4s3 mission1 % docker build -t my-web:1.0 .
[+] Building 7.5s (7/7) FINISHED                                                        docker:orbstack
 => [internal] load build definition from Dockerfile                                               0.2s
 => => transferring dockerfile: 128B                                                               0.0s
 => [internal] load metadata for docker.io/library/nginx:alpine                                    2.7s
 => [internal] load .dockerignore                                                                  0.1s
 => => transferring context: 2B                                                                    0.0s
 => [internal] load build context                                                                  0.2s
 => => transferring context: 93B                                                                   0.0s
 => [1/2] FROM docker.io/library/nginx:alpine@sha256:e7257f1ef28ba17cf7c248cb8ccf6f0c6e0228ab9c31  3.6s
 => => resolve docker.io/library/nginx:alpine@sha256:e7257f1ef28ba17cf7c248cb8ccf6f0c6e0228ab9c31  0.2s
 => => sha256:589002ba0eaed121a1dbf42f6648f29e5be55d5c8a6ee0f8eaa0285cc21ac153 3.86MB / 3.86MB     0.6s
 => => sha256:e7257f1ef28ba17cf7c248cb8ccf6f0c6e0228ab9c315c152f9c203cd34cf6d1 10.33kB / 10.33kB   0.0s
 => => sha256:7e89aa6cabfc80f566b1b77b981f4bb98413bd2d513ca9a30f63fe58b4af6903 2.50kB / 2.50kB     0.0s
 => => sha256:d5030d429039a823bef4164df2fad7a0defb8d00c98c1136aec06701871197c2 12.32kB / 12.32kB   0.0s
 => => sha256:8892f80f46a05d59a4cde3bcbb1dd26ed2441d4214870a4a7b318eaa476a0a54 1.87MB / 1.87MB     0.8s
 => => sha256:91d1c9c22f2c631288354fadb2decc448ce151d7a197c167b206588e09dcd50a 626B / 626B         0.9s
 => => extracting sha256:589002ba0eaed121a1dbf42f6648f29e5be55d5c8a6ee0f8eaa0285cc21ac153          0.1s
 => => sha256:cf1159c696ee2a72b85634360dbada071db61bceaad253db7fda65c45a58414c 953B / 953B         1.1s
 => => extracting sha256:8892f80f46a05d59a4cde3bcbb1dd26ed2441d4214870a4a7b318eaa476a0a54          0.1s
 => => sha256:3f4ad4352d4f91018e2b4910b9db24c08e70192c3b75d0d6fff0120c838aa0bb 402B / 402B         1.3s
 => => sha256:c2bd5ab177271dd59f19a46c214b1327f5c428cd075437ec0155ae71d0cdadc1 1.21kB / 1.21kB     1.3s
 => => extracting sha256:91d1c9c22f2c631288354fadb2decc448ce151d7a197c167b206588e09dcd50a          0.0s
 => => extracting sha256:cf1159c696ee2a72b85634360dbada071db61bceaad253db7fda65c45a58414c          0.0s
 => => sha256:4d9d41f3822d171ccc5f2cdfd75ad846ac4c7ed1cd36fb998fe2c0ce4501647b 1.40kB / 1.40kB     1.6s
 => => extracting sha256:3f4ad4352d4f91018e2b4910b9db24c08e70192c3b75d0d6fff0120c838aa0bb          0.0s
 => => sha256:3370263bc02adcf5c4f51831d2bf1d54dbf9a6a80b0bf32c5c9b9400630eaa08 20.25MB / 20.25MB   2.0s
 => => extracting sha256:c2bd5ab177271dd59f19a46c214b1327f5c428cd075437ec0155ae71d0cdadc1          0.0s
 => => extracting sha256:4d9d41f3822d171ccc5f2cdfd75ad846ac4c7ed1cd36fb998fe2c0ce4501647b          0.0s
 => => extracting sha256:3370263bc02adcf5c4f51831d2bf1d54dbf9a6a80b0bf32c5c9b9400630eaa08          0.4s
 => [2/2] COPY html/ /usr/share/nginx/html/                                                        0.2s
 => exporting to image                                                                             0.2s
 => => exporting layers                                                                            0.1s
 => => writing image sha256:9539304791a082aaa6e3666d0f937758cb1f3e9eb91426e19d83330d0d2cac67       0.0s
 => => naming to docker.io/library/my-web:1.0                                                      0.0s
cyanc01125000@c4r4s3 mission1 % docker images
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
my-web        1.0       9539304791a0   7 seconds ago   62.2MB
hello-world   latest    e2ac70e7319a   10 days ago     10.1kB
cyanc01125000@c4r4s3 mission1 % docker run -d -p 8080:80 --name web-container my-web:1.0
b892f997cb26ce845a6dc44f06addb13cece91aeea6a58558b8598df8e2c6144
cyanc01125000@c4r4s3 mission1 % docker ps
CONTAINER ID   IMAGE        COMMAND                  CREATED         STATUS         PORTS                                     NAMES
b892f997cb26   my-web:1.0   "/docker-entrypoint.…"   7 seconds ago   Up 6 seconds   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   web-container



- 포트 매핑 접속(2회)
  . 8080 포트 매핑
cyanc01125000@c4r4s3 mission1 % docker run -d -p 8080:80 --name web-test my-web-server:1.0
480e519de3004a383b64ada4ffa7a662e13ee4

![port mapping-1 Screenshot](https://github.com/clowcat/ia-codyssey/blob/main/screenshot/port_mapping_1.png)

  . 3000 포트 매핑
cyanc01125000@c4r4s3 mission1 % docker rm web-test
web-test
cyanc01125000@c4r4s3 mission1 % docker run -d -p 3000:80 --name web-test my-web-server:1.0
5ae1c73703a04064cc1dab2c182449bf676ea9a9bdb84bdc4f095793a0774df8

![port mapping-2 Screenshot](https://github.com/clowcat/ia-codyssey/blob/main/screenshot/port_mapping_2.png)




- 바인드 마운트 반영

cyanc01125000@c4r4s3 mission1 % docker stop web-test
web-test
cyanc01125000@c4r4s3 mission1 % docker run -d -p 8080:80 --name web-bind-mount -v $(pwd)/html:/usr/share/nginx/html nginx:alpine
41f0b86fcfde7d26307251d93eee9d2dcf84bcc8544e52490aa458d3c14e602f

![bind mount-before Screenshot](https://github.com/clowcat/ia-codyssey/blob/main/screenshot/bind_mount_before.png)


![bind mount-after Screenshot](https://github.com/clowcat/ia-codyssey/blob/main/screenshot/bind_mount_after.png)




- 볼륨 영속성

yanc01125000@c4r4s3 mission1 % docker volume create my-data
my-data
cyanc01125000@c4r4s3 mission1 % docker rm vol-test
vol-test
cyanc01125000@c4r4s3 mission1 % docker run -d --name vol-test -v my-data:/app ubuntu sleep infinity
2263547e226906905a95c7a05f59ae2e2e4d71f0e6121c5bea57e31bb3d2e97c
cyanc01125000@c4r4s3 mission1 % docker exec -it vol-test bash -c "echo 'Permanent Data' > /app/save.txt"

cyanc01125000@c4r4s3 mission1 % docker rm -f vol-test
vol-test
cyanc01125000@c4r4s3 mission1 % docker run --rm -v my-data:/app ubuntu cat /app/save.txt
Permanent Data




- Git 설정 + VSCode GitHub 연동

cyanc01125000@c4r4s3 mission1 % git config --list
credential.helper=osxkeychain
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
user.name=clowcat
user.email=cyanc0112@gmail.com
remote.origin.url=https://github.com/clowcat/ia-codyssey.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
pull.rebase=false
branch.main.remote=origin
branch.main.merge=refs/heads/main

cyanc01125000@c4r4s3 mission1 % git remote -v
origin  https://github.com/clowcat/ia-codyssey.git (fetch)
origin  https://github.com/clowcat/ia-codyssey.git (push)

![GitHub Screenshot](https://github.com/clowcat/ia-codyssey/blob/main/screenshot/GitHub_connect.png)




- (보너스) Docker Compose 기초
  . 컨테이너 실행 명령이 "문서화된 실행 설정"으로 바뀌는 이유 : 명령어를 일일이 치지 않아도 설정 파일만 있으면 누구나 동일하게 실행 가능하기 때문

![docker-compose Screenshot](https://github.com/clowcat/ia-codyssey/blob/main/screenshot/docker-compose_multi_container.png)


- (보너스) Docker Compose 멀티 컨테이너
  . 운영명령어 : up, down, ps, logs

cyanc01125000@c4r4s3 mission1 % docker-compose up -d
validating /Users/cyanc01125000/codyssey/mission1/docker-compose.yml: services.my-web.depends_on must be a array
cyanc01125000@c4r4s3 mission1 % vi docker-compose.yml 
cyanc01125000@c4r4s3 mission1 % docker-compose up -d 
[+] Building 0.9s (9/9) FINISHED                                                                        
 => [internal] load local bake definitions                                                         0.0s
 => => reading from stdin 531B                                                                     0.0s
 => [internal] load build definition from Dockerfile                                               0.1s
 => => transferring dockerfile: 128B                                                               0.0s
 => [internal] load metadata for docker.io/library/nginx:alpine                                    0.0s
 => [internal] load .dockerignore                                                                  0.1s
 => => transferring context: 2B                                                                    0.0s
 => [internal] load build context                                                                  0.1s
 => => transferring context: 60B                                                                   0.0s
 => [1/2] FROM docker.io/library/nginx:alpine                                                      0.0s
 => CACHED [2/2] COPY html/ /usr/share/nginx/html/                                                 0.0s
 => exporting to image                                                                             0.1s
 => => exporting layers                                                                            0.0s
 => => writing image sha256:18946a3dd7ad4042b77dbbd0a509594d1ebfb2d1c875485b0a0c5a6f02f49516       0.0s
 => => naming to docker.io/library/mission1-my-web                                                 0.0s
 => resolving provenance for metadata file                                                         0.0s
[+] Running 4/4
 ✔ mission1-my-web           Built                                                                 0.0s 
 ✔ Network mission1_default  Created                                                               0.1s 
 ✔ Container redis-service   Started                                                               0.5s 
 ✔ Container web-service     Started                                                               0.6s 
cyanc01125000@c4r4s3 mission1 % docker-compose ps
NAME            IMAGE             COMMAND                  SERVICE   CREATED              STATUS              PORTS
redis-service   redis:alpine      "docker-entrypoint.s…"   my-db     About a minute ago   Up About a minute   6379/tcp
web-service     mission1-my-web   "/docker-entrypoint.…"   my-web    About a minute ago   Up About a minute   0.0.0.0:8081->80/tcp, [::]:8081->80/tcp
cyanc01125000@c4r4s3 mission1 % docker-compose exec my-web ping my-db
PING my-db (192.168.97.2): 56 data bytes
64 bytes from 192.168.97.2: seq=0 ttl=64 time=0.049 ms
64 bytes from 192.168.97.2: seq=1 ttl=64 time=0.109 ms
64 bytes from 192.168.97.2: seq=2 ttl=64 time=0.134 ms
64 bytes from 192.168.97.2: seq=3 ttl=64 time=0.144 ms
64 bytes from 192.168.97.2: seq=4 ttl=64 time=0.085 ms
64 bytes from 192.168.97.2: seq=5 ttl=64 time=0.077 ms
64 bytes from 192.168.97.2: seq=6 ttl=64 time=0.065 ms
64 bytes from 192.168.97.2: seq=7 ttl=64 time=0.069 ms
64 bytes from 192.168.97.2: seq=8 ttl=64 time=0.081 ms
64 bytes from 192.168.97.2: seq=9 ttl=64 time=0.066 ms
64 bytes from 192.168.97.2: seq=10 ttl=64 time=0.138 ms
64 bytes from 192.168.97.2: seq=11 ttl=64 time=0.067 ms
64 bytes from 192.168.97.2: seq=12 ttl=64 time=0.086 ms
64 bytes from 192.168.97.2: seq=13 ttl=64 time=0.068 ms
^C
--- my-db ping statistics ---
14 packets transmitted, 14 packets received, 0% packet loss
round-trip min/avg/max = 0.049/0.088/0.144 ms



- (보너스) Compose 운영 명령어 습득


cyanc01125000@c4r4s3 mission1 % docker-compose ps
NAME            IMAGE             COMMAND                  SERVICE   CREATED              STATUS              PORTS
redis-service   redis:alpine      "docker-entrypoint.s…"   my-db     About a minute ago   Up About a minute   6379/tcp
web-service     mission1-my-web   "/docker-entrypoint.…"   my-web    About a minute ago   Up About a minute   0.0.0.0:8081->80/tcp, [::]:8081->80/tcp

cyanc01125000@c4r4s3 mission1 % docker-compose logs -f
redis-service  | Starting Redis Server
redis-service  | 1:C 06 Apr 2026 11:57:43.851 * oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
redis-service  | 1:C 06 Apr 2026 11:57:43.851 * Redis version=8.6.2, bits=64, commit=00000000, modified=1, pid=1, just started
redis-service  | 1:C 06 Apr 2026 11:57:43.851 * Configuration loaded
redis-service  | 1:M 06 Apr 2026 11:57:43.852 * monotonic clock: POSIX clock_gettime
redis-service  | 1:M 06 Apr 2026 11:57:43.854 * Running mode=standalone, port=6379.
redis-service  | 1:M 06 Apr 2026 11:57:43.856 * <bf> RedisBloom version 8.6.0 (Git=unknown)
redis-service  | 1:M 06 Apr 2026 11:57:43.856 * <bf> Registering configuration options: [
redis-service  | 1:M 06 Apr 2026 11:57:43.856 * <bf>    { bf-error-rate       :      0.01 }
redis-service  | 1:M 06 Apr 2026 11:57:43.856 * <bf>    { bf-initial-size     :       100 }
redis-service  | 1:M 06 Apr 2026 11:57:43.856 * <bf>    { bf-expansion-factor :         2 }
redis-service  | 1:M 06 Apr 2026 11:57:43.856 * <bf>    { cf-bucket-size      :         2 }
redis-service  | 1:M 06 Apr 2026 11:57:43.856 * <bf>    { cf-initial-size     :      1024 }
redis-service  | 1:M 06 Apr 2026 11:57:43.856 * <bf>    { cf-max-iterations   :        20 }
redis-service  | 1:M 06 Apr 2026 11:57:43.856 * <bf>    { cf-expansion-factor :         1 }
redis-service  | 1:M 06 Apr 2026 11:57:43.856 * <bf>    { cf-max-expansions   :        32 }
redis-service  | 1:M 06 Apr 2026 11:57:43.856 * <bf> ]
redis-service  | 1:M 06 Apr 2026 11:57:43.857 * Module 'bf' loaded from /usr/local/lib/redis/modules//redisbloom.so
redis-service  | 1:M 06 Apr 2026 11:57:43.877 * <search> Redis version found by RedisSearch : 8.6.2 - oss
redis-service  | 1:M 06 Apr 2026 11:57:43.877 * <search> RediSearch version 8.6.0 (Git=7782b97)
redis-service  | 1:M 06 Apr 2026 11:57:43.877 * <search> Low level api version 1 initialized successfully
redis-service  | 1:M 06 Apr 2026 11:57:43.877 * <search> gc: ON, prefix min length: 2, min word length to stem: 4, prefix max expansions: 200, query timeout (ms): 500, timeout policy: return, oom policy: return, cursor read size: 1000, cursor max idle (ms): 300000, max doctable size: 1000000, max number of search results:  1000000, default scorer: BM25STD, 
redis-service  | 1:M 06 Apr 2026 11:57:43.877 * <search> Initialized thread pools!
redis-service  | 1:M 06 Apr 2026 11:57:43.877 * <search> Disabled workers threadpool of size 0
redis-service  | 1:M 06 Apr 2026 11:57:43.877 * <search> Subscribe to config changes
redis-service  | 1:M 06 Apr 2026 11:57:43.877 * <search> Subscribe to cluster slot migration events
redis-service  | 1:M 06 Apr 2026 11:57:43.877 * <search> Enabled role change notification
redis-service  | 1:M 06 Apr 2026 11:57:43.878 * <search> Cluster configuration: AUTO partitions, type: 0, coordinator timeout: 0ms
redis-service  | 1:M 06 Apr 2026 11:57:43.878 * Module 'search' loaded from /usr/local/lib/redis/modules//redisearch.so
redis-service  | 1:M 06 Apr 2026 11:57:43.880 * <timeseries> RedisTimeSeries version 80600, git_sha=05fd355db748676861dc4c17d19c8c1ca74c0154
redis-service  | 1:M 06 Apr 2026 11:57:43.880 * <timeseries> Redis version found by RedisTimeSeries : 8.6.2 - oss
redis-service  | 1:M 06 Apr 2026 11:57:43.880 * <timeseries> Registering configuration options: [
redis-service  | 1:M 06 Apr 2026 11:57:43.880 * <timeseries>    { ts-compaction-policy   :              }
redis-service  | 1:M 06 Apr 2026 11:57:43.880 * <timeseries>    { ts-num-threads         :            3 }
redis-service  | 1:M 06 Apr 2026 11:57:43.880 * <timeseries>    { ts-retention-policy    :            0 }
redis-service  | 1:M 06 Apr 2026 11:57:43.880 * <timeseries>    { ts-duplicate-policy    :        block }
redis-service  | 1:M 06 Apr 2026 11:57:43.880 * <timeseries>    { ts-chunk-size-bytes    :         4096 }
redis-service  | 1:M 06 Apr 2026 11:57:43.880 * <timeseries>    { ts-encoding            :   compressed }
redis-service  | 1:M 06 Apr 2026 11:57:43.880 * <timeseries>    { ts-ignore-max-time-diff:            0 }
redis-service  | 1:M 06 Apr 2026 11:57:43.880 * <timeseries>    { ts-ignore-max-val-diff :     0.000000 }
redis-service  | 1:M 06 Apr 2026 11:57:43.880 * <timeseries> ]
redis-service  | 1:M 06 Apr 2026 11:57:43.881 * <timeseries> Detected redis oss
redis-service  | 1:M 06 Apr 2026 11:57:43.881 * <timeseries> Subscribe to ASM events
redis-service  | 1:M 06 Apr 2026 11:57:43.881 * <timeseries> Enabled diskless replication
redis-service  | 1:M 06 Apr 2026 11:57:43.881 * Module 'timeseries' loaded from /usr/local/lib/redis/modules//redistimeseries.so
redis-service  | 1:M 06 Apr 2026 11:57:43.888 * <ReJSON> Created new data type 'ReJSON-RL'
redis-service  | 1:M 06 Apr 2026 11:57:43.889 * <ReJSON> version: 80600 git sha: unknown branch: unknown
redis-service  | 1:M 06 Apr 2026 11:57:43.889 * <ReJSON> Exported RedisJSON_V1 API
redis-service  | 1:M 06 Apr 2026 11:57:43.889 * <ReJSON> Exported RedisJSON_V2 API
redis-service  | 1:M 06 Apr 2026 11:57:43.889 * <ReJSON> Exported RedisJSON_V3 API
redis-service  | 1:M 06 Apr 2026 11:57:43.889 * <ReJSON> Exported RedisJSON_V4 API
redis-service  | 1:M 06 Apr 2026 11:57:43.889 * <ReJSON> Exported RedisJSON_V5 API
redis-service  | 1:M 06 Apr 2026 11:57:43.889 * <ReJSON> Exported RedisJSON_V6 API
redis-service  | 1:M 06 Apr 2026 11:57:43.889 * <ReJSON> Enabled diskless replication
redis-service  | 1:M 06 Apr 2026 11:57:43.889 * <ReJSON> Initialized shared string cache, thread safe: true.
redis-service  | 1:M 06 Apr 2026 11:57:43.889 * Module 'ReJSON' loaded from /usr/local/lib/redis/modules//rejson.so
redis-service  | 1:M 06 Apr 2026 11:57:43.889 * <search> Acquired RedisJSON_V6 API
redis-service  | 1:M 06 Apr 2026 11:57:43.889 * Server initialized
redis-service  | 1:M 06 Apr 2026 11:57:43.889 * Ready to accept connections tcp
redis-service  | 1:M 06 Apr 2026 11:57:43.889 # WARNING: Redis does not require authentication and is not protected by network restrictions. Redis will accept connections from any IP address on any network interface.
web-service    | /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
web-service    | /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
web-service    | /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
web-service    | 10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
web-service    | 10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
web-service    | /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
web-service    | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
web-service    | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
web-service    | /docker-entrypoint.sh: Configuration complete; ready for start up
web-service    | 2026/04/06 11:57:44 [notice] 1#1: using the "epoll" event method
web-service    | 2026/04/06 11:57:44 [notice] 1#1: nginx/1.29.7
web-service    | 2026/04/06 11:57:44 [notice] 1#1: built by gcc 15.2.0 (Alpine 15.2.0) 
web-service    | 2026/04/06 11:57:44 [notice] 1#1: OS: Linux 6.17.8-orbstack-00308-g8f9c941121b1
web-service    | 2026/04/06 11:57:44 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 20480:1048576
web-service    | 2026/04/06 11:57:44 [notice] 1#1: start worker processes
web-service    | 2026/04/06 11:57:44 [notice] 1#1: start worker process 30
web-service    | 2026/04/06 11:57:44 [notice] 1#1: start worker process 31
web-service    | 2026/04/06 11:57:44 [notice] 1#1: start worker process 32
web-service    | 2026/04/06 11:57:44 [notice] 1#1: start worker process 33
web-service    | 2026/04/06 11:57:44 [notice] 1#1: start worker process 34
web-service    | 2026/04/06 11:57:44 [notice] 1#1: start worker process 35
web-service    | 192.168.97.1 - - [06/Apr/2026:11:58:48 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.6 Safari/605.1.15" "-"

cyanc01125000@c4r4s3 mission1 % docker-compose down
[+] Running 3/3
 ✔ Container web-service     Removed                                                               0.4s 
 ✔ Container redis-service   Removed                                                               0.3s 
 ✔ Network mission1_default  Removed                                                               0.1s 


- (보너스) 환경변수 활용

![docker-compose Screenshot](https://github.com/clowcat/ia-codyssey/blob/main/screenshot/docker-compose_env.png)

cyanc01125000@c4r4s3 mission1 % vi docker-compose.yml
cyanc01125000@c4r4s3 mission1 % docker-compose up -d 
[+] Running 4/4
 ✔ Network mission1_default      Created                                                              0.1s 
 ✔ Network mission1_backend-net  Created                                                              0.1s 
 ✔ Container redis-service       Started                                                              0.5s 
 ✔ Container web-service         Started                                                              0.6s 
cyanc01125000@c4r4s3 mission1 % docker-compose exec my-web env | grep -E "SERVER_ROLE|ADMIN_EMAIL"
SERVER_ROLE=development
ADMIN_EMAIL=cyanc0112@gmail.com



- (보너스) GitHub SSH 키 설정

cyanc01125000@c4r4s3 ~ % ssh-keygen -t ed25519 -C "cyanc0112@gmail.com"
Generating public/private ed25519 key pair.
Enter file in which to save the key (/Users/cyanc01125000/.ssh/id_ed25519): 
Enter passphrase for "/Users/cyanc01125000/.ssh/id_ed25519" (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /Users/cyanc01125000/.ssh/id_ed25519
Your public key has been saved in /Users/cyanc01125000/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:xxxxxxxxxxxxxxxxxxxxxxxx cyanc0112@gmail.com
The key's randomart image is:
+--[ED25519 256]--+
|++EX*.           |
|.O+B*o           |
|+.+=+ .          |
|.=+=.. .         |
|=.=.o + S        |
|.= = o o         |
|... + .          |
|..o.             |
| +o              |
+----[SHA256]-----+
cyanc01125000@c4r4s3 ~ % cat ~/.ssh/id_ed25519.pub
ssh-ed25519 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx cyanc0112@gmail.com
cyanc01125000@c4r4s3 ~ % ssh -T git@github.com
Hi clowcat/ia-codyssey! You've successfully authenticated, but GitHub does not provide shell access.
#!/bin/bash

# [1] 설정 변수 (내 환경에 맞게 수정)
AGENT_PORT=15034
LOG_FILE="/var/log/agent-app/monitor.log"
MAX_LOG_SIZE=$((10 * 1024 * 1024)) # 10MB (바이트 단위)

# [2] 로그 기록 함수 (날짜와 함께 기록)
log_msg() {
    local level=$1
    local message=$2
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $level: $message" >> "$LOG_FILE"
}

# [3] Health Check (앱 생존 여부 확인)
PID=$(pgrep -f "agent_app.py")
if [ -z "$PID" ]; then
    echo "[FAIL] 앱 프로세스를 찾을 수 없습니다."
    exit 1
fi

PORT_CHECK=$(ss -tulnp | grep ":$AGENT_PORT")
if [ -z "$PORT_CHECK" ]; then
    echo "[FAIL] 포트 $AGENT_PORT 가 응답하지 않습니다."
    exit 1
fi

# [4] 리소스 수집 (CPU, 메모리, 디스크)
# %CPU 사용률 (1초 동안 측정)
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print 100 - $8}')
# 메모리 사용률 (사용중 / 전체 * 100)
MEM_USAGE=$(free | grep Mem | awk '{print $3/$2 * 100.0}')
# 디스크 사용률 (Root / 기준)
DISK_USAGE=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')

# [5] 임계값 경고 및 로그 기록
WARNING_MSG=""
# CPU 20% 초과 시
if (( $(echo "$CPU_USAGE > 20" | bc -l) )); then
    WARNING_MSG+="[CPU Warning: $CPU_USAGE%] "
fi
# 메모리 10% 초과 시
if (( $(echo "$MEM_USAGE > 10" | bc -l) )); then
    WARNING_MSG+="[MEM Warning: $MEM_USAGE%] "
fi

# 콘솔 출력 및 파일 기록
RESULT_STR="PID:$PID CPU:${CPU_USAGE}% MEM:${MEM_USAGE}% DISK:${DISK_USAGE}% $WARNING_MSG"
echo "$RESULT_STR"
log_msg "INFO" "$RESULT_STR"

# [6] 로그 파일 용량 관리 (10MB 초과 시 비우기)
FILE_SIZE=$(stat -c%s "$LOG_FILE")
if [ $FILE_SIZE -gt $MAX_LOG_SIZE ]; then
    log_msg "SYSTEM" "Log file exceeded 10MB. Rotating..."
    cat /dev/null > "$LOG_FILE"
fi
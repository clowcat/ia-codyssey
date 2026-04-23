import json
import time
import sys

class MiniNPUSimulator:
    def __init__(self):
        self.epsilon = 1e-9 # 부동소수점 허용 오차

    def normalize_label(self, label):
        """라벨 표준화: Cross, X로 통일 """
        label = str(label).lower().strip()
        if label in ['+', 'cross']:
            return "Cross"
        if label in ['x']:
            return "X"
        return label

    def calculate_mac(self, pattern, filter_data):
        """MAC(Multiply-Accumulate) 연산 구현 (O(N^2))"""
        size = len(pattern)
        score = 0.0
        for r in range(size):
            for c in range(size):
                score += pattern[r][c] * filter_data[r][c]
        return score

    def judge(self, score_a, score_b):
        """점수 비교 및 판정 (epsilon 적용)"""
        if abs(score_a - score_b) < self.epsilon:
            return "UNDECIDED"
        return "Cross" if score_a > score_b else "X"

    def measure_performance(self, pattern, filter_cross, filter_x, iterations=10):
        """연산 시간 측정 (평균 10회)"""
        start_time = time.perf_counter()
        for _ in range(iterations):
            self.calculate_mac(pattern, filter_cross)
            self.calculate_mac(pattern, filter_x)
        end_time = time.perf_counter()
        # 한 번의 패턴 판정(필터 2개 연산)에 걸리는 평균 시간(ms)
        avg_time_ms = ((end_time - start_time) / iterations) * 1000
        return avg_time_ms
    

def input_matrix(size, name):
    """사용자로부터 n x n 행렬 입력 받기 및 검증 [cite: 435-440]"""
    print(f"{name} ({size}줄 입력, 공백 구분):")
    matrix = []
    for i in range(size):
        while True:
            try:
                line = input().split()
                if len(line) != size:
                    raise ValueError(f"입력 형식 오류: {size}개의 숫자를 입력하세요.")
                matrix.append([float(x) for x in line])
                break
            except ValueError as e:
                print(f"⚠️ {e} 다시 입력해 주세요.")
    return matrix

def run_mode_1(sim):
    """모드 1: 사용자 입력 (3x3) [cite: 409-411, 480]"""
    print("\n# [1] 필터 입력")
    filter_a = input_matrix(3, "필터 A")
    filter_b = input_matrix(3, "필터 B")
    
    print("\n# [2] 패턴 입력")
    pattern = input_matrix(3, "패턴")
    
    score_a = sim.calculate_mac(pattern, filter_a)
    score_b = sim.calculate_mac(pattern, filter_b)
    avg_time = sim.measure_performance(pattern, filter_a, filter_b)
    result = sim.judge(score_a, score_b)
    
    print("\n# [3] MAC 결과")
    print(f"A 점수: {score_a}")
    print(f"B 점수: {score_b}")
    print(f"연산 시간(평균/10회): {avg_time:.6f} ms")
    print(f"판정: {result}")

def run_mode_2(sim):
    """모드 2: JSON 데이터 분석 [cite: 412-414, 481]"""
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("❌ data.json 파일을 찾을 수 없습니다.")
        return

    filters = data.get("filters", {})
    patterns = data.get("patterns", {})
    
    stats = {"total": 0, "pass": 0, "fail": 0, "fail_list": []}
    perf_results = []

    print("\n# [1] 필터 로드")
    for f_key in filters:
        print(f"✓ {f_key} 필터 로드 완료")

    print("\n# [2] 패턴 분석 (라벨 정규화 적용)")
    for p_key, p_data in patterns.items():
        stats["total"] += 1
        size = int(p_key.split('_')[1])
        pattern_input = p_data["input"]
        expected = sim.normalize_label(p_data["expected"])
        
        filter_group = filters.get(f"size_{size}")
        if not filter_group or len(pattern_input) != size:
            stats["fail"] += 1
            stats["fail_list"].append(f"{p_key}: 크기/스키마 불일치")
            continue

        # 필터 키 정규화 매칭 [cite: 452]
        f_cross = filter_group.get("cross") or filter_group.get("Cross")
        f_x = filter_group.get("x") or filter_group.get("X")
        
        score_cross = sim.calculate_mac(pattern_input, f_cross)
        score_x = sim.calculate_mac(pattern_input, f_x)
        result = sim.judge(score_cross, score_x)
        
        status = "PASS" if result == expected else "FAIL"
        if status == "PASS": stats["pass"] += 1
        else: 
            stats["fail"] += 1
            stats["fail_list"].append(f"{p_key}: 판정 {result} != 기대 {expected}")

        print(f"- {p_key} --- Cross: {score_cross}, X: {score_x} | 판정: {result} | expected: {expected} | {status}")

        # 성능 데이터 수집 (사이즈별 최초 1회만 기록)
        if not any(r['size'] == size for r in perf_results):
            avg_t = sim.measure_performance(pattern_input, f_cross, f_x)
            perf_results.append({"size": size, "time": avg_t, "ops": size*size})

    print("\n# [3] 성능 분석 (평균/10회) [cite: 469]")
    print(f"{'크기':<10} {'평균 시간(ms)':<15} {'연산 횟수(N²)'}")
    print("-" * 40)
    for r in sorted(perf_results, key=lambda x: x['size']):
        print(f"{r['size']}x{r['size']:<8} {r['time']:<15.6f} {r['ops']}")

    print("\n# [4] 결과 요약 [cite: 471-473]")
    print(f"총 테스트: {stats['total']}개 | 통과: {stats['pass']}개 | 실패: {stats['fail']}개")
    if stats["fail_list"]:
        print("실패 케이스:")
        for fail in stats["fail_list"]:
            print(f"  - {fail}")

def main():
    sim = MiniNPUSimulator()
    print("=== Mini NPU Simulator ===")
    print("1. 사용자 입력 (3x3)")
    print("2. data.json 분석")
    
    choice = input("선택: ").strip()
    if choice == '1':
        run_mode_1(sim)
    elif choice == '2':
        run_mode_2(sim)
    else:
        print("잘못된 선택입니다.")

if __name__ == "__main__":
    main()
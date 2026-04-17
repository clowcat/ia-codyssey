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
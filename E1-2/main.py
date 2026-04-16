import json
import os
import sys

import json
import os
import sys

class Quiz:
    """개별 퀴즈를 표현하는 클래스"""
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = int(answer)  # 정답은 1~4 번호로 관리

    def display(self, index):
        """퀴즈 내용 출력"""
        print(f"\n[문제 {index}]")
        print(self.question)
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")

    def check_answer(self, user_input):
        """정답 확인"""
        return self.answer == user_input

    def to_dict(self):
        """JSON 저장을 위한 딕셔너리 변환"""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

class QuizGame:
    """게임 전체 관리 클래스 (퀴즈 목록, 점수, 파일 입출력)"""
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.file_path = "state.json"
        self.load_data()  # 초기화 시 데이터 로드 

    def load_data(self):
        """파일에서 데이터 로드 및 예외 처리"""
        if not os.path.exists(self.file_path):
            self.set_default_data()  # 파일 없으면 기본 데이터 사용
            return

        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.best_score = data.get("best_score", 0)
                self.quizzes = [Quiz(**q) for q in data.get("quizzes", [])]
        except (json.JSONDecodeError, IOError):
            print("데이터 파일이 손상되었습니다. 기본 데이터로 복구합니다.")
            self.set_default_data()  # 파일 손상 시 초기화

    def set_default_data(self):
        """기본 과일 퀴즈 5개 설정"""
        defaults = [
            {"question": "사과의 색깔은 보통 무엇인가요?", "choices": ["빨간색", "파란색", "보라색", "검은색"], "answer": 1},
            {"question": "여름철 대표 과일로 속이 빨갛고 검은 씨가 있는 것은?", "choices": ["참외", "수박", "복숭아", "포도"], "answer": 2},
            {"question": "바나나를 많이 먹는 동물로 알려진 유인원은?", "choices": ["사자", "코끼리", "원숭이", "기린"], "answer": 3},
            {"question": "제주도의 특산물로 유명한 주황색 과일은?", "choices": ["망고", "딸기", "블루베리", "감귤"], "answer": 4},
            {"question": "포도를 말려서 만든 간식은 무엇인가요?", "choices": ["건포도", "곶감", "말랭이", "푸룬"], "answer": 1}
        ]
        self.quizzes = [Quiz(**q) for q in defaults]
        self.best_score = 0
        self.save_data()

    def save_data(self):
        """데이터를 state.json에 저장"""
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score
        }
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def get_valid_input(self, prompt, min_val, max_val):
        """공통 입력 처리 및 예외 기준 준수 """
        while True:
            try:
                user_input = input(prompt).strip()  # 공백 제거
                if not user_input:
                    print("빈 입력입니다. 다시 입력해 주세요.")  # 빈 입력 처리
                    continue
                
                val = int(user_input)
                if min_val <= val <= max_val:
                    return val
                else:
                    print(f"{min_val}~{max_val} 사이의 숫자만 입력 가능합니다.") # 범위 밖 입력
            except ValueError:
                print("숫자 변환에 실패했습니다. 숫자를 입력해 주세요.") # 숫자 변환 실패
            except (EOFError, KeyboardInterrupt):
                print("\n프로그램을 비정상 종료하지 않고 안전하게 닫습니다.") # 강제 종료 대응
                self.exit_game()

    def play_quiz(self):
        """퀴즈 풀기 기능 """
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"\n퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")
        correct_count = 0

        for i, quiz in enumerate(self.quizzes, 1):
            quiz.display(i)
            ans = self.get_valid_input("정답 입력(1-4): ", 1, 4)
            if quiz.check_answer(ans):
                print("정답입니다!")
                correct_count += 1
            else:
                print(f"틀렸습니다. 정답은 {quiz.answer}번입니다.")

        print(f"\n결과: {len(self.quizzes)}문제 중 {correct_count}문제 정답!")
        if correct_count > self.best_score:
            print("새로운 최고 점수입니다!")
            self.best_score = correct_count
            self.save_data()

    def add_quiz(self):
        """퀴즈 추가 기능 """
        print("\n새로운 퀴즈를 추가합니다.")
        question = input("문제를 입력하세요: ").strip()
        while not question:
            question = input("문제는 비어둘 수 없습니다. 다시 입력: ").strip()

        choices = []
        for i in range(1, 5):
            choice = input(f"선택지 {i}: ").strip()
            while not choice:
                choice = input(f"선택지를 입력해 주세요: ").strip()
            choices.append(choice)

        answer = self.get_valid_input("정답 번호 (1-4): ", 1, 4)
        self.quizzes.append(Quiz(question, choices, answer))
        self.save_data()
        print("퀴즈가 성공적으로 추가되었습니다!")

    def show_list(self):
        """퀴즈 목록 보기 """
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        print(f"\n등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"[{i}] {quiz.question}")

    def show_score(self):
        """최고 점수 확인 """
        print(f"\n최고 점수: {self.best_score}개 정답")

    def exit_game(self):
        """종료 기능 """
        print("현재 상태를 저장하고 프로그램을 종료합니다.")
        self.save_data()
        sys.exit(0)

    def main_menu(self):
        """메뉴 출력 및 선택"""
        while True:
            print("\n" + "="*40)
            print("        나만의 퀴즈 게임 ")
            print("="*40)
            print("1. 퀴즈 풀기\n2. 퀴즈 추가\n3. 퀴즈 목록\n4. 점수 확인\n5. 종료")
            print("="*40)
            
            choice = self.get_valid_input("선택: ", 1, 5)
            if choice == 1: self.play_quiz()
            elif choice == 2: self.add_quiz()
            elif choice == 3: self.show_list()
            elif choice == 4: self.show_score()
            elif choice == 5: self.exit_game()

if __name__ == "__main__":
    game = QuizGame()
    game.main_menu()
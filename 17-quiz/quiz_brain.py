class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def has_remaining_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        print(f"Question {self.question_number + 1}: {current_question.text}")
        user_answer = input("Is it 'true' or 'false': ")
        while user_answer.lower() != 'true' and user_answer.lower() != 'false':
            user_answer = input("Is it 'true' or 'false': ")

        if self.is_user_answer_correct(user_answer, current_question.answer):
            print("You got it!")
            self.score += 1
        else:
            print(f"Nope, the answer was {current_question.answer}")

        self.question_number += 1
        print(f"Score: {self.score}/{self.question_number}\n")

    def is_user_answer_correct(self, user_answer, actual_answer):
        return user_answer.lower() == actual_answer.lower()

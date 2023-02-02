from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

quiz_questions = []
for question in question_data:
    # print(question['text'], question['answer'])
    quiz_questions.append(Question(question['text'], question['answer']))

quiz = QuizBrain(quiz_questions)
while quiz.has_remaining_questions():
    quiz.next_question()

print("You reached the end of the quiz.")
print(f"You got {quiz.score} points out of the {quiz.question_number} possible.")

# https://opentdb.com/api_config.php can be used to generate more trivia questions, the API serves JSON data,
# but it can be modified and used with the current structure

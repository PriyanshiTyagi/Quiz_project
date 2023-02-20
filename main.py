from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for que in question_data:
    new_que = Question(que['question'], que['correct_answer'])
    question_bank.append(new_que)
print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz.")
print(f"You got {quiz.score} correct answers out of {quiz.question_number} questions.")





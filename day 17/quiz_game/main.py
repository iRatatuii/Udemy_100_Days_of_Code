from data import question_data
from question_module import Question
from quiz_brain import QuizBrain

question_bank = []
# for item in question_data:
#     text = item.get('text')
#     answer = item.get('answer')
#     question_bank.append(Question(text, answer))

for item in question_data['results']:
    text = item.get('question')
    answer = item.get('correct_answer')
    question_bank.append(Question(text, answer))


quiz = QuizBrain(question_list=question_bank)

while quiz.still_has_question():
    quiz.next_question()


print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{len(quiz.question_list)}")

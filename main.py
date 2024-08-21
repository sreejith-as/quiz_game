from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a list of Question objects from the question_data
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

# Create a QuizBrain object with the question bank
quiz = QuizBrain(question_bank)

# Run the quiz until there are no more questions
while quiz.still_has_questions():
    quiz.next_question()

# Print the final score
print("You have completed the quiz")
print(f"Your final score is : {quiz.score}/{quiz.question_number}")
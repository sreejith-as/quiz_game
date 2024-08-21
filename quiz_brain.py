class QuizBrain:
    # The main logic for the quiz
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """Check if there are any more questions to be asked and returns True if there are more questions, False otherwise."""
        return self.question_number < (len(self.question_list))

    def next_question(self):
        """Gets the next question, asks the user for an answer, and checks it."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} : {current_question.text} (True/False)").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Checks if the user's answer is correct and updates the score accordingly."""
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong")
        print(f"Your current score is : {self.score} / {self.question_number}")
        print("")
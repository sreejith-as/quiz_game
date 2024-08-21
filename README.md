# Quiz Game

This Python project is a simple quiz game that tests the user's general knowledge. The game presents a series of true/false questions and keeps track of the user's score.

![Python Badge](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)

## Features
- Question Bank: A collection of multiple-choice questions on various general knowledge topics.
- User Interface: Prompts the user to answer each question and provides feedback on their response.
- Score Tracking: Keeps a running count of the user's correct answers.
- Completion Summary: Displays the user's final score at the end of the quiz.

## How to Use
1. Start the Game: Run the main.py file to begin the quiz.
2. Answer the Questions: For each question, enter "True" or "False" when prompted.
3. Check Your Score: After answering all the questions, the final score will be displayed.

## Code Structure
The project is divided into four main Python files:
- data.py: Stores the question data in a list of dictionaries.
- question_model.py: Defines the Question class to represent a single question.
- quiz_brain.py: Manages the quiz logic, including tracking the user's progress and score.
- main.py: The entry point of the program, orchestrating the quiz session.

## Key Components
- Question Class: Encapsulates a single question with its text and correct answer.
- QuizBrain Class: Handles the flow of the quiz, including navigating through questions, checking answers, and updating the score.
- question_data List: Stores the collection of questions to be used in the quiz.

## Requirements
- Python 3.x

## Running the Project
1. Clone or download the project to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the script using Python:
   ```bash
   python main.py

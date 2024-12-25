# Quiz Game 🎮🧠

## Description
- A simple Python-based quiz game where users answer multiple-choice questions.
- Tracks the user's score and provides feedback at the end.
- Demonstrates the use of Python for building a menu-driven program with interactive user input, error handling, and structured logic.

---

## Features
- A **main menu** where users can choose one of three quizzes or exit the program.
- Three quizzes, each containing 10 multiple-choice questions:
  - **General Knowledge**
  - **Sports**
  - **Science**
- Immediate feedback on whether the selected answer is correct or incorrect.
- A **final score** displayed at the end of each quiz.
- Input validation to handle invalid inputs gracefully.

---

## How to Run
1. Clone this repository.
2. Navigate to the project folder.
3. Run `quiz_game.py` using Python 3.

---

## Technologies Used
- **Python 3** for core programming.

---

## Reflection
### What I Learned
- How to structure a Python program with functions for modularity.
- Using loops and conditionals to control program flow.
- Implementing error handling to validate user input and prevent crashes.
- Storing and retrieving question data using dictionaries and lists.

### Areas of Improvement
1. **Refactor Repetitive Code**:
   - Move common quiz logic into reusable functions to follow the DRY (Don’t Repeat Yourself) principle.
2. **Store Questions Dynamically**:
   - Use external files (like JSON or CSV) for storing questions, allowing for easy updates and new quizzes.
3. **Enhanced User Experience**:
   - Add features like a timer or the ability to replay quizzes without restarting the program.
4. **Readability**:
   - Use meaningful variable names and add comments to make the code easier to understand for others.

---

## Future Plans
- Add more quiz categories and questions.
- Create a graphical interface using libraries like **Tkinter** or **PyQt** for a more engaging user experience.
- Implement scoring persistence (e.g., store high scores in a file or database).

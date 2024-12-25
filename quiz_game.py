

def main_menu():
    print("Welcome to the Quiz Game!")
    print("Please select a quiz:")
    print("1. General Knowledge Quiz")
    print("2. Sports Quiz")
    print("3. Science Quiz")
    while True:
        try:
            choice = int(input("Enter your choice (1/2/3)")) #Input returns a string, so need to convert into an int

            if choice in [1,2,3]:
                return choice
            else:
                print("Invalid choice. Please select 1, 2, or 3")

        except ValueError:
            print("Invalid input. Please enter a number.")
    

quiz_choice = main_menu()

quiz_choices = ["General Knowledge Quiz", "Sports Quiz", "Science Quiz"]
selected_quiz = quiz_choices[int(quiz_choice) - 1]
print(f"You selected {selected_quiz}, good luck!")

def general_knowledge_quiz():
    print("Starting General Knowledge Quiz...")
    questions = [
    {
        "question": "Where is the Mona Lisa?",
        "options": ["A. London", "B. Madrid", "C. Paris", "D. Berlin"],
        "answer": "C"
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["A. Beijing", "B. Tokyo", "C. Seoul", "D. Bangkok"],
        "answer": "B"
    },
    {
        "question": "Who wrote Romeo and Juliet?",
        "options": ["A. William Shakespeare", "B. Charles Dickens", "C. J.K. Rowling", "D. Jane Austen"],
        "answer": "A"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Mars", "B. Earth", "C. Jupiter", "D. Saturn"],
        "answer": "C"
    },
    {
        "question": "How many continents are there in the world?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A. H2O", "B. CO2", "C. NaCl", "D. O2"],
        "answer": "A"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A. Pablo Picasso", "B. Vincent van Gogh", "C. Claude Monet", "D. Leonardo da Vinci"],
        "answer": "D"
    },
    {
        "question": "Which ocean is the largest?",
        "options": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
        "answer": "D"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["A. Gold", "B. Diamond", "C. Platinum", "D. Iron"],
        "answer": "B"
    },
    {
        "question": "Who was the first president of the United States?",
        "options": ["A. George Washington", "B. Thomas Jefferson", "C. Abraham Lincoln", "D. John Adams"],
        "answer": "A"
    }
]

    score = 0

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)

        while True:
            try:
                user_answer = input("Your answer (A/B/C/D): ").strip().upper() #Removes any leading or trailing spaces, and converts the string into uppercase.

                if user_answer in ["A", "B", "C", "D"]: #Check if the input is valid
                    break # Valid input break the loop
                else:
                    print("Invalid choice. Please select A, B, C or D.")
            except ValueError:
                print("Please enter a valid option (A, B, C, or D)")

        if user_answer == q["answer"]:
            print("Correct!")
            score += 1 #Increment score for correct answer
        else:
            print(f"Wrong! The correct answer is {q['answer']}")
    print(f"Quiz Complete! Your final score is {score}/{len(questions)}")



def sports_quiz():
    print("Starting Sports Quiz...")


def science_quiz():
    print("Starting Science Quiz...")

def general_knowledge_quiz():
    print("Starting General Knowledge Quiz...")
    questions = [
        {
            "question": "Where is the Mona Lisa?",
            "options": ["A. London", "B. Madrid", "C. Paris", "D. Berlin"],
            "answer": "C"
        },
        # Additional questions...
    ]

    score = 0

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)

        while True:
            try:
                user_answer = input("Your answer (A/B/C/D): ").strip().upper()

                if user_answer in ["A", "B", "C", "D"]:
                    break
                else:
                    print("Invalid choice. Please select A, B, C or D.")
            except ValueError:
                print("Please enter a valid option (A, B, C, or D)")

        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}")

    print(f"Quiz Complete! Your final score is {score}/{len(questions)}")


# Main Menu Loop for Multiple Attempts
while True:
    quiz_choice = main_menu()

    if quiz_choice == 1:
        general_knowledge_quiz()
    elif quiz_choice == 2:
        sports_quiz()
    elif quiz_choice == 3:
        science_quiz()
    else:
        print("Thanks for playing! Goodbye!")
        break

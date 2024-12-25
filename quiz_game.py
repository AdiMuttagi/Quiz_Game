#Main Menu Function
def main_menu():
    print("Welcome to the Quiz Game!")
    print("Please select a quiz:")
    print("1. General Knowledge Quiz")
    print("2. Sports Quiz")
    print("3. Science Quiz")
    print("4. Exit")

    while True:
        try:
            choice = int(input("Enter your choice (1/2/3/4): "))
            if choice in [1, 2, 3, 4]:
                return choice  # Return the valid choice
            else:
                print("Invalid choice. Please select 1, 2, 3, or 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")


#General Knowledge Quiz Function:

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
    print("Returning to Main Menu...")
    main_menu()  # Return to main menu


#Sports Quiz Function:
def sports_quiz():
    print("Starting Sports Quiz...")
    questions = [
    {
        "question": "Which country won the FIFA World Cup in 2018?",
        "options": ["A. Brazil", "B. Germany", "C. France", "D. Argentina"],
        "answer": "C"
    },
    {
        "question": "In which sport is a 'love' score used?",
        "options": ["A. Tennis", "B. Basketball", "C. Cricket", "D. Golf"],
        "answer": "A"
    },
    {
        "question": "How many players are on a basketball team on the court?",
        "options": ["A. 5", "B. 7", "C. 11", "D. 6"],
        "answer": "A"
    },
    {
        "question": "Which country is known for inventing cricket?",
        "options": ["A. Australia", "B. India", "C. England", "D. South Africa"],
        "answer": "C"
    },
    {
        "question": "How many rings are there on the Olympic flag?",
        "options": ["A. 3", "B. 5", "C. 7", "D. 6"],
        "answer": "B"
    },
    {
        "question": "In which sport would you perform a slam dunk?",
        "options": ["A. Volleyball", "B. Basketball", "C. Tennis", "D. Baseball"],
        "answer": "B"
    },
    {
        "question": "What is the term for scoring three goals in a single soccer game?",
        "options": ["A. Goal Streak", "B. Hat-trick", "C. Triple goal", "D. Strike"],
        "answer": "B"
    },
    {
        "question": "Who is known as the 'King of Football'?",
        "options": ["A. Lionel Messi", "B. Cristiano Ronaldo", "C. Pele", "D. Maradona"],
        "answer": "C"
    },
    {
        "question": "Which sport uses a puck instead of a ball?",
        "options": ["A. Hockey", "B. Baseball", "C. Ice Hockey", "D. Table Tennis"],
        "answer": "C"
    },
    {
        "question": "What does MLB stand for?",
        "options": ["A. Major League Basketball", "B. Major League Baseball", "C. Master League Baseball", "D. Major Local Baseball"],
        "answer": "B"
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
    print("Returning to Main Menu...")

    main_menu()  # Return to main menu

def science_quiz():
    print("Starting Science Quiz...")
    questions = [


    ]






    main_menu()  # Return to main menu


if __name__ == "__main__":
    while True:  # Main program loop
        quiz_choice = main_menu()

        if quiz_choice == 1:
            general_knowledge_quiz()
        elif quiz_choice == 2:
            sports_quiz()
        elif quiz_choice == 3:
            science_quiz()
        elif quiz_choice == 4:
            print("Thanks for playing! Goodbye!")
            break  # Exit the loop to end the program

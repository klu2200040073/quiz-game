# Quiz Game in Python

# Questions and answers data
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["A. 0", "B. 1", "C. 2", "D. 3"],
        "answer": "C"
    }
]

# Function to run the quiz
def run_quiz(questions):
    score = 0
    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for option in q["options"]:
            print(option)
        
        # Get user's answer with validation
        user_answer = input("Your answer (A, B, C, or D): ").upper()
        while user_answer not in ["A", "B", "C", "D"]:
            user_answer = input("Invalid input. Please enter A, B, C, or D: ").upper()

        # Check if the answer is correct
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {q['answer']}.")
    
    # Display final score
    print(f"\nYour final score is {score} out of {len(questions)}")

# Main program execution
if _name_ == "_main_":
    print("Welcome to the Quiz Game!")
    run_quiz(questions)
    print("Thank you for playing!")
  

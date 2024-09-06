# Define the quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "A"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    }
]

def display_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)

def get_user_answer():
    return input("Please select an option (A, B, C, or D): ").upper()

def run_quiz(questions):
    score = 0
    for question in questions:
        display_question(question)
        user_answer = get_user_answer()
        if user_answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}\n")
    print(f"Quiz Over! Your final score is {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz(questions)

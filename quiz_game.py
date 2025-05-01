# List of quiz questions with options and correct answers
import os

datacet = []
quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) London", "C) Paris", "D) Madrid"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
        "answer": "D"
    },
    {
        "question": "Which element has the atomic number 1?",
        "options": ["A) Helium", "B) Hydrogen", "C) Oxygen", "D) Carbon"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'To be, or not to be'?",
        "options": ["A) Charles Dickens", "B) J.K. Rowling", "C) William Shakespeare", "D) Mark Twain"],
        "answer": "C"
    }
]

# Function to run the quiz game
def run_quiz():
    score = 0
    print("Quiz Game - Answer the multiple-choice questions!")
    
    for question in quiz:
        print("\n" + question["question"])
        for option in question["options"]:
            print(option)
        
        answer = input("Your answer (A/B/C/D): ").upper()
        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}.")
    
    print(f"\nYour final score: {score}/{len(quiz)}")

if __name__ == "__main__":
    run_quiz()

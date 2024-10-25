import json
import random
from datetime import datetime

# Load questions from the JSON file
def load_questions(filename="questions.json"):
    with open(filename, "r") as file:
        return json.load(file)

# Save feedback to JSON file
def save_feedback(feedback, filename="feedback.json"):
    with open(filename, "a") as file:
        json.dump(feedback, file)
        file.write("\n")

# Filter questions based on category and difficulty
def filter_questions(questions, category, difficulty):
    return [
        question for question in questions
        if question["category"].lower() == category.lower()
        and question["difficulty"].lower() == difficulty.lower()
    ]

# Quiz Logic
def run_quiz():
    questions = load_questions()
    
    # Display available categories as a numbered list
    available_categories = list(set(q["category"] for q in questions))
    print("Available Categories:")
    for i, cat in enumerate(available_categories, start=1):
        print(f"{i}. {cat}")
    
    # User selects a category by number
    category_choice = int(input("Choose a category by number: ")) - 1
    if category_choice < 0 or category_choice >= len(available_categories):
        print("Invalid choice. Please restart the quiz.")
        return
    category = available_categories[category_choice]
    
    # Display available difficulties as a numbered list
    available_difficulties = list(set(q["difficulty"] for q in questions))
    print("\nAvailable Difficulties:")
    for i, diff in enumerate(available_difficulties, start=1):
        print(f"{i}. {diff}")
    
    # User selects a difficulty by number
    difficulty_choice = int(input("Choose a difficulty by number: ")) - 1
    if difficulty_choice < 0 or difficulty_choice >= len(available_difficulties):
        print("Invalid choice. Please restart the quiz.")
        return
    difficulty = available_difficulties[difficulty_choice]
    
    # Filter questions based on the user's choices
    filtered_questions = filter_questions(questions, category, difficulty)
    
    if not filtered_questions:
        print(f"No questions available for category '{category}' and difficulty '{difficulty}'.")
        return
    
    score = 0
    user_answers = []
    
    print("\nWelcome to the Quiz! Answer the following questions.\n")

    # Shuffle and select 10 random questions from the filtered list
    quiz_questions = random.sample(filtered_questions, min(10, len(filtered_questions)))
    
    for i, question in enumerate(quiz_questions, start=1):
        print(f"Q{i}: {question['question']}")
        
        for key, answer in question['answers'].items():
            if answer:
                print(f"  {key[-1].upper()}) {answer}")
        
        user_answer = input("Your answer (A, B, C, D): ").strip().lower()
        correct = check_answer(user_answer, question["correct_answers"])
        
        # Track user's answer and whether it was correct
        user_answers.append({
            "question": question["question"],
            "your_answer": user_answer,
            "correct": correct
        })

        if correct:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect.\n")

    print(f"Quiz Complete! Your score: {score}/{len(quiz_questions)}")

    # Collect feedback
    feedback = input("Please provide your feedback for this quiz: ")
    save_feedback({
        "timestamp": datetime.now().isoformat(),
        "score": score,
        "total": len(quiz_questions),
        "category": category,
        "difficulty": difficulty,
        "feedback": feedback,
        "answers": user_answers
    })

    print("Thank you! Your feedback has been saved.")

# Check if the user's answer matches the correct answer
def check_answer(user_answer, correct_answers):
    answer_key = f"answer_{user_answer.lower()}"
    return correct_answers.get(answer_key + "_correct") == "true"

# Run the quiz
if __name__ == "__main__":
    run_quiz()

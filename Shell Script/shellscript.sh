#!/bin/bash

# Initialize score
score=0

# Function to ask a question and check the answer
ask_question() {
    local question="$1"
    local answer="$2"

    echo -e "Question: $question"
    read -p "Your answer: " user_answer

    if [ "$user_answer" = "$answer" ]; then
        echo "Correct!"
        ((score++))
    else
        echo "Incorrect. The correct answer is: $answer"
    fi
    echo
}

# Main quiz
clear
echo "Welcome to the Quiz!"
echo

ask_question "What is the capital of France?" "Paris"
ask_question "What is the largest planet in our solar system?" "Jupiter"
ask_question "How many continents are there on Earth?" "7"
ask_question "What is the boiling point of water in Celsius?" "100"

# Display the final score
clear
echo "Quiz completed! Your score: $score / 4"

import random

# Define the cricket quiz questions and answers
cricket_quiz = [
    {
        "question": "Who is known as the 'God of Cricket'?",
        "options": ["A. Sachin Tendulkar", "B. Virat Kohli", "C. Ricky Ponting"],
        "correct_answer": "A"
    },
    {
        "question": "Which country won the ICC Cricket World Cup in 2019?",
        "options": ["A. Australia", "B. India", "C. England"],
        "correct_answer": "C"
    },
    {
        "question": "What is the highest individual score in a One Day International (ODI) cricket match?",
        "options": ["A. 183", "B. 200", "C. 264"],
        "correct_answer": "C"
    },
    {
        "question": "Who has the most Test wickets in cricket history?",
        "options": ["A. James Anderson", "B. Anil Kumble", "C. Shane Warne"],
        "correct_answer": "B"
    },
    {
        "question": "What is the length of a cricket pitch in meters?",
        "options": ["A. 18.12 meters", "B. 20.12 meters", "C. 22.12 meters"],
        "correct_answer": "A"
    }
]

# Shuffle the questions for variety
random.shuffle(cricket_quiz)

# Initialize the user's score
score = 0

# Display welcome message and rules
print("Welcome to the Cricket Quiz!")
print("You will be presented with multiple-choice questions about cricket. Choose the correct option.")
print("Let's test your cricket knowledge!\n")

# Iterate through each question
for index, question_data in enumerate(cricket_quiz, start=1):
    print(f"Question {index}: {question_data['question']}")
    
    # Display answer options
    for option in question_data["options"]:
        print(option)
    
    # Prompt the user for an answer
    user_answer = input("Your answer (A/B/C): ").strip().upper()
    
    # Evaluate the user's answer
    if user_answer == question_data["correct_answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Sorry, the correct answer was {question_data['correct_answer']}.\n")

# Calculate the final score
total_questions = len(cricket_quiz)
final_score = (score / total_questions) * 100

# Display final results
print(f"Quiz Completed! Your Final Score: {final_score}%")
if final_score == 100:
    print("Congratulations! You're a cricket genius.")
elif final_score >= 70:
    print("Well done! You passed the cricket quiz.")
else:
    print("You might want to brush up on your cricket knowledge. Keep learning!")


import json
import math

with open("questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)


for question in data:
    for index,alternatives in enumerate(question["alternatives"]):
        print(index + 1, "-", alternatives)
    use_choice = int(input("Enter answer: "))
    question["user_choice"] = use_choice

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    message = f"{result} {index + 1} - Your answer: {question['user_choice']}, " \
              f"Correct answer is: {question['correct_answer']}"
    print(message)


print(score, "/", len(data))

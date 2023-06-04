import json

with open("bonus15.json","r") as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["questions"])
    for index,attributes in enumerate(question["attributes"]):
        print(index + 1,'-',attributes)
    users_choice = int(input("Enter your answer:"))
    question["users_choice"] = users_choice

score = 0
for index, question in enumerate(data):
    if question["users_choice"] == question["Correct_ans"]:
        score = score + 1
        result = "correct answer"
    else:
        result = "Wrong answer"

    message = f"{index + 1} {result} - Your answer: {question['users_choice']} ," \
              f"Correct Answer : {question['Correct_ans']}"
    print(message)

print(score,'/', len(data))
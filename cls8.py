# todays_date = input("Enter todays date: ")
# users_mood = input("Enter your mood ,happy or sad??: ")
# thoughts = input("Thought of the day:\n")
#
# with open(f"{todays_date}.txt","w") as file:
#     file.write(users_mood)
#     file.write(thoughts)

while True:
    with open(r'C:\Disha\venv\heads.txt','r') as file:
        files = file.readlines()

    users_answer = input("throw the coin and enter head or tail here: ?") + "\n"

    files.append(users_answer)

    with open(r'C:\Disha\venv\heads.txt','w') as file:
        file.writelines(files)

    heads_count = files.count("head\n")
    percentage = heads_count / len(files) * 100
    print(f'Head = {percentage}%')


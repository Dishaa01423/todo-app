# def avg_temp():
#     with open("report.txt",'r') as file:
#         temp = file.readlines()
#     values = temp[1:]
#     values = [float(i) for i in values]
#
#     average = sum(values)/len(values)
#     return average
#
# average = avg_temp()
# print(average)

# decoupling funtion example :-
feet_inches = input("Enter feet and inches: ")

def func(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}

def convert(feet,inches):
     meters = feet * 0.3048 + inches * 0.0254
     return meters

functn = func(feet_inches)

result = convert(functn["feet"], functn["inches"])

print(f"{functn['feet']} feet and {functn['inches']} is equal to {result}")

if result > 1:
    print("Kid is too small")
else:
    print("Kid can use slide")

# def calculate_time(h,g=9.80665):
#     t = (2 * h / g) ** 0.5
#     return t
# """default parameters always comes after non-default parameters"""
#
# time = calculate_time(100)
# print(time)

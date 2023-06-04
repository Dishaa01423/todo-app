# remove extra space
# file = open(r"C:\Disha\todos.txt","r")
# todo = file.readlines()

# best method
# for index,item in enumerate(todo):
#     item = item.strip('\n')
#     print(f'{index + 1}-{item}')

# new_todo = []
# for item in todo:
#     item = item.strip('\n')
#     new_todo.append(item)
# for index, item in enumerate(new_todo):
#     print(f'{index + 1}-{item}')

# new_todo = [item.strip('\n') for item in todo]
# for index, item in enumerate(new_todo):
#       print(f'{index + 1}-{item}')

# 77.
# names = ["john smith", "jay santi", "eva kuki"]
# new = [name.title() for name in names]
# print(new)

# usernames = ["john 1990", "alberta1970", "magnola2000"]
# new = [len(i) for i in usernames]
# print(new)

# user_entries = ['10', '19.1', '20']
# new = [float(i) for i in user_entries]
# print(new)

user_entries = ['10', '19.1', '20']
new = [float(i) for i in user_entries]
print(sum(new))
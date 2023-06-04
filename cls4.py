# CODE 1
filenames = ['document', 'report', 'presentation']
for i,char in enumerate(filenames):
    print(f'{i}-{char.capitalize()}.txt')

# CODE 2
ips = ['100.122.133.105', '100.122.133.111']
for x,char in enumerate(ips):
    x = int(input("Enter the index of IP you want: "))
    print(f'You chose: {char}')

ips = ['100.122.133.105', '100.122.133.111']
users_choice = int(input("Enter the index of tha IP you want: "))
address = f"You chose: {ips[users_choice]}"
print(address)



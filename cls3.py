# CODE 1
ingredients = ["john smith", "sen plakay", "dora ngacely"]
for i in ingredients:
    i = i.title()
    print(i)

# CODE 2
while True:
    users_country = input("Which country u belong to USA, India, or Germany?? -")
    users_country.strip()

    match users_country:
        case 'USA':
            print("Hello")
        case 'India':
            print("Namaste")
        case 'Germany':
            print("Hallo")



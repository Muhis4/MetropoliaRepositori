print("Welcome to the Game!\nPlease, enter your name and age.")
name = input("Name: ")
age = int(input("Age: "))

if(age < 12):
    print(f"Sorry {name}, you are not allowed to play this game.")
    exit()

print("Welcome to the game! Please, give command:\n1. Character\n2. Game info\n3. Commands\n4. Exit")
command = int(input("Command (number 1-4): "))

while True:
    if(command == 1):
        print(f"Character name: {name}\nCharacter age: {age}")
    elif(command == 2):
        print("This is a simple text-based game where you can create a character and have fun in future updates.")
    elif(command == 3):
        print("Available commands:\n1. Character\n2. Game info\n3. Commands\n4. Exit")
    elif(command == 4):
        print("Exiting the game. Goodbye!")
        exit()
    command = int(input("Command (number 1-4): "))
    
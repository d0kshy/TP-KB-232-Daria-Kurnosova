import random

choices = ["stone", "paper", "scissors"]
usersChoice = ''
winsCounter = 0

while usersChoice != "Exit" and usersChoice != "exit":
    usersChoice = input("Choose one option: [St stone, P paper, Sc scissors]\nYour answer is ")
    compChoice = choices[random.randint(0, 2)]

    if usersChoice == "St" or usersChoice == "st" or usersChoice == "Sc" or usersChoice == "sc" or usersChoice == "P" or usersChoice == "p":
        print(f"Computer answer is {compChoice}")

    # Drawn
    if compChoice == "stone" and (usersChoice == "St" or usersChoice == "st"):
        print("- - Drawn - -\n")

    elif compChoice == "scissors" and (usersChoice == "Sc" or usersChoice == "sc"):
        print("- - Drawn - -\n")

    elif compChoice == "paper" and (usersChoice == "P" or usersChoice == "p"):
        print("- - Drawn - -\n")

    # You won
    elif compChoice == "stone" and (usersChoice == "P" or usersChoice == "p"):
        winsCounter += 1
        print("- - You won - -")
        print(f"You already won for {winsCounter} times\n")

    elif compChoice == "scissors" and (usersChoice == "St" or usersChoice == "st"):
        winsCounter += 1
        print("- - You won - -")
        print(f"You already won for {winsCounter} times\n")

    elif compChoice == "paper" and (usersChoice == "Sc" or usersChoice == "sc"):
        winsCounter += 1
        print("- - You won - -")
        print(f"You already won for {winsCounter} times\n")

    # You lose
    elif compChoice == "stone" and (usersChoice == "Sc" or usersChoice == "sc"):
        print("- - You lose - -\n")

    elif compChoice == "paper" and (usersChoice == "St" or usersChoice == "st"):
        print("- - You lose - -\n")

    elif compChoice == "scissors" and (usersChoice == "P" or usersChoice == "p"):
        print("- - You lose - -\n")

    # Wrong input message
    elif usersChoice != "Exit" and usersChoice != "exit":
        print("Wrong option! Try again.\n")

    else:
        print("Thanks for playing!")

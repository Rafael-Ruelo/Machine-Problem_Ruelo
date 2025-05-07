import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def simpleCalculator():
    clear_screen()
    result = 0
    while True:
        print("---Simple Calculator---")
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter your second number: "))

        opChoice = int(input("Choose an operation [1-5]: "))

        
        if opChoice == 1:
            result = num1 + num2
            print(num1, "+", num2 ,"is" ,result)
            
        if opChoice == 2:
            result = num1 - num2
            print(num1, "-", num2 ,"is" ,result)
            
        if opChoice == 3:
            result = num1 * num2
            print(num1, "*", num2 ,"is" ,result)
            
        if opChoice == 4:
            result = num1 / num2
            print(num1, "/", num2 ,"is" ,result)
            
        if opChoice == 5:
            print("Thanks for using my calculator! ")
            break


        repeatCalc = (input("Do you want to use it again?: ")).strip().lower()
        if repeatCalc == 'y' or repeatCalc == '':
            clear_screen()
            print("Restarting...")
        else:
            print("Thanks for using my program!")
            break

def tempConverter(): 
    clear_screen()
    tempResult = 0.0
    while True:
        print("---Temperature Calculator---")
        print("Choices: " \
        "\n 1. Convert Celsius to Fahrenheit" \
        "\n 2. Convert Fahrenheit to Celsius" \
        "\n 3. Exit")

        tempChoice = int(input("Enter your choice: "))

        if tempChoice == 1:
            celsius = float(input("Enter Celsius: "))
            tempResult = (celsius * 9/5) + 32
            print(celsius, "To Fahrenheit is: ", tempResult)

        if tempChoice == 2:
            fahrenheit = float(input("Enter Fahrenheit: "))
            tempResult = (fahrenheit - 32) * 5/9
            print(fahrenheit, "To Celsius is: ", tempResult)


        repeatTemp = (input("Do you want to do it again?: ")).strip().lower()
        if repeatTemp == 'y' or repeatTemp == '':
            clear_screen()
            print("Restarting...")
        if tempChoice == 3:
            print("Thanks for using my program!")
            break
        else:
            print("Invalid choice!")
            break

def toDoList():
    clear_screen()
    tasks = []
    
    while True:
        print("--- To-Do List---" 
              "\n1. Add task"
              "\n2. View Task"
              "\n3. Remove Tasks"
              "\n4. Exit")
        listChoice = int(input("Enter choice: "))
        if listChoice == 1:
            while True:
                task = input("Add your task: ")
                tasks.append(task)
                repeatList = (input("Do you want to add another task?: ")).strip().lower()
                if repeatList == 'y' or repeatList == '':
                    print("Loading...")
                else:
                    break

        if listChoice == 2:
            if not tasks:
                print("There are no tasks to delete")
                return
            print("Your tasks: \n")
            for task in tasks:
                print(task)

        if listChoice == 3:
            if not tasks:
                print("There are no tasks to view")
                return
            print("Removed previous task ", tasks.pop())

        if listChoice == 4:
            print("Thanks for using my program!")
            break

        repeatList = (input("Do you want to go back to the menu?: ")).strip().lower()
        if repeatList == 'y' or repeatList == '':
            clear_screen()
        else:
            print("Thanks for using my program!")
            break


def numberGuessingGame():
    clear_screen()
    attempts = 10
    while True:
        secret_number = random.randint(1, 100)
        print("---Number Guessing Game---")
        print("1. Play Game")
        print("2. Exit")

        gameChoice = (int(input("Pick one: ")))

        if gameChoice == 1:
            while True:
                userNum = (int(input("Take a guess![1-100]: ")))
                if userNum < 1 or userNum > 100:
                    print("Oops! your guess is out of bounds!")
                if userNum > secret_number:
                    print("Your guess is too high!")
                    attempts -= 1
                    print("You now have", attempts, "attempts left!")
                if userNum < secret_number:
                    print("Your guess is too low!")
                    attempts -= 1
                    print("You now have", attempts, "attempts left!")
                if userNum == secret_number:
                    print("Congratulations! you guessed it!")
                    break
                if attempts == 0:
                    print("You have no more attempts! The secret number was: ", secret_number)
                    repeatGame = (input("Do you want to play again?: ")).strip().lower()
                    if repeatGame == 'y' or repeatGame == '':
                        clear_screen()
                        print("Restarting...")
                        attempts = 10
                        break
                    else:
                        print("Thanks for playing my game!")
                        clear_screen()
                        break
        elif gameChoice == 2:
            print("Thanks for playing my game!")
            break


def gradeCalc():
    clear_screen()
    scores = []
    while True:
        print("---Student Grade Calculator---"
              "\n1. Add Score"
              "\n2. Calculate Average"
              "\n3. Exit")
        gradeChoice = (int(input("Enter your choice: ")))
        if gradeChoice == 1:
            while True:
                score = (float(input("Enter your score: ")))
                if score < 0 or score > 100:
                    print("Invalid score!")
                    continue
                else:
                    print("Score added!")
                    scores.append(score)
                    repeatGrade = (input("Do you want to add another score?: ")).strip().lower()
                    if repeatGrade == 'y' or repeatGrade == '':
                        continue
                    else:
                        print("Invalid input!")
                        break
        if gradeChoice == 2:
            if not scores or len(scores) == 0:
                print("You have no scores to calculate!")
                return
            if len(scores) > 0:
                averageScore = sum(scores) / len(scores) 
                print("The average of your scores are: ", averageScore) 
                repeatGrade = (input("Do you want to add another score?: ")).strip().lower()
                if repeatGrade == 'y' or repeatGrade == '':
                    continue
                else:
                    print("Invalid input!")
                    break
        if gradeChoice == 3: 
            print("Thanks for using my program!")
            break
        else:
            print("Invalid choice!")
            break

while True:
    print("Machine Problem")
    print("Functions: "
    "\n1. Simple Arithmetic calculator"
    "\n2. Temperature Converter"
    "\n3. To-Do List"
    "\n4. Number Guessing Game"
    "\n5. Student Grade Calculator")

    choice = (int(input("Enter your choice: ")))

    if choice == 1:
        simpleCalculator()

    elif choice == 2:
        tempConverter()

    elif choice == 3: 
        toDoList()

    elif choice == 4: 
        numberGuessingGame()

    elif choice == 5:
        gradeCalc()
    else:
        print("Invalid choice!")
        break

    clear_screen()
    repeatProgram = (input("Do you want to try our services again?: ")).strip().lower()
    if repeatProgram == 'y' or repeatProgram == '':
        clear_screen()
        print("Restarting...")
    else:
        print("Thanks for using my program!")
        break
# toolkit.py
# Personal Mini-Toolkit - a menu-driven program with four tools.
# Each tool is a separate function, and the main loop keeps showing the
# menu until the user chooses Quit.

import random

# Tool 1: Number Guessing Game
# The computer picks a secret number and the user guesses until
# they get it right, with "too high" / "too low" hints.

def guessing_game():
    print("\n Number Guessing Game ")
    secret = random.randint(1, 20)
    attempts = 0

    while True:
        guess_text = input("Guess a number between 1 and 20: ")

        try:
            guess = int(guess_text)
        except ValueError:
            print("That is not a number. Try again.")
            continue

        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You got it in {attempts} attempts.")
            break


# Tool 2: To-Do List
# A running list the user can add to, view, or remove items from.
# Shows the whole list change while the program runs.
# ---------------------------------------------------------------

def todo_list():
    print("\n To-Do List")
    tasks = []

    while True:
        action = input("add / view / done / back: ").strip().lower()

        if action == "add":
            task = input("Task to add: ").strip()
            if task:
                tasks.append(task)
                print(f"Added: {task}")
            else:
                print("Empty task ignored.")

        elif action == "view":
            if tasks:
                print("Your tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"  {index}. {task}")
            else:
                print("Your list is empty.")

        elif action == "done":
            task = input("Task to mark done: ").strip()
            if task in tasks:
                tasks.remove(task)
                print(f"Done: {task}")
            else:
                print("That task is not on your list.")

        elif action == "back":
            print("Returning to the main menu.")
            break

        else:
            print("Unknown command. Type add, view, done, or back.")


# Tool 3: Simple Calculator
# Asks for two numbers and an operation, then prints the result.
# Uses try / except so non-number input never crashes the program.
# ---------------------------------------------------------------

def calculator():
    print("\n Simple Calculator ")

    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
    except ValueError:
        print("Those were not numbers. Returning to the menu.")
        return

    op = input("Operation (+, -, *, /): ").strip()

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            print("Cannot divide by zero.")
            return
        result = a / b
    else:
        print("Unknown operation.")
        return

    print(f"{a} {op} {b} = {result}")


# Tool 4: Name Formatter
# Asks for a first and last name and prints it in several styles.
# ---------------------------------------------------------------
def name_formatter():
    print("\n Name Formatter ")
    first = input("First name: ").strip()
    last = input("Last name: ").strip()

    if not first or not last:
        print("Both names are needed.")
        return

    full = f"{first} {last}"
    initials = f"{first[0].upper()}.{last[0].upper()}."

    print(f"Title case:  {full.title()}")
    print(f"Uppercase:   {full.upper()}")
    print(f"Initials:    {initials}")


# Main menu
# Shows the numbered menu, reads the choice, and routes to the
# matching tool. Loops until the user picks Quit.
# ---------------------------------------------------------------
def main():
    print("Welcome to your Personal Mini-Toolkit!")

    while True:
        print("\n MY PERSONAL MINI-TOOLKIT")
        print("1. Number Guessing Game")
        print("2. To-Do List")
        print("3. Simple Calculator")
        print("4. Name Formatter")
        print("5. Quit")

        choice = input("Choose a tool (1-5): ").strip()

        if choice == "1":
            guessing_game()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            calculator()
        elif choice == "4":
            name_formatter()
        elif choice == "5":
            print("Thanks for using your toolkit. Goodbye!")
            break
        else:
            print("Sorry, that is not a valid choice. Please pick 1-5.")


# Start the program
main()

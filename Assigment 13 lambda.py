'''"""Q1:Write a Python lambda function that takes two parametersa and b, and 
returns the sum of their squares. Assign the lambda function to a variable
called sum_of_squares. test the lambda functionby passing different values for a and b. """

sum_of_squares = lambda a, b: a**2 + b**2
print(sum_of_squares(2, 3))

sum_of_squares = lambda a, b: a**2 + b**2
print(sum_of_squares(7, 4))


"""Write a decorator function called timer that measures the execution time of a 
function and prints the elapsed time. Apply the timer decorator to a function of your 
choice and test its functionality."""

import time


def timer(func):
    def wrapper(*args, **kwargs):
        T1 = time.time()
        result = func(*args, **kwargs)
        T2 = time.time()
        T3 = T2 - T1
        print(f"{func.__name__} took {T3} seconds to execute task")
        return result

    return wrapper


@timer
def funct():
    time.sleep(1)


funct()


@timer
def simple_cal(a, b, c):
    return a * b / c


e = simple_cal(2, 2, 1)
print(e)


@timer
def greet():
    name = input("Please enter your name: ")
    print(f"Hello, {name}! This is Mercy.")


greet()


@timer
def complaint_form():
    name = input("please provide your name ")
    problem = str(input("Please describe your problem "))
    Ideas = str(input("What do you think is broken or damaged "))
    estimated_fix_time = input("When do you need it working again ")
    price = int(
        input(
            "How much did you pay for the services 'just the value in number please' "
        )
    )
    warranty_date = input("When is your warranty due ")
    try:
        if price == str:
            print("Please provide a valid amount")
        else:
            pass
    except ValueError:
        print("invalid")

    print("PLEASE CONFIRM YOUR ENTRIES AS SEEN BELOW")
    print(f"my name is {name}")
    print(f"I have a complait on the {problem} aspect of your program")
    print(f"I think the {Ideas} is broken or not working")
    print(f"I am hoping the problem to be fix within {estimated_fix_time} working days")
    print(f"I paid ${price} for the services")
    print(f"My warranty is due {warranty_date}")


complaint_form()


@timer
def input_diff_4rm_users(first_name, last_name, age, location):
    first_name = input("what is your  first name ")
    last_name = input("what is your name ")
    age = input("How old are you? ")
    location = input("what is your location ")
    return first_name + " " + last_name + " " + age + " " + location


user_info = input_diff_4rm_users("first_name", "last_name", "age", "location")
print(user_info)'''


# rock paper and scissor game


def get_user_choice():
    user_choice = input("enter a chioce (rock paper or scissors); ")
    return user_choice


def get_computer_choice():
    import random

    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    return computer_choice


computer_choice = get_computer_choice()
print(computer_choice)


def winner(x, y):
    if user_choice == computer_choice:
        print("its a tie, go again")
    elif (
        user_choice == "rock"
        and computer_choice == "scissors"
        or user_choice == "paper"
        and computer_choice == "rock"
        or user_choice == "scissors"
        and computer_choice == "paper"
    ):
        print("YOU WIN")
    else:
        print("COMPUTER WINS")


user_choice = get_user_choice()
computer_choice = get_computer_choice()
result = winner(x=user_choice, y=computer_choice)
print(result)

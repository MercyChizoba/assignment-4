#PART 1A
def is_even(number):
    if number % 2 == 0:
        print(True)
    else:
        print(False)
is_even(10)

#question 2
def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
factorial(-1)

#question 3
def fibonacci(n):
    if n <= 0:
        return "Invalid input. n must be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
fibonacci(2)

#WHILE LOOP
secret_number = 8
guess = 0
attempts = 0

while guess != secret_number:
    try:
        guess = int(input("Guess a number (between 1 and 10): "))
        attempts += 1

        if guess < secret_number:
            print("Try a higher number.")
        elif guess > secret_number:
            print("Try a lower number.")
        else:
            print(f"Congratulations! You've guessed the secret number {secret_number} in {attempts} attempts!")
    except ValueError:
        print("invalid")
    

#WHILE LOOP QUESTION 2
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 4
    return True

count = 0
number = 1 

while count < 6:
    if is_prime(number):
        print(number)
        count += 1
    number += 1


#FOR LOOP QUESTION 1
fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    uppercase_fruit = fruit.upper()
    char_count = len(fruit)
    print(f"{uppercase_fruit} ({char_count})")

#FOR LOOP QUESTION 2
number = 7

for multiple in range(1, 13):
    result = number * multiple
    print(f"{number} x {multiple} = {result}")


#IF STATEMENT
Fav_number = int(input ("What is your fav number = " ))
if Fav_number == 0:
    print ("number is zero")
if Fav_number >= 0:
    print ("number is a positive number")
if Fav_number < 0:
    print("number is a negative number")

#GRADING SYSTEM
GRADE = int(input ("What is your score from 1 to 100 = " ))
if GRADE >= 90:
    print("A" + " " + str("EXCELLENT"))
if GRADE >= 80:
    print("B" + " " + str("VERY GOOD"))
if GRADE >= 70:
    print("C" + " " + str("GOOD"))
if GRADE >= 60:
    print("D" + " " + str("FAIR"))
if GRADE <= 59:
    print("F" + " " + str("FAIL"))

#PART 2 OBJECT ORIENTED PROGRAMMING
class dog ():
    def __init__(self, name, age):
        self.name = name
        self.age = age
dog = dog("Billy", 4)
print(f"{dog.name} is {dog.age} years old.")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"Woof! My name is {self.name}.")

dog = Dog("Billy", 4)
dog.bark()






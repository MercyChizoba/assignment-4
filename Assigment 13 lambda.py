'''Q1:Write a Python lambda function that takes two parametersa and b, and 
returns the sum of their squares. Assign the lambda function to a variable
called sum_of_squares. test the lambda functionby passing different values for a and b. '''

sum_of_squares = lambda a,b: a**2 + b**2
print(sum_of_squares(2,3))

sum_of_squares = lambda a,b: a**2 + b**2
print(sum_of_squares(7,4))



'''Write a decorator function called timer that measures the execution time of a 
function and prints the elapsed time. Apply the timer decorator to a function of your 
choice and test its functionality.'''

import time
def timer(func):
    def wrapper(*args, **kwargs):
        T1= time.time()
        result = func(*args, **kwargs)
        T2 =time.time()
        T3 = T2-T1
        print(f"{func.__name__} took {T3} seconds to execute task")
        return result

    return wrapper

@timer
def funct():
    time.sleep(1)
funct()
@timer
def simple_cal(a, b, c):
    return a*b/c
e = simple_cal(2, 2, 1)
print(e)

def greet():
   name = input("Please enter your name: ")
    print(f"Hello, {name}! Welcome to our program.")

greet()

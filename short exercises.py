# while loop exercises. 1) Write a program to keep asking for a number until
# you enter a negative number. At the end, print the sum of all entered numbers.
# 2) Write a program to ask for a name until the user enters END.

trial = 0
guess = 0
while True:
    try:
        guess = int(input("Give a number  "))
        trial += 1
        if guess < 0:
            print("great job")
            break
        else:
            print("give a new one")
            guess > 0
            continue
    except:
        print("not valid")
# print("the sum of all number is:", trial)

# TASK 2

name = str
end = str("END")
while True:
    try:
        name = str(input("tell us your name "))
        if name != end:
            print("go on")
            continue
        elif name.isdigit():
            print("not a valid name")
        else:
            name == end
            print("thank you")
            break
    except:
        print("give a name")

    print("hello world")
    print("hello")

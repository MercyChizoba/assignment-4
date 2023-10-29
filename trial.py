'''x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()
print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#format strings
quantity = 2
item = 45
price = 4
my_order = "i want {} of {} at {} dollars"
print (my_order.format(quantity, item, price))
print(isinstance(1, int))
print(isinstance(1, float))
x = 2
y = 6
print(x**y)
print(pow(2,5))
A = int(input("enter a fav number "))
if A == str:
  print ("ADD ONLY NUMBERS")
B = int(input("enter a number "))
if A > B:
  print("A")
elif A == B:
   print("same value")
else:
  print ("B")

#HOW TO GET JUST THE INTERGER NUMBER
#FROM A FLOAT
t = float(input(str("Drop a number here ")))
r = round(t)
if r>t:
  mainint = r - 1
else:
  mainint = int(r)
print (mainint) 

#LOOPS!!!!!!!!
N = int(input("guve a number "))
i = 6
while (i < N):
  print (i)
  i += 1 #i = i+1
print ("no please")

kn = int(input("number please"))
i = 17
while i < kn:
  if i%2 == 0:
     i +=1
     print (i)
  else:
    pass
 
print("loop is over")

#Implement a guessing game using a while loop: the program 
#should keep prompting the user to guess a secret number until the correct
#number is guessed

guess = 0
secret_number = 8
trial = 0
while guess != secret_number:
    try:
        guess =int(input("whats your guess  "))
        trial += 1

        if guess > secret_number:
            print ("too high, go again")
        elif guess < secret_number:
            print("too low try again")
        else:
            print(f"congratulation, you have gotten the secret number which is {str(secret_number)} in {trial} trial")
    except:
        print("invalid number")

#break and continueloop

j = int(input("drop a number"))
i = 2
while True:
   if i%5 ==0:
      print("ok")
      break
   else:
      print("alrighty")
      i +=1
      continue'''

#for loop 
'''listindope = ["apple", "sample", "gate", "dogg"]
for x in listindope:
   print (x)'''

#FUNCTIONS
'''A FUNCTION IS QUITE IMPORTANCE FOR PYTHON,
YOU CAN USE IT OVER AND OVER AGAIN AND CAN ASSIGN SOME
VARIBLES TO IT'''

def function1(name):
    print(name + " Ihediohamma")

function1("Mercy")
function1("blessing")
function1("chidinma")

#Calculator Function:
#Write a function that takes two numbers and an operator 
#(+, -, *, /) as input
#and returns the result of the operation
def calculatesome(x, b):
    return 5 * x + b

print(calculatesome(5,2))

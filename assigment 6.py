list = [ "apple",1,2,3,4.5, False, "hello"]
print(list)
print (len(list))
print (list[5])
if list [3]== False:
    print("that is true")
else:
    print("not true")
#for loops
cities = ["lagos","abuja","kano","newyork","ontario","berlin"]
for city in cities:
    print(city)
for city in cities:
    if city == "kano":
        print("true")
    else: print("not there")

#range
range1 = range(10)
range2 = range (-1, 9, 2)
for element in range2:
    print(element)

for e in range1:
    print(e)

#while loop
count = 5
while count >= 0:
    print (count)
    count -= 1
#list conprehension
numbers = [2, 4, 6, 7]
new_number = []
for number in numbers:
    new_number.append(number *2)
print(new_number)

#list conprehension with condition
divide_by_2 =[number for number in numbers if number % 2 ==0]
print(divide_by_2)


#FUNCTION

def greet(name):
    print("hello", name)
greet("mercy")

def smile(name):
    print("you have to smile", name)
smile("Mercy")
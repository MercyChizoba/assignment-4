#QUESTION1
number1 = int(input('Enter number:')) # number1 is 18
number2 = int(input('Enter number:')) #number2 ia 25
# ARE BOTH OF THEM EVEN
if (number1 % 2) == 0 and (number2 % 2) == 0:
    print("true")
else:
    print("false")

if (number1 % 2) == 0 or (number2 % 2) == 0:
    print("true")
else:
    print("false")

#ARE BOTH OF THEM ODD
if (number1 % 2) == 1 and (number2 % 2) == 1:
    print("true")
else:
    print("false")
if (number1 % 2) == 1 or (number2 % 2) == 1:
    print("true")
else:
    print("false")
# AT LEAST 1 IS A MULTIPLY OF 5
if (number1 % 5)  == 0 or (number2 % 5) == 0:
    print("true")

#QUESTION 2
Temp = int(input('what is the temperature for the day? ')) #temp of the day is 5 
#you can use different temp input and keep picking\inserting new inputs but i just picked 5 as the temperature for the first 3 question :)
if (Temp < 12):
    print("wear a jacket")

if (Temp < 4):
    print("wear a glove")
else:
    print("it's not so cold outside")

if (Temp < 8):
    print("wear a scarf")

TEMP = int(input ("What is the temperature for the day today"))
if TEMP > 25:
    print("Wear sunglasses")


#QUESTION 3
Rare_steak = 2
medium_steak = 4
welldown_steak = 4
burnt_steak = 8

#steak for 3 minutes
if medium_steak >= 3:
    print ("the steak is perfect")
else:
    print("you ruined my steak")

#steak for over 10 minutes
if welldown_steak >= 10:
    print ("my steak is perfect")
else:
    print("you ruined my steak and, your friend is furious")


#QUESTION 4

required_dept = 2
required_distance = 50

#for ocean
Odept = 4000
Odistance = 500

if (Odept > required_dept) and (Odistance < required_distance):
    print("you can swim here")
elif (Odept >= required_dept) and (Odistance <= required_distance):
    print("you can swim here")
else:
    print("you cannot swim here")

#lake
Ldept = 15
Ldistance = 25
if (Ldept > required_dept) and (Ldistance< required_distance):
    print("you can swim here")
elif (Ldept >= required_dept) and (Ldistance <= required_distance):
    print("you can swim here")
else:
    print("you cannot swim here")

#Swimming pool 
Sdept = 2
Sdistance = 10
if (Sdept > required_dept) and (Sdistance < required_distance):
    print("you can swim here")
elif (Sdept >= required_dept) and (Sdistance <= required_distance):
    print("you can swim here")
else:
    print("you cannot swim here")

#POND
Pdept = 0.5
Pdistance = 5
if (Pdept > required_dept) and (Pdistance < required_distance):
    print("you can swim here")
elif (Pdept >= required_dept) and (Pdistance <= required_distance):
    print("you can swim here")
else:
    print("you cannot swim here")


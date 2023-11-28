"""2.1– Coin flip
Create a module that returns the result of a coin flip
(either heads to tails). Name the module as coin.py. 
You may code the probability yourself or import random library
 from python"""
import random


def coin_flip():
    random.random()
    if random.random() > 0.75:
        print("heads")
    else:
        print("tails")


coin_flip()

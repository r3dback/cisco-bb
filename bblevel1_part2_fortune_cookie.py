# Python 3.6.5
# By: Francisco Rojo, 30/7/2018
# Cisco BB Level 1 _assignment
# 
# How to run on Python3
# > python3 <file>.py

import random


Messages = [
    "Good luck",
    "Keep trying, next time may work",
    "I see Network DevOps in your future.",
]

def message_selector() -> str:
    return random.choice(Messages)

def number_selector(n: int) -> list:
	array =[]
	for item in range(n):
		array.append(random.randint(0,500))
	return array

def create_message(n: int) -> str:
	message = message_selector()
	number = number_selector(n)
	return "{message}\nLucky Numbers: {number}".format(message=message,number=number)



def main():
	print ('Get your fortune cookie')

	i = input("How many lucky numbers would you like? : ")
	i = int(i)

	message = create_message(i)
	print ("\nHere is your fortune:\n")
	print (message)

main ()
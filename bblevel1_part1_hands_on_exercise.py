# Python 3.6.5
# By: Francisco Rojo, 30/7/2018
# Cisco BB Level 1 _assignment
# 
# How to run on Python3
# > python3 hands_on_exercise.py


import math
import random

# Expected Output
#pi is a  with a value of 3.141592653589793
#i is greater than 50
#The fruit is orange
#12 x 96 = 1152
#48 x 17 = 816
#196523 x 87323 = 17160977929


# TODO: Write a print statement that displays both the type and value of `pi`
print ("pi is a ",type(math.pi),"with a value of ",math.pi)

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0,500)
if int(i) < 50:
	print (i," is less than 50")
elif int(i) > 50:
	print (i," is greater than 50")	

# TODO: Write a conditional that prints the color of the picked fruit
select_fruit = random.choice(['orange', 'strawberry', 'bannana'])
fruit = { 'orange':'Orange','strawberry':'Red','bannana':'Yellow'}
print ("The Fruit is ",fruit.get(select_fruit))


# TODO: Write a function that multiplies two numbers and returns the result

def _multiply (n1,n2):
	result = int(n1) * int (n2)
	return(result)

# TODO: Now call the function a few times to calculate the following answers

n1=12
n2=96
print (n1," x ",n2," = ",_multiply(n1,n2))
n1=48
n2=17
print (n1," x ",n2," = ",_multiply(n1,n2))
n1=196523
n2=87323
print (n1," x ",n2," = ",_multiply(n1,n2))




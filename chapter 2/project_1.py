'''
1. The tax calculator program of the case study outputs a 
floating-point number that might show more than two digits of precision. 
Use the round function to modify the program to display at most 
two digits of precision in the output number.

'''
import math

print(f"value of pi {math.pi}") 

print (f"value of pi with 2 decimal {round(math.pi,2)}")

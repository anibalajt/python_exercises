'''
  1.	Package Newton’s method for approximating square roots
  (Case Study 3.6) in a function named newton. This function expects
  the input number as an argument and returns the estimate of its square
  root. The script should also include a main function that allows the user
  to compute square roots of inputs until she presses the enter/return key
'''


import math
def newton(x):
    # Initialize the tolerance and estimate
    tolerance = 0.000001
    estimate = 1.0
    # Perform the successive approximations
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break
    return estimate


def main():
    end = False
    while (end == False):
        # Receive the input number from the user
        x = float(input("Enter a positive number: "))

        estimate = newton(x)
        # Output the result
        print("The program's estimate:", estimate)
        print("Python's estimate:	", math.sqrt(x))

        if(input("exit (y/n)") == "y"):
            end = True
    print("\nthe program is over")


main()

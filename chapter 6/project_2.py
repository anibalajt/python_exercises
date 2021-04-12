'''
  2.Convert Newton’s method for approximating square roots 
  in Project 1 to a recur- sive function named newton. 
  (Hint: The estimate of the square root should be passed 
  as a second argument to the function.)
'''


import math
# Initialize the tolerance and estimate
tolerance = 0.000001
estimate = 1.0


def newton(x, estimate):
    # Perform the successive approximations
    estimate = (estimate + x / estimate) / 2
    difference = abs(x - estimate ** 2)
    if difference <= tolerance:
        return estimate

    return newton(x, estimate)


def main():
    end = False
    while (end == False):
        # Receive the input number from the user
        x = float(input("Enter a positive number: "))

        # Output the result
        print("The program's estimate:", newton(x, estimate))
        print("Python's estimate:	", math.sqrt(x))

        if(input("exit (y/n)") == "y"):
            end = True
    print("\nthe program is over")


main()

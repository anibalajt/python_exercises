'''
2.	Write a program that accepts the lengths of three sides 
    of a triangle as inputs. The program output should 
    indicate whether or not the triangle is a right tri-angle. 
    Recall from the Pythagorean theorem that in a right triangle, 
    the square of one side equals the sum of the squares of 
    the other two sides.

'''
def right_angled(x, y, z):
    if (x*x+y*y == z*z) or (z*z+y*y == x*x) or (x*x+z*z == y*y):
        return "The triangle is a right tri-angle."
    else:
        return "The triangle is not a right tri-angle.."


def main():
    end = False
    while (end == False):
        print("Enter lengths of the triangle sides: ")
        x = int(input("x: "))
        y = int(input("y: "))
        z = int(input("z: "))

        msg = right_angled(x, y, z)

        print(msg)
        
        if(input("exit (y/n)") == "y"):
            end = True

main()

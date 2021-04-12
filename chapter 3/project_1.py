'''
1.	Write a program that accepts the lengths of three sides 
    of a triangle as inputs. The program output should 
    indicate whether or not the triangle is an equilateral 
    triangle.

'''
end = False
while (end == False):
    print("Enter lengths of the triangle sides: ")
    x = int(input("x: "))
    y = int(input("y: "))
    z = int(input("z: "))

    if x == y == z:
        print("Equilateral triangle")
    else:
        print("It is not an equilateral triangle")

    if(input("exit (y/n)") == "y"):
        end = True

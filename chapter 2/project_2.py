'''
2.	You can calculate the surface area of a cube if you know
    the length of an edge. Write a program that takes the length
    of an edge (an integer) as input and prints the cube’s surface
    area as output.
'''

#get the length of any side
l = float(input('Enter the length of any side of a Cube: '))

#If we know the length of any edge in Cube then we can calculate the surface area of a Cube using the formula:
#Surface Area of a Cube = 6l² (Where l is the Length of any side of a Cube).

sa = 6 * (l * l)

print(f"Surface area of cube = {sa}")

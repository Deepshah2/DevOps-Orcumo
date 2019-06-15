
"""
Program to check if two lines A(X1,X2) and B(X3,X4) on the x-axis are overlapping.
Variables used:
x1: coordinate 1 of line1
x2: coordinate 2 of line1
x3: coordinate 1 of line2
x4: coordinate 2 of line2

TEST CASES:
1.) x1 = 1, x2 = 3, x3 = 2, x4 = 5
2.) x1 = 1, x2 = 5, x3 = 3, x4 = 5
3.) x1 = 2, x2 = 6, x3 = 3, x4 = 5
4.) x1 = 1, x2 = 6, x3 = 0, x4 = 8
5.) x1 = 4, x2 = 8, x3 = 7, x4 = 8
6.) x1 = 4, x2 = 8, x3 = 4, x4 = 6
7.) x1 = 4, x2 = 8, x3 = 4, x4 = 8

"""


def check_valid(x2,x1):
    """
    Function to check if coordinates entered for the line are valid.
    Returns True if line is not valid.
    x2: second coordinate
    x1: first coordinate
    """
    if x2 < x1 or x2==x1:
        return True

def check_overlap(x1,x2,x3,x4):
    """
    Function to check if the two lines entered are overlapping
    x1: first coordinate of line1
    x2: second coordinate of line1
    x3: first coordinate of line2
    x4: first coordinate of line2
    """
    if x3<x2 and x4>=x2:
        return True
    elif x3<=x1 and x4>x1:
        return True
    elif x3>x1 and x4<x2:
        return True
    elif x3<=x1 and x4>=x2:
        return True
    else:
        return False


x1 = input("Enter line X1 of line 1:\t")
x2 = input("Enter line X2 of line 1:\t")
"""
Querying user repeatedly until a valid value for x2 is provided.
"""
while check_valid(x2,x1):
    x2 = input("Enter x2 again, can't be smaller than or equal to x1:\t")


x3 = input("Enter line X3 of line 2:\t")
x4 = input("Enter line X4 of line 2:\t")

"""
Querying user repeatedly until a valid value for x1 is provided.
"""
while check_valid(x4,x3):
    x4 = input("Enter x4 again, can't be smaller than or equal to x3:\t")


"""
Calling function check_overlap to check if there is an overlap.
"""

if check_overlap(x1,x2,x3,x4):
    print("There is an overlap")
else:
    print("No overlap")

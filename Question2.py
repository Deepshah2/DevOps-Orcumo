
"""
Program to check if two lines A(X1,X2) and B(X3,X4) on the x-axis are overlapping.

TEST CASES:
1.) x1 = 1, x2 = 3, x3 = 2, x4 = 5
2.) x1 = 1, x2 = 5, x3 = 3, x4 = 5
3.) x1 = 2, x2 = 6, x3 = 3, x4 = 5
4.) x1 = 1, x2 = 6, x3 = 0, x4 = 8
"""


def check_valid(x2,x1):
    """
    Function to check if coordinates entered for the line are valid.
    """
    if x2 < x1 or x2==x1:
        return True

def check_overlap(x3,x2):
    """
    Function to check if the two lines entered are overlapping
    """
    if x3<x2 and x4>x2:
        return True
    elif x3<x1 and x4>x1:
        return True
    elif x3>x1 and x4<x2:
        return True
    elif x3<x1 and x4>x2:
        return True
    else:
        return False


x1 = input("Enter line X1 of line 1:\t")
x2 = input("Enter line X2 of line 1:\t")
if check_valid(x2,x1):
    x2 = input("Enter x2 again, can't be smaller than or equal to x1")

x3 = input("Enter line X3 of line 2:\t")
x4 = input("Enter line X4 of line 2:\t")
if check_valid(x4,x3):
    x4 = input("Enter x4 again, can't be smaller than or equal to x3")

if check_overlap(x3,x2):
    print("There is an overlap")
else:
    print("No overlap")

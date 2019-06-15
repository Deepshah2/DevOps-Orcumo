
"""
Program to check greater version

TEST CASES:
1.) v1 = 1.2, v2 = 1.1
2.) v1 = 1.1, v2 = 1.1.1
3.) v1 = 2.1.0 , v2 = 1.2.9
4.) v1 = 1.2 , v2 = <blank>

"""

def check_digit(lst):
    """
    Function to check if the version number is a valid version ie. all digits.
    lst: contains version elements after splitting with delimiter as '.'
    Returns True if all values are digits.
    """
    for i in lst:
        if not i.isdigit():
            return False
    return True

def check_version(version1,version2):
    """
    Function to check which version is greater
    returns 1 if version1 is greater.
    returns 2 if version2 is greater.
    returns 0 if both versions are the same.
    version1: the first version.
    version2: the second version.
    length: contains the smaller of the two version lengths.
    """
    length = min(len(version1),len(version2))
    i = 0
    while i<length:
        if version1[i]>version2[i]:
            return 1

        elif version1[i]<version2[i]:
            return 2
        else:
            i+=1
    if len(version1) > len(version2):
        return 1
    elif len(version2) > len(version1):
        return 2
    else:
        return 0

"""
Querying a user repeatedly to enter a valid version number.
"""
v1 = input("Enter first version:\t")
version1 = v1.split('.')
while check_digit(version1) != True:
    v1 = input("Enter Again! Must be all digits:\t")
    version1 = v1.split('.')

"""
Querying a user repeatedly to enter a valid version number.
"""
v2 = input("Enter second version:\t")
version2 = v2.split('.')
while check_digit(version2) != True:
    v2 = input("Enter Again! Must be all digits:\t")
    version2 = v2.split('.')

"""
Calling function check_version to figure out which version is greater.
"""
if check_version(version1,version2) == 1:
    print("{} is greater".format(v1))
elif check_version(version1,version2) == 2:
    print("{} is greater".format(v2))
else:
    print("They are equal")

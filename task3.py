#!python3

"""
Create a function that determines the length of a hypotenuse given the lengths of 2
shorter sides
2 input parameters
float: the length of one side of a right triangle
float: the length of the other side of a right triangle

return: float value for the length of the hypotenuse rounded to 2 decimals
        None if the hypotenuse does not exist

Sample assertions:
assert hypotenuse(6,8) == 10
(2 points)
"""


def hypotenuse(a,b):
    if a > 0 and b > 0:
        h = (a**2 + b**2)**0.5 
        return round(h,2)
    else:
        return None


assert hypotenuse(6,8) == 10
assert hypotenuse(5,12) == 13
assert hypotenuse(4,6) == 7.21
print(hypotenuse(-3,4))
assert hypotenuse(-3,4) == None
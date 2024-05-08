#!python3
"""
Create a function that converts from degrees F to degrees C or
vice versa, depending on which initial unit is given
2 input parameters:
float: the number of degrees
string: the unit that you currently have: may be 'C' of 'F'

return: float the number of degrees of the other unit. Round answers to 2 decimals

Sample assertions:
assert convertTemp(10,'C') == 50
assert converTemp(32,'F') == 0
"""

## 1.8 + 32 and for reverse divide by 1.8 and subtract 32
def convertTemp(d, t):
    if t == 'C':
        print(d,t)
        f = (d* 1.8) + 32
        return round(f,2)

    if t == 'F':
        print(t,d)
        c = (d-32)/1.8
        print(c)
        return round(c,2)

def tests():
    assert convertTemp(10,'C') == 50.00
    assert convertTemp(32,'F') == 0.00
    assert convertTemp(100,'C') == 212.00
    assert convertTemp(100,'F') == 37.78
    
    


if __name__== "__main__":
    tests()
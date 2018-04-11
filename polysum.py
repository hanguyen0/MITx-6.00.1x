import math

def polysum(n,s):
    '''
    n: interger
    s: interger or float

    A program returns the sum of the square of a polygon's perimeter and area
    '''
    perimeter=0
    for i in range(n):
        perimeter+=s
    area=(0.25*n*(s**2))/(math.tan(math.pi/n))
    return round(perimeter**2+area, 4)

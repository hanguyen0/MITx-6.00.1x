def gcdRecur(a, b):
    if b==0:
        return a
    elif a >=b:

        return gcdRecur(b, a%b)
    else:
        return gcdRecur(a, b%a)

gcdRecur(1071, 462)


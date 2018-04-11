def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    oStr = ''.join(sorted(aStr))
    if len(oStr)==0 or len(oStr)==1:
        return False
    elif len(char) > len(oStr):
        return isIn(char, oStr)
    else:
        return isIn(char, oStr)


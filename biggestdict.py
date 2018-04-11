animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    max=1
    key=''
    for k in aDict:
        if len(aDict[k]) > max:
            max = len(aDict[k])
            key = k
    print(max)
    return key

print(biggest(animals))

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    values=[]
    n = []
    for v in aDict.values():
        for i in range(len(v)):
            n.append(v[i])
    print(n)
    return len(n)
print(how_many(animals))



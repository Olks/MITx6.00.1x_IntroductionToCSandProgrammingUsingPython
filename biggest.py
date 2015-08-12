
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    if aDict=={}:
        return None
    else:
        index=aDict.keys()[0]
        m=0
        for i in aDict:
            if len(aDict[i])>m:
                index=i
                m=len(aDict[i])
    return index
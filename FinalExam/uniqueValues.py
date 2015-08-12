__author__ = "Olks"

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    result = []
    index = 1
    values = aDict.values()
    for x in aDict.keys():
        if aDict[x] in values[index:]:
            values.append(aDict[x])            
        else: 
            result += [x]            
        index +=1
    return list(sorted(result))
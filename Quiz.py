# swapping values
a = 'gr'
b = 3
a,b = b,a

# break only inside  loops ('for' or 'while')
# SyntaxError: 'break' outside loop
def fun(x,y):
    while x>7:
        print x
        x = x-1
    if x<7:
        print 'a'
        break
        print 'b'
    print x+y
    return 101
    
    
# for
a='abc'
for letter in a:
    if letter == 'ab':
        print 'hurra!'
        
        
        
# recursion
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    if x < b:
        return 0
    else:
        return myLog(x/b,b)+1
        
        
#sublists
def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    result=[]
    for stuff in aList:
        if len(stuff)<4:
            result.append(stuff)
    return result
    
    
# sum of digits
def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    if N < 10:
        return N
    else:
        return sumDigits(N/10) + N%10
            
# values in a dict
def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    result=[]
    for key in aDict.keys():
        if aDict[key] == target:
            result.append(key)
    return result

# NOTE!!! G = L[:] is necessary because we iterate over 
# a list that fucntion is mutating!!
def f(s):
    return 'a' in s
      
L = ['c', 'b', 'c']

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    # Your function implementation here
    G = L[:]
    for letter in G:
        if f(letter)==False:
            L.remove(letter)
    return len(L)
    


print satisfiesF(L)
print L

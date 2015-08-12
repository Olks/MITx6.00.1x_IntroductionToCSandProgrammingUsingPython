## Problem 1
def f(s):
    '''
    s: string
    '''
    num=0
    vowels='aeiouAEIOU'
    for letter in vowels:
        num+=s.count(letter)
    return num 
#print ('Number of vowels: ' + str(f(s)))


## Problem 2
s='abcbobobakjhfkdbob'
def g(s):
    '''
    s: string
    '''
    num=0
    i=0
    while (i<len(s)):
        if s[i:].find('bob')!=-1: 
            i=i+s[i:].index('bob')+1
            print i-1
            num+=1
        else:
            break
    return num 

print ('Number of times bob occurs: ' + str(g(s)))


# Problem 3
def order(s):
    d=len(s)
    points=0
    for i in range(d-1):
        if s[i]<=s[i+1]:
            points+=1
    return (points+1)
    
def check(s):
    max_points=1
    max_string=s[0]
    d=len(s)    
    for i in range(d):
        for j in range(i+1,d+1):
            t=s[i:j]
            p=order(t)
            if p==len(t):
                if p>max_points:
                    max_points=p
                    max_string=t
    return max_string 
    
print ("Longest substring in alphabetical order is: " + check(s))
     



            




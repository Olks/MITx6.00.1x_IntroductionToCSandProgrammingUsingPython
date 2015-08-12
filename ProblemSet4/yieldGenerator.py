def genTest():
    yield 1
    yield 2
    
foo = genTest()

foo.next()
foo.next()
foo.next()

for n in genTest():
    print n
    
def fun(x):
    for n in x:
        yield n
    
    
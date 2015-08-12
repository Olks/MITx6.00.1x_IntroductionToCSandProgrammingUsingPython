def genPrimes():
    primes = []
    x = 2
    while True:
        prime = True
        for n in primes:
            if (x % n) == 0:
                prime = False
                break
        if prime == True:
            primes.append(x)
            yield x
        x += 1
        
        
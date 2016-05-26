import math

def naturallog(x):
    mantissa , exponent = math.frexp(x)
    ln2 = 0.693147180559945309417
    answer = 0
    for i in range (1,40):
        answer += -(-1)**i * ((mantissa - 1)**i/i)
    return(answer + exponent * ln2)

def etothe(x):
    answer = 1
    for i in range(1,20):
        answer += x**i/factorial(i)
    return(answer)

def factorial(x):
    answer = 1
    for i in range(2,x+1):
        answer *= i
    return answer

def altsquareroot(x):
    print(etothe(naturallog(x)/2))
    
altsquareroot(4096)
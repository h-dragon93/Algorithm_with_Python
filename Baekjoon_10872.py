N = int(input())

def customFactorial(N) :

    if N <= 1  :
         return 1

    return customFactorial(N-1)*N

print(customFactorial(N))

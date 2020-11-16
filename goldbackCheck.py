import math
def isPrime(x):
    half = x/2
    counter = 2
    while counter <= half:
        if(x % counter == 0):
            return False
        counter = counter + 1
    return True


def goldbachCheck(N):
    counter = 2
    half = N/2
    while counter <= half:
        if(isPrime(counter) and isPrime(N-counter)):
            return (counter, N-counter)
        counter = counter + 1


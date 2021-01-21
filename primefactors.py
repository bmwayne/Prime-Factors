factors = []


def isPrime():
    n = int(input("enter a number:"))

    for i in range(1,n):
        if n%i == 0:
            factors.append(i)
            n = n/i
    return factors

print(isPrime())    #prints the prime factors of the given number


def isPrime(n):

    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def countPrime(n):
    number = 0
    for i in range(2, n + 1):
        if isPrime(i):
            number += 1
    print(number)


if __name__ == "__main__":
    n = 5
    countPrime(n)

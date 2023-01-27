"""
Algorithm Design - HW2 - Q1
Samin Mahdipour - 9839039
"""
import math

ingredients = [2, 3, 5, 7]


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True


def createPass(N):
    global ingredients
    nums = []
    c = 0
    while c < N:
        if c == 0:
            nums = ingredients
            c = c + 1
        else:
            newNums = []
            for num in nums:
                for i in range(1, 10):
                    newNum = num * 10 + i
                    if isPrime(newNum):
                        newNums.append(newNum)
            nums = newNums
            c = c + 1
    return nums


if __name__ == '__main__':
    N = int(input())
    if 1 <= N <= 8:
        passwords = createPass(N)
        for p in passwords:
            print(p)

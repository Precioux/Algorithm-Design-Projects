'''
Samin Mahdipour - 9839039
Algorith Design - HW#
'''
def deletePolindrome(inpt):
    n = len(inpt)

    # declaring an array for dpArr journey
    dpArr = [[0 for x in range(n + 1)]
          for y in range(n + 1)]


    for v in range(1, n + 1):
        i = 0
        j = v - 1
        while j < n:
            if (v == 1):
                dpArr[i][j] = 1
            else:
                dpArr[i][j] = 1 + dpArr[i + 1][j]

                if (inpt[i] == inpt[i + 1]):
                    dpArr[i][j] = min(1 + dpArr[i + 2][j], dpArr[i][j])

                for K in range(i + 2, j + 1):
                    if (inpt[i] == inpt[K]):
                        dpArr[i][j] = min(dpArr[i + 1][K - 1] +
                                       dpArr[K + 1][j], dpArr[i][j])

            i += 1
            j += 1

    return dpArr[0][n - 1]


if __name__ == "__main__":
    inpt = input()
    print(deletePolindrome(inpt))


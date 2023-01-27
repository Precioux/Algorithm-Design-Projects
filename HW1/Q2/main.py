"""
Algorithm Design - HW1 -Samin Mahdipour
"""
def flip(str, t, m):
    newStr = ''
    for s in range(0, t + 1):
        if str[s] == '0':
            newStr = newStr + '1'
        else:
            newStr = newStr + '0'

    if t + 1 < m:
        for x in range(t + 1, m):
            newStr = newStr + str[x]

    return newStr


def changeStr(p, arr, n, m):
    arra = arr.copy()
    forThis = 0
    for i in range(0, n):
        if i != p:
            t = m - 1
            f = 0
            while t > -1:
                if arra[i][t] == arra[p][t]:
                    t = t - 1
                else:
                    arra[i] = flip(arra[i], t, m)
                    f = f + 1
            forThis = forThis + f
    return forThis


def checkStrings(arr, n, m):
    t = []
    for p in range(0, n):
        t.append(changeStr(p, arr, n, m))
    return min(t)


if __name__ == '__main__':
    result =[]
    number = int(input())
    for i in range(0, number):
        nm = input()
        nm2 = nm.split(" ")
        n = int(nm2[0])
        m = int(nm2[1])
        arr = []
        for j in range(0, n):
            a = input()
            arr.append(a)
        result.append(checkStrings(arr,n,m))

    for r in result:
        print(r)


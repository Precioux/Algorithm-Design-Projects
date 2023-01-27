"""
Algorithm Design - HW2 - Q2
Samin Mahdipour - 9839039
"""


def mergeSort(arr, n):
    copy = []
    for i in range(0, n):
        copy.append(0)
    return mergeCall(arr, copy, 0, n - 1)


def mergeCall(arr, copy, L, R):
    v = 0

    if L < R:
        mid = (L + R) // 2

        v += mergeCall(arr, copy, L, mid)
        v += mergeCall(arr, copy, mid + 1, R)
        v += merging(arr, copy, L, mid, R)
    return v


def merging(arr, copy, L, mid, R):
    i = L
    j = mid + 1
    k = L
    v = 0

    while i <= mid and j <= R:
        if arr[i] <= arr[j]:
            copy[k] = arr[i]
            k += 1
            i += 1
        else:
            copy[k] = arr[j]
            v += (mid - i + 1)
            k += 1
            j += 1

    while i <= mid:
        copy[k] = arr[i]
        k += 1
        i += 1

    while j <= R:
        copy[k] = arr[j]
        k += 1
        j += 1

    for x in range(L, R + 1):
        arr[x] = copy[x]

    return v


if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(0, n):
        arr.append(int(input()))
    print(mergeSort(arr, n))

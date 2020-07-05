def maxInArray2(a):
    a_max = a[0][0]
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] > a_max:
                a_max = a[i][j]
    return a_max


def findXinA2(x, a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == x:
                return i, j
    return -1, -1


def printArray(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(a[i][j], end=" ")
        print()
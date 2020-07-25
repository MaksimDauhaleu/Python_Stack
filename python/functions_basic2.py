def countdown(arr):
    start = arr
    while start > 0:
        start -= 1
        print(start+1)


countdown(5)



def printreturn(a, b):
    print(a)
    return b


print(printreturn(5, 6))



def firstpluslast(arr):
    count = ""
    count = arr[0] + len(arr)
    print(count)


firstpluslast([1, 4, 2, 3, 4])




def vgts(arr):
    newarr = []
    for i in range(0, len(arr)):
        if arr[i] > arr[1]:
            newarr.append(arr[i])
    print(len(newarr))
    return newarr


print(vgts([5, 2, 3, 2, 1, 4]))


def lv(a, b):
    arr = []
    for i in range(0, a):
        arr.append(b)
    return arr


print(lv(6, 2))
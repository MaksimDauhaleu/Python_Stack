def biggie(arr):
    for i in range(0, len(arr)):
        if arr[i] > 0:
            arr[i] = "big"
    print(arr)


biggie([-2, 5, 2, -7])



def countpositives(arr):
    count = 0
    for i in range(0, len(arr)):
        if arr[i] > 0:
            count += 1
        arr[-1] = count
        print(count)
    print(arr)


countpositives([-1, 1, 1, 1])




def sumtotal(arr):
    count = 0
    for i in range(0, len(arr)):
        count += arr[i]
    print(count)


sumtotal([1, 1, 55, 1])




def Average(arr):
    count = 0
    for i in range(0, len(arr)):
        count += arr[i]
    return count / len(arr)


print(Average([3, 4, 5, 6]))



def Length(arr):
    count = 0
    count += len(arr)
    return count


print(Length([3, 4, 5, 6, 5, 6]))



def Minimum(arr):
    min = arr[0]
    for i in range(0, len(arr)):
        if arr[i] < min:
            min = arr[i]
    print(min)


Minimum([3, 4, 5, 6, -5, 6])



def Maximum(arr):
    max = arr[0]
    for i in range(0, len(arr)):
        if arr[i] > max:
            max = arr[i]
    print(max)


Maximum([3, 44, 5, 6, -5, 6])


def ultanalist(arr):
    max = arr[0]
    min = arr[0]
    avg = 0
    count = 0
    for i in range(0, len(arr)):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
        avg += arr[i]
        count = 0
        count += len(arr)
    print(avg / len(arr))
    print(min)
    print(max)
    return count


print(ultanalist([3, 44, 5, 6, -5, 6]))

def reveselist(arr):
    for i in range(0, int(len(arr) / 2)):
        temp = arr[i]
        arr[i] = arr[len(arr) - i - 1]
        arr[len(arr) - 1] = temp
    return arr


print(reveselist([1, 3, 3, 6, 2, 1]))

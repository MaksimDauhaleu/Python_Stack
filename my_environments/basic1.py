for i in range(0, 256):
    print(i)


for i in range(0, 1000, 5):
    print(i)


for count in range(1, 100, 1):
    if count / 5:
        print("Coding")
    if count / 10:
        print("Coding DoJo")


for countOdd in range(0, 300, 1):
    if countOdd % 2 != 1:
        countOdd += countOdd
        print(countOdd)



y = 2018
while y > 0:
    print(y)
    y = y - 4
    if y == 0:
        break
else:
    print("Final")

def reverslist(arr):
    reversed(arr)
reverslist([1,2,3,4,5])

















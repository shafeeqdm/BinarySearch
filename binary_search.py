
def binarySearch(a,x,low,high):
    while low != high:
        mid = round(low+high/2)
        if a[mid] == x:
            return mid
        elif x < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1 

n = int(input("Enter the number of elements : "))
arr = list()
print("Enter the numbers : ")
for i in range(0,n):
    num = input()
    arr.append(num)
print(arr)
x = input('Enter the number to be searched : ')
arr.sort(reverse=False)
print(arr)
pos = binarySearch(arr,x,0,n)

if pos == -1:
    print("Number not found")
else:
    print("Number found in ",pos)


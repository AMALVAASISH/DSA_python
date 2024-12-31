# brute force approach

# def rotatebyonePlace(arr,n):
#     temp = [0] * n
#     for i in range(1,n):
#         temp[i-1] = arr[i]
#
#     temp[n-1] = arr[0]
#     for i in range(n):
#         print(temp[i], end=" ")
#     print()
#
#
# arr = [1,2,3,4,5]
# n = len(arr)
# rotatebyonePlace(arr,n)

#
# Time Complexity: O(n), as we iterate through the array only once.
#
# Space Complexity: O(n) as we are using another array of size, same as the given array.


# optimal approach

def rotatebyonePlace(arr,n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp
    for i in range(n):
        print(arr[i],end=" ")

arr = [1,2,3,4,5,6]
n = len(arr)
rotatebyonePlace(arr,n)

#
# Time Complexity: O(n), as we iterate through the array only once.
#
# Space Complexity: O(1) as no extra space is used
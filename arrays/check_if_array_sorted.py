# brute force approach

# def checkifSorted(arr,n):
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[j]<arr[i]:
#                 return False
#     return True
#
#
# arr = [2,10,3,4,5,6]
# n = len(arr)
#
# value = checkifSorted(arr,n)
# print(value)
#
#
# Time Complexity: O(N^2)
#
# Space Complexity: O(1)

#optimal approach

def checkifSorted(arr,n):
    for i in range(n):
        if arr[i]< arr[i-1]:
            return False

    return True

arr = [1,2,3,4,5,6]
n = len(arr)

value = checkifSorted(arr,n)
print(value)


#
# Time Complexity: O(N)
#
# Space Complexity: O(1)
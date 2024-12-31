# brute approach

# def findtheElements(arr,n):
#     if n == 0 or n == 1:
#         print(-1,-1)
#     arr.sort()
#     small = arr[1]
#     large = arr[n-2]
#
#     print("The second smallest", small)
#     print("The second largest", large)
#
# arr = [4,2,7,3,9,17,8,2]
# n = 8
# findtheElements(arr,n)
#
#
# Time Complexity: O(NlogN), For sorting the array
#
# Space Complexity: O(1)



# Better approach

# doing simple traversal, then comparing

# def getElements(arr,n):
#     if n == 0 or n ==1:
#         print(-1,-1)
#
#     small = float('inf')
#     second_small = float('inf')
#     large = float('-inf')
#     second_large = float('-inf')
#
#     for i in range(n):
#         small = min(small,arr[i])
#         large = max(large, arr[i])
#
#     for i in range(n):
#         if arr[i] < second_small and arr[i]!=small:
#             second_small = arr[i]
#
#         if arr[i] > second_large and arr[i]!= large:
#             second_large = arr[i]
#
#     print("Second smallest", second_small)
#     print("second largest", second_large)
#
#
# arr = [2,4,3,1,7,9,11,6]
# n = len(arr)
#
# getElements(arr,n)

# Time Complexity: O(N), We do two linear traversals in our array
#
# Space Complexity: O(1)

#
# optimal approach

arr = [1,2,4,7,7,5,6]
n = len(arr)

def secondSmallest(arr,n):
    if (n<2):
        return -1
    small = float('inf')
    second_small = float('inf')
    for i in range(n):
        if (arr[i]<small):
            second_small = small
            small = arr[i]
        elif (arr[i] < second_small and arr[i] != small):
            second_small = arr[i]

    return second_small


def secondLargest(arr,n):
    if (n<2):
        return -1
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        if (arr[i]> large):
            second_large = large
            large = arr[i]

        elif (arr[i] > second_large and arr[i] != large):
            second_large = arr[i]

    return second_large

sS = secondSmallest(arr,n)

sL = secondLargest(arr,n)


# Time Complexity: O(N), Single-pass solution
#
# Space Complexity: O(1)
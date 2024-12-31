 # first method is to sort the array

# from typing import List
#
# def sortArr(arr: List[int]) -> int:
#     arr.sort()
#     return arr[-1]
#
#
# arr2 = [4,17,5,8]
#
# print("The largest element is ", sortArr(arr2))
#


# this is the brute force approach
# Time Complexity: O(N*log(N))
#
# Space Complexity: O(n)


# second approach is using a max variable

def findtheLargestnumber(arr, n):
    max = arr[0]

    for i in range(0,n):
        if (max < arr[i]):
            max = arr[i]

    return max

arr1 = [4,0,9,2,4,17,8]
n = 7

max = findtheLargestnumber(arr1,n)
print("this is the largest element",max)

# Time Complexity: O(N)
#
# Space Complexity: O(1)
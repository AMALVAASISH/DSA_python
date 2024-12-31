# brute approach
# from typing import List
#
# def removeDuplicates(arr: List[int]) -> int:
#     st = set()
#     for i in range(len(arr)):
#         st.add(arr[i])
#     k = len(st)
#     j = 0
#     for x in st:
#         arr[j] = x
#         j += 1
#     return k
#
#
#
#
# arr = [1,1,2,2,3,3,3,4]
# k = removeDuplicates(arr)
# print(k)
#
# Time complexity: O(n*log(n))+O(n)
#
# Space Complexity: O(n)



# optimal approach
from typing import List
def removeDuplicates(arr: List[int]) -> int:
    i = 0
    for j in range(1,len(arr)):
        if arr[i]!= arr[j]:
            i+= 1
            arr[i] = arr[j]
    return i+1

arr = [1,1,1,1,2,3,3,3,3,4,4]
k = removeDuplicates(arr)
print(k)

# Time Complexity: O(N)
#
# Space Complexity: O(1)

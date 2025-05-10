# def length_list(arr: list) -> int:
#     return len(arr)

# arr1 = [1, 2, 3]
# print(length_list(arr1))



# solution with use class
class Solution:
    def lengthList(self, arr: list) -> int:
        return len(arr)

arr1 = [1, 2, 3]
arr2=[]
print(Solution().lengthList(arr1))  # Output: 3
print(Solution().lengthList(arr2))
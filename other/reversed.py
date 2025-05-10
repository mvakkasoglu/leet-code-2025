class Solution:
     def reversedString(self, s:str):
        for ch in reversed(s):
            print(ch)
    # def reversedString(self, s:str) -> str:
    #     for ch in reversed(s):
    #         print(ch)

input_str = input("Enter a string:")
print(Solution().reversedString(input_str))
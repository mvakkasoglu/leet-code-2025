class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


# to read from standard input, include the lines below
# if __name__ == "__main__":
#     input_str = input("Enter a string: ")
#     sol = Solution()
#     print(sol.lengthOfLastWord(input_str))

# or

# input_str = input("Enter a string: ")
# print(Solution().lengthOfLastWord(input_str))
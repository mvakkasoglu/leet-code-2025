class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]
        return strs[0]

    # alternative solution with stack
    # Start with an empty stack.
    # Loop through each character of the first string by index.
    # For each index, check:
    # Does every other string have the same character at that position?
    # If yes: push to the stack.
    # If no: stop and return what's in the stack.
    
        # first_str=strs[0]
        # stack=[]
        # for i in range(len(first_str)):
        #     char=first_str[i]
        #     for s in strs[1:]:
        #         if i >= len(s) or s[i] != char:
        #             return "".join(stack)
        #     stack.append(char)
        # return "".join(stack)
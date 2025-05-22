class Solution:
    def isValid(self, s: str) -> bool:
        open=[
            "(",
            "{",
            "["
        ]
        close=[
            ")",
            "}",
            "]"
        ]
        p={
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack=[]
        
        if len(s)%2==1 or s[0] in close:
            return False
      
        for char in s:
            if char in open:
                stack.append(char)
            else:
                if len(stack) == 0 or stack[-1] != p[char]:
                    return False
                else:
                    stack.pop()
                    
        if len(stack)!=0:
            return False

        return True
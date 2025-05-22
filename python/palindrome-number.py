class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        reverse=""
        print(str(x))
        for i,n in enumerate(x):
            reverse=n+reverse

        return reverse==x

    # def isPalindrome(self, x: int) -> bool:
    #     if (str(x)==str(x)[::-1]):
    #         return True
    #     else:
    #         return False
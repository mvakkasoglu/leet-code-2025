class Solution:
    def romanToInt(self, s: str) -> int:
        roman={"I": 1, "V": 5, "X":10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total=0
        for i in range(len(s)):
            value=roman[s[i]]
            if i+1<len(s) and value<roman[s[i+1]]:
                total-=value
            else:
                total+=value

        return total


#  alternative (better) solution
        # current=0
        # previous=0
        # value=0

        # for ch in reversed(s):
        #     current = roman[ch]
        #     if current < previous:
        #         value -= current
        #     else:
        #         value += current
        #     previous = current

        # return value
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:    
        # Dictionary to store numbers we've seen so far and their indices
        seen = {}

        # Loop through the list with both index (i) and value (num)
        for i, num in enumerate(nums):
            # Calculate the number we need to find to reach the target
            complement = target - num

            # Check if we've already seen the complement
            if complement in seen:
                # If yes, return the index of the complement and the current index
                return [seen[complement], i]

            # Otherwise, store the current number and its index in the dictionary
            seen[num] = i



#  alternative but not optimal solution
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        nums2=[]
        for i,n in enumerate(nums):
            if n not in nums2:
                nums2.append(nums[i])
                k+=1
                continue;

        nums[:]=nums2[:]
        
        return k
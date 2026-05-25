class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        difference = 0
        maximum = 0
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                difference += 1
                maximum = max(maximum,difference)
            if nums[i] - nums[i-1] > 1:
                difference = 0
                maximum = max(maximum,difference)

        if len(nums) == 0:
            return(0)
        else:
            return(maximum+1)  

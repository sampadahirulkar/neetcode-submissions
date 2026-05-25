class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r=0
        l=len(numbers) - 1  
        while l>=0 and r<=len(numbers) - 1 :
            s = numbers[r] + numbers[l] 
            if s > target:
                l -= 1
            elif s < target:
                r += 1
            else:
                return[r+1,l+1]
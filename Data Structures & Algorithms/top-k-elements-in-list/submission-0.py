class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        ans = []
        for item in nums:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        s = sorted(d.items(), key=lambda x: x[1], reverse=True)  
        for i in range(k):
            ans.append(s[i][0])
        return ans  
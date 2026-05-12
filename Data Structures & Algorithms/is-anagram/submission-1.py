class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        d2={}

        def add_to_dict(arr , d):
            for item in arr:
                if item in d:
                    d[item] += 1
                else:
                    d[item] = 1


        if len(s) != len(t):
            return False
        else:
            add_to_dict(s,d1)
            add_to_dict(t,d2)
            return(d1 == d2)
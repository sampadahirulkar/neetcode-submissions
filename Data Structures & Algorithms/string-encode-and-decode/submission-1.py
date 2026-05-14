class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s = s + str(len(word)) + "#" + word
        return s

    def decode(self, s: str) -> List[str]:
        ans = []
        i=0
        while i < len(s):
            hash_index = s.index("#", i)
            l = int(s[i:hash_index])
            word = s[hash_index+1 : hash_index+1+l]
            ans.append(word)
            i = hash_index+1+l
        return(ans)



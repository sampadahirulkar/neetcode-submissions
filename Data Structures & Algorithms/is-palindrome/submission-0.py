class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for item in s:
            if item.isalpha() == True or item.isdigit() == True:
                if item.isupper() == True:
                    cleaned += item.lower()
                else:
                    cleaned += item
                
        if cleaned == cleaned[::-1]:
            return True
        else:
            return False
        
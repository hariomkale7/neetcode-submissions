class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = sorted(s)      
        b = sorted(t)
        return a == b

s = "racecar"
t = "carrace"
x = Solution()
print(x.isAnagram(s,t))
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicti = {}
        dicti_1 = {}
        for i in s:
            if i in dicti:
                dicti[i] += 1
            else:
                dicti[i] = 1 

        for j in t:
            if j in dicti_1:
                dicti_1[j] += 1
            else:
                dicti_1[j] = 1 
        return dicti == dicti_1

s = "racecar"
t = "carrace"
x = Solution()
print(x.isAnagram(s,t))
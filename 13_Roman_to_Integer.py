class Solution:
    def __init__(self):
        self.dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    def romanToInt(self, s: str) -> int:
        ans = 0
        for i in range(len(s)-1):
            if self.dict[s[i]]< self.dict[s[i+1]]:
                ans-=self.dict[s[i]]
            else:
                ans+=self.dict[s[i]]
        ans += self.dict[s[len(s)-1]]
        return ans

s = Solution()
ans = s.romanToInt('MCMXCIV')
print(ans)
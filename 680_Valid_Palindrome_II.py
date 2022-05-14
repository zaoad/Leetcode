class Solution:
    def validPalindrome(self, s: str) -> bool:
        def pallindrome(s: str, i: int, j: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i = i + 1
                j = j - 1
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return pallindrome(s, i + 1, j) or pallindrome(s, i, j - 1)
            i = i + 1
            j = j - 1
        return True

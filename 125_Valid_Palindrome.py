class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            c1 = s[i]
            c2 = s[j]
            flag = False
            if not c1.isalnum():
                i += 1
                flag = True
            if not c2.isalnum():
                j -= 1
                flag = True
            if flag:
                continue
            if c1 != c2:
                return False
            i+=1
            j-=1
        return  True



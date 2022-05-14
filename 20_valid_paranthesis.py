class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if c==')':
                    t = stack.pop()
                    if t != '(':
                        return False
                if c=='}':
                    t = stack.pop()
                    if t != '{':
                        return False
                if c==']':
                    t = stack.pop()
                    if t != '[':
                        return False
        if len(stack)>0:
            return False
        return True
s = Solution()
ans = s.isValid('(){[]})')
print(ans)
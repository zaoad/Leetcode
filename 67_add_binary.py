class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = 0
        l1 = len(a)
        l2 = len(b)
        i = l1 - 1
        j = l2 - 1
        s = ''
        values = {0: (0, 0), 1: (1, 0), 2: (0, 1), 3: (1, 1)}
        while i >= 0 or j >= 0:
            a_val = int(a[i]) if i >= 0 else 0
            b_val = int(b[j]) if j >= 0 else 0
            ans = a_val + b_val + c
            (add, carry) = values[ans]
            # print(a_val, b_val, ans, add, carry)
            s = str(add) + s
            c = carry
            i -= 1
            j -= 1
        s = str(c) + s if c == 1 else s
        return s


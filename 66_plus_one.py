from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        c = 1
        while i>=0:
            add = int(digits[i])+c
            # print(add)
            c = int(add / 10)
            d = add % 10
            digits[i] = d
            i-=1
        if c > 0:
            digits.insert(0,c)
        return digits
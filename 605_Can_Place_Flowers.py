from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = 0
        next = 0
        total = 0
        for i, v in enumerate(flowerbed):
            if i > 0:
                prev = flowerbed[i - 1]
            if i < len(flowerbed) - 1:
                next = flowerbed[i + 1]
            if prev == 0 and next == 0:
                flowerbed[i] = 1
                if v == 0:
                    print(i, v)
                    total += 1
        print(total)
        if n <= total:
            return True
        else:
            return False









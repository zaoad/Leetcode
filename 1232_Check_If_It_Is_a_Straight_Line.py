class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        [x, y] = coordinates[0]
        [x1, y1] = coordinates[1]
        a = x-x1
        b = y-y1
        for p, q in coordinates[2:]:
            if a*(q-y) != b*(p-x):
                return False
        return True

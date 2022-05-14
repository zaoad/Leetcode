rows, cols = (5,4)
matrix = [[0]*cols]*rows
rows = len(matrix)
cols = len(matrix[0])
low = 0
high = rows - 1
target = 10
ans = False
lower_limit = -1
while True:
    mid = int((low+high)/2.0)
    if matrix[mid][0] == target:
        ans = True
        lower_limit = mid
    if matrix[mid][0]>target:
        low = mid + 1
    if matrix[mid][0]<target:
        high = mid - 1

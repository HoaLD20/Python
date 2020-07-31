"""
DONE
"""
i = 1
col = 0
col2 = 0
re = 0
while i <= 5:
    numL = list(map(int, input().split()))
    col += 1
    if sum(numL) >= re:
        re = sum(numL)
        col2 = col
    numL = []
    i += 1
print(col2, re, end=" ")

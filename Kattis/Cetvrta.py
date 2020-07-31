def meo(arr):
    hi = dict()
    for i in range(len(arr)):
        if arr[i] in hi.keys():
            hi[arr[i]] += 1
        else:
            hi[arr[i]] = 1
    for j in hi:
        if hi[j] == 1:
            print(j, end=" ")


numx = []
numy = []
for i in range(0, 3):
    x, y = map(int, input().split())
    numx.append(x)
    numy.append(y)
meo(numx)
meo(numy)

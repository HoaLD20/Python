a, b = map(int, input().split())  # a la so nguoi toi da, b la so luot ra vao
gr = 0  # so nhom nguoi tren san thuong
peo = 0  # so nguoi dang o tren san thuong
mu = []
for i in range(b):
    n = input()
    if "enter" in n:
        if peo + int(n[-1]) <= a:
            peo += int(n[-1])
            gr += 1
            mu.append(int(n[-1]))
    elif "leave" in n:
        if int(n[-1]) in mu:
            gr -= 1
            peo -= int(n[-1])
        else:
            peo -= int(n[-1])

print(gr)

"""
khong tap trung duoc 
"""

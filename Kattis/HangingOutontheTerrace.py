a, b = map(int, input().split())  # a la so nguoi toi da, b la so luot ra vao
gr = 0  # so nhom nguoi khong duoc vao san thuong
peo = 0  # so nguoi dang o tren san thuong
for i in range(b):
    m, n = map(str, input().split())
    if m[0] == "e":
        if peo + int(n) > a:
            gr += 1
        else:
            peo += int(n)
    else:
        peo -= int(n)

print(gr)

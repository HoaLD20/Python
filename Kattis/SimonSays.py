n = int(input())
simon = []
for i in range(n):
    a = input()
    simon.append(a)
for i in simon:
    if "Simon says" in i:
        print(i[10:])
n = input()
re = 1
if n[0] == "A":
    re = 2
if n[0] == "C":
    re = 3
for i in range(1, len(n)):
    if n[i] == "A" and re == 2:
        re = 1
    elif n[i] == "A" and re == 1:
        re = 2
    elif n[i] == "B" and re == 2:
        re = 3
    elif n[i] == "B" and re == 3:
        re = 2
    elif n[i] == "C" and re == 1:
        re = 3
    elif n[i] == "C" and re == 3:
        re = 1

print(re)

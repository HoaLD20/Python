n = input()
re = 1

if n[0] == "A":
    re = 2
    for i in range(1, len(n)):
        if n[i] == "A":
            re = 1
        if n[i] == "B":
            re = 3
        if n[i] == "C":
            re = 3
elif n[0] == "C":
    re = 3
    for i in range(1, len(n)):
        if n[i] == "A":
            re = 1
        if n[i] == "B":
            re = 3
        if n[i] == "C":
            re = 3


print(re)

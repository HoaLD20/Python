n = int(input())
a = bin(n)[2:]
b = a[::-1]
print(int(b, 2))
n = int(input())
a = list(range(n, n+n))
b = list(range(0, n))
if sum(a) %2 == 0 and sum(b) %2 == 0:
    print("Even")
elif sum(a) %2 != 0 and sum(b) %2 != 0:
    print("Odd")
else:
    print("Either")
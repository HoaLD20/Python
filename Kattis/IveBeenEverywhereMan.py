n = int(input())
trip = []
for i in range(n):
    m = int(input())
    for j in range(m):
        a = input()
        if a not in trip:
            trip.append(a)
    print(len(trip))
    trip = []

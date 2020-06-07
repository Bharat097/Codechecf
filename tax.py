mapping = {0: 0, 1: 12500, 2: 37500, 3: 75000, 4: 125000, 5: 187500, 6: 262500}
per = {0: 0, 1: 0.05, 2: 0.10, 3: 0.15, 4: 0.20, 5: 0.25, 6: 0.30}
T = int(input())
for _ in range(T):
    t = int(input())
    n = t // 250000
    # print(n)
    a1 = mapping[n-1] if n-1 > 0 else 0
    rem = t % 250000
    # print(rem)
    a2 = rem * per[n]
    print(int(t - (a1+a2)))

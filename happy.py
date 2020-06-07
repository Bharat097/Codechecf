T = int(input())
ans = []
for _ in range(T):
    n, total = input().split()
    ak = list(map(int, input().split()))
    s = sum(ak)
    t = int(total) - s
    ans.append("Yes") if t >= 0 else ans.append("No")
print('\n'.join(ans))

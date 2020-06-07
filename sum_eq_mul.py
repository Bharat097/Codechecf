T = int(input())
ans = []
for _ in range(T):
    n = int(input())
    p = list(map(int,input().split()))
    
    z = p.count(0)
    t = p.count(2)
    a = int(z*(z-1)/2)
    b = int(t*(t-1)/2)
    ans.append(str(a + b))
print("\n".join(ans))
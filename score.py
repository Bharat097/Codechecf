T = int(input())
ans = []
for _ in range(T):
    n = int(input())
    st = {}
    for _ in range(n):
        p, s = map(int,input().split())
        if p < 9 and p > 0 and p in st.keys() and s > st[p]:
            st[p] = s
        else:
            st[p] = s
    ans.append(str(sum(st.values())))
print("\n".join(ans))
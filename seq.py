T = int(input())
s = [0,0]
# print(s[0])
ans = []
for _ in range(T):
    n = int(input())
    for i in range(len(s),n):
        val = i-1-max(c for c, v in enumerate(s[:i-1]) if v == s[i-1]) if s[i-1] in s[:i-1] else 0
        s.append(val)
        # print(s)
    else:
        ans.append(s[:n].count(s[n-1]))
print(*ans, sep='\n')

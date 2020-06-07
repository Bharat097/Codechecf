T = int(input())
ans = []
for _ in range(T):
    alpha = 'a'
    ls = []
    n = int(input())
    s = input()
    for i in range(0, 26):
        try:
            fi = s.index(alpha)
            si = s[fi+1:].index(alpha) + fi + 1
            ls.append(si)
        except ValueError:
            pass
        alpha = chr(ord(alpha) + 1)
    try:
        lb = min(ls)
    except ValueError:
        lb = n
    ans.append(str(n - lb))
print("\n".join(ans))
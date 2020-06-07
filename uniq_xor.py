import math
T = int(input())
ans = []

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

for _ in range(T):
    n = int(input())
    odd = 1 if n % 2 != 0 else 0
    a = input()
    b = input()
    count = 0
    ac = a.count('1')
    bc = b.count('1')
    ones = ac + bc
    if ones <= n:
        val = ones
    else:
        if ones == 2 * n:
            count = 1
            ans.append(str(count))
            continue
        else:
            val = n-(ones % n)
    while val >= 0:
        count += nCr(n, val)
        val -= 2
    ans.append(str(count % 1000000007))
print("\n".join(ans))

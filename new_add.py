T = int(input())
ans = []
for _ in range(T):
    a = input()
    b = input()
    ai = int(a, 2)
    bi = int(b, 2)
    c = 0
    while (bi>0):
        # print("a: {}".format(bin(ai)))
        # print("b: {}".format(bin(bi)))
        c += 1
        u = ai ^ bi
        v = ai & bi
        ai = u
        bi = v * 2
    ans.append(str(c))
print("\n".join(ans))

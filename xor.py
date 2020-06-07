# a = '1111'
# b = '0101'
# c = zip(a,b)
# # for each in c:
# #     print(each)
# d = ''.join('0' if x==y else '1' for x, y in c)
# print(d)
# print(d.count('1'))

T = int(input())
ans = []
for _ in range(T):
    n = int(input())
    f = input()
    for _ in range(n-1):
        s = input()
        f = ''.join('0' if x==y else '1' for x, y in zip(f, s))
    ans.append(str(f.count('1')))
print('\n'.join(ans))
T = int(input())

for _ in range(T):
    N, P = map(int, input().split())
    ans = [0] * N
    flag = False
    arr = list(map(int, input().split()))

    for i in range(N):
        if P % arr[i] != 0:
            c = (P // arr[i]) + 1
            ans[i] = c
            flag = True
            break    
    if flag:
        print('YES', end=" ")
        print(*ans, sep=" ")
    else:
        print('NO')

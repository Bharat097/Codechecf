# cook your dish here
T = int(input())
ans = []
for _ in range(T):
    r, c = map(int, input().split())
    n = r*c
    mat = []
    total_count = 0
    for _ in range(r):
        mat.append(list(map(int, input().split())))

    for i in range(1, r-1):
        for j in range(1, c-1):
            counter = 1
            flag = True
            m = min(i, j, r-i-1, c-j-1)
            while (flag and counter <= m):
                if((mat[i][j-counter] == mat[i][j+counter]) and (mat[i-counter][j] == mat[i+counter][j])):
                    total_count += 1
                    # print("({}{}) and ({}{})".format(i, i-counter, i, i+counter))
                    # print("({}{}) and ({}{})".format(j-counter, j, j+counter, j))
                else:
                    flag = False
                counter += 1
            # print("done({}{})".format(i, j))
    ans.append(n+total_count)
print(*ans, sep='\n')

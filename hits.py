import math
T = int(input())
ans = []
for _ in range(T):
    arr = list(map(int, input().split()))
    s = arr[0]
    arr.remove(arr[0])
    # print(s)
    # print(arr)
    count = 0
    flag = False
    while arr:
        if arr[0] > s:
            arr = arr[::-1]
        else:
            ts = 0
            while arr and ts+arr[0] <= s: 
                ts += arr.pop(0)
            #     print("TS: {}".format(ts))
            # print(arr)
            count += 1
    ans.append(str(count))
print('\n'.join(ans))
ref = [
    [1, 2, 3, 4],
    [1, 2, 4, 3],
    [1, 3, 2, 4],
    [1, 3, 4, 2],
    [1, 4, 2, 3],
    [1, 4, 3, 2],
    [2, 1, 3, 4],
    [2, 1, 4, 3],
    [2, 3, 1, 4],
    [2, 3, 4, 1],
    [2, 4, 1, 3],
    [2, 4, 3, 1],
    [3, 1, 2, 4],
    [3, 1, 4, 2],
    [3, 2, 1, 4],
    [3, 2, 4, 1],
    [3, 4, 1, 2],
    [3, 4, 2, 1],
    [4, 1, 2, 3],
    [4, 1, 3, 2],
    [4, 2, 1, 3],
    [4, 2, 3, 1],
    [4, 3, 1, 2],
    [4, 3, 2, 1],
]
val = {0: 25, 1: 50, 2: 75, 3:100}
screen_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
time_map = {3: 0, 6: 1, 9: 2, 12: 3}
total_profit = 0

T = int(input())

for _ in range(T):
    mat = [[0]*4 for _ in range(4)]
    max_profit = -400
    N = int(input())
    for _ in range(N):
        screen, time = input().split()
        time = int(time)
        mat[screen_map[screen]][time_map[time]] += 1

    for each in ref:
        profit = 0
        temp = [mat[0][each[0]-1], mat[1][each[1]-1], mat[2][each[2]-1], mat[3][each[3]-1]]
        temp.sort()
        for i in range(4):
            if temp[i] == 0:
                profit -= 100
            else:
                profit += temp[i] * val[i]
        if profit > max_profit:
            max_profit = profit
    print(max_profit)
    total_profit += max_profit
print(total_profit)


def is_safe(board, i, j):
    # print("**********")
    global N
    diag1 = [board[p][q] for p in range(N) for q in range(N) if p - q == i - j]
    diag2 = [board[p][q] for p in range(N) for q in range(N) if p + q == i + j]
    if 1 in board[i]:
        # print("111")
        return False
    elif 1 in [x[j] for x in board]:
        # print("222")
        return False
    elif 1 in diag1 or 1 in diag2:
        # print("333")
        # print(diag1)
        # print(diag2)
        return False
    else:
        return True


def solve_nq(board, pos):
    # print("Called: {}".format(pos))
    global N

    if pos >= N:
        return True

    for i in range(N):
        # print("check for: ({}{}): ans: {}  board: {}".format(i, pos, is_safe(board, i, pos), board))
        # print("check for: {}{}".format(i, pos))
        if is_safe(board, i, pos):
            board[i][pos] = 1
            # print("Set: {} {}".format(i, pos))

            if solve_nq(board, pos+1):
                # print("-----")
                return True
            
            board[i][pos] = 0
            # print("Reset: {} {}".format(i, pos))



if __name__ == "__main__":
    global N
    T = int(input())
    for _ in range(T):
        N = int(input())
        board = [[0]*N for _ in range(N)]

        if solve_nq(board, 0):
            print("YES")
            for each in board:
                print(*each)
        else:
            print("NO")
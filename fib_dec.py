import math
T = int(input())
if T > 0:
    sol = []
    phi = (math.sqrt(5) + 1)/2
    # print(phi)
    def fib(index):
        return int(round(math.pow(phi, index)/math.sqrt(5)))

    for case in range(T):
        index = 1
        N = int(input())
        if N > 0:
            while N != 1:
                N = N//2
                # print(N)
                index = index * 2
            sol.append(fib(index-1)%10)
    for each in sol:
        print(each)

    N = int(input())
    fib = [0, 1]
    for i in range(2, N):
        fib.append(fib[i-1] + fib[i-2])
    D = [i%10 for i in fib]
    print(D)
    while len(D) != 1:
        D = [D[i] for i in range(len(D)) if i%2!=0]
        print(D)
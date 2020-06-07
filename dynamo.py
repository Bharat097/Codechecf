import random
import sys
T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    A = int(input())
    S = random.randint(1, 5*(10**N))
    print(S)
    total = S - A
    total -= int(input())
    total -= random.randint(1, 10**N)
    total -= int(input())
    total -= random.randint(1, 10**N)
    if int(input()) == -1:
        sys.stdout.flush()
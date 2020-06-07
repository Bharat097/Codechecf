import math
import sys
from math import sqrt
# min = sys.maxint
T = int(input())
# T = 1
final_ans = []
for _ in range(T):
    x, y = map(int, input().split())
    # x, y = 1, 4
    na, nb, nc = map(int, input().split())
    # na, nb, nc = 3, 2, 2
    aa = list(map(int, input().split()))
    bb = list(map(int, input().split()))
    cc = list(map(int, input().split()))
    # aa = [4, 4, 2, 0, 8, 1]
    # bb = [10, 1, 3, 1]
    # cc = [1, 3, 9, 5]
    bb_min = []
    aa_min = []
    final_min_bb = final_min_cc = float(sys.maxsize)

    for i in range(0, 2*nb, 2):
        min_a = min_b = float(sys.maxsize)
        b1, b2 = bb[i], bb[i+1]
        for j in range(0, 2*na, 2):
            a1, a2 = aa[j], aa[j+1]
            dist = sqrt((b1-a1)**2 + (b2-a2)**2)
            from_xy_a = sqrt((x-a1)**2 + (y-a2)**2)
            xy_a_b = from_xy_a + dist
            min_a = xy_a_b if xy_a_b < min_a else min_a
            # print("({}, {}) - ({}, {}): {} - ({}, {}): dist: {}".format(x, y, a1, a2, from_xy_a, b1, b2, dist))
        for k in range(0, 2*nc, 2):
            c1, c2 = cc[k], cc[k+1]
            dist = sqrt((b1-c1)**2 + (b2-c2)**2)
            min_b = dist if dist < min_b else min_b
            # print("({}, {}) to ({}, {}) -- dist: {}".format(b1, b2, c1, c2, dist))
        temp = min_a + min_b
        # print("bb - {} - {} -- {}".format(form_xy, min_a, min_b))
        final_min_bb = temp if temp < final_min_bb else final_min_bb

    for i in range(0, 2*na, 2):
        min_b = min_c = float(sys.maxsize)
        a1, a2 = aa[i], aa[i+1]
        for j in range(0, 2*nb, 2):
            b1, b2 = bb[j], bb[j+1]
            dist = sqrt((b1-a1)**2 + (b2-a2)**2)
            xy_b = sqrt((x-b1)**2 + (y-b2)**2)
            xy_b_a = dist + xy_b
            min_b = xy_b_a if xy_b_a < min_b else min_b
        for k in range(0, 2*nc, 2):
            c1, c2 = cc[k], cc[k+1]
            dist = sqrt((a1-c1)**2 + (a2-c2)**2)
            min_c = dist if dist < min_c else min_c
        # print("aa - {} - {}".format(from_xy, (min_b + min_c)))
        temp = min_b + min_c
        final_min_cc = temp if temp < final_min_cc else final_min_cc
    
    final_ans.append(min(final_min_bb, final_min_cc))

for each in final_ans:
    print(each)


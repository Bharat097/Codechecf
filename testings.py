#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.


def countTriplets(arr, r):
    cnt = 0
    tmp = {}
    tmpl = {}
    for each in arr:
        if tmp.get(each):
            tmp[each] += 1
        else:
            tmp[each] = 1
    # print(tmp)
    # print("---")
    if r == 1:
        for each in arr:
            c = tmp[each]
            tmp[each] = 0
            cnt += int((c * (c-1) * (c-2))/6)
    else:
        for each in arr:
            tmp[each] -= 1
            if each % r == 0:
                cnt += ((tmpl.get(each//r, 0) * tmp.get(each*r, 0)))
            # print(tmp)
            # print(cnt)
            if tmpl.get(each):
                tmpl[each] += 1
            else:
                tmpl[each] = 1
            print(tmp)
    return cnt


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    with open('D:\\Bharat - Cisco DCN\\Bharat\\CodeChef\\testcase.txt') as t:
        data = t.read()
        print(data)


    arr = list(map(int, data.rstrip().split()))
    print(arr)
    print(len(arr))

    ans = countTriplets(arr, r)
    print(ans)

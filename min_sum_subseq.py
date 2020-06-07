import math, sys
T = int(input())
sol = []
for _ in range(T):
    sum = 100000000000
    count = 0 
    n, k = map(int, raw_input().split())
    lst = map(int, raw_input().split())
    a = int(math.pow(2, n))
    for i in range(a):
        temp_sum = 0
        bin_a_n = []
        bin_a = list(int(each) for each in bin(i)[2:])
        t_l = len(bin_a)
        while(t_l != n):
            bin_a.insert(0, 0) 
            t_l += 1
        # print(bin_a)
        if bin_a.count(1) == k:
            for j in range(len(bin_a)):
                temp_sum += bin_a[j] * lst[j]
                if temp_sum > sum:
                    print("Breaks: {}".format(temp_sum))
                    break
            if temp_sum < sum:
                print("temp_sum < sum: {}, {}, {}".format(temp_sum, sum, bin_a))
                sum = temp_sum
                count = 1
            elif temp_sum == sum:
                print("temp_sum == sum: {}, {}, {}".format(temp_sum, sum, bin_a))
                count += 1
            else:
                print("else: {}, {}, {}".format(temp_sum, sum, bin_a))
                pass
    sol.append(count)
for each in sol:
    print(each)

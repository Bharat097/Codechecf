import math
T = int(input())
final_ans = []
for _ in range(T):
    x, y = map(int, input().split())
    na, nb, nc = map(int, input().split())
    ab = list(map(int, input().split()))
    cd = list(map(int, input().split()))
    ef = list(map(int, input().split()))

    abz = list(zip(ab[0::2], ab[1::2]))
    cdz = list(zip(cd[0::2], cd[1::2]))
    efz = list(zip(ef[0::2], ef[1::2]))
    a = {}
    lab = len(abz)
    lcd = len(cdz)
    size = lab + lcd
    s_all = [math.sqrt((x-a)**2+(y-b)**2) for a,b in abz] + [math.sqrt((x-c)**2+(y-d)**2) for c,d in cdz]
    # print(s_all)
    # e_all = [math.sqrt((x-a)**2+(y-b)**2) for a,b in abz] + [math.sqrt((x-c)**2+(y-d)**2) for c,d in cdz]

    min_arr = []
    for i in range(size):
        min_val = 100000000000
        s_all_i = s_all[i]
        if i < lab:
            x,y = abz[i][0], abz[i][1]
            for c, d in cdz:
                t = math.sqrt((x-c)**2+(y-d)**2) + s_all_i
                for e, f in efz:
                    u = math.sqrt((e-c)**2+(f-d)**2) + t
                    if u < min_val:
                        min_val = u
            min_arr.append(min_val) 

            # ans.append(temp + [math.sqrt((x-c)**2+(y-d)**2) + s_all[i] for c,d in cdz])
        else:
            x, y = cdz[i-lab][0], cdz[i-lab][1]
            for a, b in abz:
                t = math.sqrt((x-a)**2+(y-b)**2) + s_all_i
                for e, f in efz:
                    u = math.sqrt((e-a)**2+(f-b)**2) + t
                    if u < min_val:
                        min_val = u
            min_arr.append(min_val)
            # ans.append([math.sqrt((x-a)**2+(y-b)**2) + s_all[i] for a,b in abz] + temp)
    final_ans.append(min(min_arr))
for each in final_ans:
    print(each)
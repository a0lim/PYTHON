n_list = list(range(1,10000))
non_self_num = []

for i in range(0,10000):
    #i=111
    n = n_list[i-1]
    d_n = n
    for j in range(0,len(str(n))):
        each = str(n)[j]
        d_n += int(each)
    non_self_num.append(d_n)

non_self_num = list(set(non_self_num)) ## delete rep
    
for k in range(1,10000):
    if k not in non_self_num:
        print(k)
ex = [] # 제외

for i in range(10001):
    sum = i
    s_i = str(i)
    for j in range(len(s_i)):
        sum += int(s_i[j])
    ex.append(sum)

    if i not in ex:
        print(i)
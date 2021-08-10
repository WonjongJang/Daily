a = int(input())
b = int(input())
c = int(input())
m = list(map(int, str(a*b*c)))
l = [0] * 10

for i in range(len(m)):
    l[m[i]] += 1

for j in range(len(l)):
    print(l[j])
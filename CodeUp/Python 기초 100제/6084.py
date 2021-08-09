h, b, c, s = input().split()

h = int(h)
b = int(b)
c = int(c)
s = int(s)

cal = h * b * c * s

byte = cal / 8
kb = cal / 8 / 1024
mb = format(cal / 8 / 1024 / 1024, '.2f')

print(f'{mb} MB')
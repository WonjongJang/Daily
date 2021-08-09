r, g, b = input().split()

r = int(r)
g = int(g)
b = int(b)

cal = r * g * b

byte = cal / 8
kb = cal / 8 / 1024
mb = format(cal / 8 / 1024 / 1024, '.2f')

print(f'{mb} MB')
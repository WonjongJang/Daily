while True:
    l1, l2, l3 = map(int, input().split())
    if l1 == 0 and l2 == 0 and l3 == 0:
        break

    ans = ''
    if (l1 ** 2) + (l2 ** 2) == (l3 ** 2) or (l1 ** 2) + (l3 ** 2) == (l2 ** 2) or (l2 ** 2) + (l3 ** 2) == (l1 ** 2):
        print('right')
    else:
        print('wrong')
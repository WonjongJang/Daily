import sys
sys.stdin = open('input.txt')


N = int(input())
tree = {}
for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

def preorder(n):
    if n != '.':
        l, r = tree[n]

        print(n, end='')
        preorder(l)
        preorder(r)

def inorder(n):
    if n != '.':
        l, r = tree[n]

        inorder(l)
        print(n, end='')
        inorder(r)

def postorder(n):
    if n != '.':
        l, r = tree[n]

        postorder(l)
        postorder(r)
        print(n, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
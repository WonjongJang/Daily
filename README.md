[TOC]

# 알고리즘

## 정렬(Sort)

### 버블 정렬(Bubble Sort)

인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식

평균 수행시간 : O(n^2)

최악 수행시간 : O(n^2)

기법 : 비교와 교환

- 장점
  - 코딩이 쉬움

```python
arr = [...]

for i in range(len(arr)-1, 0, -1):
    for j in range(0, i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
```

### 카운팅 정렬 (Counting Sort)

배열에 각 항목이 몇 개씩 있는지 세어 새로운 배열을 만듬

평균 수행시간 : O(n+k)

최악 수행시간 : O(n+k)

기법 : 비교환

- 단점
  - n이 비교적 작을 때만 가능

```python
arr = [...]		# 0 ~ k
ans = [0] * len(arr)
count = [0] * (k+1)

for i in range(0, len(ans)):
    count[arr[i]] += 1

for j in range(1, len(count)):
    count[j] += count[j-1]

for k in range(len(ans)-1, -1, -1):
    ans[count[arr[k]]-1] = arr[k]
    count[arr[k]] -= 1
```

### 선택 정렬(Selection Sort)

주어진 자료들 중 가장 작은 값의 원소부터 선택하여 위치 교환

평균 수행시간 : O(n^2)

최악 수행시간 : O(n^2)

기법 : 비교와 교환

- 장점
  - 교환 횟수가 버블, 삽입보다 작음

```python
arr = [...]

for i in range(len(arr)-1):
    min = i
    for j in range(i+1, len(arr)):
        if arr[min] > arr[j]:
            min = j
    arr[i], arr[min] = arr[min], arr[i]

# Selection Algorithm -> k번째로 작은 원소 구하기
arr[k-1]
```

### 퀵 정렬 (Quick Sort)

주어진 배열을 두 개로 분할하고 각각을 정렬

평균 수행시간 : O(nlogn)

최악 수행시간 : O(n^2)

기법 : 분할 정복

- 특징
  - 기준(Pivot)을 중심으로 작은 것은 왼편, 큰 것은 오른편에 위치

- 장점
  - 최악의 경우 아니라면, 평균적으로 가장 빠름
  - 두 부분 정렬 후 병합 작업 필요 X

```python
# Hoare-Patition
def partition(a, l, r):
    p = a[l]    # 피봇 값
    i, j = l, r
    while i <= j:
        while i <= j and a[i] <= p:
            i += 1
        while i <= j and a[j] >= p:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def quick_sort(a, l, r):
    if l < r:
        s = partition(a, l, r)
        quick_sort(a, l, s-1)
        quick_sort(a, s+1, r)

arr = [...]

quick_sort(arr, 0, len(arr)-1)
```

### 삽입 정렬 (Insertion Sort)

평균 수행시간 : O(n^2)

최악 수행시간 : O(n^2)

기법 : 비교와 교환

- 장점
  - n의 개수 작을 때 효과적

```python

```

### 병합 정렬 (Merge Sort)

여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식

평균 수행시간 : O(nlogn)

최악 수행시간 : O(nlogn)

기법 : 분할 정복

- 장점
  - 연결 리스트의 경우 가장 효율적

```python
```



## 그래프

### 탐욕(Greedy)

결정을 할 때 마다 최종 결과에 관계없이 그 순간에서 최선의 선택을 하는 것

그 순간의 선택은 그 수간에서 최적의 선택 (locally optimal solution)

하지만, 최종의 결과가 최적이라는 보장 X (global optimal solution)



## 재귀

- 재귀적 정의
  - 하나 또는 그 이상의 기본 경우(Basis case or rule) : 집합에 포함되어 있는 원소로 induction을 생성하기 위한 seed 역할
  - 하나 또는 그 이상의 유도된 경우(Inductive case or rule) : 새로운 집합의 원소를 생성하기 위해 결합되어지는 방법

### 재귀 함수(Recursive function)

함수 내부에서 직접/간접적으로 자기 자신을 호출하는 함수

- 특징
  - 일반적으로 재귀적 정의로 구현하여 기본 부분과 유도 부분으로 구성

- 장점
  - 반복에 비해 간결하고 이해하기 쉬움
- 단점
  - 재귀에 익숙하지 않으면 어려움
  - 함수 호출은 프로그램 메모리 구조에서 스택 사용 → 반복적인 스택 사용 → 메모리 및 속도 성능저하
  - 반복보다 더 많은 메모리와 연산 필요 (**n이 커질수록 반복에 비해 비효율적일 수 있음**)

#### 팩토리얼

```python
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)
```

#### 피보나치 수열(Fibonacci)

제0항을 0, 제1항을 1로 두고, 둘째 번 항부터는 바로 앞의 두 수를 더한 수

```python
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```

#### 하노이의 탑

3개의 기둥에 적당한 개수의 원반을 쌓아 놓고 다른 쪽으로 옮기는 게임

```python
def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:  # 원반 한 개를 옮기는 문제면 그냥 옮기면 됨
        print(from_pos, "->", to_pos)
        return

    # 원반 n - 1개를 aux_pos로 이동(to_pos를 보조 기둥으로)
    hanoi(n - 1, from_pos, aux_pos, to_pos)
    # 가장 큰 원반을 목적지로 이동
    print(from_pos, "->", to_pos)
    # aux_pos에 있는 원반 n-1개를 목적지로 이동(from_pos를 보조 기둥으로)
    hanoi(n - 1, aux_pos, to_pos, from_pos)

hanoi(1, 1, 3, 2)  # 원반 한 개를 1번 기둥에서 3번 기둥으로 이동(2번을 보조 기둥으로)
hanoi(2, 1, 3, 2)  # 원반 두 개를 1번 기둥에서 3번 기둥으로 이동(2번을 보조 기둥으로)
hanoi(3, 1, 3, 2) # 원반 세 개를 1번 기둥에서 3번 기둥으로 이동(2번을 보조 기둥으로)
```

#### 최소공배수(LCM : Least Common Multiple)

두 수/그 이상의 수들의 공통인 배수 중 가장 작은 것

```python
# A, B의 최소공배수는 A * B // GCD(A,B)

A = int(input())
B = int(input())

temp = A * B
while A % B != 0:
    A, B = B, A % B

print(temp // B)
```



# 기법


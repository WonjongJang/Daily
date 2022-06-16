[TOC]

# 알고리즘

## 정렬

### 버블 정렬(Bubble Sort)

인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식

`O(n^2)`

```python
arr = [...]

for i in range(len(arr)-1, 0, -1):
    for j in range(0, i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
```

### 선택 정렬(Selection Sort)

주어진 자료들 중 가장 작은 값의 원소부터 선택하여 위치 교환

`O(n^2)`

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

### 삽입 정렬 (Insertion Sort)

`O(n^2)`



## 그래프

### 탐욕(Greedy)

결정을 할 때 마다 최종 결과에 관계없이 그 순간에서 최선의 선택을 하는 것

그 순간의 선택은 그 수간에서 최적의 선택 (locally optimal solution)

하지만, 최종의 결과가 최적이라는 보장 X (global optimal solution)


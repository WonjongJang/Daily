function solution(A, B) {
  A.sort((a, b) => {
    return a - b;
  });
  B.sort((a, b) => {
    return a - b;
  });

  let result = 0;
  let left = 0; // A의 index
  for (let i = 0; i < A.length; i++) {
    // A의 첫번째 요소가 B의 요소 보다 작은 게 있을 때까지 찾음
    if (A[left] < B[i]) {
      left++;
      result++;
    }
  }
  return result;
}

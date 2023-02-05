function solution(n, computers) {
  const visited = new Array(n).fill(0); // 연결 체크

  // 연결 함수
  const recur = (x) => {
    visited[x] = 1; // 첫 컴퓨터 연결
    for (let j = 0; j < n; j++) {
      if (visited[j] === 0 && computers[x][j]) {
        // 체크 안했고, 연결 되어 있는 것
        recur(j);
      }
    }
  };

  let result = 0; // 네트워크 개수
  for (let i = 0; i < n; i++) {
    if (visited[i] === 0) {
      // 체크 안한 것만
      result++;
      recur(i);
    }
  }
  return result;
}

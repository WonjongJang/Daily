function solution(array) {
  array.sort((a, b) => {
    return a - b;
  });
  return array[parseInt(array.length / 2)];
}
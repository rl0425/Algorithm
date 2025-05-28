function solution(n, water) {
  const map = Array.from({ length: n }, () => Array(n).fill(0));
  const visited = Array.from({ length: n }, () => Array(n).fill(false));

  for (const [row, col] of water) {
    map[row - 1][col - 1] = 1;
  }

  const dy = [-1, 1, 0, 0];
  const dx = [0, 0, -1, 1];

  function bfs(y, x) {
    const queue = [[y, x]];
    visited[y][x] = true;

    while (queue.length) {
      const [cy, cx] = queue.shift();
      for (let i = 0; i < 4; i++) {
        const ny = cy + dy[i];
        const nx = cx + dx[i];
        if (
          ny >= 0 && ny < n &&
          nx >= 0 && nx < n &&
          !visited[ny][nx] &&
          map[ny][nx] === 0
        ) {
          visited[ny][nx] = true;
          queue.push([ny, nx]);
        }
      }
    }
  }

  let count = 0;
  for (let y = 0; y < n; y++) {
    for (let x = 0; x < n; x++) {
      if (map[y][x] === 0 && !visited[y][x]) {
        bfs(y, x);
        count++;
      }
    }
  }

  return count;
}

console.log("1:", solution(4, [[3,2]]));                     // 1
console.log("2:", solution(4, [[2,3],[3,2],[4,3]]));         // 3
console.log("3:", solution(4, [[1,2],[2,3],[3,1],[3,4]]));   // 3
console.log("4:", solution(3, [[1,3],[2,1],[3,3]]));         // 2

/**
 * 최소 인원으로 전체 빈 영역을 탐험하는 함수
 *
 * 문제 해석:
 * 1. 물 웅덩이(water)는 탐험대원이 갈 수 없는 장애물임
 * 2. 빈 영역은 모두 탐험해야 함
 * 3. 탐험대원은 이미 방문한 칸으로 돌아갈 수 없음 (즉, 막다른 길에 갇/**
 * 최소 인원으로 전체 빈 영역을 탐험하는 함수
 *
 * 문제 해석:
 * 1. 물 웅덩이(water)는 탐험대원이 갈 수 없는 장애물임
 * 2. 빈 영역은 모두 탐험해야 함
 * 3. 탐험대원은 이미 방문한 칸으로 돌아갈 수 없음
 * 4. 모든 빈 영역을 탐험하기 위한 최소 인원수를 구해야 함
 *
 * @param {number} n - 격자의 크기
 * @param {Array<Array<number>>} water - 물 웅덩이(장애물)의 좌표 배열 [[y1, x1], [y2, x2], ...]
 * @return {number} - 필요한 최소 인원수
 */
function solution(n, water) {
  // 물 웅덩이(장애물) 좌표를 Set에 저장
  const obstacles = new Set(water.map(([y, x]) => `${y},${x}`));

  // 격자의 모든 빈 칸을 그래프로 표현
  const graph = {};

  // 빈 칸 식별 및 그래프 구성
  for (let y = 1; y <= n; y++) {
    for (let x = 1; x <= n; x++) {
      const key = `${y},${x}`;
      if (!obstacles.has(key)) {
        graph[key] = [];

        // 상하좌우 인접 칸 확인
        const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        for (const [dy, dx] of directions) {
          const ny = y + dy;
          const nx = x + dx;
          const neighborKey = `${ny},${nx}`;

          if (ny >= 1 && ny <= n && nx >= 1 && nx <= n && !obstacles.has(neighborKey)) {
            graph[key].push(neighborKey);
          }
        }
      }
    }
  }

  // 가장 깊은 경로를 찾는 함수 (Longest Path)
  function findLongestPath(startNode, currentGraph) {
    // 이미 모든 노드가 방문되었거나 시작 노드가 없으면 빈 경로 반환
    if (Object.keys(currentGraph).length === 0 || !currentGraph[startNode]) {
      return [];
    }

    // 시작 노드의 방문 처리
    const path = [startNode];

    // 그래프 복사 (깊은 복사를 직접 구현)
    const updatedGraph = {};
    for (const node in currentGraph) {
      if (node !== startNode) {
        updatedGraph[node] = currentGraph[node].filter(neighbor => neighbor !== startNode);
      }
    }

    // 다음으로 갈 수 있는 노드 중 가장 긴 경로 찾기
    let bestPath = [];

    for (const neighbor of currentGraph[startNode] || []) {
      if (updatedGraph[neighbor]) {
        const subPath = findLongestPath(neighbor, updatedGraph);
        if (subPath.length > bestPath.length) {
          bestPath = subPath;
        }
      }
    }

    return [...path, ...bestPath];
  }

  // 남은 노드로 구성된 그래프 (원본 복사)
  let remainingGraph = {};
  for (const node in graph) {
    remainingGraph[node] = [...graph[node]];
  }


  // 탐험대원 수
  let explorerCount = 0;

  // 모든 빈 칸을 탐험할 때까지 반복
  while (Object.keys(remainingGraph).length > 0) {
    // 새로운 탐험대원 추가
    explorerCount++;

    // 시작 노드 선택 (남아있는 첫 노드)
    const startNode = Object.keys(remainingGraph)[0];

    // 가장 긴 경로 찾기
    const path = findLongestPath(startNode, remainingGraph);

    // 경로에 있는 노드를 남은 그래프에서 제거
    for (const node of path) {
      delete remainingGraph[node];

      // 제거된 노드를 다른 노드의 인접 목록에서도 제거
      for (const remainingNode in remainingGraph) {
        remainingGraph[remainingNode] = remainingGraph[remainingNode].filter(
          neighbor => neighbor !== node
        );
      }
    }
  }

  return explorerCount;
}

// 테스트 케이스
const testCases = [
  {
    n: 3,
    water: [ [1, 2],, [2,1], [2,2], [2,3], [3,2] ],
    expected: 4,
  },
  {
    n: 4,
    water: [[2, 3], [3, 2], [4, 3]],
    expected: 3
  },
  {
    n: 4,
    water: [[1, 2], [2, 3], [3, 1], [3, 4]],
    expected: 3
  },
  {
    n: 3,
    water: [[1, 3], [2, 1], [3, 3]],
    expected: 2
  }
];

// 테스트 실행
for (const { n, water, expected } of testCases) {
  const result = solution(n, water);
  console.log(`n: ${n}, water: ${JSON.stringify(water)}, 결과: ${result}, 예상: ${expected}`);
}
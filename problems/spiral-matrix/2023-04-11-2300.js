// Spiral Matrix
// https://leetcode.com/problems/spiral-matrix/
// Accepted 2023-04-11 23:00 UTC · JavaScript · 62 ms · 41.9 MB

/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
function spiralOrder(matrix) {
  if (!matrix.length) {
    return [];
  }

  const rows = matrix.length;
  const cols = matrix[0].length;
  const visited = new Set();
  const result = [];

  function dfs(row, col, directionIndex) {
    if (
      row < 0 ||
      row >= rows ||
      col < 0 ||
      col >= cols ||
      visited.has(`${row},${col}`)
    ) {
      return;
    }

    visited.add(`${row},${col}`);
    result.push(matrix[row][col]);

    const directions = [
      [0, 1],
      [1, 0],
      [0, -1],
      [-1, 0],
    ];
    const nextDirectionIndex =
      directionIndex  +1 >= directions.length ? 0 : directionIndex + 1;

    dfs(
      row + directions[directionIndex][0],
      col + directions[directionIndex][1],
      directionIndex
    );
    dfs(
      row + directions[nextDirectionIndex][0],
      col + directions[nextDirectionIndex][1],
      nextDirectionIndex
    );
  }

  dfs(0, 0, 0);

  return result;
}

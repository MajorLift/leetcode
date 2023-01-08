// Walls and Gates
// https://leetcode.com/problems/walls-and-gates/
// Accepted 2023-01-08 06:07 UTC · JavaScript · 740 ms · 51.9 MB

/**
 * @param {number[][]} rooms
 * @return {void} Do not return anything, modify rooms in-place instead.
 */
var wallsAndGates = function(rooms) {
    const[m, n] = [rooms.length, rooms[0].length]
    const queue = rooms.reduce((acc, row, i) => {
        row.forEach((e, j) => e === 0 ? acc.push([i, j]) : null)
        return acc
    }, [])
    while (queue.length) {
        const [r, c] = queue.shift()
        for (const [i, j] of [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]) {
            if (i >= 0 && i < m && j >= 0 && j < n && rooms[r][c] + 1 < rooms[i][j]) {
                rooms[i][j] = rooms[r][c] + 1
                queue.push([i, j])
            }
        }
    }
};

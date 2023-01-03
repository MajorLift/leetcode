// Pacific Atlantic Water Flow
// https://leetcode.com/problems/pacific-atlantic-water-flow/
// Accepted 2023-01-03 03:31 UTC · JavaScript · 363 ms · 64.1 MB

/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
var pacificAtlantic = function(heights) {
    const [m, n] = [heights.length, heights[0].length]
    const adj = Array.from({ length: m }, () => (Array.from({ length: n }, () => (new Array()))))
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            for (const [r, c] of [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]) {
                if (r >= 0 && r < m && c >= 0 && c < n && heights[i][j] >= heights[r][c]) {
                    adj[r][c].push([i, j])
                }
            }
        }
    }
    function dfs(stack = [], output = new Set()) {
        while (stack.length) {
            const [i, j] = stack.pop()
            output.add([i, j].join(','))
            for (const u of adj[i][j]) {
                if (!output.has(u.join(','))) {
                    stack.push(u)
                }
            }
        }
        return output
    }
    const pacific = dfs([...Array.from({ length: m }, (_, i) => ([i, 0])), ...Array.from({ length: n - 1 }, (_, j) => ([0, j + 1]))])
    const atlantic = dfs([...Array.from({ length: m }, (_, i) => ([i, n - 1])), ...Array.from({ length: n - 1 }, (_, j) => ([m - 1, j]))])
    return [...pacific].filter((e) => atlantic.has(e)).map((e) => e.split(','))
}

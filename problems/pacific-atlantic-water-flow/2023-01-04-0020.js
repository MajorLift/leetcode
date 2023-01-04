// Pacific Atlantic Water Flow
// https://leetcode.com/problems/pacific-atlantic-water-flow/
// Accepted 2023-01-04 00:20 UTC · JavaScript · 156 ms · 50 MB

/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
var pacificAtlantic = function(heights) {
    const [m, n] = [heights.length, heights[0].length]
    function dfs(r, c, visited) {
        visited.add([r, c].join(','))
        for (const [i, j] of [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]) {
            if (i >= 0 && i < m && j >= 0 && j < n 
                && !visited.has([i, j].join(',')) 
                && heights[i][j] >= heights[r][c]) {
                dfs(i, j, visited)
            }
        }
        return visited
    }
    const [pacific, atlantic] = [new Set(), new Set()]
    for (let i = 0; i < m; ++i) {
        dfs(i, 0, pacific)
        dfs(i, n - 1, atlantic)
    }
    for (let j = 0; j < n - 1; ++j) {
        dfs(0, j + 1, pacific)
        dfs(m - 1, j, atlantic)
    }
    return [...pacific].filter((e) => atlantic.has(e)).map((e) => e.split(','))
}

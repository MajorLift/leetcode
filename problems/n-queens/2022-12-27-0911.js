// N-Queens
// https://leetcode.com/problems/n-queens/
// Accepted 2022-12-27 09:11 UTC · JavaScript · 84 ms · 45.4 MB

/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function(n) {
    const output = []
    const init = Array.from(new Array(n), () => new Array(n).fill("."))
    const [cols, diags, antiDiags] = Array.from(new Array(3), () => new Set())
    ;(function backtrack(row = 0, state = init) {
        if (row === n) {
            output.push(state.map((row) => row.join('')))
            return
        }
        for (let col = 0; col < n; ++col) {
            if (cols.has(col) || diags.has(row - col) || antiDiags.has(row + col)) continue
            cols.add(col); diags.add(row - col); antiDiags.add(row + col)
            state[row][col] = "Q"
            backtrack(row + 1, state)
            state[row][col] = "."
            cols.delete(col); diags.delete(row - col); antiDiags.delete(row + col)
        }
    })()
    return output
};

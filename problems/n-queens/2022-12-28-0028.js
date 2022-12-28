// N-Queens
// https://leetcode.com/problems/n-queens/
// Accepted 2022-12-28 00:28 UTC · JavaScript · 93 ms · 45.8 MB

/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function(n) {
    const output = []
    const init_board = Array.from({ length: n }, () => new Array(n).fill("."))
    const [cols, diags, antiDiags] = Array.from({ length: 3 }, () => new Set())
    ;(function backtrack(row = 0, state = init_board) {
        if (row === n) {
            output.push(state.map((row) => row.join('')))
            return
        }
        for (let col = 0; col < n; ++col) {
            if (cols.has(col) || diags.has(row - col) || antiDiags.has(row + col)) continue
            cols.add(col); diags.add(row - col); antiDiags.add(row + col)
            state[row][col] = "Q"
            backtrack(row + 1)
            state[row][col] = "."
            cols.delete(col); diags.delete(row - col); antiDiags.delete(row + col)
        }
    })()
    return output    
}

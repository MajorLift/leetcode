// Word Search
// https://leetcode.com/problems/word-search/
// Accepted 2022-12-21 23:08 UTC · JavaScript · 874 ms · 47.8 MB

/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    const [m, n] = [board.length, board[0].length]
    // const wordChars = word.split('').reduce((acc, curr) => (acc[curr] = (acc[curr] || 0) + 1), {})
    // const boardChars = board.flat().reduce((acc, curr) => (acc[curr] = (acc[curr] || 0) + 1), {})
    // if (m * n < word.length 
    //     || !Object.keys(wordChars).every((k) => (wordChars[k] <= (boardChars[k] || -math.inf)))) return false
    
    function backtrack([x, y], idx) {
        if (idx === word.length - 1) return true
        const char = board[x][y]
        board[x][y] = "0"
        for (const [i, j] of [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]) {
            if (!(i >= 0 && i < m && j >= 0 && j < n) || board[i][j] !== word[idx + 1]) continue
            if (backtrack([i, j], idx + 1)) return true
        }
        board[x][y] = char
        return false
    }

    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (board[i][j] == word[0]) {
                if (backtrack([i, j], 0)) return true
            }
        }
    }
    return false
}

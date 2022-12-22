// Word Search
// https://leetcode.com/problems/word-search/
// Accepted 2022-12-22 04:56 UTC · JavaScript · 71 ms · 44 MB

/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    const [m, n] = [board.length, board[0].length]
    const wordCharsCount = word.split('').reduce((acc, curr) => {
        acc[curr] = (acc[curr] || 0) + 1
        return acc
    }, {})
    const boardCharsCount = board.flat().reduce((acc, curr) => {
        acc[curr] = (acc[curr] || 0) + 1
        return acc
    }, {})
    
    if (m * n < word.length
        || !Object.keys(wordCharsCount)
            .every((k) => (wordCharsCount[k] <= (boardCharsCount[k] || -Math.infinity)))
    ) return false

    if (wordCharsCount[word[0]] > wordCharsCount[word[word.length - 1]]) {
        word = word.split('').reverse().join('')
    }
    
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

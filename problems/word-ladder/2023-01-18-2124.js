// Word Ladder
// https://leetcode.com/problems/word-ladder/
// Accepted 2023-01-18 21:24 UTC · JavaScript · 166 ms · 55.9 MB

/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
var ladderLength = function(beginWord, endWord, wordList) {
    const words = new Set(wordList)
    if (!words.has(endWord)) return 0

    const k = beginWord.length
    const adj = wordList.reduce((acc, curr) => {
        for (let i = 0; i < k; ++i) {
            const pattern = curr.slice(0, i) + "*" + curr.slice(i + 1)
            acc[pattern] = (acc[pattern] ?? []).concat(curr)
        }
        return acc
    }, {})
    const dist = wordList.reduce((acc, curr) => {
        acc[curr] = curr !== beginWord ? Number.POSITIVE_INFINITY : 0
        return acc
    }, {})
    
    const queue = [beginWord]
    let level = 0
    while (queue.length) {
        level++
        const next_queue = []
        while (queue.length) {
            const word = queue.shift()
            if (word === endWord) return level
            for (let i = 0; i < k; ++i) {
                const pattern = word.slice(0, i) + "*" + word.slice(i + 1)
                for (const s of (adj[pattern] ?? [])) {
                    if (level + 1 < dist[s]) {
                        dist[s] = level + 1
                        next_queue.push(s)
                    }
                }
            }
        }
        queue.push(...next_queue)
    }
    return 0
};

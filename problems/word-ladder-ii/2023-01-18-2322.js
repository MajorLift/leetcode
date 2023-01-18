// Word Ladder II
// https://leetcode.com/problems/word-ladder-ii/
// Accepted 2023-01-18 23:22 UTC · JavaScript · 111 ms · 46.1 MB

/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {string[][]}
 */
var findLadders = function(beginWord, endWord, wordList) {
    wordList.push(beginWord)
    const words = new Set(wordList)
    if (!words.has(endWord)) return []
    
    const adj = wordList.reduce((acc, curr) => {
        for (let i = 0; i < beginWord.length; ++i) {
            const pattern = curr.slice(0, i) + "*" + curr.slice(i + 1)
            acc[pattern] = (acc[pattern] ?? []).concat(curr)
        }
        return acc
    }, {})
    const tree = {}
    const dist = wordList.reduce((acc, curr) => {
        acc[curr] = curr !== endWord ? Number.POSITIVE_INFINITY : 0
        return acc
    }, {})
    
    let level = 0
    let flag = false
    const queue = [endWord]
    while (queue.length) {
        level++
        const next_queue = []
        while (queue.length) {
            const word = queue.shift()
            if (word === beginWord) {
                flag = true
                continue
            }
            for (let i = 0; i < beginWord.length; ++i) {
                const pattern = word.slice(0, i) + "*" + word.slice(i + 1)
                for (const prev of (adj[pattern] ?? [])) {
                    if ((!tree[prev] || !tree[prev].has(word)) && level + 1 <= dist[prev]) {
                        dist[prev] = level + 1
                        if (!tree[prev]) tree[prev] = new Set([word])
                        else tree[prev].add(word)
                        next_queue.push(prev)
                    }
                }
            }
        }
        if (flag) break
        queue.push(...next_queue)
    }

    const output = []
    const stack = [[beginWord]]
    while (stack.length) {
        const path = stack.pop()
        const word = path[path.length - 1]
        if (word === endWord) {
            output.push(path)
            continue
        }
        for (const next_word of (tree[word] ?? [])) stack.push(path.concat(next_word))
    }
    return output
};

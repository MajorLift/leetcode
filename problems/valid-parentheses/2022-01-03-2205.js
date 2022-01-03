// Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/
// Accepted 2022-01-03 22:05 UTC · JavaScript · 145 ms · 39.9 MB

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const stack = []
    for (let i = 0; i < s.length; i += 1) {
        const p = s[i]
        if (['(', '{', '['].includes(p)) stack.push(p)
        else {
            const open = stack.pop()
            if (open === undefined || (p === ')' && open !== '(') || (p === '}' && open !== '{') || (p === ']' && open !== '[')) return false
        }
    }
    return stack.length === 0
};

// Count Unhappy Friends
// https://leetcode.com/problems/count-unhappy-friends/
// Accepted 2023-10-15 23:28 UTC · JavaScript · 99 ms (15.63%) · 59.8 MB (6.25%)

/**
 * @param {number} n
 * @param {number[][]} preferences
 * @param {number[][]} pairs
 * @return {number}
 */
var unhappyFriends = function(n, preferences, pairs) {
    const people = preferences.map((e) => new Person(e))
    const partnerOf = {}
    for (const [x, y] of pairs) {
        partnerOf[x] = y
        partnerOf[y] = x
    }

    let unhappy = 0
    for (let x = 0; x < n; ++x) {
        const [X, y] = [people[x], partnerOf[x]]
        for (const u of X.getPreferredOver(y)) {
            const [U, v] = [people[u], partnerOf[u]]
            if (U.getPreferredOver(v).has(x)) {
                unhappy += 1
                break
            }
        }
    }
    
    return unhappy
};

class Person {
    constructor(preference) {
        this.preference = preference
    }

    getPreferredOver(friend) {
        return new Set(this.preference.slice(0, this.preference.indexOf(friend)))
    }
}

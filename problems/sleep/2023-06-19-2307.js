// Sleep
// https://leetcode.com/problems/sleep/
// Accepted 2023-06-19 23:07 UTC · JavaScript · 55 ms · 42.1 MB

/**
 * @param {number} millis
 */
async function sleep(millis) {
    return new Promise((resolve) => setTimeout(() => {
        resolve()
    }, [millis]))
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */

// Sleep
// https://leetcode.com/problems/sleep/
// Accepted 2023-06-20 02:20 UTC · JavaScript · 70 ms · 42 MB

/**
 * @param {number} millis
 */
async function sleep(millis) {
    let timer
    return new Promise((resolve, reject) => {
        try {
            timer = setTimeout(() => {
                resolve()
            }, millis)
        } catch(err) {
            reject(err)
        } finally {
            () => clearTimeout(timer)
        }
    })
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */

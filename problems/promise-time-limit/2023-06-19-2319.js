// Promise Time Limit
// https://leetcode.com/problems/promise-time-limit/
// Accepted 2023-06-19 23:19 UTC · JavaScript · 62 ms · 41.8 MB

/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
	return async function(...args) {
        return new Promise(async (resolve, reject) => {
            const timer = setTimeout(() => {
                reject("Time Limit Exceeded")
            }, t)
            try {
                const res = await fn(...args)
                resolve(res)
            } catch(err) {
                reject(err)
            } finally {
                clearTimeout(timer)
            }
        })
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */

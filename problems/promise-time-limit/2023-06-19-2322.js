// Promise Time Limit
// https://leetcode.com/problems/promise-time-limit/
// Accepted 2023-06-19 23:22 UTC · JavaScript · 69 ms · 42 MB

/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
	return async function(...args) {
        const timeLimitPromise = new Promise((resolve, reject) => {
            const timer = setTimeout(() => {
                reject("Time Limit Exceeded")
            }, t)
        })
        const returnedPromise = fn(...args)
        return Promise.race([timeLimitPromise, returnedPromise])
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */

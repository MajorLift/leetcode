// Timeout Cancellation
// https://leetcode.com/problems/timeout-cancellation/
// Accepted 2023-06-21 01:30 UTC · JavaScript · 67 ms · 41.8 MB

/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    let isCancelled = false
    const cancelFn = () => {
        isCancelled = true
    }
    setTimeout(() => {
        if (!isCancelled) fn(...args)
    }, t)
    return cancelFn
};

/**
 *  const result = []
 *
 *  const fn = (x) => x * 5
 *  const args = [2], t = 20, cancelT = 50
 *
 *  const log = (...argsArr) => {
 *      result.push(fn(...argsArr))
 *  }
 *       
 *  const cancel = cancellable(fn, args, t);
 *           
 *  setTimeout(() => {
 *     cancel()
 *     console.log(result) // [{"time":20,"returned":10}]
 *  }, cancelT)
 */

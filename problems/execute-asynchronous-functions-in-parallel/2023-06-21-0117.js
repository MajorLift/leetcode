// Execute Asynchronous Functions in Parallel
// https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/
// Accepted 2023-06-21 01:17 UTC · JavaScript · 76 ms · 42.6 MB

/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = async function(functions) {
    return new Promise(async (resolve, reject) => {
        let completed = 0
        const output = new Array(functions.length).fill(null)
        functions.forEach(async (func, i) => {
            try {
                output[i] = await func()
                completed += 1
                if (completed === functions.length) resolve(output)
            } catch(err) {
                reject(err)
            }
        })
    })
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */

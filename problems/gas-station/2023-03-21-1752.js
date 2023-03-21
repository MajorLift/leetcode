// Gas Station
// https://leetcode.com/problems/gas-station/
// Accepted 2023-03-21 17:52 UTC · JavaScript · 88 ms · 52.4 MB

/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
    if (gas.reduce((acc, curr) => (acc + curr)) < cost.reduce((acc, curr) => (acc + curr))) {
        return -1
    }
    let start = tank = 0
    for (let i = 0; i < gas.length; ++i) {
        tank += gas[i] - cost[i]
        if (tank < 0) {
            ;[start, tank] = [i + 1, 0]
        }
    }
    return start
}

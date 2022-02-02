// Maximum Value after Insertion
// https://leetcode.com/problems/maximum-value-after-insertion/
// Accepted 2022-02-02 17:33 UTC · JavaScript · 299 ms · 76.8 MB

/**
 * @param {string} n
 * @param {number} x
 * @return {string}
 */
var maxValue = function(n, x) {
    let output = "";
    let negFlag = false;
    let insertFlag = false;
    for (let i = 0; i < n.length; i++) {
        if (n[i] === "-") {
            output += "-";
            negFlag = true;
            continue;
        }
        const curr = parseInt(n[i]);
        if (!insertFlag && ((!negFlag && x > curr) || (negFlag && x < curr))) {
            output += x;
            insertFlag = true;
        }
        output += n[i];
    }
    if (!insertFlag) output += x;
    return output;
};

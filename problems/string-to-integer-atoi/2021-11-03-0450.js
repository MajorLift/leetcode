// String to Integer (atoi)
// https://leetcode.com/problems/string-to-integer-atoi/
// Accepted 2021-11-03 04:50 UTC · JavaScript · 92 ms · 41.5 MB

/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function(s) {
    let i = 0;
    // trim whitespace
    while (s[i] === ' ' && i < s.length) i += 1;
    if (i === s.length) return 0;
    
    // parse sign
    let negative = false;
    if (s[i] === '-') {
        negative = true;
        i += 1;
    } 
    else if (s[i] === '+') i += 1;
    if (i === s.length) return 0;
        
    // non-digit
    let output = '';
    while (i < s.length) {
        if (s[i].search(/[0-9]/) === -1) break;
        output += s[i];
        i += 1;
    }
    
    output = negative ? -1 * Number(output) : Number(output);
    return output > Math.pow(2, 31) - 1 ? Math.pow(2, 31) - 1 : output < -1 * Math.pow(2, 31) ? -1 * Math.pow(2, 31) : output;
    
};

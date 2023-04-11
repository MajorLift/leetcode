// Spiral Matrix
// https://leetcode.com/problems/spiral-matrix/
// Accepted 2023-04-11 15:28 UTC · JavaScript · 58 ms · 42.2 MB

/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
   let [nr, nc] = [matrix.length, matrix[0].length]
   const output = []
   while (nr >= 1 && nc >= 1) {
      if (nr === 0) break
      output.push(...(matrix.shift()))
      nr--

      if (nc === 0) break
      for (let i = 0; i < nr; ++i) {
         output.push(matrix[i].pop())
      }
      nc--

      if (nr === 0) break
      output.push(...(matrix.pop().reverse()))
      nr--

      if (nc === 0) break
      for (let i = nr - 1; i >= 0; --i) {
         output.push(matrix[i].shift())
      }
      nc--
   }
   return output
}

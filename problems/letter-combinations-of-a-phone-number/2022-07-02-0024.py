# Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Accepted 2022-07-02 00:24 UTC · Python · 46 ms · 14 MB

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dictionary = {k: [chr(3 * (k - 2) + i + ord("a")) for i in range(3)] for k in range(2, 7)}
        dictionary[7] = ['p', 'q', 'r', 's']
        dictionary[8] = ['t', 'u', 'v']
        dictionary[9] = ['w', 'x', 'y', 'z']
        # print(dictionary)

        output = []
        def backtrack(prev, currDigitIdx):
            if len(prev) == len(digits):
                output.append("".join(prev))
                return
            for letter in dictionary[int(digits[currDigitIdx])]:
                prev.append(letter)
                backtrack(prev, currDigitIdx + 1)
                prev.pop()
    
        backtrack([], 0)            
        return output

# Reconstruct Original Digits from English
# https://leetcode.com/problems/reconstruct-original-digits-from-english/
# Accepted 2022-09-27 03:58 UTC · Python · 64 ms · 14.4 MB

class Solution:
    def originalDigits(self, s: str) -> str:
        counts = defaultdict(int)
        for char in s:
            counts[char] += 1
        # print(counts)
            
        output = {}
        output["0"] = counts["z"]
        output["2"] = counts["w"]
        output["4"] = counts["u"]
        output["6"] = counts["x"]
        output["8"] = counts["g"]
        
        output["3"] = counts["h"] - output["8"]
        output["5"] = counts["f"] - output["4"]
        output["7"] = counts["s"] - output["6"]
        
        output["9"] = counts["i"] - (output["5"] + output["6"] + output["8"])
        output["1"] = counts["n"] - (output["7"] + 2 * output["9"])
        # print(output)

        return "".join([num * output[num] for num in sorted(output.keys())])

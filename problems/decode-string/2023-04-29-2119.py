# Decode String
# https://leetcode.com/problems/decode-string/
# Accepted 2023-04-29 21:19 UTC · Python · 43 ms · 16.4 MB

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "]":
                decoded = ""
                while stack and stack[-1] != "[":
                    decoded = stack.pop() + decoded
                stack.pop()
                count = ""
                while stack and stack[-1].isnumeric():
                    count = stack.pop() + count
                stack.append(decoded * int(count or 1))
            else:
                stack.append(char)
        return ''.join(stack)

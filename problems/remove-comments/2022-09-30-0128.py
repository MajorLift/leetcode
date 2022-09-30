# Remove Comments
# https://leetcode.com/problems/remove-comments/
# Accepted 2022-09-30 01:28 UTC · Python · 79 ms · 14 MB

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        block_sw = False
        output = []
        for line in source:
            stripped = ""
            # if newline is encountered while parsing a block comment, 
            # append subsequent output to previous non-empty line
            if block_sw:
                stripped = output.pop()
            i = 0
            while i < len(line):
                if not block_sw:
                    # remove line comment contents "//"
                    if i < len(line) - 1 and line[i] == line[i + 1] == "/":
                        break
                    # process open block comment "/*"
                    elif i < len(line) - 1 and line[i] == "/" and line[i + 1] == "*":
                        block_sw = True
                        i += 1 # skip next character
                    # append non-comment code to output
                    else:
                        stripped += line[i]
                # process close block comment "*/"
                elif i < len(line) - 1 and line[i] == "*" and line[i + 1] == "/":
                    block_sw = False
                    i += 1 # skip next character
                i += 1 # increment index

            if len(stripped):
                output.append(stripped)
        return output

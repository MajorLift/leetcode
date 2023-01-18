# Word Ladder
# https://leetcode.com/problems/word-ladder/
# Accepted 2023-01-18 20:57 UTC · Python · 124 ms · 17.6 MB

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words, visited = set(wordList), set()
        if endWord not in words:
            return 0
            
        k = len(beginWord)
        adj = defaultdict(list)
        for word in words: 
            for i in range(k):
                pattern = word[:i] + '*' + word[i+1:]
                adj[pattern].append(word)

        queue = deque([beginWord])
        dist = 0
        while queue:
            dist += 1
            next_queue = deque([])
            while queue:
                word = queue.popleft()
                if word == endWord:
                    return dist
                for i in range(k):
                    pattern = word[:i] + '*' + word[i+1:]
                    for s in adj[pattern]:
                        if s not in visited and s in words:
                            visited.add(s)
                            next_queue.append(s)
            queue = next_queue
        return 0

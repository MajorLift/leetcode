# Word Ladder
# https://leetcode.com/problems/word-ladder/
# Accepted 2023-01-18 21:16 UTC · Python · 148 ms · 17.8 MB

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
            
        k = len(beginWord)
        adj = defaultdict(list)
        for word in words: 
            for i in range(k):
                pattern = word[:i] + '*' + word[i+1:]
                adj[pattern].append(word)

        visited = {word: +math.inf for word in words}
        visited[beginWord] = 0
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
                    if pattern not in adj:
                        continue
                    for s in adj[pattern]:
                        if dist + 1 < visited[s]:
                            visited[s] = dist + 1
                            next_queue.append(s)
            queue = next_queue
        return 0

# Word Ladder
# https://leetcode.com/problems/word-ladder/
# Accepted 2023-01-18 21:18 UTC · Python · 139 ms · 17.9 MB

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

        dist = {word: 0 if word == beginWord else +math.inf for word in words}
        queue = deque([beginWord])
        level = 0
        while queue:
            level += 1
            next_queue = deque()
            while queue:
                word = queue.popleft()
                if word == endWord:
                    return level
                for i in range(k):
                    pattern = word[:i] + '*' + word[i+1:]
                    if pattern not in adj:
                        continue
                    for s in adj[pattern]:
                        if level + 1 < dist[s]:
                            dist[s] = level + 1
                            next_queue.append(s)
            queue = next_queue
        return 0

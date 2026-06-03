from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        sourceIdx = 0
        targetIdx = -1
        nWords = len(wordList)
        q = deque([(0, 0)])
        visited = [False] * (nWords + 1)
        visited[0] = True
        for idx, w in enumerate(wordList):
            if w == endWord:
                targetIdx = idx + 1

        adj = [[] for _ in range(nWords + 1)]
        for i in range(nWords):
            for j in range(nWords):
                w1 = wordList[i]
                w2 = wordList[j]
                if edgeExists(w1, w2):
                    adj[i+1].append(j+1)

        for i in range(nWords):
            w = wordList[i]
            if edgeExists(beginWord, w):
                adj[0].append(i + 1)

        while q:
            for _ in range(len(q)):
                weight, wordIdx = q.popleft()
                if wordIdx == targetIdx:
                    return weight +1

                for neigh in adj[wordIdx]:
                    if not visited[neigh]:
                        q.append((weight+1, neigh))
                        visited[neigh] = True
        return 0

def edgeExists(s1, s2):
    diff = 0
    for i in range(len(s1)):
        diff += (s1[i] != s2[i])
    return diff == 1
        
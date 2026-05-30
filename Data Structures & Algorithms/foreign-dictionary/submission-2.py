from collections import deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # build graph based on pair
        # find u -> v based on first different character between pairs
        # do topological sort on the created graph. if no cycle, return the string

        if not words:
            return ""
        nWords = len(words)
        orderedAlphabet = ""
        graph = [[] for _ in range(26)]
        q = deque()
        ingoing = [0] * 26
        full = "".join(words)
        allLetters = set(full)
        nLetters = len(allLetters)

        for i in range(1, nWords):
            prev = words[i-1]
            curr = words[i]
            diffIdx = findFirstDifferentCharacterIndex(prev, curr)
            if diffIdx != -1:
                graph[ord(prev[diffIdx]) - ord('a')].append(ord(curr[diffIdx]) - ord('a'))
            else:
                if len(prev) > len(curr):
                    return ""

        for i in range(26):
            for node in graph[i]:
                ingoing[node] += 1

        for i in range(26):
            letter = chr(i + ord('a'))
            if not ingoing[i] and letter in allLetters:
                orderedAlphabet += letter
                q.append(i)
        
        while q:
            curr = q.popleft()
            for neigh in graph[curr]:
                ingoing[neigh] -= 1
                if not ingoing[neigh]:
                    orderedAlphabet += chr(neigh + ord('a'))
                    q.append(neigh)

        print(orderedAlphabet, nLetters)
        if len(orderedAlphabet) == nLetters:
            return orderedAlphabet
        return ""

        
def findFirstDifferentCharacterIndex(w1, w2):
    minLength = min(len(w1), len(w2))
    for i in range(minLength):
        if w1[i] != w2[i]:
            return i
    return -1
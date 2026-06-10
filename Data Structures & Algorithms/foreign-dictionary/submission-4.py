from collections import deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        ordered = []
        nWords = len(words)
        adj = [[] for _ in range(26)]
        ingoing = [0] * 26
        q = deque()
        allLetters = ""
        for w in words:
            allLetters += w
        allLetters = set(allLetters)

        for i in range(1, nWords):
            idx = findFirstDifferentIndex(words[i-1], words[i])
            if idx == -1:
                if len(words[i-1]) > len(words[i]):
                    return ""
                continue
            adj[ ord(words[i-1][idx])- ord('a')].append(ord(words[i][idx]) - ord('a'))
            ingoing[ord(words[i][idx]) - ord('a')] += 1

        for i in range(26):
            if not ingoing[i] and chr(i + ord('a')) in allLetters:
                ordered.append(chr(i + ord('a')))
                q.append(i)

        while q:
            curr = q.popleft()
            for neigh in adj[curr]:
                ingoing[neigh] -= 1
                if not ingoing[neigh] and chr(neigh + ord('a')) in allLetters:
                    q.append(neigh)
                    ordered.append(chr(neigh + ord('a')))

        if len(ordered) == len(allLetters):
            return "".join(ordered)
        return ""



def findFirstDifferentIndex(w1, w2):
    # hrn, hrf ->
    for i in range(min(len(w1), len(w2))):
        if w1[i] != w2[i]:
            return i

    return -1
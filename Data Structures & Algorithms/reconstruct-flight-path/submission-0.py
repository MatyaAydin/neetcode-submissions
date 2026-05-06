class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        source = "JFK"
        path = []
        tickets.sort()
        adj = defaultdict(list)
        for t in tickets[::-1]:
            # if t[0] not in adj:
            #     adj[t[0]] = []
            adj[t[0]].append(t[1])
        print(adj)

        def dfs(src):
            while adj[src]:
                to = adj[src].pop()
                dfs(to)
            path.append(src)

        dfs(source)
        return path[::-1]
        
class Solution:
	def canFinish(self, numCourses, prerequisites):
		adj = [[] for _ in range(numCourses)]
		for u,v in prerequisites:
			adj[u].append(v)

		visited = [False] * numCourses
		visiting = [False] * numCourses
		def cyclicUtil(node, visiting, visited):
			if visiting[node]:
				return True
			if visited[node]:
				return False
			visited[node] = True
			visiting[node] = True
			for neigh in adj[node]:
				if cyclicUtil(neigh, visiting, visited):
					return True
			visiting[node] = False
			return False
		for i in range(numCourses):
			if not visited[i] and cyclicUtil(i, visiting, visited):
				return False
		return True



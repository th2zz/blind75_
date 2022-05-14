import collections
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1 and len(edges) == 0:  # handle base case
            return True
        if len(edges) != n - 1:  # 排除不连通 和有环的情况 边的数量<n-1不连通 >n-1有环
            return False
        graph = collections.defaultdict(set)
        for u, v in edges:  # build undirected graph by two-way edges
            graph[u].add(v)
            graph[v].add(u)
        q = collections.deque([0])  # bfs检查是否为连通的
        visited = {0}
        print(graph)
        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        return len(visited) == n
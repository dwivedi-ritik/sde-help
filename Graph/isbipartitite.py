class Solution:
    # Check bipartite for each components
    def isBipartite(self, adj: List[List[int]]) -> bool:
        V = len(adj)
        visited = [ False for _ in range(V+1)]
        colored = [ -1 for _ in range(V+1)]
        for i in range(V):
            if colored[i] == -1:
                if not self.ifBipar(i , adj , colored , visited):
                    return False
        return True

    def ifBipar(self, i , adj , colored , visited):
        q = []
        while True:
            if not visited[i]:
                visited[i] = True
                colored[i] = 1
                q.append(i)

            for el in adj[i]:
                if not visited[el]:
                    visited[el] = True
                    q.append(el)
                if (colored[el] == 0 and colored[i] == 0) or (colored[el] == 1 and colored[i] == 1):
                    return False
                else:
                    colored[el] = 0 if colored[i] == 1 else 1

            q.pop(0)
            if not q:
                break
            else:
                i = q[0]
        return True

        
# 3 4
# 3 0
# 3 2
# 0 2
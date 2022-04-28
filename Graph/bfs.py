#User function Template for python3

# https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1#

class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        visited = [ False for _ in range(V)]
        q = []
        res = []
        i = 0
        while True:
            if not visited[i]:
                visited[i] = True
                q.append(i)
            
            for el in adj[i]:
                if not visited[el]:
                    visited[el] = True
                    q.append(el)
            res.append(q.pop(0))
            if not q:
                break
            else:
                i = q[0]
        return res








class Solution:    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # print(adj)
        stack = []
        visited = [False for _ in range(V)]
        
        def dfs(i):
            visited[i] = True
            for el in adj[i]:
                if not visited[el]:
                    dfs(el)
            stack.append(i)
                    
        for i in range(V):
            if not visited[i]:
                dfs(i)
                
        return stack[::-1]
        # Code here


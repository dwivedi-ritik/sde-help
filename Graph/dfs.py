# https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1#

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        trav = []
        visted = [ False for _ in range(V)]
        i = 0
        def dfs(i):
            if not visted[i]:
                visted[i] = True
                trav.append(i)
                
            for el in adj[i]:
                if not visted[el]:
                    trav.append(el)
                    visted[el] = True
                    dfs(el)
        
        dfs(0)
        
        return trav
    
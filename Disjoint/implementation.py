# Where s is total number of sets
par = [ i for i in range(len(s))]
        
def find(n):
    if n != par[n]:
        par[n] = find(par[n])
    return par[n]
        
def union(n1 , n2):
    p1 , p2 = find(n1) , find(n2)
    if p1 != p2:
        par[p2] = p1
                

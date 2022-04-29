# Union find algorithm can be used to find the cycle in indirected graph

# https://www.codingninjas.com/codestudio/problems/1062670?topList=striver-sde-sheet-problems&leftPanelTab=0

def cycleDetection(edges, n, m):

    # Write your code here.
    # Return "Yes" if cycle id present in the graph else return "No".
	par = [ i for i in range(n+1) ]
	rank = [ 1 for _ in range(n+1) ]

	def find(n):
		p = par[n]
		while p != par[p]:
			p = par[p]
		return p

	def union(n1 , n2):
		p1 , p2 = find(n1) , find(n2)

		if p1 == p2:
			return False

		if rank[p1] > rank[p2]:
			par[p2] = p1
			rank[p1] += 1
		else:
			par[p1] = p2
			rank[p2] += 1
		return True

	for n1 , n2 in edges:
		if not union(n1 , n2):
			return "Yes"
	return "No"
	return True

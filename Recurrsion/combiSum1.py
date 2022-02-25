def combinationSum(candidate , target):
	ans = []
	def dfs(i , curr_sum , curr_list):
		if curr_sum == target:
			print(curr_list)
			ans.append(curr_list)
		if curr_sum > target or i > len(candidate):
			return

		for j in range(i , len(candidate)):
			curr_list.append(candidate[j])
			dfs(j , curr_sum + candidate[j] , curr_list)
			curr_list.pop()
	dfs(0,0, [])
	return ans
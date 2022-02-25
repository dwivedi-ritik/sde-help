#Algorithm
# Sort the jobs in descending order of profit. 
# If the maximum deadline is x, make an array of size x .Each array index is set to -1 initially as no jobs have been performed yet.
# For every job check if it can be performed on its last day.
# If possible mark that index with the job id and add the profit to our answer. 
# If not possible, loop through the previous indexes until an empty slot is found.

def jobSeq(jobs):
	jobs = sorted(jobs , reverse = True , key=lambda x:x[-1])
	max_deadline = max([el[1] for el in jobs])
	print(jobs)
	arr = [-1]*(max_deadline+1)

	count , deadline , profit = 0 , 0, 0 
	
	i , j = 0 , 0
	for el in jobs:
		if  arr[el[1]] == -1:
			arr[el[1]] = el[0]
			count += 1
			profit += el[2]
		else:
			i = el[1]
			while i >= 1:
				if arr[i] == -1:
			
					arr[i] = el[0]
					count += 1
					profit += el[2]		
					break
				i -=1
	return (count , profit)


if __name__ == "__main__":
	# arr = [[1, 56 ,288], [2, 27, 435], [3, 67, 401] , [4, 64, 368] ,  [5, 94, 248] , [6, 54, 361] , [7 ,43, 108] ,[8, 96, 167] ,[9, 73, 251] ,[10, 96, 170] ,[11, 14, 156] ,[12, 78, 184] ,[13, 61, 370],[ 14, 77, 424] ,[15, 68, 397],[ 16, 40, 375] ,[17 ,36, 218]]
	arr = [(1,2,100),(2,1,19),(3,2,27),
        (4,1,25),(5,1,15)]
	print(jobSeq(arr))

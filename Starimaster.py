"""
Good morning,

Today's Byte

This question is asked by Apple. Given a staircase 
where the ith step has a non-negative cost associated with it 
given by cost[i], return the minimum cost of climbing to the top of 
the staircase. You may climb one or two steps at a time and you may start 
climbing from either the first or second step.

Ex: Given the following cost array…

cost = [5, 10, 20], return 10.

Ex: Given the following cost array…

cost = [1, 5, 10, 3, 7, 2], return 10.
Thanks,
The Daily Byte
"""


# 1   5 	10 	3 	7 	2 
#                     x
# 0 	0	0	0	0	0	

#minimum_at_i = min(minimum_at_(i -1),minimum_at_(i -1)) 

def stairmaster(cost):
	if not cost: return None 

	dp = [0 for i in range(len(cost))]

	if len(cost) == 1:
		return cost[0]
	dp[0] = cost[0]

	if len(cost) == 2:
		return min(cost[0],cost[1])

	dp[1] = min(cost[1],cost[0] + cost[1])

	for i in range(2,len(cost)):
		dp[i] = min(dp[i-1],dp[i-2]) + cost[i]

	print(dp)

	return dp[-1]

cost = [1, 5, 10,3,2]
#cost = [8,9,10]

print(stairmaster(cost))












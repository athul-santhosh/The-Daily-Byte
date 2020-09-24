# nums = [5,6,7,9,3]      target = 5

# nums = [5,5,9,2,1,2]    target = 10

# nums = [1,3,3,5,6,8,9,9,10]  target = 11



def TwoSum(nums,target):
	has_ = set()
	for num in nums:
		if target - num in has_:
			print(num,target-num)
			return True
		else:
			has_.add(num)
	return False


print(TwoSum([5,6,7,9,3] ,5))
print(TwoSum([5,5,9,2,1,2] ,10))
print(TwoSum([1,3,0,3,5,6,8,9,9,10],5))
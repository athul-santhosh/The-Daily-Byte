def max_sum_subarray(arr):
	# edge case , what if no array
	if not arr : return None
	
	current_max = max_sum = arr[0]
	
	for i in range(1,len(arr)):
	
		current_max = max(arr[i],current_max + arr[i])
	
		max_sum = max(max_sum,current_max)
	
	return max_sum

print(max_sum_subarray([1,7,8,9,10,-13]))
print(max_sum_subarray([1,4,-6, 7 ,-9, 10 ,16]))



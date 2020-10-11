# This question is asked by Amazon. Given two arrays of numbers, 
# where the first array is a subset of the second array, return an array 
# containing all the next greater elements for each element in the first array, 
# in the second array. 
# If there is no greater element for any element, output -1 for that number.

# nums1 = [4,1,2], nums2 = [1,3,4,2], return [-1, 3, -1] because no element in 
# nums2 is greater than 4, 3 is the first number in nums2 greater than 1, 
# and no element in nums2 is greater than 2.
# nums1 = [2,4], nums2 = [1,2,3,4], return [3, -1] because 3 is the 
# first greater element that occurs in nums2 after 2 and no element is 
# greater than 4.
def greater_element(nums1,nums2):

	if not nums2: return None
	if not nums1: return []

	def great_right(i):
		current = nums2[i]
		for j in range(i+1,len(nums2)):
			if nums2[j] > current:
				return nums2[j]
		return -1

	result = []
	d = {nums2[-1]:-1}
	for i in range(len(nums2)):
		d[nums2[i]] = great_right(i)

	for i in nums1:
		result.append(d[i])

	return result
# O(n^2 ) time O(n) space
print(greater_element([4,1,4],[1,3,4,2]))
print(greater_element([2,4],[1,2,3,4]))
print(greater_element([6,4,3,5,6],[1,2,3,9,4,5,6]))
	
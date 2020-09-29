# nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
# nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
# nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []


def intersection(nums1,nums2):
	s = set()
	result = []
	for i in nums1:
		if i not in s:
			s.add(i)
	for i in nums2:
		if i in s and i not in result:
			result.append(i)
	return result


print(intersection([2, 4, 4, 2],[2, 4]))
print(intersection([1, 2, 3, 3],[3, 3]))
print(intersection([2, 4, 6, 8],[1, 3, 5, 7]))


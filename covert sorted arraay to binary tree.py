class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None
		


def sortedArrayToBST(self, nums):

	if not nums:
	    return 


	mid = len(nums)//2

	root = TreeNode(nums[mid])
	root.left = self.sortedArrayToBST(nums[:mid])
	root.right = self.sortedArrayToBST(nums[mid+1:])

	return root
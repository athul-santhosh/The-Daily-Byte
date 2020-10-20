class Node():
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None


class BinarysearchTree():

	def __init__(self):
		self.root = None


	def insert(self,data):
		if self.root is None:
			self.root = Node(data)
			return 
		else:
			self._insert(data,self.root)

	def _insert(self,data,cur_node):
		if cur_node.data < data:
			if cur_node.right is None:
				cur_node.right = Node(data)
			else:
				self._insert(data,cur_node.right)

		elif cur_node.data > data:
			if cur_node.left is None:
				cur_node.left = Node(data)
			else:
				self._insert(data,cur_node.left)

		else:
			print("No dubplicate values allowed in this tree :(")


	def min_difference(self):

		# first do an inorder traversal
		self.arr = []
		diff_arr = []

		def inorder(start):
			if start:
				inorder(start.left)
				self.arr.append(start.data)
				inorder(start.right)


		inorder(self.root)

		# store the minimum value between two adjacent nodes

		

		for i in range(1,len(self.arr)):
			diff_arr.append(self.arr[i]-self.arr[i-1])

		if len(diff_arr) == 0:
			return 0

		return min(diff_arr)








athul = BinarysearchTree()
for i in [21,89,65,18,98,13]:
	athul.insert(i)


print(athul.min_difference())


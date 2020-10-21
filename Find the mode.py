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

		elif cur_node.data >= data:
			if cur_node.left is None:
				cur_node.left = Node(data)
			else:
				self._insert(data,cur_node.left)

	def mode(self):

		self.count = {}

		def inorder(start):
			if start:
				inorder(start.left)
				if start.data not in self.count:
					self.count[start.data] = 1
				else:
					self.count[start.data] += 1
				inorder(start.right)

		inorder(self.root)

		if not self.count.values():
			return -1

		x = max(self.count.values())

		for key,val in self.count.items():
			if val == x:
				return key

# O(n) time.     O(n). space
 













athul = BinarysearchTree()
for i in [21,89,65,18,98,13,13,13,89,65,65,65]:
	athul.insert(i)

print(athul.mode())




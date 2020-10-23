
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


	def level_order(self):
		# this could be solved using 2 qeues

		cur = []
		next = []
		each_level = []
		result = []

		cur.append(self.root)

		while cur:
			node = cur.pop(0)
			each_level.append(node.data)

			if node.left:
				next.append(node.left)
			if node.right:
				next.append(node.right)

			if len(cur) == 0:
				result.append(max(each_level))
				cur,next = next,cur
				each_level = []

		return result







# O(n) time.     O(n) space






athul = BinarysearchTree()
for i in [21,89,65,18,98,13,45,67,109,77,34,691]:
	athul.insert(i)


print(athul.level_order())


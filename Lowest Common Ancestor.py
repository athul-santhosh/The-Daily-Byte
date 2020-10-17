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


	def lowest_common_ancestor(self,node,n1,n2):

		if not node:
			return None

		if node.data > n1 and node.data > n2:
			return self.lowest_common_ancestor(node.left,n1,n2)

		if node.data < n2 and node.data < n1:
			return self.lowest_common_ancestor(node.right,n1,n2)

		return node.data


athul = BinarysearchTree()
for i in [5,6,2,1,4,7,8,12,15]:
	athul.insert(i)


print(athul.lowest_common_ancestor(athul.root,4,1))
print(athul.lowest_common_ancestor(athul.root,8,12))
print(athul.lowest_common_ancestor(athul.root,2,15))
print(athul.lowest_common_ancestor(athul.root,6,4))

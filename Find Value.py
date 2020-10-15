class Node():
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None


class BinaryTree():

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

	def find_value(self,cur,target_node):
		if cur is None:
			print("there is no data")
			return None               						                                   
		if cur.data == target_node:
			print("the data exists @")
			print(cur)
			return cur
		elif cur.data > target_node:
			self.find_value(cur.left,target_node)
		else:
			self.find_value(cur.right,target_node) 


athul = BinaryTree()
for i in range(1,10):
	athul.insert(i)
for i in range(1,12):
	athul.find_value(athul.root,i)















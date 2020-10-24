"""
            1

         2      3


      4     5        16


         6         4       9


             8 

# use a level order traversal and put the first element on to the result list





"""




from collections import deque

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


# do a level order , print the first value from the front

	def visible_values(self):
		result = []
		cur = deque()
		next = deque()
		cur.append(self.root)
		each_level = []

		while cur:

			node = cur.popleft()
			each_level.append(node.data)
			if node.left:
				next.append(node.left)
			if node.right:
				next.append(node.right)

			if len(cur) == 0:
				result.append(each_level[0])
				cur,next = next,cur
				each_level =[]
		return result









athul = BinarysearchTree()
for i in [21,89,65,18,98,13,45,35,29]:
	athul.insert(i)


print(athul.visible_values())


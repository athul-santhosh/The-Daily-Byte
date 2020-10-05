#       s
#             f
# 1->2->3->4->5-> null, return 2
#       s
#             f
# 1->2->3->4->null, return 3
# 1->null, return 1


class Node():
	def __init__(self,data):
		self.data = data
		self.next = None



class LinkedList():
	def __init__(self):
		self.head = None

	def append(self,data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		cur = self.head
		while cur.next:
			cur = cur.next
		cur.next = new_node

	def display(self):
		cur = self.head
		while cur:
			print(cur.data,end = " --> ")
			cur = cur.next

	def middle(self):
		fast = self.head
		slow = self.head
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
		return slow.data




athul = LinkedList()
athul.append(1)
athul.append(2)
athul.append(3)
athul.display()
print("\n")
print(athul.middle())

print("\n")
l3 = LinkedList()
l3.append(1)
l3.append(2)
l3.append(3)
l3.append(4)
l3.append(5)
l3.append(6)
l3.display()
print("\n")
print(l3.middle())
print("\n")

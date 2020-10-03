# 1->2->3->null, value = 3,        return 1->2->null
# 8->1->1->4->12->null, value = 1, return 8->4->12->null
# 7->12->2->9->null, value = 7,    return 12->2->9->null


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


	def removeNode(self,node):
		if self.head.data == node:
			self.head = self.head.next

		cur = self.head
		prev = None
		while cur:
			if cur.data == node:
				prev.next = cur.next
			else:
				prev = cur
			cur = cur.next







athul = LinkedList()
athul.append(1)
athul.append(2)
athul.append(3)
athul.display()
athul.removeNode(3)
print("\n")
athul.display()
print("\n")

l2 = LinkedList()
m = [8,1,1,4,12]
for i in m:
	l2.append(i)
l2.display()
print("\n")
l2.removeNode(1)
l2.display()
print("\n")
l3 = LinkedList()
l3.append(7)
l3.append(12)
l3.append(2)
l3.append(9)
l3.display()
l3.removeNode(7)
print("\n")
l3.display()

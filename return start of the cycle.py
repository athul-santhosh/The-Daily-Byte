 """
 		     		s
 			 f		f
 1  2.  3.   4.     5  	
        7 --------  6
        
"""

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

	def has_cycle(self):
		fast = self.head
		slow = self.head
		# if it has a cycle
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
			if slow == fast:
				break

		if fast == None or fast.next == None:      # if fast reaches the end of the list then we can be sure that
			return "No cycle"					   # there is no cycle

		fast = self.head
		while fast != slow:
			fast = fast.next
			slow = slow.next

		return slow      # we can return either slow or fast , if we want the element , then return slow.data     
		










athul = LinkedList()
athul.append(1)
athul.append(2)
athul.append(3)
athul.display()
print("\n")


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


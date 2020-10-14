class queuestack():
	def __init__(self):
		self.q = []

	def push(self,data):
		self.q.append(data)

	def empty(self):
		return len(self.q) == 0

	def pop(self):
		if not self.empty():
			self.q.pop(-1)
		else:
			return "stack empty"
	def peek(self):
		if not self.empty():
			return self.q[-1]
		else:
			return "Stack empty"
	def display(self):
		return self.q



athul = queuestack()
athul.pop()
athul.push(1)
print(athul.display())
athul.push(5)
athul.push(8)
athul.push(12)
athul.push(3)
print(athul.peek())
athul.pop()
print(athul.display())



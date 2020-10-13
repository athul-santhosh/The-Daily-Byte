# // i.e. the moving average has a capacity of 3.
# MovingAverage movingAverage = new MovingAverage(3);
# m.next(3) returns 3 because (3 / 1) = 3
# m.next(5) returns 4 because (3 + 5) / 2 = 4 
# m.next(7) = returns 5 because (3 + 5 + 7) / 3 = 5
# m.next(6) = returns 6 because (5 + 7 + 6) / 3 = 6

from collections import deque
class moving_average():

	def __init__(self):
		self.q = deque()

	def next(self,data):
		if len(self.q) == 3:
			self.q.popleft()
		self.q.append(data)
		return sum(self.q)//len(self.q)

athul = moving_average()
print(athul.next(3))
print(athul.next(5))
print(athul.next(7))
print(athul.next(6))
print(athul.next(13))
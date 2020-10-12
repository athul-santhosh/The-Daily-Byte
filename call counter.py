from collections import deque
class callCounter:

    def __init__(self):
        self.q = deque()
        self.cnt = 0
    def ping(self, t: int) -> int:
        self.q.append(t)
        self.cnt +=1
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
            self.cnt -= 1
        return self.cnt

athul = callCounter()
print(athul.ping(1))
print(athul.ping(300))
print(athul.ping(3000))
print(athul.ping(3002))
print(athul.ping(7000))
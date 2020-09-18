"""
“Cat”, return “taC”
“The Daily Byte”, return "etyB yliaD ehT”
“civic”, return “civic”
"""
# first approach
def reverse1(string):
	s = list(string)
	s = reversed(s)
	return "".join(s)

# O(n)  time     O(n)
# second approach:
def reverse2(string):
	# 1 2 3 4 5 6 7
	# 1 2 3 4 5 6
	n = len(string)
	string = list(string)
	offset = 0
	for i in range((n//2) + 1):
		string[i],string[n-offset-1] =   string[n -offset-1], string[i]
		offset += 1

	return "".join(string)

# Time O(n // 2) => O(n)     space #O(n)



print(reverse2("Cat"))
print(reverse2("The Daily Byte"))
print(reverse2("civic"))
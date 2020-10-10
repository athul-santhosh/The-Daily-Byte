# s = "abccba", return ""
# s = "foobar", return "fbar"
# s = "abccbefggfe", return "a"

# abccba = > abba => aa => ""

def remove_adjacent_duplicates(s):
	# if string is None:
	if not s: return None

	stack = [s[0]]
	i = 1

	while i < len(s):
		if len(stack) != 0 and stack[-1] == s[i]: 
			stack.pop()
		else:
			stack.append(s[i])
		i += 1

	return "".join(stack)

# O(n) time and O(n) space

print(remove_adjacent_duplicates("abccba"))
print(remove_adjacent_duplicates("foobar"))
print(remove_adjacent_duplicates("abccbefggfe"))
print(remove_adjacent_duplicates("aaaaaccccc"))


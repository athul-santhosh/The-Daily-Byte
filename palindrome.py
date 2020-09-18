"""
level", return true
"algorithm", return false
"A man, a plan, a canal: Panama.", return true
"""

def palindrome(s):
	string = ""
	for i in s:
		if i.isalpha():
			string += str(i.lower())
	def palindrome_(string_):
		if string_ != "".join(reversed(string_)):
			return False
		return True
	return palindrome_(string)

# O(n) time             O(n) space


# approach 2 

def palindrome2(s):
	string = ""
	for i in s:
		if i.isalpha():
			string += str(i.lower())
	n = len(string)
	def reverse(s):
		offset = 0
		for i in range(n//2 +1):
			if s[i] != s[n - i - 1]:
				return False
		return True
	return reverse(string)

# O(n) time O(n) space

print(palindrome("level"))
print(palindrome("algorithm"))
print(palindrome2("A man, a plan, a canal: Panama."))
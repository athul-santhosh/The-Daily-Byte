# "abcba", return true
# "foobof", return true (remove the first 'o', the second 'o', or 'b')
# "abccab", return false


def valid_palindrome(s):
	def is_palindrome(string):
		return string == "".join(reversed(string))


	if is_palindrome(s):
		return True

	for i in range(len(s)):
		string = s[0:i] + s[i+1:len(s)]
		#print(string)
		if is_palindrome(string):
			return True
	return False


print(valid_palindrome("abcba"))
print(valid_palindrome("foof"))
print(valid_palindrome("abccab"))
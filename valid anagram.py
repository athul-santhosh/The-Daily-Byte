# s = "cat", t = "tac", return true
# s = "listen", t = "silent", return true
# s = "program", t = "function", return false


# first approach
# using collections.Counter

from collections import Counter

def valid_anagram(s,t):
	return Counter(s) == Counter(t)

# second approach

def valid_anagrams(s,t):
	if len(s) != len(t):
		return False
	s_d = {}
	for i in s:
		if i not in s_d:
			s_d[i] = 1
		else:
			s_d[i] += 1

	for i in t:
		if i not in s_d:
			return False
		else:
			s_d[i] -= 1
	for i in s_d:
		if s_d[i] != 0:
			return False
	return True


#def valid_anagram(s,t):
print(valid_anagrams("cat","tac"))
print(valid_anagrams("listen","silent"))
print(valid_anagrams("program","fun"))
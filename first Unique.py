# "abcabd", return 2
# "thedailybyte", return 1
# "developer", return 0



def first_unique(s):
	d = dict()
	for i in range(len(s)):
		if s[i] not in d:
			d[s[i]] = 1
		else:
			d[s[i]] += 1

	for i in range(len(s)):
		if d[s[i]] == 1:
			return i
	return - 1

# time O(n)    space O(26) => O(1)



print(first_unique("abcabd"))
print(first_unique("thedailybyte"))
print(first_unique("developer"))
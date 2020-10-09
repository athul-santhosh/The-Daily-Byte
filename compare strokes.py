# s = "ABC#", t = "CD##AB", return true
# s = "como#pur#ter", t = "computer", return true
# s = "cof#dim#ng", t = "code", return false


def comparer(s):
	result = []
	for i in s:
		if i == "#" and len(result) == 0:
			continue
		if i == "#" and len(result) > 0:
			result.pop()

		else:
			result.append(i)
	return result

def compare_strokes(s,t):
	return comparer(s) == comparer(t)







print(compare_strokes("ABC#","CD##AB"))
print(compare_strokes("como#pur#ter","computer"))
print(compare_strokes("cof#dim#ng","code"))
print(compare_strokes("y#fo##f","y#f#o##f"))
# "y#fo##f" fo##f     f
# "y#f#o##f" #f

# "USA", return true
# "Calvin", return true
# "compUter", return false
# "coding", return true

# first approach
def correctCapitil(s):
	return s == s.lower() or s == s.upper() or s == s.title()
# second approach
def correctCapitil_(s):
	first_capital = s[0].isupper()
	capitals = 0
	for i in s:
		if i.isupper():
			capitals += 1
	if capitals == len(s):
		return True 
	elif capitals == 1 and first_capital is True:
		return True
	elif capitals == 0:
		return True
	else:
		return False




print(correctCapitil("USA"))
print(correctCapitil("Calvin"))
print(correctCapitil("compUter"))
print(correctCapitil("coding"))

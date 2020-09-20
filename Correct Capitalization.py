# "USA", return true
# "Calvin", return true
# "compUter", return false
# "coding", return true


def correctCapitil(s):
	return s == s.lower() or s == s.upper() or s == s.title()





print(correctCapitil("USA"))
print(correctCapitil("Calvin"))
print(correctCapitil("compUter"))
print(correctCapitil("coding"))
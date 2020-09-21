# "100" + "1", return "101"
# "11" + "1", return "100"
# "1" + "0", return  "1"


def binaryadd(s1,s2):
	if len(s1) < len(s2):
		s2,s1 = s1,s2
		

	if len(s1) != len(s2):
		for i in range(len(s1) - len(s2)):
			s2 = "0" + s2
	st  = []
	i = len(s1) -1
	carry = 0
	while i >= 0:
		if s1[i] == "1" and s2[i] == "1":
			if carry == 1:
				st.insert(0,"1")
				carry = 1
			else:
				st.insert(0,"0")
				carry = 1
		elif s1[i] == "0" and s2[i] == "0":
			if carry == 1:
				st.insert(0,"1")
				carry = 0
			else:
				st.insert(0,"0")
				carry = 0
		else:
			if carry == 1:
				st.insert(0,"0")
				carry = 1
			else:
				st.insert(0,"1")
				carry = 0
		i -= 1
	if carry == 1:
		st.insert(0,"1")


	return "".join(st)





print(binaryadd("100","1"))
print(binaryadd("11","1"))
print(binaryadd("1","0"))
print(binaryadd("1001010101010","110100100101"))
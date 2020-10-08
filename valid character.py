# "(){}[]", return true
# "(({[]}))", return true
# "{(})", return false

def ismatch(left,right):
	if left == "(" and right == ")":
		return True
	elif left == "[" and right == "]":
		return True
	elif left == "{" and right == "}":
		return True
	else:
		return False

 
def valid_character(s):
	stack  = []
	for i in s:
		if i in "( [ {":
		 	stack.append(i)	
		else:
			if len(stack) == 0:
				return False
			else:
				top = stack.pop()
				if not  ismatch(top,i):
					return False
	if len(stack) == 0:
		return True
	else:
		return False	

print(valid_character("(){}"))
print(valid_character("{(})"))
print(valid_character("(({[]}))"))
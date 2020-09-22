# ["colorado", "color", "cold"], return "col"
# ["a", "b", "c"], return ""
# ["spot", "spotty", "spotted"], return "spot"



def lps(arr):
	arr.sort()
	result = ""
	for i in range(len(arr[0])):
		if arr[0][i] == arr[-1][i]:
			result += arr[0][i]
		else:
			break
	return result
			
print(lps(["colorado", "color", "cold"]))
print(lps(["a", "b", "c"]))
print(lps(["spot", "spotty", "spotted"]))



	
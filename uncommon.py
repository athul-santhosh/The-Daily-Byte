# This question is asked by Amazon. Given two strings representing sentences, return the words that are not 
# common to both strings (i.e. the words that only appear in one of the sentences). You may assume that each 
# sentence is a sequence of words (without punctuation) correctly separated using space characters.


sentence1 = "the quick",            sentence2 = "brown fox", return  ["the", "quick", "brown", "fox"]
sentence1 = "the tortoise beat the haire", sentence2 = "the tortoise lost to the haire", return [  "beat", "to", "lost"]
sentence1 = "copper coffee pot", sentence2 = "hot coffee pot", return ["copper", "hot"]




def uncommon(s1,s2):
	result = []
	s1 = s1.split()
	s2 = s2.split()
	for i in s1:
		result.append(i)
	for i in s2:
		if i in result:
			result.remove(i)`
		else:
			result.append(i)
	return result

# time O(n) space = O(n)


print(uncommon("the quick","brown fox"))
print(uncommon("the tortoise beat the haire","the tortoise lost to the haire"))
print(uncommon("copper coffee pot","hot coffee pot"))
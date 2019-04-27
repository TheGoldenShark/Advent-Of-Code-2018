alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def splitList(originalList, n):
	splitLists=[]
	for i in range(0, len(originalList), n):
		splitLists.append(originalList[i:i+n])
	return splitLists
output = splitList(alphabet, 5)

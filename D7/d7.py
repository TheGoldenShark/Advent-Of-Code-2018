sortedData=[]
moreSortedData=[[],[]]
avaliable=[]
completed=[]
with open("test.txt","r") as f: data=f.readlines()
with open("input.txt","r") as f: data=f.readlines()
for i in data: sortedData.append([i[5],i[36]])
#Overly Complicated way of finding Start point
moreSortedData[0] = [n[0] for n in sortedData]
moreSortedData[1] = [n[1] for n in sortedData]
startPoint=min([x for x in moreSortedData[0] if x not in moreSortedData[1]])
#MOVING ON
completed.append(startPoint)
p=set([])
p.update(moreSortedData[0])
p.update(moreSortedData[1])
#Calculating dependencies for all the letters
dependencyDict = {}
for i in p:
	tempDependencyList=[]
	for j in sortedData:
		if i == j[1]:
			tempDependencyList.append(j[0])
	dependencyDict[i] = tempDependencyList
notCompleted=list(p)
notCompleted.remove(startPoint)
while len(completed)<len(p):
	avaliable=[]
	for i in notCompleted:
			if dependencyDict[i] == [x for x in dependencyDict[i] if x in completed]:
				avaliable.append(i)
	nextLetter=min(avaliable)
	completed.append(nextLetter)
	notCompleted.remove(nextLetter)
print(''.join(completed))










def splitList(originalList, n):
	splitLists=[]
	for i in range(0, len(originalList), n):
		splitLists.append(originalList[i:i+n])
	return splitLists
sortedData=[]
moreSortedData=[[],[]]
completed=[]
with open("test.txt","r") as f: data=f.readlines()
# with open("input.txt","r") as f: data=f.readlines()
for i in data: sortedData.append([i[5],i[36]])
moreSortedData[0] = [n[0] for n in sortedData]
moreSortedData[1] = [n[1] for n in sortedData]
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
totaltime=0
while len(completed)<len(p):
	avaliable=[]
	for i in notCompleted:
			if dependencyDict[i] == [x for x in dependencyDict[i] if x in completed]:
				avaliable.append(i)
	timeAvailable = [ord(x)-64 for x in avaliable]
	# timeAvaliableSplit = splitList(timeAvailable, 5)
	workerTimes=[0,0]
	for i in timeAvailable:
		workerTimes[workerTimes.index(min(workerTimes))]+=i
	totaltime+=(max(workerTimes))
	nextLetter=min(avaliable)
	completed.append(nextLetter)
	notCompleted.remove(nextLetter)
input()











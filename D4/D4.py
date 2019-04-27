currentID=""
timeAsleepDict={}
# Passed Y
# with open("test.txt","r") as f: data=f.readlines()
# Passed N
with open("input.txt","r") as f: data=f.readlines()
for i in range(0,len(data)):
    tempSplit=[]
    data[i]=[data[i][1:17],data[i][19:-1]]
    if data[i][1][6]=="#":
       tempSplit=data[i][1].split()
       tempSplit=[" ".join([tempSplit[2],tempSplit[3]]),tempSplit[1][1:]]
       del data[i][1]
    for j in tempSplit:
        data[i].append(j) 
dataSorted=sorted(data, key=lambda data: data[0])
for i in range(0,len(dataSorted)):
    if len(dataSorted[i])==3:
        if currentID in timeAsleepDict:
            timeAsleepDict[currentID]+=timeAsleep
        elif currentID!="":
            timeAsleepDict[currentID]=timeAsleep
        currentID=dataSorted[i][2]
        timeAsleep=0

    if dataSorted[i][1]=="falls asleep":
        timeAsleep+=int(dataSorted[i+1][0][14:])-int(dataSorted[i][0][14:])
sleepyGuard=max(timeAsleepDict, key=timeAsleepDict.get)
guardSleeping=[]
rightGuard=False
for i in range(0,len(dataSorted)):
    if len(dataSorted[i])==3:
        if dataSorted[i][2]==sleepyGuard:
            rightGuard=True
        else:
            rightGuard=False
    if len(dataSorted[i])==2 and dataSorted[i][1]=="falls asleep" and rightGuard==True:
        guardSleeping.append([dataSorted[i][0][14:],dataSorted[i+1][0][14:]])
guardSleepingMinutes=[]
for i in range(0,60):
    guardSleepingMinutes.append(0)
for i in guardSleeping:
    for j in range(int(i[0]),int(i[1])):
        guardSleepingMinutes[j]+=1
output=(int(guardSleepingMinutes.index(max(guardSleepingMinutes))))*int(sleepyGuard)
print(output)
input()

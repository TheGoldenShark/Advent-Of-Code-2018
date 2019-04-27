sortedData=[]
tempData=[]
coordList=set()
tempList=[]
intersect=set()
# Passed Y
# data=["#123 @ 3,2: 5x4 "]
# Passed Y
# data=["#1 @ 1,3: 4x4 ","#2 @ 3,1: 4x4 ","#3 @ 5,5: 2x2 "]
#Passed N
with open("input.txt","r") as f: data=f.readlines()

for i in range(0,len(data)): data[i]=data[i][:-1]
for i in range(0,len(data)): sortedData.append(data[i].split(" "))
for i in range(0,len(sortedData)): 
    sortedData[i][0]=sortedData[i][0].replace("#","")
    del sortedData[i][1]
    sortedData[i][1]=sortedData[i][1].replace(":","")
    temp=sortedData[i][1].split(",")
    del sortedData[i][1]
    sortedData[i].insert(1,temp[0])
    sortedData[i].insert(2,temp[1])
    temp=sortedData[i][3].split("x")
    del sortedData[i][3]
    sortedData[i].insert(3,temp[0])
    sortedData[i].insert(4,temp[1])
    tempID=sortedData[i][0]
    del sortedData[i][0]
    sortedData[i].append(tempID)
sortedData=[list(map(int,x)) for x in sortedData]
for i in range(0,len(sortedData)):
    #pos=[y(from top),x(from left)]
    pos=[sortedData[i][1],sortedData[i][0]]
    newPos=list(pos)
    for k in range(0,sortedData[i][3]):    
        for j in range(0,sortedData[i][2]):
            #Can you do lists inside a set? nope
            newPos[1]=str(pos[1]+j)
            newPos[0]=str(pos[0]+k)
            newPosStr=",".join(newPos)
            if newPosStr not in intersect:
                if newPosStr in coordList:
                    intersect.add(newPosStr)
                    coordList.remove(newPosStr)
                else:
                    coordList.add(newPosStr)
print(len(intersect))
input()
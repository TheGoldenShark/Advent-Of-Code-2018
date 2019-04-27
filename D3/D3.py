sortedData=[]
tempData=[]
coordList=[]
tempList=[]
intersect=[]
#Passed Y
# data=["#123 @ 3,2: 5x4 "]
#Passed Y
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
    del sortedData[i][0]
sortedData=[list(map(int,x)) for x in sortedData]
for i in range(0,len(sortedData)):
    #pos=[y(from top),x(from left)]
    pos=[sortedData[i][1],sortedData[i][0]]
    newPos=list(pos)
    tempList=[]
    for k in range(0,sortedData[i][3]):    
        for j in range(0,sortedData[i][2]):
            #Can you do lists inside a set? nope
            newPos[1]=pos[1]+j
            newPos[0]=pos[0]+k
            tempList.append(list(newPos))
    coordList.append(tempList)
    print(i)
return coordList

# for i in range(0,len(coordList)):
#     for j in range(0,len(coordList)):
#         if i!=j:
#             for q in [x for x in coordList[i] if x in coordList[j]]:
#                 intersect.append(q)
#     print(i)
# finalIntersect=[]
# for x in intersect:
#     if x not in finalIntersect:
#         finalIntersect.append(x)
# print(len(finalIntersect))  
input()
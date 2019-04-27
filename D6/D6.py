def manhattanDist(coord1,coord2):
    output=abs(coord1[0]-coord2[0])+abs(coord1[1]-coord2[1])
    return output
crossover=False
dispMod=10
line=[]
grid=[]
dist=[]
counts=[]
# Passed N
with open("test.txt","r") as f: data=f.readlines()
# Passed N
# with open("input.txt","r") as f: data=f.readlines()
for i in range(len(data)):
    data[i]=data[i].strip() 
    data[i]=data[i].split(", ")
for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j]=int(data[i][j])
for i in data:
    counts.append(0)
# maxX=dispMod+max(data,key=lambda data:data[0])[0]
# maxY=dispMod+max(data, key=lambda data:data[1])[1]
maxX=max(data,key=lambda data:data[0])[0]
maxY=max(data, key=lambda data:data[1])[1]
# for i in range(len(data)):
#     for j in range(len(data[i])):
#         data[i][j]+=dispMod/2
for i in range(maxX):
    line.append([])
for i in range(maxY):
    grid.append(line)
for i in range(maxY):
    for j in range(maxX):
        #You don't understand what's happening here
        dist=[]
        for k in data:
            dist.append(manhattanDist([j,i],k))
        # remember to account for coords that overlap :)
        # this returns crossover==True when crossover is found and breaks to increase perf
        # otherwise it gives a currentMin value which is min and an index value at currentMinIndex
        currentMin=-10
        for p in range(len(dist)):
            if dist[p]==currentMin and crossover==False:
                crossover==True
                break
            if dist[p]<currentMin or currentMin==-10:
                currentMin=dist[p]
                currentMinIndex=p
        if crossover==False:
            counts[currentMinIndex]+=1
        else:
            crossover=True
input()
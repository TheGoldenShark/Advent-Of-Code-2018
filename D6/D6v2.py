toIgnore=set()
counts=[]
areasList=[]
def manhattanDist(coord1,coord2):
    output=abs(coord1[0]-coord2[0])+abs(coord1[1]-coord2[1])
    return output
# Passed Y
# with open("test.txt","r") as f: data=f.readlines()
with open("input.txt","r") as f: data=f.readlines()
for i in range(len(data)):
    data[i]=data[i].strip() 
    data[i]=data[i].split(", ")
for i in range(len(data)): counts.append(0)
data = list(map(lambda x:list(map(int,x)),data))
for i in range(400):
    for j in range(400):
        distances=[]
        for k in range(len(data)):
            distances.append(manhattanDist(data[k],[i,j]))
        dataIndex=distances.index(min(distances))
        if distances.count(distances[dataIndex])>1:
            pass
        else:
            counts[dataIndex]+=1
        if (i==0 or j==0 or i==399 or j==399) and (dataIndex not in toIgnore):
            toIgnore.add(dataIndex)
for i in range(len(distances)):
    if i not in toIgnore:
        areasList.append(counts[i])
print(max(areasList))

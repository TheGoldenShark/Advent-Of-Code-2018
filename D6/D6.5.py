count=0
def manhattanDist(coord1,coord2):
    output=abs(coord1[0]-coord2[0])+abs(coord1[1]-coord2[1])
    return output
# Passed N
# with open("test.txt","r") as f: data=f.readlines()
# maxDist=32
with open("input.txt","r") as f: data=f.readlines()
maxDist=10000
for i in range(len(data)):
    data[i]=data[i].strip() 
    data[i]=data[i].split(", ")
data = list(map(lambda x:list(map(int,x)),data))
for i in range(-400,400):
    for j in range(-400,400):
        totalDist=0
        for k in data:
            totalDist+=manhattanDist(k,[i,j])
            if totalDist>=maxDist:
                break
        else:
            count+=1
print(count)


    
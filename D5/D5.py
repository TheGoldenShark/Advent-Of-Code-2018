with open("input.txt","r") as f: data=f.read().strip()
# data="dabAcCaCBAcCcaDA"
data=list(data)
finished=False
while finished==False:
    finished=True
    for i in range(0,len(data)-1):
        if data[i]==data[i+1].swapcase():
            del data[i]
            del data[i]
            finished=False
            break
print(len(data))

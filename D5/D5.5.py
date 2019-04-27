results=[]
with open("input.txt","r") as f: data=f.read().strip()
# data="dabAcCaCBAcCcaDA"
data=list(data)
# alphabet="d"
alphabet="qwertyuiopasdfghjklzxcvbnm"
for p in alphabet:
    dataMod=data
    dataMod=[x for x in dataMod if x!=p and x!=p.upper()]
    finished=False
    while finished==False:
        finished=True
        for i in range(0,len(dataMod)-1):
            if dataMod[i]==dataMod[i+1].swapcase():
                del dataMod[i]
                del dataMod[i]
                finished=False
                break
    results.append("".join(dataMod))
    print(p)
print("The answer is:")
print(len(min(results, key=len)))
input()
# import timeit
# def main():
results=[]
with open("input.txt","r") as f: data=f.read().strip()
data=list(data)
alphabet="qwertyuiopasdfghjklzxcvbnm"
for p in alphabet:
    dataMod=data
    dataMod=[x for x in dataMod if x!=p and x!=p.upper()]
    i=0
    while i<len(dataMod)-1:
        if dataMod[i]==dataMod[i+1].swapcase():
            del dataMod[i]
            del dataMod[i]
            i-=1
            continue
        i+=1
    results.append("".join(dataMod))
print(len(min(results, key=len)))
# print(timeit.timeit("main()", globals=globals(), number=2))
# input()
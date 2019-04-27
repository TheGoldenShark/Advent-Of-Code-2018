with open("input.txt","r") as f: f1=f.readlines()
f2=[]
for i in f1: 
    f2.append(i[:-1])
outputlist=[]
# Test - Successful
# f2=["abcde","fghij","klmno","pqrst","fguij","axcye","wvxyz"]
for i in f2:
    for j in f2:
        sameornot=[]
        if i!=j:
            for k in range(0,len(f2[0])):
                if i[k]==j[k]:
                    sameornot.append(True)
                else:
                    sameornot.append(False)
            if sameornot.count(False)<=1:
                for p in range(0,len(i)):
                    if i[p]==j[p]:
                        outputlist.append(i[p])
                print("".join(outputlist))
                input()






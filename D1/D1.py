f=open("input.txt","r")
f1=f.readlines()
count=0
for i in range(0,len(f1)):
    tempcount=0
    p=0
    if f1[i][0]=="+":
        for j in range(len(f1[i])-2,0,-1):
            tempcount+=int(f1[i][j])*(10**(p))
            p+=1
        
    if f1[i][0]=="-":
        for j in range(len(f1[i])-2,0,-1):
            tempcount-=int(f1[i][j])*(10**(p))
            p+=1
    count+=tempcount
print(tempcount)
print(count)
    
        

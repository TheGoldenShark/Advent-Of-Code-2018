previouscounts=[0]
solved=False
f=open("input.txt","r")
f1=f.readlines()
# Passed 0
# f1=["+1 ","-1 "]
#Passed 10
# f1=["+3 ","+3 ","+4 ","-2 ","-4 "]
#Passed 5
# f1=["-6 ","+3 ","+8 ","+5 ","-6 "]
#Passed 14
# f1=["+7 ","+7 ","-2 ","-7 ","-4 "]
count=0
while solved!=True:
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
            for q in range(0,len(previouscounts)):
                if count==previouscounts[q]:
                    solved==True
                    print("solved!")
                    print(count)
                    input()
            previouscounts.append(count)
    print("still goin")
    





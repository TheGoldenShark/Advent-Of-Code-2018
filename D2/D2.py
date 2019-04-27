num2=False
num3=False
num2int=0
num3int=0
with open("input.txt","r") as f: f1=f.readlines()
f2=[]
for i in f1: 
    f2.append(i[:-1])
# f2=['abcdef','bababc','abbcde','abcccd','aabcdd','abcdee','ababab']
for j in f2:
    for k in j:
        num=j.count(k)
        if num==2 and num2==False:
            num2=True
        if num==3 and num3==False:
            num3=True 
    if num2==True:
        num2int+=1
        num2=False
    if num3==True:
        num3int+=1
        num3=False
print(num2int*num3int)


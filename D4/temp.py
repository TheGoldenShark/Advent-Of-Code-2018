guardSleeping=[]
rightGuard=False
for i in range(0,len(dataSorted)):
    if len(dataSorted[i])==3:
        if dataSorted[i][2]==str(maxTimesGuardNum):
            rightGuard=True
        else:
            rightGuard=False
    if len(dataSorted[i])==2 and dataSorted[i][1]=="falls asleep" and rightGuard==True:
        guardSleeping.append([dataSorted[i][0][14:],dataSorted[i+1][0][14:]])
guardSleepingMinutes=[]
for i in range(0,60):
    guardSleepingMinutes.append(0)
for i in guardSleeping:
    for j in range(int(i[0]),int(i[1])):
        guardSleepingMinutes[j]+=1
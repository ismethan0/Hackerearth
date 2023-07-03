#My first solution but stuck on speed limit:
n=int(input())
playlist=list(map(int,input().split()))
kontrol=0
num=[]
cashe=[]
denet=0
denetlenem=[]
for i in playlist:
    if i in denetlenem:
        continue
    else:    
        denetlenem.append(i)
    kontrol1=playlist.count(i)    
    if kontrol1==kontrol:
        if cashe:
            cashe.append(i)
        else:
            cashe.append(num)
            cashe.append(i)    
        denet="B"
    if kontrol1>kontrol:
        cashe=[]
        kontrol=kontrol1
        num=i
        denet="A"
if cashe=="A":
    print(1)
else:
    if (len(cashe))==0:
        print(1)
    else:
        print(len(cashe))    


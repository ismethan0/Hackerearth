t=int(input())
for i in range(t):
    N = int(input())
    sayac=0
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            if(i^j)<=N:
                sayac+=1
    print(sayac)
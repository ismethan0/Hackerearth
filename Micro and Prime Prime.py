import numpy as np
 
def sieve(n):
    asal=np.ones(n+1, dtype=bool)
    asal[0:2] = 0
    p=2
    while p * p <= n:
        if asal[p]:
            asal[p*p : n+1 : p]=0
        p+=1
 
    return asal
 
def asal_sayan(size):
    asal=sieve(size)
    sayac=primesayac = 0
    prefix_sum=[0]*size
    for i in range(n+1):
        if asal[i]:
            sayac +=1
        if asal[sayac]:
            primesayac += 1
        prefix_sum[i] = primesayac
    return prefix_sum
 
t=int(input())
lines=[]
n =0
for i in range(t):
    l,r=map(int, input().strip().split())
    lines.append((l,r))
    n=max(n,r)
pp=asal_sayan(n+1)
for l, r in lines:
    ans=pp[r] - pp[l-1]
    print(ans)
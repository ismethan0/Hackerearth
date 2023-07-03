 
def sera(s,h,n):
  h=h%n
  kayan=s[(n-h):]+s[:(n-h)]
  return kayan
  
def xhaka(s,A,n):
  kayit=[]
  for i in range(n):
    if i%2:
      temp=str((int(s[i])+A)%10)
    else:
      temp=s[i]
    kayit.append(temp)
  return ''.join(kayit)

for a in range(int(input())):
  s=input()
  A,H=map(int,input().split())
  kume=set()
  n=len(s)
  stack=[]
  stack.append(s)
  while(len(stack)>0):
    temp=stack.pop()
    ser=sera(temp,H,n)
    xha=xhaka(temp,A,n)
    if ser not in kume:
            kume.add(ser)
            stack.append(ser)
    if xha  not in kume:
            kume.add(xha)
            stack.append(xha)
      
  print(min(kume))
  
# coding: utf-8

n=6
peqs=[[d for d in range(n,0,-1)],[],[]]

f=-1
t=f+1
n=t+1

f=(f+1)%3
t=(t+1)%3
n=(n+1)%3
last=f

def tail(list):
    return list[-1]

def isSmaller(l1,l2):
    return tail(l1)<tail(l2)

def op(l1,l2,l):
    global last
    if l1!=[]:
        try:    
            if isSmaller(l1,l2):
                m=l1.pop()
                l2.append(m)
                last=l
        except:
            m=l1.pop()
            l2.append(m)
            last=l

def move(peqs,f,t,n):
    fro=peqs[f]
    to=peqs[t]
    nxt=peqs[n]
    op(fro,to,t)
    print([peqs[f],peqs[t],peqs[n]],f,t,n,last)
    op(fro,nxt,n)
    print([peqs[f],peqs[t],peqs[n]],f,t,n,last)
    p,f,t,n=rotate(peqs,f,t,n)
    #print([peqs[f],peqs[t],peqs[n]])
    print()
    return [peqs[f],peqs[t],peqs[n]],f,t,n

def rotate(peqs,f,t,n):
    print('rotate')
    f=(f+1)%3
    t=(t+1)%3
    n=(n+1)%3
    #print(last)
    print([peqs[f],peqs[t],peqs[n]],f,t,n,last)
    if last==f:
        p,f,t,n=rotate(peqs,f,t,n)
    return [peqs[f],peqs[t],peqs[n]],f,t,n

for k in range(7):
    p,f,t,n=move(peqs,f,t,n)
    #print(p)
'''
print(p,f,t,n)
p,f,t,n=rotate(peqs,f,t,n)
#print(p,f,t,n)
p,f,t,n=move(peqs,f,t,n)
print(p,f,t,n)
p,f,t,n=rotate(peqs,f,t,n)
print(p,f,t,n)
p,f,t,n=move(peqs,f,t,n)
print(p,f,t,n)
p,f,t,n=rotate(peqs,f,t,n)
print(p,f,t,n)
p,f,t,n=move(peqs,f,t,n)
print(p,f,t,n)
'''

    

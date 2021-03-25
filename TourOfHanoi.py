# coding: utf-8

ndisks=6
peqs=[[k for k in range(ndisks,0,-1)],[],[]]
peq1,peq2,peq3=peqs

print(peqs)
print(len(peq1),len(peq2),len(peq3))
print(sum(peq1))

fro=peqs[0]
to=peqs[1]
m=fro.pop()
if len(to)==0:
    to.append(m)
elif m<to[-1]:
    to.append(m)
print(peq1,peq2,peq3)

fro=peqs[0]
to=peqs[2]
m=fro.pop()
if len(to)==0:
    to.append(m)
elif m<to[-1]:
    to.append(m)
print(peq1,peq2,peq3)

def move2(f,t,n):     
    op=0
    fro=peqs[f]
    to=peqs[t]
    nxt=peqs[n] 
    last=f
    
    if len(fro)!=0:
        m=fro.pop()        
        if len(to)==0:
            to.append(m)     #first append peq empty
            op+=1
            last=t
        elif m<to[-1]:            
            to.append(m)    #first append valid peq 
            op+=1
            last=t
        else:
            fro.append(m)   #push back - no move
            return f,t,n
        
        if last==t:
            if len(fro)!=0:
                m=fro.pop()       #second pop if first append is success and peq not empty
                if len(nxt)==0:
                    nxt.append(m)    #second append peq empty
                    op+=1
                    last=n
                elif m<nxt[-1]:
                    nxt.append(m)    #second append valid peq
                    op+=1
                    last=n
                else:
                    fro.append(m)   #push back - no move                

        #if op!=0:print(peq1,peq2,peq3,'(',op,')')
    
    if (f+1)%3!=last:
        f=(f+1)%3
        t=(t+1)%3
        n=(n+1)%3
    else:        
        f=(f+2)%3
        t=(t+2)%3
        n=(n+2)%3
    return f,t,n

peqs=[[5,4,3,2,1],[],[]]
peq1,peq2,peq3=peqs

f=0
t=1
n=2

total=sum(peq1)
print(total)

coup=0
while sum(peq2)!=total and sum(peq3)!=total:    
    f0=f
    t0=t
    n0=n
    f,t,n=move2(f0,t0,n0) 
    if f!=f0:
        coup+=1
        print(coup,end=' ')
        print(peq1,peq2,peq3)

def test(f,t):
    if len(peqs[f])==0: return False
    if len(peqs[t])!=0:        
        return peqs[f][-1]<peqs[t][-1]
    else: return True

def move1(f,t):        
    op=0
    fro=peqs[f]
    to=peqs[t] 
        
    m=fro.pop()        
    if len(to)==0:
        to.append(m)     #first append peq empty
        op+=1
        
    elif m<to[-1]:            
        to.append(m)    #first append valid peq 
        op+=1
                    
    #if op!=0:print(peq1,peq2,peq3)
    
    return f,t

peq1=[4,3,2,1]
peq2=[]
peq3=[]
peqs=[peq1,peq2,peq3]
f=0
t=1
n=2
total=sum(peq1)
print(total)
coup=0


while sum(peq2)!=total and sum(peq3)!=total:
    
    f0=f
    t0=t
    n0=n
    if test(f,t):
        coup+=1
        print(coup,end=' ')
        f,t=move1(f0,t0)
        last=t
        print(peq1,peq2,peq3)
    if test(f,n):
        coup+=1
        print(coup,end=' ')
        f,n=move1(f0,n0)
        last=n
        print(peq1,peq2,peq3)
    if (f+1)%3!=last:
        f=(f+1)%3
        t=(t+1)%3
        n=(n+1)%3
    else:
        f=(f+2)%3
        t=(t+2)%3
        n=(n+2)%3

def move3(f,t,n):
        
    op=0
    fro=peqs[f]
    to=peqs[t]
    nxt=peqs[n] 
    last=f
    
    if len(fro)!=0:
        m=fro.pop()        
        if len(to)==0:
            to.append(m)     #first append peq empty
            op+=1
            last=t
        elif m<to[-1]:            
            to.append(m)    #first append valid peq 
            op+=1
            last=t
        
        if last==f:
            if len(nxt)==0:
                nxt.append(m)    #second append peq empty
                op+=1
                last=n
            elif m<nxt[-1]:
                nxt.append(m)    #second append valid peq
                op+=1
                last=n
            else:
                fro.append(m)   #push back - no move
                     

        #if op!=0:print(peq1,peq2,peq3)
    
    if (f+1)%3!=last:
        f=(f+1)%3
        t=(t+1)%3
        n=(n+1)%3
    else:        
        f=(f+2)%3
        t=(t+2)%3
        n=(n+2)%3
    return f,t,n,op

peq1=[5,4,3,2,1]
peq2=[]
peq3=[]
peqs=[peq1,peq2,peq3]

f=0
t=1
n=2
l=len(peq1)
total=sum(peq1)
print(l,total)

coup=0

while sum(peq2)!=total and sum(peq3)!=total:
    f0=f
    t0=t
    n0=n

    f,t,n,op=move3(f0,t0,n0) 
    if op!=0:
        coup+=1
        print(coup,end=' ')
        if l%2!=0:
            print(peq1,peq3,peq2)
        else:
            print(peq1,peq2,peq3)

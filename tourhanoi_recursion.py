
def move_one(start,end):
    global r
    r+=1
    end.append(start.pop())
    print(r,peq1,peq2,peq3)

def move_n(n,start,end,via):
    #print(n,start,via,end)
    if n==1:
        move_one(start,end)
        return
    move_n(n-1,start,via,end)
    move_one(start,end)
    move_n(n-1,via,end,start)

def move_all(n,start,end,via):
    global r
    if n==1:
        r+=1
        end.append(start.pop())
        print(r,peq1,peq2,peq3)
        return
    move_all(n-1,start,via,end)
    move_all(1,start,end,via)
    move_all(n-1,via,end,start)

n=4
peq1,peq2,peq3=[[k for k in range(n,0,-1)],[],[]]
r=0
print(r,peq1,peq2,peq3)
nd=2**n-1
print(nd,'moves')
#move_n(n,peq1,peq3,peq2)
move_all(n,peq1,peq3,peq2)



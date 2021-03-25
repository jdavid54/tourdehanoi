disk1='*****'
disk2='*'
disk3='***'

#showdisk1='{:^{width}}'.format(disk1, align='^', width=str(widthmax))
#showdisk2='{:^{width}}'.format(disk2, align='^', width=str(widthmax))
#showdisk3='{:^{width}}'.format(disk3, align='^', width=str(widthmax))
#print(showdisk1,showdisk2,showdisk3)
#print(showdisk2,showdisk3,showdisk1)

disks=5
widthmax=disks+3
basewidth=3*widthmax

peqs=peq1,peq2,peq3=[[k for k in range(disks,0,-1)],[],[]]
#print(peqs)
print('{:{align}{width}}'.format('Tours de Hanoi', align='^', width=str(basewidth)))
print(0,peq1,peq2,peq3)
base='{:=^{width}}'.format('', width=str(basewidth))
r=0

def show(*p):
    peqs=[*p]
    piles=[pile1,pile2,pile3]=[[],[],[]]
    print()
    for p,q in zip(piles,peqs):
        for k in range(len(q)):
            #print(len(peq1),k)
            p.append(''.join('*' for c in range(q[k])))
        for k in range(len(q),disks):
            p.append(''.join('|'))
    for level in range(disks-1,-1,-1):
        showdisk1='{:^{width}}'.format(pile1[level], width=str(widthmax))
        showdisk2='{:^{width}}'.format(pile2[level], width=str(widthmax))
        showdisk3='{:^{width}}'.format(pile3[level], width=str(widthmax))
        print(showdisk1,showdisk2,showdisk3)
    print(base)

def move_all(n,start,end,via):
    global r
    if n==1:
        r+=1
        end.append(start.pop())
        print(r,peq1,peq2,peq3)
        show(peq1,peq2,peq3)
        return
    move_all(n-1,start,via,end)
    move_all(1,start,end,via)
    move_all(n-1,via,end,start)

show(peq1,peq2,peq3)
move_all(disks,peq1,peq3,peq2)
#show(peq1,peq2,peq3)

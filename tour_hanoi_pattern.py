k = 2# numbers of disks
peg1 = [k+1 for k in range(k)]
peg1.reverse()   # return none but the function reverses peg1
peg2 = []
peg3 = []
pegs = [peg1, peg2, peg3]

max_moves = 2**k-1
print('max moves',max_moves)

def move(here, target):  
    if here == [] : return False
    #print('here', here)
    if target != []:
        if here[-1] < target[-1]:
            target.append(here.pop())
            return True
    else:
        target.append(here.pop())
        return True


def alt_move(here, to, via):  # try target 'to' else try target 'via'
    global n, moves
    if move(here, to):
        moves += 1
        print(moves,peg1,'\t', peg2, '\t',peg3,'move from ',(n%3)+1,'to ',(n+1)%3+1)
        n+=1    # don't use the next peg  for start if it's just been the last move target !
    elif move(here, via):
        moves += 1
        print(moves,peg1,'\t', peg2, '\t',peg3,'move from ',(n%3)+1,'to ',(n+2)%3+1)
    
n=0     # pointer to the start peg 'here'
moves = 0

while moves < max_moves:
    here = pegs[n%3]
    to = pegs[(n+1)%3]
    via = pegs[(n+2)%3]
    alt_move(here, to, via)
    n+=1 # next peg

def equ(k=1):
    return 2**(n-k) + 2**(n-k)- 1

def equ2(n):
    return 2**n - 1

def M(n):
    if n==1: return 1  #base case
    return 2*M(n-1) + 1

n = 10
print(M(n))

for k in range(1,n):
    print(k, equ(k))

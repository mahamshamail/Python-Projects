class move:
   def __init__(self,index, score):
      self.index = index
      self.score = score
      
print("\n*********************************\n***********TIC TAC TOE***********\n*********************************\n\n              GUIDE\n1. The player is represented by 'x'\n2. The computer is represented by '0'\n3. To complete your turn enter the\ntile number where you want to input 'x'\n\n")

w = 9
board = [0 for x in range(w)] 
PLYR="x"
COMP=0
turn=1 #PLYR

def fun(a1):
  if(a1!=PLYR and a1!=COMP):
    return 1
  else:
    return 0
    
def emptyIndexies(my=[9]):
  n=0
  x=0
  while(x<9):
    n=n+fun(my[x])
    x=x+1
  return n

def emptyIndexies2(my=[9]):
  a = [0 for x in range(emptyIndexies(my))] 
  n=0
  x=0
  while(x<len(my)):
    if(my[x]!=PLYR and my[x]!=COMP):
      print(n)
      print(x)
      print(len(my))
      print(len(a))
      a[n]=my[x]
    n=n+1
    x=x+1
  return a

def winlose():
  if(match(0,1,2)==1
  or match(3,4,5)==1
  or match(6,7,8)==1
  or match(0,3,6)==1
  or match(1,4,7)==1
  or match(2,5,8)==1
  or match(0,4,8)==1
  or match(2,4,6)==1
  ):
     return 1
  if(match(0,1,2)==-1
  or match(3,4,5)==-1
  or match(6,7,8)==-1
  or match(0,3,6)==-1
  or match(1,4,7)==-1
  or match(2,5,8)==-1
  or match(0,4,8)==-1
  or match(2,4,6)==-1
  ):
    return 0

def termStates(avail,wl):
  if(avail==0):
    return 0
  else:
    if(wl==1):
     return -10
    else:
      return 10

#print the matrix
def pM():
  y=0
  c=0
  while(y<3):
    print("         |         |         ")
    print("    "+str(board[c])+"    |"+"    "+str(board[c+1])+"    |     "+str(board[c+2])+"     "  )
    print("         |         |         ")
    if(y!=2):
      print("--------------------------------")
    c=c+3
    y=y+1


# assigning values 1 to 9 to tiles
j=0
while(j<w):
  board [j]=j+1
  j=j+1

#win or lose
def match(n1,n2,n3):
  if((board[n1]==board[n2]) & (board[n3]==board[n2])):
    #win
    if(board[n1]==PLYR):
      return 1 #match
    #lose
    else:
      return -1 
  else :
    return 0 #does not match

def minmax(pl , b = [9]):
  #available spots
  availSpots=emptyIndexies2(b)
  
  #win,lose,tie termStates
  
  moves = []
  d=0
  while(d<len(availSpots)):
    m=move(b[availSpots[d]],termStates(len(availSpots),winlose()))
    b[availSpots[d]]=pl
    
    if (pl == COMP):
      result = minmax(PLYR, b)
      m.score = result.score
    else:
      result=minmax(COMP, b)
      m.score = result.score
    b[availSpots[d]] = m.index
    moves.append(m)
    d=d+1
  bestMove=0 
  if(pl == COMP):
    bestScore = -10000
    h=0 
    while(h<len(moves)):
      if(moves[h].score > bestScore):
        bestScore = moves[h].score
        bestMove = h
      h=h+1 
  else:
    bestScore = 10000
    while(h<len(moves)):
      if(moves[h].score < bestScore):
        bestScore = moves[h].score
        bestMove = h
      h=h+1 
  return moves[bestMove] 
     

  


i1=0 #game loop

while(i1==0):
  #if wins/loses/draws (righ now inefficient)
  if(winlose()):
      pM()
      print("\n*********************************\n*************YOU WON*************\n*********************************")
      break; #break loop
  if(winlose()==0):
    pM()
    print("\n*********************************\n*************YOU LOSE*************\n*********************************")
    break; #break loop
     
  else:
    pM()
    x = input("\n\nChoose a the tile number to complete your turn: ")
    #INPUT: CHARACTERS (ALWAYS WRONG)
    if(x>='a' and x<='z'):
      print("ERROR: You must enter a number!")
    
          #INPUT: NUMBERS 
    else:
    #INPUT: NUMBERS (WRONG)
      if(int(x)<1 or int(x)>9):
        print("ERROR: Title number is not in range. Try Again.")
    #INPUT: NUMBERS (RIGHT)
      else:
        #DRAW OR NEXT TURN
        
        
        #draw---> all turns taken (9) reached yet no match
        
        #turn--->player
        k=0
        while(k<9 and turn==1):
          if(int(x)==board[k]):
            board[k]=PLYR
            turn=0
            break;
          k=k+1
          
        #turn---> computer (minmax algo)
        if(turn==0):
          print("computer's turn")
          minmax(COMP,board)
          turn=1
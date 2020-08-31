s = [1,1,1,0,2,2,2]

def validsteps (totalsteps):
  steps = []
  for index, frog in enumerate( totalsteps ):
    j=0
    m=index
    if(frog==1):
       j=index+2
       m=m+1
    elif (frog==2):
      j=index-2
      m=m-1
    else:
      j=0
        
    if ( frog == 0 ):
      continue
    if (not (( j < 0 ) or ( j >= len(totalsteps)))):
      if (totalsteps[j] == 0):
        t = list(totalsteps)
        t[index] = 0
        t[j] = frog
        steps.append(t)
    if (not ((m < 0) or ( m >= len(totalsteps)))):
      if ( totalsteps[m] == 0):
        t = list(totalsteps)
        t[index] = 0
        t[m] = frog
        steps.append(t)
  return steps


def solAll( current, target ):
  next = []
  k=-1
  a2=0
  for a in current:
    
    k=k+1
    n = validsteps(a[-1])
    #print("\t")
    if(len(a)-1==0):
      print("~~~~~~~~~~~~~~~~~ ROOT NODE ~~~~~~~~~~~~~~~~~~~~~~~  ")
    elif( a2 != len(a)-1):
      print("\n##################### Depth "+str(len(a)-1) +" ##################### ")
      a2=len(a)-1
    else:
      print("\n____________________________________________________")
    print("\n"+str(a[len(a)-1])+" at DEPTH: "+str(len(a)-1) +" NODE: "+str(k)+"\nHas the following children:")
    print(n)

    for q in n:
      #print(" jhh   ")
      t = list(a)
      t.append(q)
      if ( q == target ):
        #print("sdsd")
        return t
      next.append(t)
    
  return next




def win(start):
    #print(start)
    temp=[[start]]
    #print (temp)
    #print("her")
    #print(temp)
    end = list(start)
    end.reverse()
    #print(end)
    #print("uuu")
    while(temp[-1] != end):
        #print(temp[-1])
        #print("uuu77")
        temp = solAll(temp, end)
        #print(temp)
        #print("\n-----------------------------------------------------")
    return temp

win(s)

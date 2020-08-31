import random
import matplotlib.pyplot as plt

bestfit=[]#graph
bestaveragefit=[]#graph
popsize=8#
cities=6
costs = [
[0 ,7 ,11 ,8 ,4 ,6 ],
[7 ,0 ,9, 5 ,10 ,8 ],
[11, 9, 0, 7, 6,12 ],
[8, 5, 7, 0, 8, 11 ],
[4, 10, 6, 8, 0, 8 ],
[6, 8, 12, 11, 8, 0],
	]
	
#-------Random Population Indices----------

population=[] #need to generate

for i in range(0,popsize): #range(0,8)
  index = random.sample(range(0,cities),cities)
  population.append(index)
#print("     Random Population Indices:\n")
#print(population)

#-------------------------------------------
x=[]
x1=[]
for u in range(0,100):
#making sure tour always starts from   city C
  for p in range(0,popsize):
    population[p][0]=2
  print("\n\n---Random Population Indices--------:\n")
  print(population)
  #termination ondition is 100
  popPool=[]
  for h in range(0,5):#WHYYYYY is range 5 here????????????????????
#--#fitness calculation (same: ost of tour)----------------
    fitness=[]
    for i in range(0,popsize):#0,8
      total=0
      for a in range(1,cities):#0,6
        total=total+costs[ population[i][a-1]] [population[i][a] ]
      fitness.append(total)
    #print("\n     Fitness of Each Population:\n")
    #print (fitness)
   
#---------Normalise Fitness----------------------------
    totes= fitness[0]+fitness[1]+fitness[2]+fitness[3]+fitness[4]+fitness[5]+fitness[6]+fitness[7]
    #print("totes")
    #print(totes)
    fit2=[]
    num=0
    for j in range(0,popsize):
      num=num+(fitness[j]/totes)
      fit2.append(num) 
    #print("f2")
    #print(fit2)

#-------------------Random Numbers-------------------
    noOfParents=2
    parents=[]
    randNum = random.uniform(0.0, 1.0)
    randNum2 = random.uniform(0.0, 1.0)
    #print(randNum) 
    #print(randNum2) 
#---------------Parent Seletion---------------------------
    def psel(rn):
      if((rn<fit2[0])):
        l=0
      else:
        for l in range(1,popsize):
         if((rn>fit2[l-1])
          and 
          (rn<fit2[l])):
            break
      return l
      
    parents.append(population[int(psel(randNum))])
    parents.append(population[int(psel(randNum2))])

    popPool.append(parents[0])#added parents to popPool
    popPool.append(parents[1])#
    #print("\npopPool")
    #print(popPool)
    #print("\nParents According to Fitness:")
    #print(parents)

 #-----------------one point crossover--------------------
    
    noOfOffspring=2
   
    offsprings=[[0,0,0,0,0,0],
                [0,0,0,0,0,0]]
    arbitraryIndex = random.randint(0,cities-1)
    #print("arbitraryIndex")
    #print(arbitraryIndex)
    m=0
    while(m<arbitraryIndex):
      offsprings[0][m]=parents[0][m]
      offsprings[1][m]=parents[1][m]
      m=m+1
    while( m<cities ):
      offsprings[0][m]=parents[1][m]
      offsprings[1][m]=parents[0][m]
      m=m+1
      
    #print("\nOffsprings Found using Crossover:")
    #print(offsprings)
    
#--------------insert mutation-------------------------------
    randNo= random.randint(0,cities-1)
    randNo2= random.randint(0,cities-1)
    randNo1= random.randint(0,cities-1)
    randNo12= random.randint(0,cities-1)

    
    
    while(randNo2==randNo):
      randNo2= random.randint(0,cities-1)
    big=0
    small=0
    while(randNo12==randNo1):
      randNo12= random.randint(0,cities-1)
    big1=0
    small1=0

    if(randNo<randNo2):
      small=randNo
      big=randNo2
    else:
      small=randNo2
      big=randNo

    if(randNo1<randNo12):
      small1=randNo1
      big1=randNo12
    else:
      small1=randNo12
      big1=randNo1
      
    if(not(big==small+1)):
      tt=big
      t1=offsprings[0][tt]

      while(tt>small):
        offsprings[0][tt]=offsprings[0][tt-1]
        tt=tt-1
      offsprings[0][small+1]=t1

    if(not(big1==small1+1)):
      tt=big1
      t2=offsprings[1][tt]
      while(tt>small1):
        offsprings[1][tt]=offsprings[1][tt-1]
        tt=tt-1
      offsprings[1][small1+1]=t2
    #print("mutated offsprings")   
    #print(offsprings)
    popPool.append(offsprings[0])
    popPool.append(offsprings[1])
    #print("\n poppool")   
    #print(popPool)
    
 #----------killing proess------------   
    
  offspringfitness=[]
  for i in range(0,20):#RANGE??????
    total=0
    for a in range(1,cities):
     total=total+costs[popPool[i][a-1]][popPool[i][a]]
    offspringfitness.append(total)
  #print("\n     Fitness of offsprings:\n")
  #print (offspringfitness)
  
  averageBF=0
  population=[]
  bestfit.append(min(offspringfitness))
  for y in range(0,10):#RANGE??????
    o=offspringfitness.index(min(offspringfitness))
    averageBF=averageBF+min(offspringfitness)
    population.append(popPool[o])
    offspringfitness[o]=1000
   # print(offspringfitness)
  averageBF=float(averageBF/10)
  bestaveragefit.append(averageBF)
#print(bestfit)
#print(bestaveragefit)
  x.append(u)
  x1.append(u)
  
print(x)
print("\nBest Fit Values:")
print(bestfit)
print("\nBest Average Fit Values:")
print(bestaveragefit)

plt.plot(x, bestfit)
plt.plot(x, bestfit, label = "Best Fit")
plt.plot(x1, bestaveragefit)
plt.plot(x1, bestaveragefit, label = "Best average fit")
plt.xlabel('Generations')
plt.ylabel('Fitness')
plt.legend()
plt.show()

  
print("\npopulation:")
print(population)

  
  
    

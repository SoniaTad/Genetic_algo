import random
import copy
import matplotlib.pyplot as plt
from operator import  attrgetter
from statistics import mean
P= 50    #Population size
N=20       #number of genes
Generation=50
run=10 #number of times the algorithm is initialized 
class individual:
  #each individual has number of genes 
  
  genes=[]
  fitness=0
#fitness faunction to calculate the fitness value 
def fitnes(newind):
  
  
  utility=0
  for x in range(1,N):
    utility += (x * ((2*((newind.genes[x] ** 2)) - (newind.genes[x-1])) **2))
  utility = utility + (newind.genes[0] - 1)**2
   
  return utility
  
# selection function
def selection():  
  global offspring
  
  for y in range(0,P):
    #randomly selecting a first individual from the initial Population
    ind1= random.randint( 0, P-1 )
    offs=Population[ind1]
    #randomly selecting a second individual from the initial Population
    ind2=random.randint(0,P-1)
    offs2=Population[ind2]
    #depending on which of the two individuals has the best fitness , the one with the higher will be added to the offspring array 
    if  offs.fitness < offs2.fitness:

      offspring.append( offs )
    else:
      offspring.append( offs2 )
  
# crossover function
def crossingover():
  global offspring
  #Recombine a pair of parents
 
  for i in range (0,P,2):
    tempo=[]
      
    for T in range (0 ,N):

       tempo.append(offspring[i].genes[T])
    #selecting a random point for the swapping  
    point=random.randint(0,N-1)
    #swapping the tails of the two individuals 
    for t in range (point,N):

     


      offspring[i].genes[t]=offspring[i+1].genes[t]
     
      offspring[i+1].genes[t]=tempo[t]
   #calculatng the fitness value after crossover 
  for i in range(0,P):
    offspring[i].fitness=fitnes(offspring[i])  

  # Mutation 
afterMutation=[]
def Mutation():
  global afterMutation
  global offspring
  MUTRATE=0.01
  for i in range(0,P):
    newind=individual()
    newind.genes=[]
    for o in range(0,N):

    
      prob=random.random()  #for each gene selecting a random probability
      if prob < MUTRATE:
        
        Mustep=3
        Alter=random.uniform(-Mustep,Mustep)   #the value to add or substract to each gene
        alter=abs(Alter)
        
        if (prob % 2):

           offspring[i].genes[o]=offspring[i].genes[o]+alter
           if offspring[i].genes[o]>10:                   # !!!!! if it was the Stiblinsky-Tank function 10 would be replaced by 5 !!!!!
              offspring[i].genes[o]=10
        else:
            offspring[i].genes[o]=offspring[i].genes[o] - alter

            if offspring[i].genes[o]<-10:               # !!!!! if it was the Stiblinsky-Tank function -10 would be replaced by -5
               offspring[i].genes[o]=-10
    newind.genes=offspring[i].genes.copy()
    
    afterMutation.append(newind)
average=[]

def AVG():
    global average
    global afterMutation
    sum=0
    
    for I in range(0,P):
       afterMutation[I].fitness=fitnes(afterMutation[I])    #calculating the fitness value of each ind after mutation
      
       
       sum=sum+afterMutation[I].fitness
    
   
    AVERAGE=sum/P    #calculating the average of each population then appending it to a list 
    
    average.append(AVERAGE)
avg=[]


avgavg=[]    #create list to append the average of average 
bestavg=[]   #create list to append the best of each generation to have an average of best
#running the algorithm for multiple runs 
for exp in range(0,run):
  Population=[]
  offspring=[]
  for I in range (0, P):
    tempgene=[]

    for t in range (0, N):
    
     tempgene.append( random.uniform(-10,10))    #when running Stiblinsky-Tank function change the bounds to (-5,5)  !!!!!!!!!!!
   #creating the object newind
    newind = individual()
  #everytime an array of genes is created for each individual we will have to copy it to the genes array defined by the previous class 
    newind.genes = tempgene.copy()
  #each new object(new individual created would be added to the Population array )
    Population.append(newind)
    #putting best fitness =fitness of the first ind in population
  best_fitness=fitnes(Population[0])
      # running for a cetrain number of gen
  for q in range (0,Generation):
    selection()
    crossingover()
    Mutation()
    AVG()
    for p in range (0,P):
      
      t=afterMutation[p].fitness
      if t < best_fitness:
        best_fitness=t
    avg.append(best_fitness)
    #creating an elitism rate er 
    Population=sorted(Population,key=attrgetter('fitness'),reverse=False)       #sort list from lower to higher 
    afterMutation=sorted(afterMutation,key=attrgetter('fitness'),reverse=True)  #sort list from higher to lower
    er=round(P*0.02) 
    
    for x in range(0,er):  # passsing inds from pop to aftermutation ,depending on the % of the elitism rate 

       afterMutation[x].genes=copy.deepcopy(Population[x].genes)
    
      #next step is clearing all lists 

    Population.clear()
    Population=copy.deepcopy(afterMutation)
    offspring.clear()
    afterMutation.clear()
  
  
  bestavg.append(avg[-1])   #appending the last best of each run
  
  avgavg.append(average[-1])    #appending the last avg of each run
print('the best of all runs ',bestavg) 
print("\n")
print('the average of all runs  ',avgavg)  
print("\n")
thebest=mean(bestavg)
theavg=mean(avgavg)

TheBest=bestavg[0]       #to get the best score out of all the runs we ran
for d in bestavg:
  if d < TheBest:
    TheBest=d

print("the best out of all",TheBest)
print('--------------------------------')
print('| best of ',run,'runs',thebest,'|')
print('average of ',run,'runs',theavg)
print('|--------------------------------- |')
y=(average)
h=(avg)
for t in y:
  plt.plot(y)
 
for w in h:
  plt.plot(h)
  plt.show()

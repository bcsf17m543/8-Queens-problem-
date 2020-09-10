import numpy as np
import random as rand


def Place_Random(chess):
    for i in range(chess.shape[0]):
        chess[rand.randint(0, 7)][i] = 1


def Second_Rep(chess, rep):
    for i in range(chess.shape[0]):
        for j in range(chess.shape[1]):
            if(chess[i][j] == 1):
                rep[j] = i
    
def Distance(a,b,dis):
    dis=a-b
    if(dis<0):
        dis=dis*(-1)
    return dis        
      
def Fitness(rep):
    fit=0
    dist=0
    for i in range(rep.size):
        for j in range(rep.size):
            if(i!=j):
                dist=Distance(i,j,dist)
                if(rep[i]+dist==rep[j]): 
                    fit+=1
                if(rep[i]-dist==rep[j]):
                    fit+=1
                if(rep[i]==rep[j]):
                    fit+=1
    return fit  

def Mutation(arr):
    idx=rand.randint(0,7)
    val=rand.randint(0,7)
    arr[idx]=val
    return arr


def CrossOver(one,two,Pop_arr,fit_arr):
    three=np.array([one[0],one[1],one[2],one[3],two[4],two[5],two[6],two[7]])
    four=np.array([two[0],two[1],two[2],two[3],one[4],one[5],one[6],one[7]])
    three=Mutation(three)
    four=Mutation(four)
    three_f=Fitness(three)
    four_f=Fitness(four)
    Pop_arr=np.append(Pop_arr,[three,four],axis=0)
    fit_arr=np.append(fit_arr,[three_f,four_f])
    return Pop_arr,fit_arr


def Populate(Pop_arr,fit_arr):
    for i in range(Pop_arr.shape[0]):
        fit_arr[i]=Fitness(Pop_arr[i])


def Find_Max(Pop_arr,fit_arr,max,idx):
    for i in range(Pop_arr.shape[0]):
        if(fit_arr[i]>max):
            max=fit_arr[i]
            idx=i
    return max,idx


def CheckFitness(Pop_arr,fit_arr):
    for i in range(Pop_arr.shape[0]):
        if(fit_arr[i]==0):
            return True
    return False


def Generate_OffSprings(Pop_arr,fit_arr):
    max1,max2,idx1,idx2=0,0,0,0
    max1,idx1=Find_Max(Pop_arr,fit_arr,max1,idx1)
    Pop_arr=np.delete(Pop_arr,idx1,axis=0)
    fit_arr=np.delete(fit_arr,idx1)
    max2,idx2=Find_Max(Pop_arr,fit_arr,max2,idx2)
    Pop_arr=np.delete(Pop_arr,idx2,axis=0)
    fit_arr=np.delete(fit_arr,idx2)
    Pop_arr,fit_arr=CrossOver(Pop_arr[0],Pop_arr[1],Pop_arr,fit_arr)
    return Pop_arr,fit_arr

def Main_func(Pop_arr,fit_arr):
    while( 0 not in fit_arr):
        Pop_arr,fit_arr=Generate_OffSprings(Pop_arr,fit_arr)
    for i in range(Pop_arr.shape[0]):
        if(fit_arr[i]==0):
            print(Pop_arr[i])
            ans=np.zeros((8,8),dtype=int)
            ans=Inverse_Rep(Pop_arr[i])
            print(ans)    
            break    
    
def Inverse_Rep(rep):
    my_arr=np.zeros((8,8),dtype=int)
    for i in range(rep.size):
        my_arr[i][rep[i]]=1
    return my_arr    

pop_size = 4
chess1 = np.zeros((8, 8), dtype=int)
chess2 = np.zeros((8, 8), dtype=int)
chess3 = np.zeros((8, 8), dtype=int)
chess4 = np.zeros((8, 8), dtype=int)
Place_Random(chess1)
Place_Random(chess2)
Place_Random(chess3)
Place_Random(chess4)

rep1 = np.zeros((8), dtype=int) #Representation of chesses like [1 2 3 4]
rep2 = np.zeros((8), dtype=int)
rep3 = np.zeros((8), dtype=int)
rep4 = np.zeros((8), dtype=int)

Second_Rep(chess1, rep1)
Second_Rep(chess2, rep2)
Second_Rep(chess3, rep3)
Second_Rep(chess4, rep4)

Pop=np.array([rep1,rep2,rep3,rep4])
fit=np.array([0,0,0,0])
Populate(Pop,fit)
Main_func(Pop,fit)

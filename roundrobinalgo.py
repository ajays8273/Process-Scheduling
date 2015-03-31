import os.path, math
from collections import deque
from configDic import taskDictionary, taskDictETime, TotalTimePerProcessor

def roundRobin(filename): #returns Miss for one datafile
#check file exist or not
	
	#print os.path.isfile(filename)
	no_task = (filename.split('.')[0]).split('-')[1]  #2-5-34.txt -> 5
	no_processor = (filename.split('.')[0]).split('-')[0] #get number of processor
	#taskDictionary(filename)
	sigmaE = 0  #Initialize sigma ei
	for key, value in sorted(taskDictETime.iteritems()) :  #store sum of execution time of all tasks 
		sigmaE += value

	weight = []          #store weight of each task
	subtaskCompleted = []#counter for storing number of subtask completed for each task
	readyQueue = deque() #The Queue for RoundRobin Algorithm

        scalingfactor = TotalTimePerProcessor*int(no_processor)/sigmaE #Scaling Factor
        scaledEi = []             #list of scaled Ei value
        if(scalingfactor==0):     #if scaling factor is zero make it 1
                scalingfactor = 1
                
	currentTasksinQueue = []  #list of Current Task in Queue
	#Initialize all lists
	for task in range(1,int(no_task)+1) :   
		currentTasksinQueue.append(task) #initially contains list of all tasks
		scaledEi.append(math.floor(taskDictETime[str(task)]*scalingfactor)) #Generate and Store ei' in a list
		weight.append(float(taskDictETime[str(task)])/float(sigmaE))  #weight[i-1] = ei / sigma ei
		subtaskCompleted.append(0)       #initially no Subtask is complete
		readyQueue.append(task)          #initializing RoundRobin Queue

	t = 0    #timeline
	miss = 0 #stores all misses
	proc = int(no_processor)
	while readyQueue : #is not empty or sigma E not over
		t += 1
		#print readyQueue, filename
		added=[]  # contains list of  dequeued task
		processor = int(no_processor) #get Number of Processors 
		#print readyQueue
		while (processor > 0) and readyQueue :
			processor -= 1
			task = readyQueue.popleft() #Pop executed Subtask form queue
			subtaskCompleted[task-1] = subtaskCompleted[task-1] +1 #increment subtask counter
			#print h, subtaskCompleted
			if(scaledEi[task-1] - subtaskCompleted[task-1] != 0) : #task still left taskDictETime[str(task)] - subtaskCompleted[task-1] != 0
				#readyQueue.append(task)
				added.append(task)  #add tasks back to Queue
			else :
				currentTasksinQueue.remove(task)  #remove task  from queue when task is completed
		for tt in range(0,len(added)) :  #for each task in added list put them back to queue
			readyQueue.append(added[tt]) #Put dequeued tasks back to queue
		#for eachtask in range(0,int(no_task)) : #eachtask  = pid of task -1
		
		for eachtask in currentTasksinQueue : #
			lag = weight[eachtask-1]*t*proc - subtaskCompleted[eachtask-1]
			if(lag > 1) :#lag >1
				miss += 1#math.floor(lag)
		
	return miss

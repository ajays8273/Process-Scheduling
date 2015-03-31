import heapq
import math
from configDic import taskDictionary, taskDictETime, TotalTimePerProcessor


def prop(filename):  #Preemptive Scheduling
	no_task = (filename.split('.')[0]).split('-')[1]  #2-5-34.txt -> 5
	no_processor = (filename.split('.')[0]).split('-')[0]
	#taskDictionary(filename)
	sigmaE = 0        #Initializing 
	sigmaEiScaled = 0 #Initializing
	for key, value in sorted(taskDictETime.iteritems()) : #Iterate for each item in dictionary
		sigmaE += value     #Calculate Sigma ei

	subtaskCompleted = []   #Initializing  
	h = []                  #Initializing 
	currentTasksinHeap = [] #Initializing 
	scaledEi = []           #Initializing 
	#scalingfactor = float(TotalTimePerProcessor*int(no_processor))/float(sigmaE)
	scalingfactor = TotalTimePerProcessor*int(no_processor)/sigmaE #Calculate Scaling Factor
	if(scalingfactor==0):
		scalingfactor = 1
	
	#initialize
	for task in range(1,int(no_task)+1) : # Initializing each list 
		currentTasksinHeap.append(task)   # List of Current Task in Heap
		subtaskCompleted.append(0)        # List of total Subtask Completed
	for task in range(1,int(no_task)+1) : #except for last task
		scaledEivalue = float(math.floor(float(taskDictETime[str(task)])*scalingfactor))
		sigmaEiScaled += scaledEivalue    #Scaled value
		scaledEi.append(scaledEivalue)    #Scaled value
		heapq.heappush(h,(float(1/scaledEivalue),task))  #j=1 Heappush
	
	t = 0    #timeline
	miss = 0
	proc = int(no_processor)
	while h : #heap not empty
	
		t += 1
		added = []
		processor = int(no_processor)
		while (processor > 0) and h : #While heap is not empty or no. of processors over
			processor -= 1            #Decrement processor
			tupple = heapq.heappop(h) #Pop task wiht min priority
		
			task = tupple[1]          #Task 
			subtask = tupple[0] #priority value of jth subtask
			subtaskCompleted[task-1] = subtaskCompleted[task-1] +1 #Increment subtask Completed

			if(scaledEi[task-1] - subtaskCompleted[task-1] != 0) : #task0 still left
				added.append((subtaskCompleted[task-1],task))      #Store next task in added
	
			else :
				currentTasksinHeap.remove(task)   #remove completed Task

		for tasktup in range(0,len(added)):
			prioritykey = (added[tasktup][0]+1)*(float(1/scaledEi[added[tasktup][1]-1]))
			keyvalue = added[tasktup][1] 
			heapq.heappush(h,(prioritykey,keyvalue)) #Push incomplete task back to heap
		
		for eachtask in currentTasksinHeap : #for each task in heap
			lag = (float(scaledEi[eachtask-1])/float (sigmaEiScaled))*t - subtaskCompleted[eachtask-1]
			if(lag>1) :#lag >1
				miss += 1  #Increment Misses

	return miss

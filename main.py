from random_datagenerator import dataFileGenerator
from roundrobinalgo import roundRobin
from proportionatealgo import prop
from configDic import taskDictionary, MaxFile, period, startTask
import matplotlib.pyplot as plt

number_of_processors = '' # no of processors
maxTask = ''              # Get maximum tasks from user for plotting graph
maxProcessor = ''         # Get maximum number of processors from the user
number_of_tasks = ''      # Get number of tasks from user 
option = ''               # Select option
MissR = [] #list of misses fro each point in x axis for Round Robin
MissP = [] #list of misses for each point in x axis for preemptive

while option =='': # Get option form user
	option =raw_input("Enter 1 for number of task v/s miss graph \nEnter 2 for number of processor v/s miss graph : ")

if option == '1':  # Check: Option for Round Robin 

	while number_of_processors=='':  # while is none
		number_of_processors = input("Enter number_of_processors : ") #input as int make it raw_input convert to int

	while maxTask=='':  #Get maximum number of tasks from user
		maxTask = input("Enter Maximum number of Task : ")

	for each_numberoftask in range(startTask,maxTask+period,period): #for each x point
		dataFileGenerator(number_of_processors,each_numberoftask) #create 20 data files for each
	print 'Data File Generated'

	for each_numberoftask in range(startTask,maxTask+period,period): #for each x point
		missSumR = 0  #initialize number of misses to zero in Round Robin
		missSumP = 0  #initialize number of misses to zero in Preemptive
		for i in range(1,MaxFile+1):					 #run RoundRobin 50 times for each point
			filename = str(number_of_processors)+'-'+str(each_numberoftask)+'-'+str(i)+'.txt'
			taskDictionary(filename)          #Initialize task ditionary for each file
			missSumR += roundRobin(filename)  #Get number of misses for roundrobin for each file
			missSumP += prop(filename)        #Get number of misses for premptive for each file
		MissR.append(round(float(missSumR)/float(MaxFile),2)) #take average RoundRobin
		MissP.append(round(float(missSumP)/float(MaxFile),2)) #task average Premptive
		print each_numberoftask
	
	plt.plot(range(startTask,maxTask+period,period),MissR, color = 'r',label = 'RoundRobin') #Plot ROundRobin in red Color
	plt.plot(range(startTask,maxTask+period,period),MissP, color = 'b',label = 'Preemtive') #Plot Premptive in blue Color
	plt.legend(loc=2)              #Label Graphs
	plt.title('Tasks v/s Misses')
	plt.ylabel('Number of Misses')
	plt.xlabel('Number of Tasks')
	plt.show()                     #Show Graphs

else :  #Run for Number of Processor v.s Miss graph
	while number_of_tasks=='':  # while is none
		number_of_tasks = input("Enter number_of_tasks : ") #input as int make it raw_input convert to int

	listofprocessor = ['1','2','4','8','16','32']  #List of Processors
	for each_numberofprocessor in listofprocessor: #for each x point
		dataFileGenerator(each_numberofprocessor,number_of_tasks) #create 50 data files
	print 'Data File Generated'

	for each_numberofprocessor in listofprocessor: #for each x point
		missSumR = 0  #initialize number of misses to zero in Round Robin
		missSumP = 0  #initialize number of misses to zero in Premptive
		for i in range(1,MaxFile+1):					 #run RoundRobin 50 times for each point
			filename = str(each_numberofprocessor)+'-'+str(number_of_tasks)+'-'+str(i)+'.txt'
			taskDictionary(filename)   #Get task Dictionary for each File
			missSumR += roundRobin(filename) #Get number of misses for round Robin
			missSumP += prop(filename)       #Get number of misses for Premptive
		MissR.append(round(float(missSumR)/float(MaxFile),2)) #take average
		MissP.append(round(float(missSumP)/float(MaxFile),2)) #take average
		print each_numberofprocessor
	plt.plot(listofprocessor,MissR, color = 'r',label = 'RoundRobin') #Plot Graph for Round Robin in red
	plt.plot(listofprocessor,MissP, color = 'b',label ='Preemtive')  #Plot Graph for Premptive in blue
	plt.legend(loc=1) #Lable Graps
	plt.title('Processor v/s Misses')
	plt.ylabel('Number of Misses')
	plt.xlabel('Number of Processor')
	plt.show()  #Plot the Graph








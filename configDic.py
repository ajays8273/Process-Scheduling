taskDictETime = {}          #Dictionary for storing the values of Ei
TotalTimePerProcessor = 10000      #Time slots per processor
MaxFile = 20            # Number of files corresponding to a data ( for more randomization)
period = 10              #Difference between two consecutive values of task in graph
startTask = 10          #Number of tasks to start from
Eirange = [200,500]     #Range of Ei
def taskDictionary(filename):
	dataFile = open(filename, 'r')
	data = dataFile.read()
	lines = data.split('\n') #creates list of lines
	#print lines
	no_of_processor = lines[0]        #Processors in first line
	numberoftasksis = lines[1]        #Number of tasks in the file
	for line in lines[2:] :           #Storing i and Ei
		line = line.lstrip().rstrip()
		taskPID = line.split(' ',1)[0]
		taskDictETime[taskPID] = int(line.split(' ',1)[1])
		dataFile.close()

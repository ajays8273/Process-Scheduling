from random import randint                      #Including library for giving random data
from configDic import MaxFile, Eirange          #Importing values from config file

def dataFileGenerator(no_processors, no_tasks): #takes input as integer
	for filenumber in range(1,MaxFile + 1) :    #make data files for each combination
		with open(str(no_processors)+'-'+str(no_tasks)+'-'+str(filenumber)+'.txt', 'w') as f: #format: 4-100-1.txt
			f.write(str(no_processors)+'\n')         
			f.write(str(no_tasks)+'\n')          
			for eachtask in range(1,no_tasks+1) :			 #assuming total task = 1000
				f.write(str(eachtask) + ' ' + str(randint(Eirange[0],Eirange[1])) ) #write task and its corresponding execution time
				if(eachtask != no_tasks):    #skipping the last 'enter'
					f.write('\n')

			

#dataFileGenerator(4,100) #call this way





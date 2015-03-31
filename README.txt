
This Program is the implementation of Round Robin and Pre-emptive Scheduling Algorithms.
The program compares both the algorithms by varying number of tasks and number of processors
and checking the number of misses for each case. Finally, a graph is generated wherein both 
the algorithms' performance is plotted.

!!----------------------------------------------------------------------------------------------!!
To test the program run: main.py

Code Execution:

1. Choose the option: a) No. of tasks vs No. of misses OR b) No. of Processors vs No. of misses
2. For case a) the program will ask to enter number of processors and the maximum number of tasks
   to be completed and then files will be generated. The file format is:
   no_of_processors-no_of_tasks-file_number.txt
   Here the file_number can go upto 20 (for better data values, while plotting the graph average 
   value is taken)
3. For case b) the program will ask to enter number of tasks to be completed and then files will 
   be generated. The file format is same as above. Since, the number of processors are varied, 
   they are varied as discrete values- 1,2,4,8,16 etc. 
4. Then each file is read and sent to round robin and pre-emptive algorithm separately 
5. In round robin algorithm queue data structure has been used
6. In pre-emptive algorithm min-heap data structure has been used.
7. Each task has been scaled with the help of scaling factor
   scalingFactor = (TotalTimePerProcessor*no_processor)/(sigmaE)
   where: sigmaE = total execution time given in each data file,
   		  TotalTimePerProcessor = total time per processor(initialized to 10000)
   		  no_processor = number of processors	
8. If lag > 1 then a miss is counted.
9. Subtask completed is the portion of the task which has been completed up to that cycle.
10. Finally a graph between no. of processors v/s misses and number of tasks v/s misses is drawn.

!!----------------------------------------------------------------------------------------------!!   

Files:

i)   configDic.py: configures/intitializes the various variables 
ii)  main.py: main file which calls every other function/file
iii) proportionatealgo.py: implements pre-emptive scheduling algorithm
iv)  roundrobinalgo.py: implements round-robin scheduling algorithm
v)   random_datagenerator: generates the data file with format(inside each file):
	 Number of processors
	 Number of tasks
	 Execution time of each of the above tasks

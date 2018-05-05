tp = input("Enter no of processes you want to enter: ")  #Getting total number of processes

print ("Enter Process name, Arrival time, Burst time")
pdic = [ map(str,(raw_input()+' '+'0'+' '+'0').split()) for x in range(tp)] #Gettting process name arival time and burst time and by default storing wating time and turnaround time 0

i = 0 #Loop variable
while i < tp:
	j = 0  #Inner Loop variable
	while j < tp-1:
	   if  pdic[j][1] > pdic[j+1][1]:
	       pdic[j], pdic[j+1] = pdic[j+1], pdic[j]
   	   j += 1
	i += 1

finishtime = starttime = int(pdic[0][1])

for k in range(tp):	
	waitingtime = 0
	turnaround = 0

	if finishtime<int(pdic[k][1]):
		temp = int(pdic[k][1]) - finishtime
		finishtime += temp
		starttime = int(plist[k][1])
		
	finishtime += int(pdic[k][2])
	waitingtime = starttime-int(pdic[k][1])
	pdic[k][3] = str(waitingtime)
	turnaround = finishtime-int(pdic[k][1])
	pdic[k][4] = str(turnaround)
        starttime += int(pdic[k][2])

print ("Process name  Arrival time  Burst time  Waiting time  Turnaround time")
i = 0
while i < tp:
    print '    ',pdic[i][0],'          ',pdic[i][1],'          ',pdic[i][2],'          ',pdic[i][3],'          ',pdic[i][4]
    i += 1

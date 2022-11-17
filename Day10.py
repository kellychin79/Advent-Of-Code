import time
start_time = time.time()

file = open('day10.txt')
data = [int(x.strip()) for x in file] #OR data = file.read().split('\n')
data.sort()

#--- Part One ---
differences = {'1':0,'2':0,'3':0}

if data[0]-0 > 3:
	print('fail. cannot connect the charging outlet')
else:
	differences[str(data[0]-0)] += 1
	for i in range(len(data)-1):
		differences[str(data[i+1]-data[i])] += 1
	differences['3'] += 1 #for the last connection to your device

print(differences['1']*differences['3'])

#--- Part Two --- (A wonderful solution from others)
sol = {0:1}
for i in sorted(data):
    sol[i] = 0
    if i - 1 in sol:
        sol[i]+=sol[i-1]
    if i - 2 in sol:
        sol[i]+=sol[i-2]
    if i - 3 in sol:
        sol[i]+=sol[i-3]

print(sol[max(data)])

#--- Part Two --- 
#mine works on test data, but it took forever to run on real data => The answer is 226775649501184, no wonder it is still running after half an hour

theDevice = max(data) 
arrangNum = 0
def arrange(point,goal):
	print('start')
	global arrangNum
	if point == goal:
		arrangNum += 1
		print('succeed')
	elif point > goal:
		print('end')
		return
	for i in range(1,4):
		if point+i in data:
			arrange(point+i,goal)
	print('end')

arrange(0,theDevice)
print(arrangNum)

file.close()

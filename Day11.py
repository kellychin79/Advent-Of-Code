import time
STARTTIME = time.time()

file = open('day11.txt')
data = [x.rstrip() for x in file.readlines()]
data = [list(line) for line in data]

rows, cols = len(data), len(data[0])
deltas = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

#-----Part One-----
def count_occupied(row, col, grid):
    count=0
    for i,j in deltas:
        newRow,newCol = row+i, col+j
        if 0<=newRow<rows and 0<=newCol<cols and grid[newRow][newCol]=='#':
            count+=1
    return count

def check_occupied(data, threshold = 4):
    x = 0
    while True:
        print(x)
        print(data[0])
        valid = True
        #data will change at every round and duplicate as a new one in the next round for processing
        temp_grid=[r.copy() for r in data] 
        x += 1 #=> To know that after 76 times, the seats arrangement became stable.
        for i, r in enumerate(temp_grid):
            for j, c in enumerate(r):
                count = count_occupied(i, j, temp_grid)
                #rule number 1
                if c=='L' and count==0:
                    data[i][j]='#'
                #rule number 2
                elif c=='#' and count>=threshold:
                    data[i][j]='L'
                #binary bitwise operator
                valid &= (r[j]==data[i][j])
        if valid:
            break
    ans=0
    for i in range(rows):
        for j in range(cols):
            if data[i][j]=='#':
                ans+=1
    print(f"There are {ans} occupied seats.")

check_occupied(data)

#-----Part Two-----

def count_occupied2(row, col, grid):
	count=0
	for i,j in deltas:
		newRow,newCol = row+i, col+j
		#The main change is below
		while 0<=newRow<rows and 0<=newCol<cols:
			if grid[newRow][newCol]=='#':
				count+=1
				break
			elif grid[newRow][newCol]=='L':
				break
			else: #when it is . but not # or L
				newRow+=i #keep moving forward 1 step until # or L shows up
				newCol+=j #keep moving forward 1 step until # or L shows up
	return count

def check_occupied2(data, threshold = 5):
    while True:
        valid = True
        #data will change at every round and duplicate as a new one in the next round for processing
        temp_grid=[r.copy() for r in data] 
        for i, r in enumerate(temp_grid):
            for j, c in enumerate(r):
                count = count_occupied2(i, j, temp_grid)
                #rule number 1
                if c=='L' and count==0:
                    data[i][j]='#'
                #rule number 2
                elif c=='#' and count>=threshold:
                    data[i][j]='L'
                #binary bitwise operator
                valid &= (r[j]==data[i][j])
        if valid:
            break
    ans=0
    for i in range(rows):
        for j in range(cols):
            if data[i][j]=='#':
                ans+=1
    print(f"There are {ans} occupied seats.")

check_occupied2(data)

print("Elapsed time: "+str(round(time.time()-STARTTIME,4)))

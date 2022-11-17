file = open('expense_report.txt')
readFile = file.read()
content = readFile.split('\n')

#--- Part One ---
newList = content.copy()
while len(newList) > 0:
	firstNum = int(newList[0])
	secondNum = 2020 - firstNum
	if str(secondNum) in newList:
		print(firstNum*secondNum)
	del newList[0]


#--- Part Two ---
newList2 = content.copy()
while len(newList2) > 0:
	firstNum2 = int(newList2[0])
	toMatch = 2020 - firstNum2
	subList = newList2.copy()
	del newList2[0]
	while len(subList) > 0:
		secondNum2 = int(subList[0])
		thirdNum2 = toMatch - secondNum2
		if str(thirdNum2) in subList:
			print(firstNum2*secondNum2*thirdNum2)
		del subList[0]

file.close()


def printer(myList, root, goal):

	print(myList)
	print()

	rootPosition = findPosition(myList, root)
	goalPosition = findPosition(myList, goal)
	print("Path From {0} - {1}:".format(root, goal))

	findDirection(rootPosition, goalPosition)

def findDirection(rootPosition, goalPosition):

	if goalPosition[0] - rootPosition[0] >= 0:
		directionForRow = "down"
		rowDistance = goalPosition[0] - rootPosition[0]
	else:
		directionForRow = "up"
		rowDistance = rootPosition[0] - goalPosition[0]

	if goalPosition[1] - rootPosition[1] >= 0:
		directionForColumn = "right"
		columnDistance = goalPosition[1] - rootPosition[1]
	else:
		directionForColumn = "left"
		columnDistance = rootPosition[1] - goalPosition[1]

	print("Go {0} row {1} and {2} column to {3} / Vice-Versa".format(rowDistance, directionForRow, columnDistance, directionForColumn))
	
def findPosition(myList, node):
	i, j = 0, 0

	for everyList in myList:
		for eachlist in everyList:
			if eachlist == node:
				position = i, j
				return position
			j += 1
		j = 0 
		i += 1	
	
#function testing			
myList = [["A","B","C"], ["D","E","F"], ["G","H","I"]]
printer(myList,'B','I')

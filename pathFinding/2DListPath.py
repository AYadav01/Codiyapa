#this function will access the index location of root and goal nodes and print the path directions
def printer(myList, root, goal):
	#will print the list first
	print(myList)
	print()

	#gather the index positions of root and goal
	rootPosition = findPosition(myList, root)
	goalPosition = findPosition(myList, goal)
	print("Path From {0} - {1}:".format(root, goal))

	#will print the final path
	findDirection(rootPosition, goalPosition)

#this will will determine the direction and length depending upon the index position of the nodes
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

	#print the accumulated data
	print("Go {0} row {1} and {2} column to {3} / Vice-Versa".format(rowDistance, directionForRow, columnDistance, directionForColumn))
	
#this function will find the index position of any specified node
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
	
#make a 2D List
def Lister(row,column):
  myList = [[None]*column for i in range(row)]  
  return fillPositions(myList, column)

#this function will fill the elements of the 2D list create above
def fillPositions(myList, column):
  i = 0  
  start = 65 #we will start from 'A' (ASCII representation)

  for everyList in myList:
    while i < column:
      everyList[i] = chr(start)
      i += 1
      start += 1
    
    i = 0
  return myList

#function testing

#will print the path from point 'B' to 'G' in a 3x3 list (as specified in the paramter)
printer(Lister(3,3), 'B','G')
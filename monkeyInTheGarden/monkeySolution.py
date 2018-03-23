def monkeyTime(array):

	#empty dictionary
	data = {}

	#this array will handle the circular references
	newArray = list(array)

	#threshold point
	divisor = (len(array)-1)//2

	for i in range(len(array)):

		#the threshold point (divisor) will increase each time the monkey chanegs tree
		if i > 0:
			divisor += 1
			temp = newArray[0]
			del(newArray[0])
			newArray.append(temp)
			#print("i is {0}, divisor is {2} and newArray is {1}".format(i, newArray, divisor))

		for j in range(len(array)):
			if i != j:

				if (i,j) and (j,i) not in data.keys():
					#if second monkey with-in the threshold
					if j <= divisor:
						distance = j-i
					
					#if second monkey is outside the threshold; then
					elif j > divisor:
						target = newArray.index(array[j])
						distance = 0
						for indexAgain in newArray[target:]:
							distance += 1

					#finallly calculating the total cost
					cost = array[i] + distance + array[j]
					#writing the data to our hash table/dictionray in python ;-)
					data[i,j] = distance, cost

	#call for the findTime function
	return findTime(data)

#this function finds the highest time taken in the hashTable
def findTime(data):
	maximum = 0

	#finding maximum number
	for everyValues in data.values():
		distance, time = everyValues
		if time > maximum:
			maximum = time
	return "The maximum time taken is {0} units".format(maximum)

#function testing
array = [3,5,4,3,7,1]
print(monkeyTime(array))
def monkeyTime(array):

	#empty dictionary
	data = {}
	newArray = list(array)

	#threshold
	divisor = (len(array)-1)//2
	#print(divisor)

	for i in range(len(array)):

		if i > 0:
			divisor += 1
			temp = newArray[0]
			del(newArray[0])
			newArray.append(temp)
			print("i is {0}, divisor is {2} and newArray is {1}".format(i, newArray, divisor))

		for j in range(len(array)):

			if i != j:

				if (i,j) and (j,i) not in data.keys():

					if j <= divisor:
						distance = j-i
						
					elif j > divisor:
						#print("j is {}".format(j))

						target = newArray.index(array[j])
						distance = 0
						for indexAgain in newArray[target:]:
							distance += 1

					cost = array[i] + distance + array[j]
					data[i,j] = distance, cost

	return findTime(data)

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
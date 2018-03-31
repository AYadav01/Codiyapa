#every vertex in the graph is an instane of the node class
class Node(object):

	def __init__(self, name):
		self.name = name
		self.neighbors = list()
		self.visited = False

	def addNeighbors(self, vertex):
		if vertex not in self.neighbors:
			self.neighbors.append(vertex)

#graph class
class Graph(object):
	vertices = {}
	visitedIterative = ""
	visitedRecursive = ""

	def addVertex(self, node):
		if isinstance(node, Node) and node.name not in self.vertices:
			self.vertices[node.name] = node

	def addEdge(self, source, destination):
		if source in self.vertices and destination in self.vertices:
			for key, values in self.vertices.items():
				if key == source:
					values.addNeighbors(destination)

				if key == destination:
					values.addNeighbors(source)

	def printGraph(self):
		for keys in self.vertices.keys():
			print(keys + " -> " + str(self.vertices[keys].neighbors))

	def dfsIterative(self, source):
		#source.visited += source.name
		#print(source.visited)
		#initialize a stack with visited node
		stack = [source.name]

		while stack:
			currentNode = stack.pop()
			#this helps gets rid of circular references
			if currentNode not in self.visitedIterative:
				self.visitedIterative += str(currentNode)
			#print(self.visitedString)

			#traversing through the currentNode branches
			for everyNode in self.vertices[currentNode].neighbors:
				if everyNode not in self.visitedIterative:
					stack.extend(everyNode)

		print("DFS (Iterative) Travarsal: {0.visitedIterative}".format(self))

	def dfsRecursive(self, source):
		#adding visited node to the string (once its True)
		source.visited = True
		self.visitedRecursive += source.name
		for everyEdge in source.neighbors:
			if self.vertices[everyEdge].visited == False:
				self.dfsRecursive(self.vertices[everyEdge])

	def findPath(self, source, goal):
		path = []
		stack = [source]

		while stack:			
			currentNode = stack.pop()

			if currentNode not in path:
				path.extend(currentNode)
				#print("path is {0}".format(path))

			if path [-1] == goal:
				stack.clear()
			else:
				for everyEdge in self.vertices[currentNode].neighbors:
					if everyEdge not in path:
						stack.extend(everyEdge)

					if everyEdge != source and everyEdge in path:
						path.pop()

		print("The path form {0} - {1} is {2}".format(source, goal, path))


#testing the class
g = Graph()
edges = ['AB','AD','BC','CE','DE','DF','EG']

def makeGraph(g, edges):
	a = Node("A")
	g.addVertex(a)

	#adding vertex upt 'G' with a loop
	for i in range(ord('A'), ord('H')):
		g.addVertex(Node(chr(i)))

	#adding edges
	for everyEdges in edges:
		g.addEdge(everyEdges[:1], everyEdges[1:])

	#printing the graph
	g.printGraph()
	print()

	#Depth first search iterative call
	g.dfsIterative(a)

	#Depth first search recursive call
	g.dfsRecursive(a)
	print("DFS (Recursive) Travarsal: {0.visitedRecursive}".format(g))
	print()

	#finding path
	g.findPath('A','E')

#function test
makeGraph(g, edges)





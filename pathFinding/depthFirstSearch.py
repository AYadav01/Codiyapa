#every vertex is an instane of the node class
class Node(object):

	def __init__(self, name):
		self.name = name
		self.neighbors = list()

	def addNeighbors(self, vertex):
		if vertex not in self.neighbors:
			self.neighbors.append(vertex)

#graph class
class Graph(object):
	vertices = {}
	visitedString = ""

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
			self.visitedString += str(currentNode)
			#print(self.visitedString)

			#traversing through the currentNode branches
			for everyNode in self.vertices[currentNode].neighbors:
				if everyNode not in self.visitedString:
					stack.extend(everyNode)

		print("DFS (Iterative) Travarsal: {0.visitedString}".format(self))

	def dfsRecursive(self):
		pass

#testing the class
g = Graph()
edges = ['AB','AD','BC','DE','DF','EG']

def dfs(g, edges):
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

	#Depth first search iterative call
	g.dfsIterative(a)

#function test
dfs(g, edges)





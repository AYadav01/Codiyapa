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

	def addVertex(self, node):
		if isinstance(node, Node) and node not in self.vertices:
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

#testing the class
def makeGraph(graph, node):
	g = Graph()
	for i in range(ord('A'), ord('H')):
		g.addVertex(Node(chr(i)))

	edges = ['AB','AD','BC','DE','DF','EG']

	for everyEdges in edges:
		g.addEdge(everyEdges[:1], everyEdges[1:])

	#see the graph
	g.printGraph()

#function test
makeGraph(Graph, Node)


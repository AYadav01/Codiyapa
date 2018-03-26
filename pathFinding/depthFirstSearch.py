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
			self.vertices[node.name] = vertex

	def addEdge(self, source, destination):
		if soure in self.vertices and destination in self.vertices:
			for key, values in self.items():
				if key == source:
					values.addNeighbors(destination)

				if key == destination:
					values.addNeighbors(source)


	def printGraph(self):
		for keys in self.vertices.keys():
			print(keys + " -> " +self.vertices[key].neighbors)


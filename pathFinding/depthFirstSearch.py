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
    onGoing = [source]
    print("starting set is {}".format(onGoing))
    stack = [source]
    traversed = ""
    print("current stack: {}".format(stack))
    i = 0
    finalPath = {}

    while stack:
      marked = None
      currentNode = stack.pop()
      if currentNode != goal:

          traversed += currentNode  
          print("popped element is {}".format(currentNode))
    
          for everyElement in self.vertices[currentNode].neighbors:
            if everyElement not in traversed:
              stack.extend(everyElement)
              
            for everyPath in onGoing:
              if everyElement not in everyPath:
                if everyPath[-1] == currentNode:
                  temp = everyPath
                  marked = temp
                  temp += everyElement
                  if temp[0] == source and temp[-1] == goal:
                    finalPath[i] = temp
                    i += 1
                  else:
                    onGoing.append(temp)

          if marked is not None:
              onGoing.remove(marked)
          print("stack now is {}".format(stack))
          print("my set is {}".format(onGoing))
    print("final path is {}".format(finalPath))
          
#testing the class
g = Graph()
edges = ['AB','AD','BC','BE','CE','DE','DF','FE','EG']

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





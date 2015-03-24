
class Graph():
	root = 0
	def __init__(self,root):
		self.root = root
		self.node = Node()
		self.addRight()
		self.addLeft()		

	def addRight(self):
		self.node.addRight(5)
	def addLeft(self):
		self.node.addLeft(6)
	def printIt(self):
		print str(self.node.left)+ ' <-- ' +str(self.root) +' --> '+ str(self.node.right)  
		
class Node():
	left = 0
	right = 0
	
	def addRight(self, node):
		self.right = node
	def addLeft(self, node):
		self.left = node

if __name__ == '__main__':
	graph = Graph(800)
	graph.printIt()

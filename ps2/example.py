class Digraph(object):
    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        if node in self.edges:
            raise ValueError("duplicate node")
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self.edges or dest in self.edges):
            raise ValueError('Node not in the graph')
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for n in self.edges:
            if name == n.getName():
                return n
        raise NameError

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in src.edges[src]:
                result = result + src.getName() + '->' + dest.getName()

        return result[:-1]


def printPath(path):
    result = ''
    for i in range(len(path)):
        result += str(path[i])
        if i != len(path) - 1:
            result += '->'
    return result


def dfs(graph, start, end, path, shortest, toPrint=False):
    path = path + [start]
    if toPrint:
        printPath(path)
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:
            if shortest is None or len(path)<len(shortest):
                newPath=dfs(graph,node,end,path,shortest,toPrint)
                if newPath !=None:
                    shortest=newPath

    return shortest
def shortestPath(graph,start,end,toPrint=False):
    return dfs(graph,start,end,[],None,toPrint)

class graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(edge)
        rev = Edge(edge.get_destination(), edge.getSource())
        Digraph.addEdge(rev)


class Node(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()

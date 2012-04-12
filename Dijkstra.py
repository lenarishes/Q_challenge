import collections, heapq

class Digraph(object):
    def __init__(self):
        self.nodes = collections.defaultdict(list)
        self.edges = {}
    
    def addEdge(self, tail, head, dist):
        self.nodes[tail].append(head)
        if head not in self.nodes.keys():
            self.nodes[head] = []
        edge = (tail, head)
        self.edges[edge] = dist
        
    def getNodes(self):
        return self.nodes.keys()
        
    def countNodes(self):
        return len(self.nodes.keys())
        
    def edgeLength(self, a, b):
        edge = (a,b)
        if edge in self.edges:
            return self.edges[edge]        
        return 0
    
    def getHeads(self, tail):
        return self.nodes[tail]
        
    def __str__(self):
        result = ""
        for t, heads in self.nodes.items():
            for h in heads:
                string = "%s %s %d" % (t, h, self.edges[(t,h)]) 
                result = result + string + "\n"
        return result  

def findPath(G, start, goal):
    dist = collections.defaultdict(int)
    dist[start] = 0    
    path = collections.defaultdict(list)
    #processed nodes
    seen = [start]
    #heap to choose minimal from available paths
    h = []
    if start == goal:
        return []
              
    while len(seen) < G.countNodes():
        tail = seen[-1]    
        for head in G.getHeads(tail):
            if head not in seen:
                heapq.heappush(h, (dist[tail] + G.edgeLength(tail, head), (tail, head)))
        #until we find a shortest path to a node not reached yet
        while True:
            distance, nodes = heapq.heappop(h)
            b,e = nodes[0], nodes[1]
            if e not in seen:
                dist[e] = distance
                path[e] = path[b] + [nodes]
                seen.append(e)
                if e == goal:
                    return path[e]
                else:
                    break                
    #goal is unreachable
    return None

def getGraphFromFile(path):
    graph = Digraph()
    for line in open(path, 'r'):
        line = line.split()
        graph.addEdge(line[0], line[1], int(line[2]))
        graph.addEdge(line[1], line[0], int(line[2]))
    return graph
    
print findPath(getGraphFromFile('map.txt'), 'Paris', 'Barcelona')

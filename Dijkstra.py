import collections, heapq

class Digraph(object):
    def __init__(self):
        """
        Adjacency lists representation of directed graph
        
        edge: dict, for each node v contains a list of edge u such that (v,u) is an outgoing edge
        edges: dict, for each edge (v,u) contains its length         
        """
        self.edge = collections.defaultdict(list)
        self.edges = {}
    
    def addEdge(self, tail, head, dist):
        """
        Add edge 'tail', 'head' and the edge of length 'dist' connecting them to the graph
        
        tail: string 
        head: string
        dist: int
        """
        self.edge[tail].append(head)
        if head not in self.edge.keys():
            self.edge[head] = []
        edge = (tail, head)
        self.edges[edge] = dist
        
    def getNodes(self):
        """
        Get the list of all graph edge
        """
        return self.edge.keys()
        
    def countNodes(self):
        """
        Get the number of all graph edge
        """
        return len(self.edge.keys())
        
    def edgeLength(self, a, b):
        """
        Get the length of edge going from node 'a' to node 'b'.
        Returns 0 if there is no such edge.
        
        a: string
        b: string
        """
        edge = (a,b)
        if edge in self.edges:
            return self.edges[edge]        
        return 0
    
    def getHeads(self, tail):
        """
        Get the list of edge that can be reached from 'tail'
        
        tail: string
        """
        return self.edge[tail]
        
    def __str__(self):
        result = ""
        for t, heads in self.edge.items():
            for h in heads:
                string = "%s %s %d" % (t, h, self.edges[(t,h)]) 
                result = result + string + "\n"
        return result  

def findPath(G, start, goal):
    """
    Find shortest path from start to goal.
    Where start and goal are edge of a directed weighted graph
    
    G: a Digraph object
    start: string
    goal: string
    returns: a list of tuples representing the edges in the path
    """
    # contains lengths of shortest paths to the edge found so far
    dist = collections.defaultdict(int)
    dist[start] = 0
    # contains the shortes paths to the edge found so far    
    path = collections.defaultdict(list)
    #processed edge
    seen = [start]
    #heap to choose the minimal path from the frontier
    h = []
    if start == goal:
        return []
              
    while len(seen) < G.countNodes():
        #expand the node which we added last
        tail = seen[-1]    
        for head in G.getHeads(tail):
            if head not in seen:
                heapq.heappush(h, (dist[tail] + G.edgeLength(tail, head), (tail, head)))
        #until we find a shortest path to a node not reached yet
        while True:
            distance, edge = heapq.heappop(h)
            b,e = edge[0], edge[1]
            if e not in seen:
                dist[e] = distance
                path[e] = path[b] + [edge]
                seen.append(e)
                if e == goal:
                    return path[e]
                else:
                    break                
    #goal is unreachable
    return None

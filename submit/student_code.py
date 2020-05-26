from heapq import heappush, heappop
from math import sqrt

### The Node objects contain the node number, the parent
### or node from which this one came from, as well as the
### distances travelled to get to this node (g), the
### estimated straight-line distance to the goal (h), and
### the sum of g+h, or the f distance, which determines
### the best choice to explore next. 
class Node(object):
    def __init__(self, num, gdist=0, hdist=0, parent=-1):
        self.gdist = gdist   ## distance travelled so far from the start node
        self.hdist = hdist   ## estimated distance from node to goal node
        self.dist = self.gdist + self.hdist     ## should be gdist + hdist        
        self.num = num
        self.where_from = parent
        
    def __lt__(self, other):
        return (self.dist < other.dist)
    
    def __eq__(self, other):
        return self.num == other.num
    
    def update_dist(self):
        self.dist = self.gdist + self.hdist
        


### A priority queue (heapq) is used to manage the frontier of
### nodes that may be visited next. The one with the minimum
### f value--a sum of the distance traveled so far (g) plus a
### heuristic (h) measuring the straight-line distance from
### the node to the goal--is the one selected to be visited next.
class HeapQueue(object):
    def __init__(self):
        self.hqueue = []
        
    def hpush(self, node):
        # update dist based on gdist and hdist  
        node.update_dist()
        heappush(self.hqueue, node)
        
    def hpop(self):
        popped = heappop(self.hqueue)
        return popped

    def is_in_heap(self, num):
        node = Node(num)
        return node in self.hqueue
    
    def print_heap(self):
        print("length of heap is {}\nheap: ".format(len(self.hqueue)))
        for i in self.hqueue:
            print("node {} has f of {} and came from {}".format(i.num, i.dist, i.where_from))
            
    def get_heap_length(self):
        return len(self.hqueue)
            
        
        
### Given a map with point intersections and two points, determine
### the distance between the points, using the Pythagorean Theorem
def distance(M, pt1, pt2):    
    dist_x = abs(M.intersections[pt1][0] - M.intersections[pt2][0])
    dist_y = abs(M.intersections[pt1][1] - M.intersections[pt2][1])
    
    dist = sqrt(dist_x ** 2 + dist_y ** 2)
    return dist

### Given a dictionary, path and the goal node, retrace steps
### that were taken to reach the goal
def construct_path(path, goal):
    short_path = [goal]
    idx = goal

    while path[idx][0] > -1:
        short_path.insert(0, path[idx][0])
        idx = path[idx][0]

    print("path: ", short_path)
    return short_path
                 

### Using the A* algorithm, find the shortest path from a starting
### node to a goal node in the given graph
def shortest_path(M, start, goal):
    distance(M, start, goal)
    h = HeapQueue()                                      # priority queue will determine which node to visit next
    node_start = Node(start, 0, distance(M,start,goal))  # jump start algorithm with starting node
    h.hpush(node_start)
    
    visited = {}
    path = {}
    
    while h.get_heap_length() > 0:  
        current_node = h.hpop()

        ### only update the path if the distance from current_node back to start is smaller/shorter
        if current_node.num in path:
            if current_node.dist < path[current_node.num][1]:
                path[current_node.num] = (current_node.where_from, current_node.dist)
        else:      
            path[current_node.num] = (current_node.where_from, current_node.dist)             
            
        visited[current_node.num] = True
        
        if current_node.num == goal:
            final_path = construct_path(path, goal)
            return final_path
        
            
        current_node_dist = current_node.gdist
        for child in M.roads[current_node.num]:            
            if child not in visited:
                current_to_new_dist = distance(M, current_node.num, child)
                g = current_node_dist + current_to_new_dist
                h_est = distance(M, child, goal)
                new_node = Node(child, g, h_est, current_node.num) 
                h.hpush(new_node)
                                
    return   
            

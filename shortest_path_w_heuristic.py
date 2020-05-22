from heapq import heappush, heappop
from math import sqrt

class Node(object):
    def __init__(self, dist=0, num=-1):
        self.dist = dist
        self.num = num

    def __lt__(self, other):
        return (self.dist < other.dist)
    
    def __eq__(self, other):
        return self.num == other.num
    
    
def distance(M, pt1, pt2):    
    dist_x = abs(M.intersections[pt1][0] - M.intersections[pt2][0])
    dist_y = abs(M.intersections[pt1][1] - M.intersections[pt2][1])
    
    dist = sqrt(dist_x ** 2 + dist_y ** 2)
    print("distance between {} and {} is {}".format(pt1, pt2, dist))
    return dist


class HeapQueue(object):
    def __init__(self):
        self.hqueue = []
        
    def hpush(self, node):
        heappush(self.hqueue, node)
        
    def hpop(self):
        popped = heappop(self.hqueue)
        return popped

    def is_in_heap(self, num):
        node = Node(-1, num)
        return node in self.hqueue
    
    def print_heap(self):
        print("length of heap is {}".format(len(self.hqueue)))
        for i in self.hqueue:
            print(i.num)
            
    def get_heap_length(self):
        return len(self.hqueue)
            
        
        
def shortest_path(M, start, goal):
    distance(M, start, goal)
    
    print("test shortest_path")
    h = HeapQueue()
    node_start = Node(0, 1)
    h.hpush(node_start)

    heaplen = h.get_heap_length()
    print("size of heap is {}".format(heaplen))
    
    visited = []
    
    while h.get_heap_length() > 0:
        current_node = h.hpop()
        print("popped")
        visited.append(current_node.num)
        
        if current_node.num == goal:
            print("found it: {}".format(current_node.num))
            return current_node.num
        
        print("current node is {}".format(current_node.num))
        print("  and my children are ", M.roads[current_node.num])
    
        current_node_dist = current_node.dist
        for child in M.roads[current_node.num]:
            if child not in visited and not h.is_in_heap(child):
                current_to_new_dist = distance(M, current_node.num, child)
                g = current_node_dist + current_to_new_dist
                h_est = distance(M, child, goal)
                new_node = Node(g+h_est, child) 
                h.hpush(new_node)
                
    return    
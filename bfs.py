class GraphNode(object):
  def __init__(self, value):
    self.value = value
    self.distance = 0          # distance from start point
    self.children = []

  def add_child(self, node):
    self.children.append(node)

  def remove_child(self, node):
    if node in self.children:
      self.children.remove(node)

class Graph(object):
  def __init__(self, node_list):
    self.nodes = node_list

  def add_edge(self, node1, node2):
    if (node1 in self.nodes and node2 in self.nodes):
      node1.add_child(node2)
      node2.add_child(node1)

  def remove_edge(self, node1, node2):
    if (node1 in self.nodes and node2 in self.nodes):
      node1.remove_child(node2)
      node2.remove_child(node1)

  def bfs_search(self, root_node, search_value):
    print("root node is {}".format(root_node.value))
    visited = []
    root_node.distance = 0
    queue = [root_node]

    while len(queue) > 0:
      current_node = queue.pop(0)
      visited.append(current_node)
      print("nodes in visited: {}".format(len(visited)))
      if current_node.value == search_value:
        print("search value found, returning {}".format(current_node.value))
        for v in visited:
          print("v {} with distance {}".format(v.value, v.distance))
        return current_node

      for child in current_node.children:
        if child not in visited and child not in queue:
          child.distance = current_node.distance + 1
          queue.append(child)
          print("appended {}".format(child.value))

    return GraphNode(' ')


# def dfs_search(root_node, search_value):
#     visited = []
#     stack = [root_node]

#     while len(stack) > 0:
#       current_node = stack.pop()
#       visited.append(current_node)

#       if current_node.value == search_value:
#         return current_node

#       for child in current_node.children:
#         if child not in visited and child not in stack:
#           stack.append(child)

#     return GraphNode(' ')


nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeB = GraphNode('B')
nodeC = GraphNode('C')

# print(nodeG.value)
graph1 = Graph([nodeG, nodeR, nodeA, nodeP, nodeH, nodeB, nodeC])
# print(graph1)
graph1.add_edge(nodeG, nodeR)
graph1.add_edge(nodeG, nodeB)
graph1.add_edge(nodeR, nodeA)
graph1.add_edge(nodeA, nodeP)
graph1.add_edge(nodeP, nodeH)

graph1.add_edge(nodeB, nodeC)
# graph1.add_edge(nodeC, nodeH)

for each in graph1.nodes:
  print(each.value)
  for each in each.children:
    print("child {} ".format(each.value))
  print("\n")

res = graph1.bfs_search(nodeG, 'H')
print(res.value)
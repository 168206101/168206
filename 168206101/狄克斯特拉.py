graph = {}       
graph["乐谱"] = {}
graph["乐谱"]["海报"] = 5
graph["乐谱"]["黑胶唱片"] = 0
graph["海报"] = {}
graph["海报"]["吉他"] = 30
graph["海报"]["架子鼓"] = 35
graph["黑胶唱片"] = {}
graph["黑胶唱片"]["吉他"] = 15
graph["黑胶唱片"]["架子鼓"] = 20
graph["吉他"] = {}
graph["吉他"]["钢琴"] = 20
graph["架子鼓"] = {}
graph["架子鼓"]["钢琴"] = 10
graph["钢琴"] = {}
#print(graph)
infinity = float("inf")
costs = {}      
costs["海报"] = 5
costs["黑胶唱片"] = 0
costs["吉他"] = infinity
costs["架子鼓"] = infinity
costs["钢琴"] = infinity
parents = {}      
parents["海报"] = "乐谱"
parents["黑胶唱片"] = "乐谱"
parents["吉他"] = None
parents["架子鼓"] = None
parents["钢琴"] = None
processed = []  #用于记录处理过的节点



#找到开销最小的节点
def find_lowest_cost_node(costs):
    lowest_cost = float("inf") #定义一个最大值
    lowest_node = None
    for node in costs :
        cost = costs[node]
        if(cost<lowest_cost and node not in processed) :
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def find_shortest_path():
    node='钢琴'
    shortest_path=["钢琴"]
    while node!="乐谱":
        node=parents[node]
        shortest_path.append(node)
    shortest_path.reverse()
    print('\n确定到达终点的最终路径：')
    print(shortest_path)  
  
  
  
node = find_lowest_cost_node(costs)   #在未处理的节点中找到最小的节点
while node is not None:
  cost = costs[node]
  neighbors = graph[node]
  for n in neighbors.keys():  #遍历当前节点的所有邻居
    new_cost = cost + neighbors[n]
    if costs[n] > new_cost: #如果经由此节点前往邻居更近
      costs[n] = new_cost #就更新该邻居的开销
      parents[n] = node   #同时将该邻居的父节点设置为当前节点
  processed.append(node)  #将该节点标记为处理过
  node = find_lowest_cost_node(costs) #找出接下来要遍历的节点，并循环
  shortest_path=find_shortest_path()
    print(shortest_path)
print('\n节点:开销')
print(costs)
print('\n节点：父节点')
print(parents) 

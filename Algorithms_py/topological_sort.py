#Kahn’s algorithm
#https://algocoding.wordpress.com/2015/04/05/topological-sorting-python/
#Time complexity: O(V+E)
#Space complexity: O(V) 
def TopologicalSort(graph):
    TopologicalSortedList = []  #result
    ZeroInDegreeVertexList = [] #node with 0 in-degree/inbound neighbours
    inDegree = { u : 0 for u in graph } #inDegree/inbound neighbours

    #Step 1: Iterate graph and build in-degree for each node
    #Time complexity: O(V+E) - outer loop goes V times and inner loop goes E times
    for u in graph:
        for v in graph[u]:
            inDegree[v] += 1

    #Step 2: Find node(s) with 0 in-degree
    for k in inDegree:
        #print(k,inDegree[k])
        if (inDegree[k] == 0):
            ZeroInDegreeVertexList.append(k)           

    #Step 3: Process nodes with in-degree = 0
    while ZeroInDegreeVertexList:
        v = ZeroInDegreeVertexList.pop(0) #order in important!
        TopologicalSortedList.append(v)
        #Step 4: Update in-degree
        for neighbour in graph[v]:
            inDegree[neighbour] -= 1
            if (inDegree[neighbour] == 0):
                ZeroInDegreeVertexList.append(neighbour)

    return TopologicalSortedList
    

#Adjacency list
graph = {
        'A': set([]),
        'B': set(['A']),
        'C': set(['B'])
        }

result = TopologicalSort(graph)
print("Topological sort >>> ", result)
# check if #nodes in result == #nodes in graph
if (len(result) == len(graph)):
    print("Directed Acyclic Graph!")
else:
    print("Graph has cycles!")
vertexList = ['0', '1', '2', '3']
edgeList = [
    (0,1),
    (0,2),  
    (1,2),  
    (2,0),  
    (2,3),  
    (3,3)   
]

graphs = (vertexList, edgeList)

def dfsTask(graph, start, end):
    vertexList, edgeList = graph

    adjList = [[] for v in vertexList]
    for edge in edgeList:
        adjList[edge[0]].append(edge[1])

    stack = [(start, [start])]  
    all_paths = []

    while stack:
        (current, path) = stack.pop()

        if current == end:
            all_paths.append(path)
            continue

        for neighbor in adjList[current]:
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))

    return all_paths

startNode = 2
endNode = 1

paths = dfsTask(graphs, startNode, endNode)

if paths:
    print(f"Yes, the paths exist from {startNode} to {endNode}:")
    for p in paths:
        print(p)
else:
    print("No path exists between the given nodes.")

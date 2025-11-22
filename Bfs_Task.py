vertexList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
edgeList = [
    ('A', 'B'), ('A', 'C'),
    ('B', 'A'), ('B', 'D'), ('B', 'E'),
    ('C', 'A'), ('C', 'F'), ('C', 'G'),
    ('D', 'B'),
    ('E', 'B'), ('E', 'H'),
    ('F', 'C'),
    ('G', 'C'),
    ('H', 'E')
]
graphs = (vertexList, edgeList)
def bfsTask(graph, start, goal):
    vertexList, edgeList = graph

    visitedList = []
    queue = [[start]]

    adjList = {v: [] for v in vertexList}
    for (u, v) in edgeList:
        adjList[u].append(v)

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == goal:
            return path

        if node not in visitedList:
            visitedList.append(node)

            for nbr in adjList[node]:
                newPath = list(path)
                newPath.append(nbr)
                queue.append(newPath)

    return None

print(bfsTask(graphs, 'A', 'F'))

def not_all_visited(visited):
    for i in range(len(visited)):
        if visited[i]==False:
            return True,(i+1)
    return False,None

def dfs(visited,graph,node):
    component_count=0
    k=1
    stack=[]

    while True:
        if visited[node]==True:
            flag,node=not_all_visited(visited)
        else:
            flag=True

        if flag==False:
            break
        stack.append(node)
        component_count = component_count + 1
        visited[node - 1] = True
        while stack:
            print(str(k) + '.' + str(stack))
            k = k + 1
            s=stack.pop()

            for neighbour in graph[s]:
                if visited[neighbour-1]==False:
                    visited[neighbour-1]=True
                    stack.append(neighbour)
    return component_count

graph={
    1:[2],
    2:[3,4],
    3:[2,4],
    4:[2,3],
    5:[6],
    6:[5]
}

visited=[False]*len(graph)
queue=[]
component_count=dfs(visited,graph,5)
print('No of components:'+str(component_count))
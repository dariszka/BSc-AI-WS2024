# Ford-Fulkerson algorithm in Python

class Graph:

    def __init__(self, graph):
        self.graph = graph  # original graph
        self.residual_graph = [[cell for cell in row] for row in graph]  # cloned graph
        self.latest_augmenting_path = [[0 for _ in row] for row in graph]  # empty graph with same dimension as graph
        self.current_flow = [[0 for _ in row] for row in graph]  # empty graph with same dimension as graph

    def ff_step(self, source, sink):
        """
        Perform a single flow augmenting iteration from source to sink. Update the latest augmenting path, the residual
        graph and the current flow by the maximum possible amount, according to the path found by BFS.
        @param source the source's vertex id
        @param sink the sink's vertex id
        @return the amount by which the flow has increased.
        """

        parent = [-1]*len(self.graph)
        path = self.bfs(source, sink, parent)
        self.latest_augmenting_path = [[0 for _ in row] for row in self.graph]
        
        if path:
            increase = float("Inf")
            s = sink
            while(s != source):
                increase = min(increase, self.residual_graph[parent[s]][s])
                s = parent[s]

            v = sink
            while(v != source):
                u = parent[v]

                self.latest_augmenting_path[u][v] = increase

                self.current_flow[u][v] += increase
                self.current_flow[v][u] -= increase 

                self.residual_graph[u][v] -= increase
                self.residual_graph[v][u] += increase

                v = parent[v]
        else:
            increase = 0
        
        return increase
            

    def ford_fulkerson(self, source, sink):
        """
        Execute the ford-fulkerson algorithm (i.e., repeated calls of ff_step())
        @param source the source's vertex id
        @param sink the sink's vertex id
        @return the max flow from source to sink
        """
        
        max_flow = 0 
        increase = self.ff_step(source, sink)
        while increase >0:
            max_flow += increase
            increase = self.ff_step(source, sink)

        self.current_flow = [[cell if cell > 0 else 0 for cell in row] for row in self.current_flow] # for unittest compatibility, expects only values >=0       
        return max_flow

    ### aux ###

    def bfs(self, source, sink, parent):
        visited = [False] * len(self.graph)
        queue = []

        queue.append(source)
        visited[source] = True

        while queue:
            u = queue.pop(0)

            for i, val in enumerate(self.residual_graph[u]):
                if visited[i] == False and val > 0:
                    queue.append(i)
                    visited[i] = True
                    parent[i] = u

                    if i == sink:
                        return True

        return False


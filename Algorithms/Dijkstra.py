from heapq import heappush, heappop

class Dijkstra:
    """
    Pseduo Code of Dijkstra's Algorithm using Min Heap:
    1. Initialize a min heap H and a distances array D.
    2. Insert the starting vertex into H and set its distance in D to 0.
    3. While H is not empty:
        4. Extract the vertex v with the minimum distance from H.
        5. For each neighbor w of v:
            6. Calculate the distance from the starting vertex to w through v.
            7. If this distance is less than the current distance in D for w, update the distance in D for w.
            8. If w is not in H, add it to H.
    9. The distances array D now contains the shortest distances from the starting vertex to all other vertices.
    10. By backtracking from the end vertex, we can find the shortest path.
    11. Return the shortest path and its cost.
    """
    def __init__(self) -> None:
        """
        Constructor of Dijkstra class.
        """
        self.iterations = {
            
        }

    def _dijkstra(self, graph:dict, start:int, end:int) -> tuple:
        """
        Method, that takes a graph and finds the shortest path by Dijkstra algorithm using min heap approach.
        @params:
            graph -> dict : dictionary which includes a directed and weighted graph in the format {node: {neighbour: weight, neighbour: weight, ...}, ...}.
            start -> int : start node.
            end -> int : end node.
        @returns:
            algorithm_type -> str : name of the algorithm.
            path -> list : list of nodes, that are in the shortest path in order.
            cost -> int : cost of the shortest path.
            distance -> int : distance of the shortest path.
        """
        # Initialize a min heap H and a distances array D.
        H = []
        D = {}

        # Insert the starting vertex into H and set its distance in D to 0.
        heappush(H, (0, start))
        D[start] = 0

        # While H is not empty:
        while H:
            # Extract the vertex v with the minimum distance from H.
            _, v = heappop(H)

            # For each neighbor w of v:
            for w in graph[v]:
                # Calculate the distance from the starting vertex to w through v.
                d = D[v] + graph[v][w]

                # If this distance is less than the current distance in D for w, update the distance in D for w.
                if w not in D or d < D[w]:
                    D[w] = d

                    # If w is not in H, add it to H.
                    heappush(H, (d, w))
        
        # Get the distance from the D array mapping.
        distance = D[end]
        
        # The distances array D now contains the shortest distances from the starting vertex to all other vertices.
        # By backtracking from the end vertex, we can find the shortest path.
        path = []
        cost = D[end]
        while end != start:
            path.append(end)
            for node in graph:
                if end in graph[node] and D[node] + graph[node][end] == D[end]:
                    end = node
                    break
        path.append(start)
        path.reverse()

        # Return values.
        return (
            "Djikstra", 
            path, 
            cost, 
            distance
        )

    def solve(self, graph:dict, start:int, end:int) -> tuple:
        """
        Method, that runs the Dijkstra algorithm. @dijkstra().
        @params:
            graph -> dict : dictionary which includes a directed and weighted graph in the format {node: {neighbour: weight, neighbour: weight, ...}, ...}.
            start -> int : start node.
            end -> int : end node.
        @returns:
            algorithm_type -> str : name of the algorithm.
            path -> list : list of nodes, that are in the shortest path in order.
            cost -> int : cost of the shortest path.
            distance -> int : distance of the shortest path.
        """
        return self._dijkstra(graph, start, end)
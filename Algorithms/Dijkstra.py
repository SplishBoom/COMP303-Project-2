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
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0,
            "E": 0,
            "F": 0,
            "G": 0,
            "H": 0,
            "I": 0,
            "J": 0,
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
            iterations -> dict : dictionary which includes the number of iterations of each step of the algorithm.
        """
        # Initialize a min heap H and a distances array D.
        H = []
        D = {}
        self.iterations["A"] += 1

        # Insert the starting vertex into H and set its distance in D to 0.
        heappush(H, (0, start))
        D[start] = 0
        self.iterations["B"] += 1

        # While H is not empty:
        while H:
            self.iterations["C"] += 1
            # Extract the vertex v with the minimum distance from H.
            _, v = heappop(H)

            # For each neighbor w of v:
            for w in graph[v]:
                self.iterations["D"] += 1
                # Calculate the distance from the starting vertex to w through v.
                d = D[v] + graph[v][w]

                # If this distance is less than the current distance in D for w, update the distance in D for w.
                if w not in D or d < D[w]:
                    self.iterations["E"] += 1
                    D[w] = d

                    # If w is not in H, add it to H.
                    heappush(H, (d, w))
        
        # The distances array D now contains the shortest distances from the starting vertex to all other vertices.
        # By backtracking from the end vertex, we can find the shortest path.
        self.iterations["F"] += 1
        path = []
        cost = D[end]
        while end != start:
            self.iterations["G"] += 1
            path.append(end)
            for node in graph:
                self.iterations["H"] += 1
                if end in graph[node] and D[node] + graph[node][end] == D[end]:
                    self.iterations["I"] += 1
                    end = node
                    break
        self.iterations["J"] += 1
        path.append(start)
        path.reverse()

        # Return values.
        return (
            "Djikstra", 
            path, 
            cost,
            self.iterations
        )

    def solve(self, graph:dict, start:int, end:int) -> tuple:
        """
        Method, that runs the Dijkstra algorithm. @dijkstra().
        @params:
            @see @dijkstra().
        @returns:
            @see @dijkstra().
        """
        return self._dijkstra(graph, start, end)
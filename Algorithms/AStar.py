
class AStar:
    """
    Pseduo Code of A* Algorithm:
    1. Initialize a priority queue Q and a distances array D.
    2. Insert the starting vertex into Q and set its distance in D to 0.
    3. While Q is not empty:
        4. Extract the vertex v with the minimum distance + heuristic cost from Q.
        5. For each neighbor w of v:
            6. Calculate the distance from the starting vertex to w through v.
            7. If this distance is less than the current distance in D for w, update the distance in D for w.
            8. Calculate the heuristic cost from w to the end vertex.
            9. If w is not in Q, add it to Q with a priority equal to the distance + heuristic cost.
    10. The distances array D now contains the shortest distances from the starting vertex to all other vertices.
    11. By backtracking from the end vertex, we can find the shortest path.
    12. Return the shortest path and its cost.
    """

    def __init__(self) -> None:
        """
        Constructor of AStar class.
        """
        self.iterations = {chr(i):0 for i in range(65, 65+21)}

    def _a_star(self, graph:dict, start:int, end:int) -> tuple:
        """
        Method, that takes an dictionary which includes a directed and weighted graph. Than it finds the shortest path by using A* algorithm. With heuristic function of abs(i-j)
        @params:
            graph -> dict : dictionary which includes a directed and weighted graph in the format {node: {neighbour: weight, neighbour: weight, ...}, ...}.
            start -> int : start node.
            end -> int : end node.
        @returns:
            path -> list : list of nodes, that are in the shortest path in order.
            cost -> int : cost of the shortest path.
            iterations -> dict : dictionary which includes the number of iterations of each step of the algorithm.
        """

        heuristic = lambda i, j: abs(i-j)                                                                           ; self.iterations['U'] += 1
        # Manhattan distance -> abs(i-j)
        # Euclidean distance -> sqrt((i-j)**2)
        # Chebyshev distance -> max(abs(i-j), abs(i-j))
        # Octile distance -> max(abs(i-j), abs(i-j)) if i != j else (sqrt(2)-1)*max(abs(i-j), abs(i-j))
        # Minkowski distance -> (abs(i-j)**p)**(1/p)
        # Diagonal distance -> min(abs(i-j), abs(i-j))
        # Dijkstra's algorithm -> 0

        # Initialize a min heap H and a distances array D.
        H = []                                                                                                      ; self.iterations['A'] += 1
        D = {}                                                                                                      ; self.iterations['B'] += 1
        P = {}                                                                                                      ; self.iterations['C'] += 1

        # Insert the starting vertex into H and set its distance in D to 0.
        H.append((0+heuristic(start, end), start))                                                                  ; self.iterations['D'] += 1
        D[start] = 0                                                                                                ; self.iterations['E'] += 1
        P[start] = None                                                                                             ; self.iterations['F'] += 1

        # While H is not empty:
        while H:
            pass                                                                                                    ; self.iterations['G'] += 1
            # Extract the vertex v with the minimum distance from H.
            _, v = H.pop(0)                                                                                         ; self.iterations['H'] += 1

            # For each neighbor w of v:
            for w in graph[v]:
                pass                                                                                                ; self.iterations['I'] += 1
                # Calculate the distance from the starting vertex to w through v.
                d = D[v] + graph[v][w]                                                                              ; self.iterations['J'] += 1

                # If this distance is less than the current distance in D for w, update the distance in D for w.
                if w not in D or d < D[w]:
                    pass                                                                                            ; self.iterations['K'] += 1
                    D[w] = d                                                                                        ; self.iterations['L'] += 1

                    # If w is not in H, add it to H.
                    H.append((d+heuristic(w, end), w))                                                              ; self.iterations['M'] += 1
                    P[w] = v                                                                                        ; self.iterations['N'] += 1
        

        path = [end]                                                                                                ; self.iterations['O'] += 1
        cost = D[end]                                                                                               ; self.iterations['P'] += 1
        while path[-1] != start:
            pass                                                                                                    ; self.iterations['Q'] += 1
            path.append(P[path[-1]])                                                                                ; self.iterations['R'] += 1

        path.reverse()                                                                                              ; self.iterations['S'] += 1

        # Return values.
        pass                                                                                                        ; self.iterations['T'] += 1
        return (
            path, 
            cost,
            self.iterations
        )

    def solve(self, graph:dict, start:int, end:int) -> tuple:
        """
        Method, that runs the A* algorithm. @_a_star().
        @params:
            see @_a_star().
        @returns:
            see @_a_star().
        """
        return self._a_star(graph, start, end)
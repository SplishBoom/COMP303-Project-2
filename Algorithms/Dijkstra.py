"""
@Script, that implements Dijkstra's Algorithm using Min Heap.

@Student_1:     "Emir Cetin Memis"    |   @Student_2:     "Emircan Yaprak"        |   @Student_3:     "Tuana Selen Ozhazday"
@StudentID_1:   041901027             |   @StudentID_2:   041901009               |   @StudentID_3:   041901024
@Contact_1:     "memise@mef.edu.tr"   |   @Contact_2:     "yaprakem@mef.edu.tr"   |   @Contact_3:     "ozhazdayt@mef.edu.tr"

@Set&Rights: "MEF University"
@Instructor: "Prof. Dr. Muhittin Gokmen"
@Course:     "Analysis of Algorithms"
@Req:        "Project 2"

@Since: 4/1/2023
"""

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
        self.iterations = {chr(i):0 for i in range(65, 65+21)}

    def _dijkstra(self, graph:dict, start:int, end:int) -> tuple:
        """
        Method, that takes a graph and finds the shortest path by Dijkstra algorithm using min heap approach.
        @params:
            graph -> dict : dictionary which includes a directed and weighted graph in the format {node: {neighbour: weight, neighbour: weight, ...}, ...}.
            start -> int : start node.
            end -> int : end node.
        @returns:
            path -> list : list of nodes, that are in the shortest path in order.
            cost -> int : cost of the shortest path.
            iterations -> dict : dictionary which includes the number of iterations of each step of the algorithm.
        """
        # Initialize a min heap H and a distances array D.
        H = []                                                                                                      ; self.iterations['A'] += 1
        D = {}                                                                                                      ; self.iterations['B'] += 1

        # Insert the starting vertex into H and set its distance in D to 0.
        heappush(H, (0, start))                                                                                     ; self.iterations['C'] += 1
        D[start] = 0                                                                                                ; self.iterations['D'] += 1

        # While H is not empty:
        while H:
            pass                                                                                                    ; self.iterations['E'] += 1
            # Extract the vertex v with the minimum distance from H.
            _, v = heappop(H)                                                                                       ; self.iterations['F'] += 1

            # For each neighbor w of v:
            for w in graph[v]:
                pass                                                                                                ; self.iterations['G'] += 1
                # Calculate the distance from the starting vertex to w through v.
                d = D[v] + graph[v][w]                                                                              ; self.iterations['H'] += 1

                # If this distance is less than the current distance in D for w, update the distance in D for w.
                if w not in D or d < D[w]:
                    pass                                                                                            ; self.iterations['I'] += 1
                    D[w] = d                                                                                        ; self.iterations['J'] += 1

                    # If w is not in H, add it to H.
                    heappush(H, (d, w))                                                                             ; self.iterations['K'] += 1
        
        # The distances array D now contains the shortest distances from the starting vertex to all other vertices.
        # By backtracking from the end vertex, we can find the shortest path.
        path = []                                                                                                   ; self.iterations['L'] += 1
        cost = D[end]                                                                                               ; self.iterations['M'] += 1
        while end != start:
            pass                                                                                                    ; self.iterations['N'] += 1
            path.append(end)                                                                                        ; self.iterations['O'] += 1
            for node in graph:
                pass                                                                                                ; self.iterations['P'] += 1
                if end in graph[node] and D[node] + graph[node][end] == D[end]:
                    pass                                                                                            ; self.iterations['Q'] += 1
                    end = node                                                                                      ; self.iterations['R'] += 1
                    break
        path.append(start)                                                                                          ; self.iterations['S'] += 1
        path.reverse()                                                                                              ; self.iterations['T'] += 1

        # Return values.
        pass                                                                                                        ; self.iterations['U'] += 1
        return (
            path, 
            cost,
            self.iterations
        )

    def solve(self, graph:dict, start:int, end:int) -> tuple:
        """
        Method, that runs the Dijkstra algorithm. @_dijkstra().
        @params:
            @see @_dijkstra().
        @returns:
            @see @_dijkstra().
        """
        return self._dijkstra(graph, start, end)
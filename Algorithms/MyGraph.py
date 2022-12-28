
class MyGraph :

    def __init__(self, number_of_nodes) :

        self.n = number_of_nodes
        
        self.initialize_graph()

    def __str__(self):
        
        string = "--- The MyGraph Object ---\n"

        odd_numbers = [i for i in range(1, self.n+1) if i % 2 == 1]
        even_numbers = [i for i in range(1, self.n+1) if i % 2 == 0]

        string1 = "---".join([str(i) for i in odd_numbers])
        string2 = "---".join([str(i) for i in even_numbers])
        
        return string + "\n" + string1 + "\n" + string2

    def initialize_graph(self) :

        self._create_graph()

        while not self._validate_graph() :
            self._create_graph()
                
    def _create_graph(self) :

        graph = {}

        for i in range(1, self.n+1):
            graph[i] = {}
            for j in range(1, self.n+1):
                if abs(i-j) <= 3 and i != j:
                    graph[i][j] = i + j
        
        self.graph = graph

    def _validate_graph(self) :

        # check that the graph has the correct number of nodes
        if len(self.graph) != self.n:
            return False

        # check that the graph has the correct edges
        for i in range(1, self.n+1):
            for j in range(1, self.n+1):
                if abs(i-j) <= 3 and i != j:
                    if j not in self.graph[i]:
                        return False
                else:
                    if j in self.graph[i]:
                        return False
        return True
"""
This module contains the MyGraph class, that creates a dictionaryt graph for the specified format from handout.
"""

class MyGraph :
    """
    Class, that creates a dictionaryt graph for the specified format from handout.
    """

    def __init__(self, number_of_nodes) -> None:
        """
        Constructor for the MyGraph class.
        @params:
            number_of_nodes: int
        """

        self.n = number_of_nodes
        
    def __str__(self) -> str:
        """
        Returns a string representation of the graph.
        @returns:
            string: str
        """
        
        string = "\n--- The MyGraph Object ---"

        odd_numbers = [i for i in range(1, self.n+1) if i % 2 == 1]
        even_numbers = [i for i in range(1, self.n+1) if i % 2 == 0]

        string1 = "---".join([str(i) for i in odd_numbers])
        string2 = "---".join([str(i) for i in even_numbers])
        
        return string + "\n" + string1 + "\n" + string2

    def generate_graph(self) -> None:
        """
        Generates a graph for the specified format from handout.
        """

        self._create_graph()

        while not self._validate_graph() :
            self._create_graph()
                
    def _create_graph(self) -> None:
        """
        Creates a graph for the specified format from handout.
        @format :
        {
            node1:{neighbor1:cost11, neighbor2:cost12, ...},
            node2:{neighbor1:cost21, neighbor2:cost22, ...},
        }
        """

        graph = {}

        for i in range(1, self.n+1):
            graph[i] = {}
            for j in range(1, self.n+1):
                if abs(i-j) <= 3 and i != j:
                    graph[i][j] = i + j

        self.vertice_count = len(graph)
        self.edge_count = sum([len(graph[i]) for i in graph])
        
        self.graph = graph

    def _validate_graph(self) -> bool:
        """
        Validates the graph for the specified format from handout.
        @returns:
            bool: bool
        """
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
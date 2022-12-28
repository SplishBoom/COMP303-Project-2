from Utilities import safeStart, safeStop, visualize
from Algorithms.MyGraph import MyGraph

if __name__ == "__main__" :
    safeStart()
    n = 10
    path_of_node_identities = [1,2,3,4,5,6,7,8,9]
    
    visualize(n, "Djikstra", path_of_node_identities)
    
    objct = MyGraph(n)
    print(objct)
    print(objct.graph)

    safeStop()
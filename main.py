from Utilities import safeStart, safeStop, visualize

if __name__ == "__main__" :
    safeStart()
    
    path_of_node_identities = [1,2,3,4,5,6,7,8,9]
    
    visualize(10, "Djikstra", path_of_node_identities)
    
    safeStop()
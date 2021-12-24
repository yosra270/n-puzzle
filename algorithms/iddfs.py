import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from utils.n_puzzle_utils import NPuzzle


def iddfs(initial_state,puzzle_dimension, max_depth):
    final_state = []
    for i in range(0,puzzle_dimension**2):
        final_state.append(i)
    
    frontier = list([NPuzzle(state=initial_state,puzzle_dimension=puzzle_dimension)]) 
    
    explored = []
    
    while frontier:
        node = frontier.pop()
        
        explored.append(node.state)
        
        #display_state(node)
        
        if node.state == final_state: 
            final_node = node
            return [explored, final_node,frontier]
        
        if node.depth == max_depth:
            continue
        
        children_nodes = list(reversed(node.children()))
        for child_node in children_nodes:
            if (child_node.state not in explored) and (child_node not in frontier):
                frontier.append(child_node)
        
    return [explored,None,frontier]
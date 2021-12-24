import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from utils.n_puzzle_utils import NPuzzle

def a_star(initial_state,puzzle_dimension, heuristic):
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

        children_nodes = node.children()
        for child_node in children_nodes:
            if(child_node.state in explored):
                continue
            child_node.f = child_node.total_cost(heuristic)
            if child_node in frontier:
                same_state_node_index = frontier.index(child_node)
                if frontier[same_state_node_index].depth <= child_node.depth:
                    continue
                frontier.pop(same_state_node_index)
            frontier.append(child_node)
                
        frontier.sort(key = lambda x:x.f,reverse=True)
    return None
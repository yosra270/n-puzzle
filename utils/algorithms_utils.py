import time
from utils.n_puzzle_utils import display_performance 

# heuristics
def nbre_of_misplaced_tiles(node):
    correct_state = [tile for tile in range(0,node.puzzle_dimension**2)]
    return sum(1 for i in range(0,node.puzzle_dimension**2) if node.state[i]!=0 and node.state[i]!=correct_state[i])

def distance_from_final_position(node): # returns the sum of tiles distances from their final positions
    correct_state = [tile for tile in range(0,node.puzzle_dimension**2)]
    return sum(abs(correct_state.index(node.state[i]) - i ) for i in range(0,node.puzzle_dimension**2) if node.state[i]!=0)


# executing algorithms
def execute_non_iterative_algorithm(algorithm,initial_state,puzzle_dimension, heuristic = None):
    start_time = time.perf_counter()
    results = algorithm(initial_state,puzzle_dimension) if heuristic is None else algorithm(initial_state,puzzle_dimension,heuristic)
    end_time = time.perf_counter()
    if results is None:
        return None
    explored, final_node, frontier = results[0],results[1], results[2]
    nbre_visited_nodes = len(explored)
    display_performance(initial_state,final_node,nbre_visited_nodes, start_time, end_time)
    return explored,frontier



def execute_iterative_algorithm(algorithm,initial_state,puzzle_dimension, heuristic = None):
    final_node = None
    nbre_visited_nodes = 0
    max_depth = 0
    start_time = time.perf_counter()
    while (final_node is None):
        results = algorithm(initial_state,puzzle_dimension,max_depth) if heuristic is None else algorithm(initial_state,puzzle_dimension,heuristic,max_depth)
        explored, final_node = results[0],results[1]
        nbre_visited_nodes += len(explored)
        max_depth += 1    
    end_time = time.perf_counter()
    if final_node is None:
        return None
    display_performance(initial_state,final_node,nbre_visited_nodes, start_time, end_time)
    frontier = results[2]
    return explored,frontier

def display_complexities(explored, frontier):
    print("Time complexity : ",len(explored))
    print("Space complexity : ",len(explored)+len(frontier))
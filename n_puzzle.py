from algorithms.iddfs import iddfs
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.a_star import a_star
from algorithms.ida_star import ida_star
from utils.algorithms_utils import execute_non_iterative_algorithm, execute_iterative_algorithm, display_complexities, nbre_of_misplaced_tiles, distance_from_final_position

def main():
    # 8-puzzle initial state example : 1 0 2 3 4 5 6 7 8
    print("\n\n**************** Solving n-puzzle using search algorithms *******************\n")
    
    puzzle_dimension = int(input("What is the dimension of the puzzle (exple : 3, 4 , ...) : "))
    
    initial_sequence = input("\nWhat is the initial state of the puzzle ? : ")
    initial_state = list(map(int, initial_sequence.split(" ")))
    
    print("\nWhat kind of search algorithms would you like to use ? : ")
    print("\n\t1/Uninformed search algorithms")
    print("\t2/Informed search algorithms")
    algorithm_type_choice = int(input("_ : "))
    if algorithm_type_choice == 1 :        
        print("\n\t\t1/ Breadth first search")
        print("\t\t2/ Depth first search")
        print("\t\t3/ Iterative deepening dfs")
        print("\t\t4/ Compare all algorithms performance")
        
        algorithm_choice = int(input("\n_: "))
        
        if algorithm_choice == 1:
            execute_non_iterative_algorithm(bfs,initial_state,puzzle_dimension)
            
        elif algorithm_choice == 2:
            execute_non_iterative_algorithm(dfs,initial_state,puzzle_dimension)
            
        elif algorithm_choice == 3:
            execute_iterative_algorithm(iddfs, initial_state,puzzle_dimension)
            
        elif algorithm_choice == 4:  
            print("\n**********BFS********** :")
            bfs_explored, bfs_frontier = execute_non_iterative_algorithm(bfs,initial_state,puzzle_dimension)
            print("\n**********DFS********** :")
            dfs_explored, dfs_frontier = execute_non_iterative_algorithm(dfs,initial_state,puzzle_dimension)
            print("\n**********Iterative deepening DFS********** :")
            iddfs_explored, iddfs_frontier = execute_iterative_algorithm(iddfs,initial_state,puzzle_dimension)
            
            print("#======================================================================================#")
            print("\n\n\tPerformance comparison :\nTime complexity (nbre of explored nodes)\nSpace complexity (maximum nbre of saved nodes in memory = frontier + explored)\n\n")
            print("For BFS :")
            display_complexities(bfs_explored, bfs_frontier)
            
            print("\nFor BFS :")
            display_complexities(dfs_explored, dfs_frontier)
            
            print("\nFor Iterative deepening DFS :")
            display_complexities(iddfs_explored, iddfs_frontier)
        
    elif algorithm_type_choice == 2:
        print("\n\t\t1/ A*")
        print("\t\t2/ Iterative deepening A*")
        print("\t\t3/ Compare all algorithms performance")
        
        algorithm_choice = int(input("\n_: "))
        
        print("PLease choose heuristic ? :")
        print("\n\t\t\t1/Nbre of misplaced tiles")
        print("\t\t\t2/Sum of misplaced tiles manhattan distances from their final positions")
        heuristic_choice = int(input("\n_ : "))
        if heuristic_choice == 1:
            heuristic = nbre_of_misplaced_tiles
        else:
            heuristic = distance_from_final_position
            
        if algorithm_choice == 1:
            execute_non_iterative_algorithm(a_star,initial_state,puzzle_dimension, heuristic)
            
        elif algorithm_choice == 2:
            execute_iterative_algorithm(ida_star, initial_state,puzzle_dimension, heuristic)
            
        elif algorithm_choice == 3:  
            print("\n**********A* **********:")
            a_star_explored, a_star_frontier = execute_non_iterative_algorithm(a_star,initial_state,puzzle_dimension, heuristic)
            print("\n**********Iterative deepening A* **********:")
            ida_star_explored, ida_star_frontier = execute_iterative_algorithm(ida_star, initial_state,puzzle_dimension, heuristic)
            
            print("#======================================================================================#")
            print("\n\n\tPerformance comparison :\nTime complexity (nbre of explored nodes)\nSpace complexity (maximum nbre of saved nodes in memory = frontier + explored)\n\n")
            print("For A* :")
            display_complexities(a_star_explored, a_star_frontier)
            
            print("\nFor Iterative deepening A* :")
            display_complexities(ida_star_explored, ida_star_frontier)       
         


if __name__ == '__main__':
    main()
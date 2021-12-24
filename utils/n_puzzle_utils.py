class NPuzzle:
    def __init__(self, state,parent = None, depth = 0,puzzle_dimension = 3):
        self.state = state
        self.depth = depth
        self.parent = parent
        self.puzzle_dimension = puzzle_dimension
        self.f = 0
    
    def children(self):    
        possibles_children = []
        possibles_children.append(NPuzzle(state=swap(self.state, 0, 1,self.puzzle_dimension),parent=self, depth=self.depth + 1,puzzle_dimension=self.puzzle_dimension)) #haut
        possibles_children.append(NPuzzle(state=swap(self.state, 0, -1,self.puzzle_dimension),parent=self, depth=self.depth + 1,puzzle_dimension=self.puzzle_dimension)) #bas
        possibles_children.append(NPuzzle(state=swap(self.state, -1, 0,self.puzzle_dimension),parent=self, depth=self.depth + 1,puzzle_dimension=self.puzzle_dimension)) #gauche
        possibles_children.append(NPuzzle(state=swap(self.state, 1, 0,self.puzzle_dimension),parent=self, depth=self.depth + 1,puzzle_dimension=self.puzzle_dimension)) #droite
       
        children = []
        for node in possibles_children:
            if (node.state != None):
                children.append(node)
        return children
    
    
    def cost_so_far(self):
        return self.depth
    def cost_till_goal(self, heuristic): # nbre of misplaced tiles or sum of tiles Manhattan distances from their final positions
        return heuristic(self)
    def total_cost(self, heuristic):
        return self.cost_so_far() + self.cost_till_goal(heuristic)
    
    def __eq__(self, other):
        return self.state == other.state



# shuffle the tiles
def swap(state, ei, ej, puzzle_dimension): 
    new_state = state.copy()

    index = new_state.index(0)
    index_to_swap = index + ei*1 + ej*(-puzzle_dimension)
    
    if index_to_swap in range(0,puzzle_dimension**2) and (( ej == 0 and index_to_swap//puzzle_dimension == index//puzzle_dimension) or(( ei == 0 and index_to_swap%puzzle_dimension == index%puzzle_dimension))):
       temp = new_state[index] 
       new_state[index] = new_state[index_to_swap] 
       new_state[index_to_swap] = temp      
       return new_state
   
    return None

# display functions
def display_state(node):  
    for i in range(0,node.puzzle_dimension**2,node.puzzle_dimension):
        print('\t'.join(str(e) for e in node.state[i:i+node.puzzle_dimension]))
    print("            ")


def display_performance(initial_state,final_node,nbre_visited_noted, start_time, end_time):  
    node = final_node
    solution_path = [final_node]
    while node.state != initial_state:
        node = node.parent
        solution_path.append(node)
        
    print("The path of the solution is :")
    for node in reversed(solution_path):
        display_state(node)
    print("Number of total visited nodes is : ", nbre_visited_noted)
    print("Depth of the solution is : ", final_node.depth)
    print("Time elapsed: " , (end_time - start_time)*(10**6), " ns")
    print("            ")
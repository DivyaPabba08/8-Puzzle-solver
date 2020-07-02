
from __future__ import division
from __future__ import print_function

"""
import sys
"""
import math
import time
#import queue as Q
import heapq 

#### SKELETON CODE ####
## The Class that Represents the Puzzle
class PuzzleState(object):
    """
        The PuzzleState stores a board configuration and implements
        movement instructions to generate valid children.
    """
    def __init__(self, config, n, parent=None, action="Initial", cost=0):
        """
        :param config->List : Represents the n*n board, for e.g. [0,1,2,3,4,5,6,7,8] represents the goal state.
        :param n->int : Size of the board
        :param parent->PuzzleState
        :param action->string
        :param cost->int
        """
        if n*n != len(config) or n < 2:
            raise Exception("The length of config is not correct!")
        if set(config) != set(range(n*n)):
            raise Exception("Config contains invalid/duplicate entries : ", config)

        self.n        = n
        self.cost     = cost
        self.parent   = parent
        self.action   = action
        self.config   = config
        self.children = []

        # Get the index and (row, col) of empty block
        self.blank_index = self.config.index(0)

    def display(self):
        """ Display this Puzzle state as a n*n board """
        for i in range(self.n):
            print(self.config[3*i : 3*(i+1)])

    def move_up(self):
        """ 
        Moves the blank tile one row up.
        :return a PuzzleState with the new configuration
        """
        i= self.config.index(0)
        if(i>2):
            child_up= PuzzleState(self.config,self.n)
            child_up.n=self.n
            child_up.parent=self
            child_up.action='up'
            child_up.cost=1
            child_up.config=self.config[:]
            child_up.config[i-3] = child_up.config[i]
            child_up.config[i]=self.config[i-3]
            return child_up 
        else:
             return None   
      
    def move_down(self):
        """
        Moves the blank tile one row down.
        :return a PuzzleState with the new configuration
        """
        i= self.config.index(0)
        if(i<6):
            child_down= PuzzleState(self.config,self.n)
            child_down.n=self.n
            child_down.parent=self
            child_down.action='down'
            child_down.cost=1
            child_down.config=self.config[:]
            child_down.config[i] = child_down.config[i+3]
            child_down.config[i+3]=self.config[i]
            return child_down 
        else:
            return None
      
    def move_left(self):
        """
        Moves the blank tile one column to the left.
        :return a PuzzleState with the new configuration
        """
        i= self.config.index(0)
        if(i != 0 and  i != 3 and  i != 6):
            child_left= PuzzleState(self.config,self.n)
            child_left.n=self.n
            child_left.parent=self
            child_left.action='left'
            child_left.cost=1
            child_left.config=self.config[:]
            child_left.config[i] = child_left.config[i-1]
            child_left.config[i-1]=self.config[i]
            return child_left
        else:
            return None


    def move_right(self):
        """
        Moves the blank tile one column to the right.
        :return a PuzzleState with the new configuration
        """
        i= self.config.index(0)
        if(i != 2 and  i != 5 and  i != 8):
            child_right= PuzzleState(self.config,self.n)
            child_right.n=self.n
            child_right.parent=self
            child_right.action='right'
            child_right.cost=1
            child_right.config=self.config[:]
            child_right.config[i] = child_right.config[i+1]
            child_right.config[i+1]=self.config[i]
            return child_right
        else:
            return None
        
    def expand(self):
        """ Generate the child nodes of this node """
        
        # Node has already been expanded
        if len(self.children) != 0:
            return self.children
        
        # Add child nodes in order of UDLR
        children = [
            self.move_up(),
            self.move_down(),
            self.move_left(),
            self.move_right()]

        # Compose self.children of all non-None children states
        self.children = [state for state in children if state is not None]
        return self.children

# Function that Writes to output.txt

### Students need to change the method to have the corresponding parameters
def writeOutput(puzzle_state):
    ### Student Code Goes here
    final_path=[]
    final_path.append(puzzle_state.action)
    parent_node=puzzle_state.parent
    while parent_node is not None:
        final_path.append(parent_node.action)
        parent_node=parent_node.parent
        final_path = list(reversed(final_path))
    print(final_path)
    print("cost_of_path:")
    print(len(final_path))
    print("nodes_expanded:")
    print("search_depth:")
    print("max_search_depth:")

def bfs_search(initial_state):
    """BFS search"""
    ### STUDENT CODE GOES HERE ###
    pass

def dfs_search(initial_state):
    """DFS search"""
    ### STUDENT CODE GOES HERE ###
    pass

def A_star_search(initial_state):
    """A * search"""
    ### STUDENT CODE GOES HERE ###
    #check_correct_input(initial_state.config)
    #check_solvable(initial_state.config)
    frontier_list=[]
    if(test_goal(initial_state)):
        writeOutput(initial_state)
        return "Success"
    else:
        frontier = []
        heapq.heappush(frontier, (calculate_total_cost(initial_state),(initial_state.action,(time.time(),initial_state))))
        frontier_list.append(initial_state)
        explored = set()
        #print("befoe while loop added element is",initial_state.config)
        
    while len(frontier_list)>0:
        current_state = frontier.pop()[1][1][1]
        frontier_list.remove(current_state)
        explored.add(current_state)
        print(len(explored))
        #print("hello")
        #print("popped element is",current_state.config)
        if(test_goal(current_state)):
            writeOutput(current_state)
            return "Success"
        
        for neighbour in current_state.expand():
           #print(neighbour.config) 
           if(neighbour not in frontier_list or explored):
                #print("neighbours added are",neighbour.config) 
                #print(len(frontier))
                heapq.heappush(frontier,(calculate_total_cost(neighbour),(neighbour.action,(time.time(),neighbour))))
                frontier_list.append(neighbour)
               
    return "Failure"                      
   
def calculate_total_cost(state):
    """calculate the total estimated cost of a state"""
    ### STUDENT CODE GOES HERE ###
    path=[]
    total_manhattan_distance=0
    path.append(state)
    parent_node=state.parent
    while parent_node is not None:
        path.append(parent_node)
        parent_node=parent_node.parent
        path = list(reversed(path))
    cost_spent=len(path)-1
    for i in range(len(state.config)):
         x= calculate_manhattan_dist(i,state.config[i], 3)
         total_manhattan_distance = x+ total_manhattan_distance
    return  total_manhattan_distance+cost_spent   

def calculate_manhattan_dist(idx, value, n):
    """calculate the manhattan distance of a tile"""
    ### STUDENT CODE GOES HERE ###
    goal_state_sequence= [0,1,2,3,4,5,6,7,8]
    actual_idx= goal_state_sequence.index(value)
    return math.floor(abs(actual_idx%3 - idx%3)) + math.floor(abs(actual_idx/3 - idx/3))

def test_goal(puzzle_state):
    """test the state is the goal state or not"""
    ### STUDENT CODE GOES HERE ###
    print("entered test goal")
    goal_state_sequence= [0,1,2,3,4,5,6,7,8]
    if(puzzle_state.config==goal_state_sequence):
        return True
    else:
        return False
    
def check_correct_input(l):
    for i in range(9):
        counter_appear = 0
        f = l[i]
        for j in range(9):
            if f == l[j]:
                counter_appear += 1
        if counter_appear >= 2:
            print("invalid input, same number entered 2 times")
            exit(0)    
            
def check_solvable(g):
    counter_states = 0
    for i in range(9):
        if not g[i] == 0:
            check_elem = g[i]
            for x in range(i + 1, 9):
                if check_elem < g[x] or g[x] == 0:
                    continue
                else:
                    counter_states += 1
    if counter_states % 2 == 0:
        print("The puzzle is solvable, generating path")
    else:
        print("The puzzle is insolvable, still creating nodes")            

# Main Function that reads in Input and Runs corresponding Algorithm
def main():
    search_mode = "ast"
    begin_state = 3,1,2,0,4,5,6,7,8
    begin_state = list(map(int, begin_state))
    board_size  = int(math.sqrt(len(begin_state)))
    hard_state  = PuzzleState(begin_state, board_size)
    start_time  = time.time()
    
    if   search_mode == "bfs": bfs_search(hard_state)
    elif search_mode == "dfs": dfs_search(hard_state)
    elif search_mode == "ast": A_star_search(hard_state)
    else: 
        print("Enter valid command arguments !")
        
    end_time = time.time()
    print("Program completed in %.3f second(s)"%(end_time-start_time))

if __name__ == '__main__':
    main()
    




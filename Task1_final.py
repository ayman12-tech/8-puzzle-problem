import copy
from queue import Queue
from collections import deque # for stack
#from queue import Queue
class states:
    #goal_state=[0,1,2,3,4,5,6,7,8]
    def __init__(self, representation):
        self.representation = representation

    def slide_left(self):
        new_state = states(copy.deepcopy(self.representation))
        empty_space = self.representation.index(0)
        if empty_space == 0 or empty_space == 3 or empty_space == 6:
            return new_state
        else:
            new_state.representation[empty_space - 1], new_state.representation[empty_space] = new_state.representation[empty_space], new_state.representation[empty_space - 1]
            return new_state

    def slide_right(self):
        new_state = states(copy.deepcopy(self.representation))
        empty_space = self.representation.index(0)
        if empty_space == 2 or empty_space == 5 or empty_space == 8:
            return new_state
        else:
            new_state.representation[empty_space+1], new_state.representation[empty_space] = new_state.representation[empty_space], new_state.representation[empty_space+1]
            return new_state

    def slide_up(self):
        new_state = states(copy.deepcopy(self.representation))
        empty_space = self.representation.index(0)
        if empty_space == 0 or empty_space == 1 or empty_space == 2:
            return new_state
        else:
            new_state.representation[empty_space-3], new_state.representation[empty_space] = new_state.representation[empty_space], new_state.representation[empty_space-3]
            return new_state

    def slide_down(self):
        new_state = states(copy.deepcopy(self.representation))
        empty_space = self.representation.index(0)
        if empty_space == 6 or empty_space == 7 or empty_space == 8:
            return new_state
        else:
            new_state.representation[empty_space+3], new_state.representation[empty_space] = new_state.representation[empty_space], new_state.representation[empty_space+3]
            return new_state

    def print_board(self):
        for i in range(len(self.representation)):
            if i%3 ==0:
                print('\n', end=' ')
            print(self.representation[i], end=' ')
        print('\n\n\n')

    def applyOperators(self):
        """
        Required method for use with the Search class.
        Returns a list of possible successors to the current
        state, some of which may be illegal.
        """
        return [self.slide_left(), self.slide_right(), self.slide_up(), self.slide_down()]

def BFS(start_state, goal_state):

    queue = Queue() #using built-in queue
    queue.put(start_state) #pushing the start state into queue
    while queue:
        path = queue.get() #dequeue node and put into the path
        entity = states(path) #make the object of class states
        leaves = entity.applyOperators() #generating the child

        if path == goal_state: #checkin' if it is the goal node
            return path

        for child in leaves:
            if (child.representation != path):
                queue.put(child.representation) #updating

# def DFS(start_state, goal_state):
#
#     stack = deque()
#     stack.append(start_state)
#
#     while stack:
#         path = stack.pop()
#         entity = states(path)
#         leaves = entity.applyOperators()
#
#         if path == goal_state:
#             return path
#
#         for child in leaves:
#             if child.representation != path:
#                 stack.append(child.representation)

start_state = [2,8,3,1,6,4,7,0,5]

goal_state = [0,1,2,3,4,5,6,7,8] #this goal state takes time in execution
Final=BFS(start_state, goal_state)
print(Final)
# obj=states(Final)
# obj.print_board()






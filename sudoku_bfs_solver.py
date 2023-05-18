from queue import Queue
from sudoku_problem_class import Problem
import time

class Node:

    def __init__(self, state, action=None):
        self.state = state
        self.action = action

    # Use each action to create a new board state
    def expand(self, problem):
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    # Return node with new board state
    def child_node(self, problem, action):
        next = problem.result(self.state, action)
        return Node(next, action)

def BFS(problem):
    # Create initial node of problem tree holding original board
    node = Node(problem.initial)
    # Check if original board is correct and immediately return if valid
    if problem.check_legal(node.state):
        return node

    frontier = Queue()
    frontier.put(node)

    # Loop until all nodes are explored or solution found
    while (frontier.qsize() != 0):

        node = frontier.get()
        for child in node.expand(problem):
            if problem.check_legal(child.state):
                return child

            frontier.put(child)

    return None

def BFS_solve(board):
    print ("\nSolving with BFS...")

    start_time = time.time()

    problem = Problem(board)
    solution = BFS(problem)
    elapsed_time = time.time() - start_time

    if solution:
        for row in solution.state:
            print (row)
    else:
        print ("No possible solutions")

    print ("\nElapsed time: " + str(elapsed_time) + " seconds")

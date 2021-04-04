# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from collections import deque

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """Search the deepest nodes in the search tree first."""
    directions = []
    start_state = problem.getStartState()
    visited = {}

    def dfs_recursive(directions, state):
        # stop if the goal is reached
        if problem.isGoalState(state): return True
        # mark that we have visted this place
        visited[state] = True
        # work with child nodes
        for s in problem.getSuccessors(state):
            next_state, direction, cost = s
            if next_state in visited: continue
            # remember the direction
            directions.append(direction)
            # recursive call
            res = dfs_recursive(directions, next_state)
            # good way, end all recursive calls
            if res: return res
            # go back, delete last direction
            directions.pop()
        return False

    dfs_recursive(directions, start_state)
    return directions

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    start_state = problem.getStartState()
    # q hold elements having this form: ( state, directions_array )
    # for example: ( (1,2) , [ 'West', 'South',... ] )
    q = deque((s[0], [s[1]]) for s in problem.getSuccessors(start_state))
    visited = {}
    visited[start_state] = True

    while len(q) > 0:
        state, directions = q.popleft()
        if problem.isGoalState(state):
            # exit if the goal is reached
            return directions
        # find and enqueue child nodes
        for s in problem.getSuccessors(state):
            next_state, direction, cost = s
            if next_state not in visited:
                visited[next_state] = True
                new_directions = [d for d in directions] # copy array
                new_directions.append(direction)
                q.append((next_state, new_directions))
    
    # if there is no solution
    return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

import math
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    x, y = state
    gx, gy = problem.goal
    return math.sqrt((x - gx) ** 2 + (y - gy) ** 2)

class AstarNode:
    def __init__(self, state, directions):
        self.state = state
        self.g = 0
        self.h = 0
        self.f = 0
        self.directions = [d for d in directions] # copy array

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    start_state = problem.getStartState()
    visited = {}
    visited[start_state] = True
    start_node = AstarNode(start_state, [])
    open_list = [start_node]

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0

        # remove last nodes
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        open_list.pop(current_index)

        # the goal state is reached
        if problem.isGoalState(current_node.state):
            return current_node.directions

        # work with child nodes
        for s in problem.getSuccessors(current_node.state):
            new_state, direction, cost = s

            # ignore if we've already visited this node
            if new_state in visited: continue

            new_node = AstarNode(new_state, current_node.directions)
            new_node.directions.append(direction)
            new_node.g = current_node.g + cost
            new_node.h = nullHeuristic(new_state, problem)
            new_node.f = new_node.g + new_node.h

            for open_node in open_list:
                if new_node.g > open_node.g:
                    continue

            visited[new_state] = True
            open_list.append(new_node)

    # if there is no solution
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

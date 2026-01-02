import heapq
import time

class Node:
    __slots__ = ['state', 'g', 'h', 'f']
    def __init__(self, state, g=0, h=0):
        self.state = state
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        # Tie-breaking: h lower --> more deep
        return self.f < other.f if self.f != other.f else self.h < other.h

def astar_search(problem, heuristic_fn):
    start_time = time.perf_counter()
    start_node = Node(problem.initial_state(), 0, heuristic_fn(problem.initial_state(), problem))
    
    frontier = [start_node]
    frontier_states = {start_node.state: start_node.f}
    explored = set()
    nodes_expanded = 0

    while frontier:
        current = heapq.heappop(frontier)
        
        if problem.is_goal(current.state):
            return {
                "solution": current.state, 
                "time": time.perf_counter() - start_time, 
                "nodes_expanded": nodes_expanded, 
                "max_memory": len(frontier) + len(explored)
            }

        explored.add(current.state)
        nodes_expanded += 1

        for action in problem.get_actions(current.state):
            child_state = problem.result(current.state, action)
            
            if child_state in explored:
                continue
            
            g_cost = current.g + 1
            h_cost = heuristic_fn(child_state, problem)
            child_node = Node(child_state, g_cost, h_cost)

            # A* logic --> add if new path is better
            if child_state not in frontier_states or child_node.f < frontier_states[child_state]:
                heapq.heappush(frontier, child_node)
                frontier_states[child_state] = child_node.f
                
    return None

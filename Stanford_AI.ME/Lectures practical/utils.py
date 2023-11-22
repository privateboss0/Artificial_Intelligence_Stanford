import heapq
# Data structure for supporting uniform cost search.
class PriorityQueue:
    def __init__(self):
        self.DONE = -100000
        self.heap = []
        self.priorities = {}  # Map from state to priority

    # Insert `state` into the heap with priority `newPriority` if
    # `state` isn't in the heap or `newPriority` is smaller than the existing
    # priority.
    # Return whether the priority queue was updated.
    def update(self, state, newPriority):
        oldPriority = self.priorities.get(state)
        if oldPriority is None or newPriority < oldPriority:
            self.priorities[state] = newPriority
            heapq.heappush(self.heap, (newPriority, state))
            return True
        return False

    # Returns (state with minimum priority, priority)
    # or (None, None) if the priority queue is empty.
    def removeMin(self):
        while len(self.heap) > 0:
            priority, state = heapq.heappop(self.heap)
            if self.priorities[state] == self.DONE:
                continue  # Outdated priority, skip
            self.priorities[state] = self.DONE
            return state, priority
        return None, None

# Performs a uniform cost search on the given problem.
def uniformCostSearch(problem):
    frontier = PriorityQueue()
    frontier.update(problem.startState(), 0)
    explored = set()

    while frontier:
        state, cost = frontier.removeMin()
        if problem.isEnd(state):
            return cost, []

        if state not in explored:
            explored.add(state)
            for action, newState, newCost in problem.succAndCost(state):
                frontier.update(newState, cost + newCost)

    return None, None

# Performs dynamic programming to solve the given problem.
def dynamicProgramming(problem):
    cache = {}  # state -> futureCost(state)

    def futureCost(state):
        # Base case
        if problem.isEnd(state):
            return 0

        # Check if the future cost of the state is already in the cache
        if state in cache:
            return cache[state]

        # Calculate the future cost of the state
        result = min(
            cost + futureCost(newState)
            for action, newState, cost in problem.succAndCost(state)
        )

        # Add the future cost of the state to the cache
        cache[state] = result

        return result

    return futureCost(problem.startState()), []
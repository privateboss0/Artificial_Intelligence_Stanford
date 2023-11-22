import sys
sys.setrecursionlimit(15000)
class TransportationProblem(object):
    def __init__(self, N):
        # N = number of blocks.
        self.N = N

    def startState(self):
        return 1

    def isEnd(self, state):
        return state == self.N

    def succAndCost(self, state):
        # return list of (action, newState, cost) triples
        result = []
        if state + 1 <= self.N:
            result.append(('walk', state + 1, 1))
        if state * 2 <= self.N:
            result.append(('Street_Car', state * 2, 2))
        return result


def printSolution(solution):
    totalCost, history = solution
    print('totalCost: {}'.format(totalCost))
    for item in history:
        print(item)


def backtrackingSearch(problem):
    # Best solution found so far (dictionary because of python scoping technicality)
    best = {
        'cost': float('+inf'),
        'history': None
    }

    def recurse(state, history, totalCost):
        # At state, having undergone history, accumulated
        # totalCost.
        # Explore the rest of the subtree under state.
        if problem.isEnd(state):
            # Update the best solution so far
            if totalCost < best['cost']:
                best['cost'] = totalCost
                best['history'] = history
            return

        # Recurse on children
        for action, newState, cost in problem.succAndCost(state):
            recurse(newState, history + [(action, newState, cost)], totalCost + cost)

    recurse(problem.startState(), history=[], totalCost=0)

    return best['cost'], best['history']


# Create a TransportationProblem object.
problem = TransportationProblem(N=100)

# Call the backtrackingSearch() function with the TransportationProblem object.
totalCost, history = backtrackingSearch(problem)

# Print the solution.
printSolution((totalCost, history))
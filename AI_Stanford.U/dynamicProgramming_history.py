import sys
sys.setrecursionlimit(15000)

class TransportationProblem(object):
  def __init__(self, N, weights):
    # N = number of blocks.
    # weights = weights of different actions
    self.N = N
    self.weights = weights

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
      result.append(('Street_Car', state * 2, 5))
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

def dynamicProgramming(problem):
    cache = {} # state -> futureCost(state), action, newState, cost
    def futureCost(state):
        # Base case
        if problem.isEnd(state):
            return 0
        if state in cache: # Exponential savings
            return cache[state][0]
        # Actually doing work
        result = min((cost+futureCost(newState), action, newState, cost) \
                for action, newState, cost in problem.succAndCost(state))
        cache[state] = result
        return result[0]

    state = problem.startState()
    totalCost = futureCost(state)
  # Recover history
    history = []
    while not problem.isEnd(state):
        _, action, newState, cost = cache[state]
        history.append((action, newState, cost))
        state = newState

    return (futureCost(problem.startState()), history)


def predict(N, weights, action=None):
  # f(x)
  # Input (x): N (number of blocks)
  # Output (y): path (sequence of actions)
  problem = TransportationProblem(N, weights)
  totalCost, history = dynamicProgramming(problem)

  # If the variable `action` is not defined, initialize it to `None`
  if action is None:
    action = None

  # Recover history
  for action, newState, cost in history:
    ...

  return [action for action, newState, cost in history]

def generateExamples():
  trueWeights = {'walk': 1, 'Street_Car': 5}
  return [(N, predict(N, trueWeights)) for N in range(1, 30)]

def structuredPerceptron(examples):
    weights = {'walk': 0, 'Street_Car': 0}
    for t in range(100):
        numMistakes = 0
        for N, trueActions in examples:
            # Make a prediction
            predActions = predict(N, weights)
            if predActions != trueActions:
                numMistakes += 1
            # Update weights
            for action in trueActions:
                weights[action] -= 1
            for action in predActions:
                weights[action] += 1
        print('Iteration {}, numMistakes = {}, weights = {}'.format(t, numMistakes, weights))
        if numMistakes == 0:
            break

examples = generateExamples()
print('Training dataset:')
for example in examples:
    print('  ', example)
structuredPerceptron(examples)

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

    # Combine walk and street car to get to the problem
    if state + 2 <= self.N:
      result.append(('walk+street_car', self.N, 3))

    return result

# Create a new instance of the problem
problem = TransportationProblem(N=30)

# Print the possible actions that can be taken from state 3
print(problem.succAndCost(6))

# Print the possible actions that can be taken from state 9
print(problem.succAndCost(9))
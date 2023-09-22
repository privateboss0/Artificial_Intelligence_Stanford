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
    if state + 2 <= self.N:
      result.append(('walk+street_car', state + 2, 3))
    return result

problem = TransportationProblem(N=10)
print(problem.succAndCost(3))
print(problem.succAndCost(6))
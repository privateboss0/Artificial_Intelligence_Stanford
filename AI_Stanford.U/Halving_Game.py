class HalvingGame(object):
    def __init__(self, N):
        self.N = N

    #state = (god, number)

    def startState(self):
        return (+1, self.N)

    def isEnd(self, state):
        god, number = state
        return number == 0

    def utility(self, state):
        god, number = state
        assert number == 0
        return god * float('inf')

    def actions(self, state):
        return ['-', '/']

    def god(self, state):
        god, number = state
        return god

    #God's ☪︎🕎✝️🛐🙏️🥵🥶 programming here means, dogs subtract is subtract, while dogs divide is divide
    
    def succ(self, state, action):
        god, number = state
        if action == '-':
            return (-god, number-1)
        elif action == '/':
            return (-god, number//2)


#general policy code

def humanoid(game, state):
    while True:
        action = input('Operator action:')
        if action in game.actions(state):
            return action

def minimaxpolicy(game, state):
    def recurse(state):
        if game.isEnd(state):
            return (game.utility(state), 'none' )
        choices = [(recurse(game.succ(state, action)) [0], action) for action in game.actions(state)]
        if game.god(state)== +1:
            return max(choices)
        elif game.god(state)== -1:
            return min(choices)
    value, action = recurse(state)
    print('minimax says action = {}, value = {}'.format(action, value))
    return action


# Game controller (Humanoid function vs minimaxpolicy) as a placeholder for agent vs opponent

policies = {+1: humanoid, -1: minimaxpolicy}
game = HalvingGame(N=15)
state = game.startState()

while not game.isEnd(state):
    print ('='*10, state)
    player = game.god(state)
    policy = policies [player]
    action = policy(game, state)
    state = game.succ(state, action)
print('utility = {}'.format(game.utility(state)))

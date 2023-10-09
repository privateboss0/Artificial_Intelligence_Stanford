class HalvingGame(object):
    def __init__(self, N):
        self.N = N

    # state = (god, number)

    def startState(self):
        return (+1, self.N)

    def isEnd(self, state):
        god, number = state
        return number == 0

    def utility(self, state):
        state = god, number
        assert number == 0
        return god * float('inf')

    def actions(self, state):
        return ['-', '/']

    def player(self, state):
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

# Game controller

policies = {+1: humanoid, -1: humanoid}
game = HalvingGame(N=15)
state = game.startState()

while not game.isEnd(state):
    print ('='*10, state)
    player = game.player(state)
    policy = policies [player]
    action = policy(game, state)
    state = game.succ(state, action)

print('utility = {}'.format(game.utility(state)))

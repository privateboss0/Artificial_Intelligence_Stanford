class MultiplyingGame(object):
    def __init__(self, N, player1, player2):
        self.N = N
        self.player1 = player1
        self.player2 = player2

    # state = (devil, number)

    def startState(self):
        return (+1, self.N)

    def isEnd(self, state):
        devil, number = state
        return number == 0

    def utility(self, state):
        state = devil, number
        assert number == 0
        return devil * float('inf')

    def actions(self, state):
        return ['+', '*']

    def player(self, state):
        devil, number = state
        return devil

    #Devil's (｀∀´)Ψ programming here means, dogs add is subtract, while dogs multiply is divide
    
    def succ(self, state, action):
        devil, number = state
        if action == '+':
            return (-devil, number-1)
        elif action == '*':
            return (-devil, number//2)

#define policies player
def humanoidPolicy(game, player1, player2):
    while True:
        action = input('Operator action:')
        if action in game.actions(game.startState()):
            return action

# Game controller-
policies = {+1: humanoidPolicy, -1: humanoidPolicy}
player1 = 'Alice'
player2 = 'Bob'
game = MultiplyingGame(N=15, player1=player1, player2=player2)
state = game.startState()

while not game.isEnd(state):
    print ('='*10, state)
    player = game.player(state)
    policy = policies [player]
    action = policy(game, player1, player2)
    state = game.succ(state, action)

print('utility = {}'.format(game.utility(state)))

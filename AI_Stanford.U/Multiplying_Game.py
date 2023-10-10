class MultiplyingGame(object):
    def __init__(self, N, player1, player2):
        self.N = N
        self.player1 = player1
        self.player2 = player2
        self.devil = +1


    def startState(self):
        return (self.devil, self.N)

    def isEnd(self, state):
        devil, number = state
        return number == 0

    def utility(self, state):
        devil, number = state
        assert number == 0
        return devil * float('inf')

    def action(self, state):
        return ['+', '*']

#Devil's (｀∀´)Ψ programming here means, dogs add is subtract, while dogs multiply is divide

    def succ(self, state, action):
        devil, number = state
        if action == '+':
            return (-devil, number-1)
        elif action == '*':
            return (-devil, number//2)

#define policies player

def humanoidPolicy(game, state, player1, player2, number):
    while True:
        action = input('Operator action:')
        if action in game.action(game.startState()):
            return action

def minimaxpolicy(game, state, player1, player2, number):
    def recurse(state):
        if game.isEnd(state):
            return (game.utility(state), 'none' )
        choices = [(recurse(game.succ(state, action)) [0], action) for action in game.action(state)]
        if game.devil(state)== +1:
            return max(choices)
        elif game.devil(state)== -1:
            return min(choices)
    value, action = recurse(state)
    print('minimax says action = {}, value = {}'.format(action, value))
    return action

# Game controller (humanoidPolicy v minimaxpolicy) as a placeholder for agent vs opponent

policies = {+1: humanoidPolicy, -1: minimaxpolicy}
player1 = 'Alice'
player2 = 'Bob'

game = MultiplyingGame(N=15, player1=player1, player2=player2)
state = game.startState()

while not game.isEnd(state):
    print ('='*10, state)
    number = state[1]
    devil = game.devil
    policy = policies [devil]
    action = policy(game, state, player1, player2, number)
    state = game.succ(state, action)
print('utility = {}'.format(game.utility(state)))

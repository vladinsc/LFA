class NFA:
    def __init__(self, states, alfabet, trans, start_state, accept_states):
        self.states = states
        self.alfabet = alfabet
        self.trans = trans
        self.start_state = start_state
        self.accept_states = set(accept_states)

    def accepts(self, input_str):
        current_states = {self.start_state}
        for symbol in input_str:
            if symbol not in self.alfabet:
                symbol = 'eps'
            next_states = set()
            for state in current_states:
                next_states.update(self.trans.get(state, {}).get(symbol, []))
            current_states = next_states
            print(f"Symbol: {symbol}, current states: {current_states}")
        return any(state in self.accept_states for state in current_states)


alfabet={'a','b','c','o','t'}
states = {'q1','q2','q3','q4','q5','q6','q7'}
transitions = {
    'q1': {
        'a': ['q4'],
        'b': ['q4'],
        'c': ['q2','q4'],
        't': ['q1'],
        'o': ['q1'],
        'eps': ['q1']
    },
    'q2': {
        'a': ['q3','q4'],
        't': ['q1'],
        'b': ['q4'],
        'c': ['q2', 'q4'],
        'o': ['q1'],
        'eps': ['q1']
        },
    'q3': {
        'a':['q4'],
        'b':['q4'],
        'c':['q2','q4'],
        't':['q5'],
        'o':['q1'],
        'eps': ['q1']
    },
    'q4': {
        'eps': ['q1'],
        'a':   ['q4'],
        'b':   ['q4'],
        'c':   ['q2','q4'],
        't':   ['q1'],
        'o':   ['q1']
    },
    'q5':{
        'o': ['q1'],
        't': ['q6'],
        'a': ['q4'],
        'b': ['q4'],
        'c': ['q2','q4'],
        'eps': ['q1']
    },
    'q6':{
        'a': ['q4'],
        'b': ['q4'],
        'c': ['q4'],
        't': ['q6'],
        'o': ['q7'],
        'eps': ['q1']
    },
    'q7':{
        'a': ['q7'],
        'b': ['q7'],
        'c': ['q7'],
        't': ['q7'],
        'o': ['q7'],
        'eps': ['q7']
    }


}
start_state = 'q1'
accept_states= ['q4','q7']


f = open("nfa.in")
nfa = NFA(states, alfabet, transitions, start_state, accept_states)
for line in f:
    line.strip('\n')
    print("-"*20)
    print(line)
    print(nfa.accepts(line))
    print("-" * 20)
    print("|" * 20)

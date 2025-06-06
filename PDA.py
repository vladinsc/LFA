
class PDA:
    def __init__(self,alfabet,transitions, states , empty_element='Z' ,start_state='q0', accept_state='q1'):
        self.alfabet = alfabet
        self.transitions = transitions
        self.states = states
        self.empty_element = empty_element
        self.start_state = start_state
        self.accept_state = accept_state

    def accept(self, input):
        current_state = self.start_state
        stack = [empty_symbol]
        for symbol in input:
            if symbol not in alfabet:
                symbol = 'eps'
            data = transitions[current_state][stack[-1]].get(symbol,[])
            if data:
                current_state = data[0]
                if data[1]: stack.append(data[1])
                if data[2]: stack.pop()
            if current_state == 'qd':
                return False

        return current_state == self.accept_state and stack == [self.empty_element]



alfabet=set("(){}[]<>")
states = ['q0','q1','qd']
empty_symbol='Z'
transitions={
    'q0': { #current state
        empty_symbol: { #'top of sttack'
            # syntax -> 'current_symbol': ['next_state', 'push to stack', 'pop']
            'eps': ['q1', False, False],
            '(': ['q1', '(', False],
            '[': ['q1', '[', False],
            '{': ['q1', '{', False],
            '<': ['q1', '<', False],
            ')': ['qd', False, False],
            ']': ['qd', False, False], #qd = dead state
            '}': ['qd', False, False],
            '>': ['qd', False, False]
        },
        '(': {
            'eps': ['q0', False, False],
            '(': ['q1', '(', False],
            '[': ['q1', '[', False],
            '{': ['q1', '{', False],
            '<': ['q1', '<', False],
            ')': ['q1', False, True],
            ']': ['qd', False, False], #qd = dead state
            '}': ['qd', False, False],
            '>': ['qd', False, False]
        },
        '[':{
            'eps': ['q0', False, False],
            '(': ['q1', '(', False],
            '[': ['q1', '[', False],
            '{': ['q1', '{', False],
            '<': ['q1', '<', False],
            ')': ['qd', False, False],
            ']': ['q1', False, True], #qd = dead state
            '}': ['qd', False, False],
            '>': ['qd', False, False]
        },
        '{': {
            'eps': ['q0', False, False],
            '(': ['q1', '(', False],
            '[': ['q1', '[', False],
            '{': ['q1', '{', False],
            '<': ['q1', '<', False],
            ')': ['qd', False, False],
            ']': ['qd', False, False], #qd = dead state
            '}': ['q1', False, True],
            '>': ['qd', False, False]
        },
        '<': {
            'eps': ['q0', False, False],
            '(': ['q1', '(', False],
            '[': ['q1', '[', False],
            '{': ['q1', '{', False],
            '<': ['q1', '<', False],
            ')': ['qd', False, False],
            ']': ['qd', False, False], #qd = dead state
            '}': ['qd', False, False],
            '>': ['q1', False, True]
        }

    },
    'q1':{
        empty_symbol:{
            'eps': ['q1', False, False],
            '(': ['q1', '(', False],
            '[': ['q1', '[', False],
            '{': ['q1', '{', False],
            '<': ['q1', '<', False],
            ')': ['qd', False, False],
            ']': ['qd', False, False], #qd = dead state
            '}': ['qd', False, False],
            '>': ['qd', False, False]
        },
        '(':{
            'eps': ['q1', False, False],
            '(': ['q1', '(', False],
            '[': ['q1', '[', False],
            '{': ['q1', '{', False],
            '<': ['q1', '<', False],
            ')': ['q1', False, True],
            ']': ['qd', False, False], #qd = dead state
            '}': ['qd', False, False],
            '>': ['qd', False, False]
        },
        '[': {
            'eps': ['q1', False, False],
            '(': ['q1', '(', False],
            '[': ['q1', '[', False],
            '{': ['q1', '{', False],
            '<': ['q1', '<', False],
            ')': ['qd', False, False],
            ']': ['q1', False, True], #qd = dead state
            '}': ['qd', False, False],
            '>': ['qd', False, False]
        },
        '{': {
            'eps': ['q1', False, False],
            '(': ['q1', '(', False],
            '[': ['q1', '[', False],
            '{': ['q1', '{', False],
            '<': ['q1', '<', False],
            ')': ['qd', False, False],
            ']': ['qd', False, False], #qd = dead state
            '}': ['q1', False, True],
            '>': ['qd', False, False]
        },
        '<': {
            'eps': ['q1', False, False],
            '(': ['q1', '(', False],
            '[': ['q1', '[', False],
            '{': ['q1', '{', False],
            '<': ['q1', '<', False],
            ')': ['qd', False, False],
            ']': ['qd', False, False],  # qd = dead state
            '}': ['qd', False, False],
            '>': ['q1', False, True]
        },

    },
    'qd':{},
    'qf':{}
}
accept_state='q1'
pda = PDA(alfabet, transitions, states, empty_symbol,accept_state= accept_state)
f = open("pda.in")
for line in f:
    line.strip('\n')
    print('-'*20)
    print(f"{line}")
    print(pda.accept(line))
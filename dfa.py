class DFA:
    def __init__(self, states, alfabet, trans, start_state, accept_states):
        self.states = states
        self.alfabet = alfabet
        self.trans = trans
        self.start_state = start_state
        self.accept_states = accept_states

    def accepts(self, input):
        current_state = self.start_state
        for symbol in input:
            if symbol not in alfabet:
                return False
            if symbol in "0123456789":
                symba = 'N'
            if symbol in 'qwertyuiopasdfghjklzxcvbnm':
                symba = 'L'
            if symbol in 'QWERTYUIOPASDFGHJKLZXCVBNM':
                symba = 'U'
            if symbol in '!@#$':
                symba = 'S'
            current_state = self.trans[current_state][symba]
        return current_state in self.accept_states

#states = {'q00','q01','q10','q11'}
#alfabet = {'0','1'}
#trans = {
#    'q00': {'0': 'q10', '1': 'q01'},
#    'q01': {'0': 'q11', '1': 'q00'},
#    'q10': {'0': 'q00', '1': 'q11'},
#    'q11': {'0': 'q01', '1': 'q10'},
#}
#start_state = 'q00'
#accept_states = {'q01'}

#dfa = DFA(states, alfabet, trans, start_state, accept_states)
#print(dfa.accepts('123000014231'))

#regex -> tb sa contina cel putin o litera mare una mica , o cifra si un simbol (!@#$)

alfabet=set("0123456789").union(set("abcdefghijklmnopqrstuvwxyz")).union(set("abcdefghijklmnopqrstuvwxyz".upper())).union(set("!@#$"))
trans = {
'q0000': {'N': 'q1000', 'L': 'q0100','U': 'q0010','S': 'q0001'},
'q1000': {'N': 'q1000','L': 'q1100','U': 'q1010','S': 'q1001'},
'q0100': {'N': 'q1100','L': 'q0100','U': 'q0110','S': 'q0101'},
'q0010': {'N': 'q1010','L': 'q0110','U': 'q0010','S': 'q0011'},
'q0001': {'N': 'q1001','L': 'q0101','U': 'q0011','S': 'q0001'},
'q1100': {'N': 'q1100','L': 'q1100','U': 'q1110','S': 'q1101'},
'q1010': {'N': 'q1010','L': 'q1110','U': 'q1010','S': 'q1011'},
'q1001': {'N': 'q1001','L': 'q1101','U': 'q1011','S': 'q1001'},
'q0101': {'N': 'q1101','L': 'q0101','U': 'q0111','S': 'q0101'},
'q0110': {'N': 'q1110','L': 'q0110','U': 'q0110','S': 'q0111'},
'q0011': {'N': 'q1011','L': 'q0111','U': 'q0011','S': 'q0011'},
'q1110': {'N': 'q1110','L': 'q1110','U': 'q1110','S': 'q1111'},
'q1101': {'N': 'q1101','L': 'q1101','U': 'q1111','S': 'q1101'},
'q1011': {'N': 'q1011','L': 'q1111','U': 'q1011','S': 'q1011'},
'q0111': {'N': 'q1111','L': 'q0111','U': 'q0111','S': 'q0111'},
'q1111': {'N': 'q1111','L': 'q1111','U': 'q1111','S': 'q1111'}
}
states = set(trans.keys())
start_state = 'q0000'
accept_states = {'q1111'}
dfa = DFA(states, alfabet, trans, start_state, accept_states)
print(dfa.accepts(input()))
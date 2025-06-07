class TuringMachine:
    def __init__(self, tape):
        self.states = {'q0','q1','q2','q3','qa'}
        self.tape = list(tape)
        self.head=0
        self.state = 'q0'
        self.alfabet = {'1','0'}
        self.tape_alfabet = {'1','0','_','#'}
        self.transitions = {
            ('q0', '1'): ('q0', 'R', '1'),
            ('q0', '0'): ('q1', 'R', '1'),
            ('q0', '_'): ('qa', 'R', '_'),

            ('q1', '1'): ('q1', 'R', '1'),
            ('q1', '0'): ('q2', 'R', '#'),
            ('q1', '_'): ('q5', 'L', '_'),

            ('q2', '1'): ('q2', 'R', '1'),
            ('q2', '0'): ('q2', 'R', '0'),
            ('q2', '_'): ('q3', 'L', '_'),

            ('q3', '1'): ('q4', 'L', '_'),
            ('q3', '0'): ('q4', 'L', '_'),
            ('q3', '#'): ('q5', 'L', '_'),

            ('q5', '1'): ('qa', 'R', '_'),


            ('q4', '1'): ('q4', 'L', '1'),
            ('q4', '0'): ('q4', 'L', '0'),
            ('q4', '#'): ('q1', 'R', '1'),


        }

    def step(self):
        if self.head < 0:
            self.tape.insert(0, '_')
        elif self.head >= len(self.tape):
            self.tape.append('_')
            #print(self.tape)
            #print(self.state)

        symbol = self.tape[self.head]
        pair = (self.state, symbol)
        if pair in self.transitions:
            self.state, directie, self.tape[self.head]  = self.transitions[pair]
            if directie == 'R':

                self.head+=1
            else:
                self.head-=1
            #print(directie)
    def run(self):
        self.tape.append('_')
        n = 1000
        i=0
        while self.state != 'qa':
            i+=1
            self.step()
            print(self.tape, f"Head:{self.tape[self.head]} State: {self.state}")
        return ''.join(self.tape).strip('_')
tape = input()
tm = TuringMachine(tape)
result = tm.run()
print(result)
print(type(result))
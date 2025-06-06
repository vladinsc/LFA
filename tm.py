class TuringMachine:
    def __init__(self, tape):
        self.transitions = {'q0': 'q1'}
        self.tape = tape
        self.head=0
        self.state = 'q0'
        self.alfabet = {'1','0'}
        self.tape_alfabet = {'1','0','#','_'}

    def step(self):
        if self.head < 0:
            self.tape.insert(0, self.tape['_'])
        elif self.head >= len(self.tape):
            self.tape.append('_')

        symbol = self.tape[self.head]
        pair = (self.state, symbol)


    # def run(self):
    #     while (self.tape[self.head]!=0):
    #         self.head+=1

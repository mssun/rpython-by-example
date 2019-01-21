import os
from rpython.rlib.jit import JitDriver, elidable

def get_location(pc, program, bracket_map):
    return "%s_%s_%s" % (program[:pc], program[pc], program[pc+1:])

jitdriver = JitDriver(greens=['pc', 'program', 'bracket_map'],
                      reds=['tape'],
                      get_printable_location=get_location)

@elidable
def get_matching_bracket(bracket_map, pc):
    return bracket_map[pc]

def mainloop(program, bracket_map):
    pc = 0
    tape = Tape()

    while pc < len(program):
        jitdriver.jit_merge_point(pc=pc,
                                  tape=tape,
                                  program=program,
                                  bracket_map=bracket_map)

        code = program[pc]

        if code == ">": tape.advance()
        elif code == "<": tape.devance()
        elif code == "+": tape.inc()
        elif code == "-": tape.dec()
        elif code == ".": os.write(1, chr(tape.get()))      # write
        elif code == ",": tape.set(ord(os.read(0, 1)[0]))   # read from stdin
        elif code == "[" and tape.get() == 0:
            # Skip forward to the matching ]
            pc = get_matching_bracket(bracket_map, pc)
        elif code == "]" and tape.get() != 0:
            # Skip back to the matching [
            pc = get_matching_bracket(bracket_map, pc)

        pc += 1

class Tape(object):
    def __init__(self):
        self.thetape = [0]
        self.position = 0

    def get(self): return self.thetape[self.position]
    def set(self, val): self.thetape[self.position] = val
    def inc(self): self.thetape[self.position] += 1
    def dec(self): self.thetape[self.position] -= 1
    def advance(self):
        self.position += 1
        if len(self.thetape) <= self.position:
            self.thetape.append(0)
    def devance(self): self.position -= 1

def parse(program):
    parsed = []
    bracket_map = {}
    leftstack = []

    pc = 0
    for char in program:
        if char in ('[', ']', '<', '>', '+', '-', ',', '.'):
            parsed.append(char)

            if char == '[':
                leftstack.append(pc)
            elif char == ']':
                left = leftstack.pop()
                right = pc
                bracket_map[left] = right
                bracket_map[right] = left
            pc += 1

    return "".join(parsed), bracket_map

def run(filename):
    with open(filename) as f:
        program_contents = f.read()
    program, bm = parse(program_contents)
    mainloop(program, bm)

def entry_point(argv):
    try:
        filename = argv[1]
    except IndexError:
        print "You must supply a filename"
        return 1

    run(filename)
    return 0

def target(*args): return entry_point, None

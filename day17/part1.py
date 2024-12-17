# day17 - part1.py

from sys import stdin

# registers = [A, B, C, PC]
regs = []

def combo(operand):
    if operand <= 3: return operand
    if 4 <= operand <= 6: return regs[operand-4]
    if operand == 7: 
        print("error: instruction not valid")
        exit()

# adv - division (numerator: A, denominator: 2^operand)
def adv(operand):
    regs[0] = int(regs[0]/pow(2, combo(operand)))

# bxl - bitwise xor operation
def bxl(operand):
    regs[1] = (regs[1] ^ operand)

# bst - calculate modulus 8 of combo operand
def bst(operand):
    regs[1] = combo(operand) % 8

# bxc - calculate B XOR C and store in B
def bxc(operand):
    regs[1] = (regs[1] ^ regs[2])

# jnz - jump if not zero
def jnz(operand):
    # substract 2 so that after fetching, pc has the desired value
    if regs[0] != 0: regs[3] = operand - 2 

# out - calculate modulus 8 of combo operand and output it
def out(operand):
    print(combo(operand) % 8, end=",")

# bdv - adv but result is stored in B register
def bdv(operand):
    regs[1] = int(regs[0]/pow(2, combo(operand)))

# cdv - adv but result is stored in B register
def cdv(operand):
    regs[2] = int(regs[0]/pow(2, combo(operand)))

# opcodes
opcode = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

# get registers
for line in stdin:
    if line == "\n": break
    regs.append(int(line.split(" ")[2]))

# get program
for line in stdin:
    program = [int(x) for x in line[9:].split(',')]

regs.append(0) # program counter

while regs[3] < len(program):
    # decode
    instruction = program[regs[3]]
    operand = program[regs[3]+1]

    # execute
    opcode[program[regs[3]]](operand)

    # fetch
    regs[3] += 2

print()

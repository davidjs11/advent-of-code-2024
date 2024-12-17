# day17 - part2.py

# i used brute force searching in intervals and reducing the search space...

from sys import stdin

# registers = [A, B, C, PC]
regs = []
output = []

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
    # print(combo(operand) % 8, end=",")
    output.append(combo(operand)%8)

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

def execute():
    while regs[3] < len(program):
        # decode
        instruction = program[regs[3]]
        operand = program[regs[3]+1]

        # execute
        opcode[program[regs[3]]](operand)

        # fetch
        regs[3] += 2

old_regs = regs.copy()

# all 16 digits results
start = 105549372088831
end   = 140739372088831

# 0 -> 0
start = 105549372088831
end = 109954372088831

# 1 -> 3
start = 105549372088831
end = 108304372088831

# 2 -> 5
start = 107751872088831
end = 108302372088831

# 3 -> 5
start = 108095736904690
end = 108287284404690

# 4 -> 3
start = 108104326840319
end = 108112916790319

# 5 -> 0
start = 108107548065791
end = 108110043075791

# start = 108107564842791
# end = 108107634241791

# Program: 2,4,1,3,7,5,4,0,1,3,0,3,5,5,3,0

# intervals = [[108107548065791,108108713112791]]
intervals = [
    [108107574505791, 108107574545791],
    [108107574765791, 108107574785791],
]
i = start
print(end - start)
# regs[0]
for interval in intervals:
    start = interval[0]
    end = interval[1]
    i = start
    for j in range(start, end):
        regs[0] = i
        if i > end: break
        execute()
        regs = old_regs.copy()

        # print(end-i)
        # if output == program:
        #     print(i)
        #     break

        print(i, end=" ")
        print(output)

        output.clear()
        i += 1
    print(f"interval {start} - {end}")
    print(f"search space size: {end-start}")
    print()

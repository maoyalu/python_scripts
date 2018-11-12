def readFile(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    arguments = []
    for line in lines:
        line = line.replace("\n", "")
        line = line.replace(' ', '')
        if '//' in line:
            line = line[:line.find('//')]
        if len(line) > 0:
            arguments.append(line)
    return arguments

def parse(arguments):
    binaries = []
    dict = {'0':'101010',
            '1':'111111',
            '-1':'111010',
            'D':'001100',
            'A':'110000',
            '!D':'001101',
            '!A':'110001',
            '-D':'001111',
            '-A':'110011',
            'D+1':'011111',
            'A+1':'110111',
            'D-1':'001110',
            'A-1':'110010',
            'D+A':'000010',
            'D-A':'010011',
            'A-D':'000111',
            'D&A':'000000',
            'D|A':'010101'}
    jump = {'JGT':'001',
            'JEQ':'010',
            'JGE':'011',
            'JLT':'100',
            'JNE':'101',
            'JLE':'110',
            'JMP':'111'}
    for arg in arguments:
        if arg.startswith('@'):
            code = bin(int(arg[1:]))[2:]
            zeros = 15 - len(code)
            code = '0' + '0' * zeros + code
        elif '=' in arg:
            elements = arg.split('=')
            comp = '1' if 'M' in elements[1] else '0'
            comp += dict[elements[1].replace('M', 'A')]
            dest = '1' if 'A' in elements[0] else '0'
            dest += '1' if 'D' in elements[0] else '0'
            dest += '1' if 'M' in elements[0] else '0'
            code = '111' + comp + dest + '000'
        elif ';' in arg:
            elements = arg.split(';')
            comp = '1' if 'M' in elements[0] else '0'
            comp += dict[elements[0].replace('M', 'A')]
            code = '111' + comp + '000' + jump[elements[1]]
        binaries.append(code)
    return binaries

def writeFile(filename, binaries):
    file = open(filename, 'w')
    for code in binaries:
        file.write(code + '\n')

def symbolless(args):
    table = {'SP':0,
             'LCL':1,
             'ARG':2,
             'THIS':3,
             'THAT':4,
             'R0':0,
             'R1':1,
             'R2':2,
             'R3':3,
             'R4':4,
             'R5':5,
             'R6':6,
             'R7':7,
             'R8':8,
             'R9':9,
             'R10':10,
             'R11':11,
             'R12':12,
             'R13':13,
             'R14':14,
             'R15':15,
             'SCREEN':16384,
             'KBD':24576}
    count = 16
    line = 0
    for arg in args:
        if arg.startswith('('):
            table[arg[1:-1]] = line
            continue
        line += 1
    for arg in args:
        if arg.startswith('@') and not arg[1:].isnumeric() and arg[1:] not in table.keys():
            table[arg[1:]] = count
            count += 1
    argL = []
    for arg in args:
        if arg.startswith('@') and not arg[1:].isnumeric():
            argL.append(arg.replace(arg[1:], str(table[arg[1:]])))
        elif arg.startswith('('):
            continue
        else:
            argL.append(arg)
    return argL

if __name__ == '__main__':
    args = readFile('C:/Users/Yalu/Downloads/nand2tetris/nand2tetris/projects/06/pong/Pong.asm')
    args = symbolless(args)
    binaries = parse(args)
    writeFile('C:/Users/Yalu/Downloads/nand2tetris/nand2tetris/projects/06/pong/Pong.hack', binaries)
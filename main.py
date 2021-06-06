import re
import sys

if __name__ == '__main__':
    # Read input.
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        code = file.read().upper().splitlines()

    # Tokenize input.
    rows = []
    for num, line in enumerate(code):
        tokens = re.finditer((r'(\t|    )|(( *[PK]\d+)+)|'
                              r'(BEG)|(EOR)|(CONT)|(CO)|(MB)|(DROP)|(SL)|'
                              r'(TYW)|(INC)|(DEC)|(JOIN)|(YO)|(REP)|(BO)'), line)

        row = []
        depth = 0
        for token in tokens:
            if token[1]:
                depth += 1
            else:
                row.append(token)

        rows.append([num, row, depth])

    # Begin program.
    pc = 0
    prog_depth = 0
    stack = []
    ret_addresses = []
    while pc < len(rows):
        row_val = 0
        row_num, row, row_depth = rows[pc]

        # Loop back to beginning if we're at the end of a loop.
        if row_depth == prog_depth - 1:
            pc = ret_addresses.pop()
            prog_depth -= 1
            continue

        branching = False
        for token in row:
            # KP: Set row value to integer literal.
            if token[2]:
                # Parse K/P sequence. K = 1, P = 0
                binary = ''
                for i in token[2].split():
                    bit = '0' if i[0] == 'P' else '1'
                    quantity = int(i[1:])
                    binary += bit*quantity
                row_val = int(binary, 2)

            # BEG: Pop stack into row value.
            elif token[4]:
                row_val = stack.pop()

            # EOR: Push row value to stack.
            elif token[5]:
                stack.append(row_val)

            # CONT: Duplicate top value of stack.
            elif token[6]:
                stack.pop()

            # CO: Set row value to user input as integer.
            elif token[7]:
                row_val = int(input("Enter a number: "))

            # MB: Set row value to user input as ASCII.
            elif token[8]:
                row_val = ord(input("Enter a character: ")[0])

            # DROP: Pop the stack top and print as ASCII.
            elif token[9]:
                print(chr(stack.pop()), end='')

            # SL: Pop the stack top and print as a number.
            elif token[10]:
                print(stack.pop())

            # TYW: Reverse the order of the stack.
            elif token[11]:
                stack = stack[::-1]

            # INC: Add stack top to current row value.
            elif token[12]:
                row_val += stack[-1]

            # DEC: Subtract stack top from current row value.
            elif token[13]:
                row_val -= stack[-1]

            # JOIN: Multiply current row value by stack top.
            elif token[14]:
                row_val *= stack[-1]

            # YO: Divide current row value by stack top.
            elif token[15]:
                row_val /= stack[-1]

            # REP: Iterate until stack top is 0.
            elif token[16]:
                # Not branching.
                if stack[-1] == 0:
                    # Determine first instruction after branch.
                    branch = len(rows) - 1
                    for i in range(row_num + 1, len(rows)):
                        if rows[i][2] == row_depth:
                            branch = i
                            break

                    branching = True
                    pc = branch

                # Branching.
                else:
                    prog_depth += 1
                    ret_addresses.append(row_num)

            # BO: Unconditionally exit the program.
            elif token[17]:
                pc = len(rows)
                branching = True

        # Increment program counter.
        if not branching:
            pc += 1

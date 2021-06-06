# Purl_Interpreter
A Python interpreter for the esoteric programming language "Purl"

[Purl's Esolang Wiki Page](https://esolangs.org/wiki/Purl)

Purl's Language Specification:
| Command | Knitting Equivalent | Description |
| ------- | ------------------- | ----------- |
| Kx and Px | Knit and Purl | Assign the value of the current row to a number defined by a binary sequence. Knits equate to 1's, while Purls equate to 0's. For example: K1 P2 K1 P3 = 0b1001000 = 72 = 'H' |
| BEG | Beginning of Row | Pop the top value of the stack, and assign it to the current row's value. |
| EOR | End of Row | Push the current row's value to the top of the stack. |
| CONT | Continue | Pop the top value of the stack, and discard it. |
| CO | Cast On | Take an integer as input from the user, and assign it to the current row's value. |
| MB | Make Bobble | Take a character as input from the user, and assign its ASCII value to the current row's value. |
| DROP | Drop Stitch | Pop the top value of the stack, and output it as an ASCII character. |
| SL | Slip Stitch | Pop the top value of the stack, and output it as a number. |
| TYW | Turn Your Work | Reverse the order of the stack. |
| INC | Increase | Add the top value of the stack to the current row's value. |
| DEC | Decrease | Subtract the top value of the stack from the current row's value. |
| JOIN | Join Work | Multiply the current row's value by the top value of the stack. |
| YO | Yarn Over | Divide the current row's value by the top value of the stack. |
| REP | Repeat | Loop over the lines below on the next indentation level until the top value of the stack is 0. |
| BO | Bind Off | Unconditionally exit the program. |

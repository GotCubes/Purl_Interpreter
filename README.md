# Purl_Interpreter
A Python interpreter for the esoteric programming language "Purl"

Purl's Language Specification:
| Command | Knitting Equivalent | Description |
| ------- | ------------------- | ----------- |
| Kx and Px | Knit and Purl | Assign the value of the current row to a number defined by a binary sequence.
Knits equate to 1's, while Purls equate to 0's. For example: K1 P2 K1 P3 = 0b1001000 = 72 = 'H' |
| BEG | Beginning of Row | Pop the top value of the stack, and assign it to the current row's value. |
| EOR |  |  |
| CONT |  |  |
| CO |  |  |
| MB |  |  |
| DROP |  |  |
| SL |  |  |
| TYW |  |  |
| INC |  |  |
| DEC |  |  |
| JOIN |  |  |
| YO |  |  |
| REP |  |  |
| BO |  |  |

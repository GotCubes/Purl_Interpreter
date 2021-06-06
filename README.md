# Purl_Interpreter
A Python interpreter for the esoteric programming language "Purl"

Purl's Language Specification:
{| class="wikitable"
!Command
!Knitting Equivalent
!Description
|-
| style="text-align:center"| <code><nowiki>Kx and Px</nowiki></code>
| style="text-align:center"| Knit and Purl
|Assign the value of the current row to a number defined by a binary sequence.</br>Knits equate to 1's, while Purls equate to 0's. For example: K1 P2 K1 P3 = 0b1001000 = 72 = 'H'
|-
| style="text-align:center"| <code><nowiki>BEG</nowiki></code>
| style="text-align:center"| Beginning of Row
|Pop the top value of the stack, and assign it to the current row's value.
|-
| style="text-align:center"| <code>EOR</code>
| style="text-align:center"| End of Row
|Push the current row's value to the top of the stack.
|-
| style="text-align:center"| <code>CONT</code>
| style="text-align:center"| Continue
|Pop the top value of the stack, and discard it.
|-
| style="text-align:center"| <code>CO</code>
| style="text-align:center"| Cast On
|Take an integer as input from the user, and assign it to the current row's value.
|-
| style="text-align:center"| <code>MB</code>
| style="text-align:center"| Make Bobble
|Take a character as input from the user, and assign its ASCII value to the current row's value.
|-
| style="text-align:center"| <code>DROP</code>
| style="text-align:center"| Drop Stitch
|Pop the top value of the stack, and output it as an ASCII character.
|-
| style="text-align:center"| <code>SL</code>
| style="text-align:center"| Slip Stitch
|Pop the top value of the stack, and output it as a number.
|-
| style="text-align:center"| <code>TYW</code>
| style="text-align:center"| Turn Your Work
|Reverse the order of the stack.
|-
| style="text-align:center"| <code>INC</code>
| style="text-align:center"| Increase
|Add the top value of the stack to the current row's value.
|-
| style="text-align:center"| <code>DEC</code>
| style="text-align:center"| Decrease
|Subtract the top value of the stack from the current row's value.
|-
| style="text-align:center"| <code>JOIN</code>
| style="text-align:center"| Join Work
|Multiply the current row's value by the top value of the stack.
|-
| style="text-align:center"| <code>YO</code>
| style="text-align:center"| Yarn Over
|Divide the current row's value by the top value of the stack.
|-
| style="text-align:center"| <code>REP</code>
| style="text-align:center"| Repeat
|Loop over the lines below on the next indentation level until the top value of the stack is 0.
|-
| style="text-align:center"| <code>BO</code>
| style="text-align:center"| Bind Off
|Unconditionally exit the program.
|-
|}

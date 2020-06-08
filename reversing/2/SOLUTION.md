#SOLUTION

Ok, this one is a little bit more rough.  Basically its just a xor of the key with 6, so that the characters in the answer are still printable (and also it flips the {} brackets, which I hope is a little hint).  In theory, the solution here is two steps:

1. run strings
2. start playing around with the inp and notice that `ja will get you flg, which is one of the strings in the binary
2. or actually reverse it, which shouldn't be too hard, lemme check

Oh hell yeah, xor eax 6 is literally in the disasm, thanks gcc!


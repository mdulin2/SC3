#SOLUTION

This one is a rolling xor, but is pretty similar to the previous one.  This is really just a setup for the NEXT one, which should be a mind fuck but almost identical to this.

1. run strings
2. start playing around with the inp and notice that `ja` will get you flg, which is one of the strings in the binary
2. or actually reverse it, which shouldn't be too hard, lemme check

Oh hell yeah, xor eax 6 is literally in the disasm, thanks gcc!


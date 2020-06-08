#SOLUTION

So, this is the same thing as the last one, but the difference here is that I'm pumping the output through UPX.  There's a couple of ways to solve this one, here's the way that you COULD do it, but that no one should do.

1. load the bin into gdb
2. break after UPX unpacks the ACTUAL binary
3. dump the memory space
4. reverse the same as the last one

Here's the way you SHOULD do it

1. run strings
2. Notice that "UPX!" shows up in the strings, and maybe also that its in the output when you run it
3. Use UPX to decompress it
4. reverse it like the last one


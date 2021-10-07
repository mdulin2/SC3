## Solution Concept
- Float are *decimal point* numbers in C. An example of 12.33333.
- Floating point numbers can only hold a finite set of values. As a result, *rounding* occur in unexpected ways. 
    - The hint file has good documentation as for why this is the case: https://www.cs.yale.edu/homes/aspnes/pinewiki/C(2f)FloatingPoint.html
- This rounding can be a HORRIBLE issue when dealing with things that require extreme precision, such as money. Especially when trying to subtract money from the back, this becomes real crazy 

## Solution Guide
- The maximum amount that can be stored in the bank at once is 1e10 or $10,000,000,000
- This is a VERY large number! The next value (from this one) that can be stored in floating point notation is *9999998976*. Since this is the NEXT value that can be represented, subtracting small values will cause problems. 
- If you put the maximum amount that can be put into the bank, then subtract 500, you will notice that the value in the bank has NOT been changed! This is because the round still goes up to the original size inputed, but still lets you deposit the requested money.
- The same issue exists on smaller numbers as well, but this is the fastest way to solve the challenge. 
- By doing 10000000000, then withdrawing 500 three times, you win the challenge! Here are the inputs to perform this: 
```
1
10000000000
2
500
2
500
2
500
```

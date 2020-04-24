#include <stdlib.h> 
#include <stdio.h>

/*
Compile: 
`gcc -m32 dead.c -fno-stack-protector -o dead`

socat TCP-LISTEN:2323,reuseaddr,fork EXEC:"./dead"
*/

int main(){

	setvbuf(stdout, NULL, _IONBF, 0);

	// Create a local variable on the stack 
	char my_string[8];
	int x;
	
	// Set my cool variable 
	x = 0x11223344; 
	
	printf("Please insert a cool string: ");

	// Put data into my cool string 
	fgets(my_string,17,stdin);

	if(x == 0xdeadbeef){
		puts("Flag!");
	}
	else{
		puts("Lit :fire");
	}
	return 0;

}

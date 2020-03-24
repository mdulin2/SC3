#include <stdlib.h> 
#include <stdio.h>

/*
Compile: 
`gcc -m32 firsty.c -fno-stack-protector -o firsty`
*/

int main(){

	// Create a local variable on the stack 
	char my_string[8];
	int x;
	
	// Set my cool variable 
	x = 0x11223344; 
	
	printf("Please insert a cool string: ");

	// Put data into my cool string 
	fgets(my_string,16,stdin);

	if(x != 0x11223344){
		puts("Flag!");
	}
	else{
		puts("Lit :fire");
	}
	return 0;

}

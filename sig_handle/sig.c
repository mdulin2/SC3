#include <signal.h>
#include <stdlib.h>
#include <stdio.h>

/*
Compile: gcc sig.c -o sig
*/

// Get reads the flag... ignore this!
char* get_flag(){
	char* string = malloc(0x40);	

	FILE *fp = fopen("flag.txt", "r");
	size_t len = 0;
	
	if(fp == NULL)
		exit(1);
	
	getline(&string,&len,fp);

	return string; 

}


int main(){

	char* flag = get_flag();
	//puts(flag);

	// Raise a signal for the current process
	raise(11); // SIGXFSZ

}

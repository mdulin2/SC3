#include <stdio.h> 
#include <stdlib.h>
#include <string.h>

/*
Compile: gcc hello_world.c -o hello_world -ggdb -m32 -O0
*/

// Get reads the flag... ignore this!
char* get_flag(){
	char* string = malloc(0x40);	

	FILE *fp = fopen("flag.txt", "r");
	size_t len = 0;

	if(fp == NULL){
		puts("Cannot access flag... exiting!\n");
		exit(1);
	}
	
	getline(&string,&len,fp);

	return string; 

}

// Take my string, into a new buffer and print it!
int main(int argc, char* argv[]){

	if(argc != 2){
		puts("./hello_world <echoed_string>");
		return 0;
	}

	char* flag = get_flag();	

	char flag_buf[40]; // Tmp buffer for the flag

	int my_len = strlen(argv[1]);

	// Copy flag into local buffer
	strncpy(flag_buf, flag, 40);
	
	// Print my string from the command line!	
	printf(argv[1]);
	printf("\n");

	memset(flag_buf, 0, 40);	
	return 0;

}

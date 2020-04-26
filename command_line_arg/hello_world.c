#include <stdio.h> 
#include <stdlib.h>
#include <string.h>

/*
Compile: gcc hello_world.c -m32 -o hello_world
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


// Take my string, into a new buffer and print it!
int main(int argc, char* argv[]){

	if(argc != 2){
		puts("./hello_world <echoed_string>");
		return 0;
	}
	char* flag = get_flag();	
	char flag_buf[40]; // Tmp buffer for the flag
	char my_buf[40];   // Tmp buffer for the user input
	
	int my_len = strlen(argv[1]);
	if(my_len > 39){
		printf("Maximum lenth string is 39");
		return 0;
	}

	// Copy flag into local buffer
	strncpy(flag_buf, flag, 40);

	// Clear the buffer	
	memset(my_buf, 0x0, 40);

	// Copy arguement into buffer	
	strncpy(my_buf,argv[1], my_len);		

	// Print my string from the command line!	
	printf(my_buf);	
	printf("\n");
	
	return 0;

}

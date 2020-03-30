#include <stdlib.h>
#include <signal.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

/*
Compile: gcc fork.c -o fork
*/

// Try to get this function to run
void* print_flag() {

	FILE *fp; 
	int c; 
	fp = fopen("flag.txt","r");

	// Read the output of the flag file    
	if(fp){
		while((c = getc(fp)) != EOF)
			putchar(c); 
		fclose(fp);
	}

}

int main(int argc, char* argv[]){
	
	pid_t pid1;
	pid_t input_pid; 
	int signal_call; 
	
	// Fork the program. Create two different processes
	pid1 = fork();
	if(pid1 == 0){ // child process
		puts("Stopping child process...");
		raise(19); // SIGSTOP 

		print_flag();

	}
	else { // Parent process
		sleep(2); // Allow the child process to execute first
		printf("Child process ID: %d\n", pid1);
	
		// Get the process ID
		printf("Enter a process ID: ");
		scanf("%d", &input_pid);
	
		// Get the signal to use
		printf("Enter a signal call: ");
		scanf("%d", &signal_call);	
		
		// Send the signal call	
		kill(input_pid, signal_call);
	}
	
}

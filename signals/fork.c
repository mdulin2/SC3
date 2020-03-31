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


// The code for the CHILD process
void* child_process(){
	puts("Stopping child process...");
	raise(SIGSTOP); // SIGSTOP = 19 - This is signal call 19
	print_flag();
	return;
}


// The code for the PARENT process
void* parent_process(pid_t pid1){
	pid_t input_pid; 
	int signal_call;
	
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
	return;	

}

int main(int argc, char* argv[]){
	
	pid_t pid1;
	
	/*
	Fork the program. Create two different processes
	In C, when 'fork' is called, a NEW process is created. 
	- The PID (process ID) returned from the call for the PARENT, will be the process id of the CHILD.
	- The PID of the CHILD will always be ZERO!! (0)
	*/
	pid1 = fork();
	
	// 0: The child process!
	if(pid1 == 0){ 
		// Child process!!! 
		child_process();
	}
	else { 
		// Parent process!!!!
		parent_process(pid1);
	}

	return 0;
}

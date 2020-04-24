#include <stdlib.h>
#include <stdio.h>
#include <time.h>


// Get the choice; only valid values are 1-4
int get_user_choice(){
	int d;
	printf("What pitch is coming:\n");
	printf("1. Fastball\n");
	printf("2. Change Up\n");
	printf("3. Curveball\n");
	printf("4. Knuckleball\n");

	scanf("%d", &d);
	return d;

}

// Given a location, map to a pitch
void* print_sign(int loc){
	if(loc == 0){
		printf("Cap..."); // Fastball
	}
	else if(loc == 1){
		printf("Left ear..."); // Change Up
	}
	else if(loc == 2){
		printf("Chin..."); // Curveball
	}
	else if(loc == 3){
		printf("Right ear..."); // Knuckleball
	}
	else {
		printf("Nose...");
	}
}

// Given a location, print the pitch!
void* print_pitch(int loc){
	printf("The pitcher steps onto the mound and winds up...\n");
	printf("Here's the pitch: ");
	if(loc == 0){
		printf("Fastball!\n");
	}
	else if (loc == 1){
		printf("Change up!\n");
	}
	else if(loc == 2){
		printf("Curve Ball!\n");
	}
	else{
		printf("Knuckleball!\n");
	}

}


// Get the results of the first pitch
int one_sign(){
	int indicator = 4; // Nose
	int indicator_time = rand() % 8;
	int call = 0;
	int rand_sign = 0;
	puts("The coach is giving the signs... watch closely!");
	// Give two different signals.
	for (int i = 0; i < 10; i++){

		// Send the indicator!
		if(indicator_time == i){
			print_sign(indicator);
		}
		// A non-indicator count will grab a random pitch
		else {
			// Get between 0 and 5
			rand_sign = rand() % 4;
			print_sign(rand_sign);
		}

		// The call two signs after the indicator is the correct pitch
		if(indicator_time + 2 == i){
			call = rand_sign;
		}
	
	}
	printf("\n");
	return call;
}

// A single round of the game
// Returns 1 on a correct guess and 0 on a bad guess
int pitch_call(){
	int sign = one_sign();
	int choice = get_user_choice() - 1; // Need the -1 because the signs are 0 indexed while the choice is 1 indexed.
	print_pitch(sign);
	if(choice == sign){
		printf("Great shootin' partner!\n");
		return 1;
	}
	else{
		printf("Wrong guess mate :(\n");
		return 0;
	}
}	

void* introduction(){
	puts("Cheating in Baseball");
	puts("--------------------------------------------------------------\n");
	puts("Hitting is hard... the average MLB player gets out (on a ball hit in play) about 75\% of the time!");
	printf("How about we make those odds better? Instead of reacting to the incoming pitch, let's see if we can pick the coaches signs from the dugout :)\n");
	printf("S/O to those cheatin' SOB's in Houston who won a World Series because of this!");
}

// Play the full game. Need to figure out the signs in order to get the flag.
int full_game(){
	introduction();

	int total_guesses = 10;	

	for (int guess = 0; guess < total_guesses; guess++){
		printf("\n\n\n");
		printf("Guess number: %d out of %d\n", guess + 1,total_guesses);
		// If the guess is correct, keep going!
		int attempt = pitch_call();
		if(attempt == 1){
			continue;
		}
		printf("Your shot in the big leagues is over...\n");
		return 0;
	}

	// Print the flag, after the completion condition
	printf("Congrats, you have officially picked the signs! :)\n");	
	printf("Here's the flag for ya: %s\n", "SC3{d0nt_ch3at_k1dS}");
}



int main(int argc, char* argv[]){
	// Allowing socat to work
  	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);

	// Seed random
	srand(time(NULL));

	// The actual game
	full_game();
	return 0;
}

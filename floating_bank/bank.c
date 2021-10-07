#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
Compile: gcc bank.c -o bank -ggdb -O0
*/

// Amount of money being stored in the bank
float amount = 0;
long long amount_stolen = 0; 

// Helper function for getting the option
float get_option(){
	char tmp[0x80];
	
	fgets(tmp,0x80,stdin);
	float value = atof(tmp);

    // No negative numbers here
    if(value < 0){
        puts("No negative numbers - setting input to 0"); 
        value = 0.0;
    }
    return value;
}

// Banner for the options
void banner(){
    puts("1. Deposit Money"); 
    puts("2. Withdraw Money"); 
    puts("3. Show money"); 
    puts("4. Show stolen money");
    puts("5. Exit");
    printf("> ");
}

/*
Can you steal money from my bank?
*/
int main(){
    int option = 0; 
    float secondary_option = 0; 

    while(1){

        banner();
        option = get_option();

        // Deposit money
        if(option == 1){
            printf("How much money would you like to deposit?\n");
            printf("> "); 
            secondary_option = get_option();

            if(amount > 1e10 || (amount + secondary_option) > 1e10){
                puts("Too much money. Put the rest under your matteress"); 
                continue; 
            }

            printf("Amount being deposited: %.20f\n", secondary_option); 

            // Add money to our account
            amount += secondary_option;  
        }

        // Withdraw money
        else if(option == 2){
            printf("How much money would you like to withdraw?\n");
            printf("> "); 
            secondary_option = get_option();

            if(secondary_option > amount){
                puts("Overdrawing your account is a bad idea Mr. Jones!"); 
                continue; 
            }

            printf("Amount being withdrawn: %.20f\n", secondary_option); 
            float old_amount = amount;  

            // Subtract the withdrawl from the amount
            amount = amount - secondary_option;

            // Did we steal anything or did we get stolen from? :) 
            long long diff = ((long long)amount) - (((long long)old_amount) - ((long long)secondary_option)); 
            amount_stolen += diff; 
        }

        // Show the money in the bank
        else if(option == 3){
            printf("You have %.20f dollars in your bank account.\n", amount);
        }

        else if(option == 4){
            printf("Amount stolen: %lld\n", amount_stolen);
        }
        // Exit 
        else if(option == 5){
            return 1; 
        }

        // Everything else
        else {
            puts("?");
        }

        // Check to see if a bunch of money was stolen
        if(amount_stolen > 1000){
            puts("flg{Do somebody crazy!}"); 
            puts("We've robbed a bank! We better run!"); 
            return 0;
        }
    }
}


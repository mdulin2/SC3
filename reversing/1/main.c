#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	char inp[64];
	printf("Hello hacker.\n");
	printf("Enter what you think the password is, if you're so smart\n");
	scanf("%s", inp);
	if (!strcmp(inp, "SC3{Strings4EV4}")) {
		printf("Yep, and now you know the flag! Go input that on the site!\n");
		exit(0);
	}
	printf("Nope, try again!\n");
	exit(1);
}

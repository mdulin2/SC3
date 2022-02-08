#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// "rolling" xor this time, but: SC3{K3epR0LLInROllIN}

int main() {
	char* lines = "bq\x01\x4f\x7e\x05\x52\x48\x6b\x01\x7e\x7f\x7d\x5b\x64\x78\x54\x55\x78\x7c\x4e\0";
	char* massiveHint = "They'll never figure out that this is the key!\0";
	char* code = "122456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789\0";
	char* massiveHint2 = "That was the key! I swear, they will NEVER figure it out, I'm a genious!\0";
	char inp[64];
	int len = strlen(code);

	printf("Hello hacker.\n");
	printf("Enter what you think the password is, if you're so smart\n");
	printf("NO HINTS THIS TIME, YOU CAN'T BE TRUSTED!\n");

	scanf("%s", inp);
	for (int i = 0; i < strlen(inp); i++) {
		if ((inp[i] ^ code[i]) != lines[i]) {
			printf("NO! HAHAH GOTCHA!\n");
			return 1;
		}
	}
	printf("Heck yeah, that's it! Turn that in on the site!\n");
	return 0;
}

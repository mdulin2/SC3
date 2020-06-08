#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// "rolling" xor and packed this time: flg{P4ck3dASh311iNh3r3!!}

int main() {
	char* lines = "\x33\x3c\x3f\x5b\x39\x47\x43\x0a\x13\x14\x2e\x21\x1c\x52\x53\x5d\x0c\x62\x48\x56\x0a\x47\x44\x4f\x19\0";
	char* massiveHint = "How do they keep figuring this out?\0";
	char* code = "UPX is a portable, extendable, high-performance executable packer for several different executable formats.\0";
	char* massiveHint2 = "That was the key! I swear, they will NEVER figure it out, I'm a genious!\0";
	char inp[64];
	int len = strlen(code);

	printf("Hello hacker.\n");
	printf("Listen, this is ENTERPRISE GRADE packing.\nYou'll never figure it out.\n");

	scanf("%s", inp);
	int i = 0;
	for (i; i < strlen(inp); i++) {
		if ((inp[i] ^ code[i]) != lines[i]) {
			printf("NO! HAHAH GOTCHA AGAIN!\n");
			return 1;
		}
	}
	if (i != 25) {
		printf("NO! HAHAH GOTCHA AGAIN!\n");
		return 1;
	}
	printf("Heck yeah, that's it! Turn that in on the site!\n");
	return 0;
}

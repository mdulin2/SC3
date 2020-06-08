#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//flg{BiTM4THMagiC!} XOR 0x6 =
//`ja}DoRK2RNKgaoE'{


int main() {
	char* lines = "`ja}DoRK2RNKgaoE'{\0";
	char inp[64];
	printf("Hello hacker.\n");
	printf("Enter what you think the password is, if you're so smart\n");
	printf("I don't know if I wanna say crib drag or known plaintext or something...\n");
	scanf("%s", inp);
	for (int i = 0; i < strlen(inp); i++) {
		inp[i] = inp[i] ^ 0x6;
	}
	if (!strcmp(inp,lines)) {
		printf("Yep, and now you know the flag! Go input that on the site!\n");
		exit(0);
	}
	printf("WTF is %s supposed to mean!\n", inp);
	exit(1);
}

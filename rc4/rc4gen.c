#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "rc4.h"

#define KL 16			//key length (no. of bytes)
#define MAX_BYTES 5000 

int main(int argc, char **argv)
{
	int i, j, n_bytes, l, kl;
	char k[3];
	byte K[KL], KS[MAX_BYTES];

	if (argc != 3) {
		printf("usage: rc4gen <key> <length of key-stream>\n");
		return 0;
	}
	kl = (strlen(argv[1])-2)/2;
	for (i = 0; i < kl; ++i) {
		k[0] = argv[1][2*i+2];
		k[1] = argv[1][2*i+3];
		k[2] = '\0';
		K[i] = (byte)strtoul(k, NULL, 16);
	}
	n_bytes = atoi(argv[2]);
	ksa(K, kl);
	prga(KS, n_bytes);
	for (i = 0; i < n_bytes; ++i) {
		printf("%02X ", KS[i]);
	}
	printf("\n");
	return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "rc4.h"

#define KL 16			//key length (no. of bytes)
#define MAX_BYTES 10

int main(int argc, char **argv)
{
	int i, j, n_bytes = 5, n_trials = (int)1e6, freq[MAX_BYTES][256];
	byte K[KL], KS[MAX_BYTES];

	if (argc > 1) {
		n_bytes = atoi(argv[1]);
		if (argc > 2)
			n_trials = atoi(argv[2]);
	}

	srand(time(NULL));

	for (i = 0; i < n_trials; ++i) {
		for (j = 0; j < KL; ++j) {
			K[j] = (int)(((double)rand())/RAND_MAX * 256); // random key
		}
		ksa(K, KL);
		prga(KS, n_bytes);
		for (j = 0; j < n_bytes; ++j) {
			++freq[j][KS[j]];
		}
	}

	printf("Byte:\t");
	for (i = 0; i < n_bytes; ++i)
		printf("%dth\t", i+1);
	printf("\n");
	for (i = 0; i < 256; ++i) {
		printf("0x%02X\t", i);
		for (j = 0; j < n_bytes; ++j) {
			printf("%d\t", freq[j][i]);
		}
		printf("\n");
	}
	printf("\n");
	
	return 0;
}

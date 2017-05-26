#include <stdint.h>

typedef uint8_t byte;

byte S[256];
void ksa(byte *K, unsigned kl)
{
	int i, j = 0;
	byte t;

	for (i = 0; i < 256; ++i) {
		S[i] = i;
	}
	for (i = 0; i < 256; ++i) {
		j = (j + S[i] + K[i % kl])% 256;
		t = S[i];
		S[i] = S[j];
		S[j] = t;
	}
}

void prga(byte *KS, unsigned n)
{
	int i = 0, j = 0, k;
	byte t;

	for (k = 0; k < n; ++k)	{
		i = (i + 1) % 256;
		j = (j + S[i]) % 256;
		t = S[i];
		S[i] = S[j];
		S[j] = t;
		KS[k] = S[(S[i] + S[j]) % 256];
	}
}

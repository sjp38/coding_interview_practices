/*
 * Request: Implement a function that reverses a null-terminating string
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void reverse(char *str)
{
	int len, i, target;
	char tmp;

	for (len = 0; str[len] != '\0'; len++)
		;

	for (i = len - 1; i >= len / 2; i--) {
		target = len - i - 1;
		tmp = str[i];
		str[i] = str[target];
		str[target] = tmp;
	}

	return;
}

int main(void)
{
	char questions[5][5] = {"abcd", "abc", "ab", "a", ""};
	char *answers[] = {"dcba", "cba", "ba", "a", ""};
	int i;

	for (i = 0; i < sizeof(questions) / sizeof(questions[0]); i++) {
		reverse(questions[i]);
		if (strcmp(questions[i], answers[i])) {
			fprintf(stderr, "[FAIL] \'%s\' for %d question\n",
					questions[i], i);
			exit(1);
		}
		fprintf(stderr, "[PASS] \'%s\' for %d question\n",
				questions[i], i);
	}

	return 0;
}

#include "stdio.h"
#include <string.h>
#include <stdlib.h>

// https://www.acmicpc.net/problem/18185

// this code is wrong, i misunderstood Question.

void Q_18185() {
    unsigned int factory = 0;
    scanf("%u", &factory);

    char *ramens = malloc(sizeof(char) * factory * 2);
    scanf(" %[^\n]", ramens);

    int totalRamenPrice = 0;

    for (int i = 0; i < strlen(ramens); i += 2) { // 0 1 2 3 4 - 10
        if (ramens[i] == '1' && i + 2 < strlen(ramens)) {
            if (ramens[i + 2] == '1' && i + 4 < strlen(ramens)) {
                if (ramens[i + 4] == '1') {
                    totalRamenPrice += 7;
                    i += 4;
                    continue;
                } else {
                    totalRamenPrice += 5;
                    i += 2;
                    continue;
                }
            } else {
                // handling last two consecutive 1
                if (ramens[i + 2] == '1' && i + 2 == strlen(ramens) - 1) {
                    totalRamenPrice += 5;
                    i += 2;
                    continue;
                } else {
                    totalRamenPrice += 3 * ((int)ramens[i] - 48);
                    continue;
                }
            }
        }

        // handling last only one 1
        if (ramens[i] != '0' && i == strlen(ramens) - 1) {
            totalRamenPrice += 3 * ((int)ramens[i] - 48);
        } else if (ramens[i] != '0'){
            totalRamenPrice += 3 * ((int)ramens[i] - 48);
        }
    }
    printf("%d", totalRamenPrice);
    free(ramens);
}
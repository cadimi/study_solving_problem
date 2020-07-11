#include<stdio.h>

void Q_5585() {
    const unsigned int MONEY = 1000;
    unsigned int spend = 0;
    scanf("%u", &spend);

    unsigned int change = MONEY - spend;
    unsigned int count500 = 0;
    unsigned int count100 = 0;
    unsigned int count50 = 0;
    unsigned int count10 = 0;
    unsigned int count5 = 0;
    unsigned int count1 = 0;

    while (change > 0) {
        if (change / 500 > 0) {
            count500++;
            change -= 500;
            continue;
        } else if (change / 100 > 0) {
            count100++;
            change -= 100;
            continue;
        } else if (change / 50 > 0) {
            count50++;
            change -= 50;
            continue;
        } else if (change / 10 > 0) {
            count10++;
            change -= 10;
            continue;
        } else if (change / 5 > 0) {
            count5++;
            change -= 5;
            continue;
        } else if (change / 1 > 0) {
            count1++;
            change -= 1;
            continue;
        }
    }
    printf("%d", count500 + count100 + count50 + count10 + count5 + count1);
}
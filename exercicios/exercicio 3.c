#include <stdio.h>

int main()
{
    int a;
    scanf("%d", &a);
    if (a < 5)
    {
        printf("abacaxi");
    }
    else
    {
        printf("kiwi");
    }
    while (a >= 0)
    {
        printf("subtraindo 1!");
        a = a - 1;
    }
    printf("goodbye world!");
}
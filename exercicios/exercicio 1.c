#include <stdio.h>

int main()
{
    int linhas, coef = 1, espaco, i, j;

    printf("Digite o numero de linhas: ");
    scanf("%d", &linhas);

    i = 0;
    while (i < linhas)
    {
        espaco = 1;
        while (espaco <= linhas - i)
        {
            printf("  ");
            espaco = espaco + 1;
        }

        j = 0;
        while (j <= i)
        {
            if (j == 0)
            {
                coef = 1;
            }
            else
            {
                if (i == 0)
                {
                    coef = 1;
                }
                else
                {
                    coef = coef * (i - j + 1) / j;
                }
            }
            printf("%d", coef);
            j = j + 1;
        }
        printf("\n");
        i = i + 1;
    }
}
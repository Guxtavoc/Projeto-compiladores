#include <stdio.h>
int main()
{
    float a;
    float b;
    float c;

    printf("Digite o primeiro lado: ");
    scanf("%f", &a);

    printf("Digite o segundo lado: ");
    scanf("%f", &b);

    printf("Digite o terceiro lado: ");
    scanf("%f", &c);

    if ((a <= 0) || (b <= 0) || (c <= 0))
    {
        printf("Valores devem ser positivos");
    }
    else
    {
        if (((a + b) <= c) || ((a + c) <= b) || ((b + c) <= a))
        {
            printf("Nao forma um triangulo");
        }
        else
        {
            printf("Forma um triangulo");
        }
    }
}
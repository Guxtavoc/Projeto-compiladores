#include <stdio.h>
int main()
{
    float a, b, c;

    printf("Digite o primeiro lado: ");
    scanf("%f", &a);

    printf("Digite o segundo lado: ");
    scanf("%f", &b);

    printf("Digite o terceiro lado: ");
    scanf("%f", &c);

    if ((a <= 0) || (b <= 0) || (c <= 0))
    {
        printf("Erro: Valores devem ser positivos");
    }
    else
    {
        if (((a + b) <= c) || ((a + c) <= b) || ((b + c) <= a))
        {
            printf("Medidas invalidas");
        }
        else
        {
            if ((a == b) && (b == c))
            {
                printf("Triangulo equilatero valido");
            }
            else
            {
                if ((a == b) || (a == c) || (b == c))
                {
                    printf("Triangulo isosceles valido");
                }
                else
                {
                    printf("Triangulo escaleno valido");
                }
            }
        }
    }
}
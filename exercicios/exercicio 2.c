#include <stdio.h>

int main() {
    float a, b, c;
    
    printf("Digite tres valores decimais positivos: ");
    scanf("%f%f%f", &a, &b, &c);
    
    if (a <= 0 || b <= 0 || c <= 0) {
        printf("Erro: Valores devem ser positivos\n");
    } else {
        if ((a + b > c) && (a + c > b) && (b + c > a)) {
            if (a == b && b == c) {
                printf("Triangulo equilatero valido\n");
            } else {
                if (a == b || a == c || b == c) {
                    printf("Triangulo isosceles valido\n");
                } else {
                    printf("Triangulo escaleno valido\n");
                }
            }
        } else {
            printf("Medidas invalidas\n");
        }
    }
    
    // Testando loop enquanto
    int contador = 0;
    while (contador < 3) {
        printf("Teste while: %d\n", contador);
        contador = contador + 1;
    }
    
    return 0;
}
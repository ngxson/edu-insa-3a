#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct point {
    char nom;
    int x;
    int y;
};

void init(struct point ***plan, int nb);

int main() {
    int arr[] = {0,1,2,3};
    int *n = arr;
    printf("%d\n", n);
}
#include <stdio.h>

int main() {
    int arr[] = {0,0xdeadbeef,2,3};
    int *n = arr;
    printf("%d\n", n);
    printf("%d\n", n+1);
    printf("%d\n", ((char *)n)+1);

    for (int i=0; i<4*4; i++) {
        char *tmp = (char *) (((char *)n)+i);
        printf("%02x ", *tmp & 0xFF);
        if (i%4 == 3) printf("\n");
    }
}

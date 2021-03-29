#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, char* argv[])
{
    char buffer[64];
    strcpy(buffer, argv[1]);
    printf("%s\n", buffer);
    printf("%p\n", buffer);
    return 0;
}

// gcc -g -fno-stack-protector -z execstack simple.c -o simple
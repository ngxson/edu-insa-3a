#include <stdio.h>
#include <stdlib.h>

int main(){
   int var = 10;
   int *p = malloc(2*sizeof(int));

   printf("address of main(TEXT SEGMENT): %p\n", main);
   printf("address of p(HEAP SEGMENT):%p\n", p);
   printf("address of var(STACK SEGMENT): %p\n", &var);

   return 0;
}
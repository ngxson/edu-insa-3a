#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(int argc, char **argv) {
  char buffer[400];
  if(argc != 2) {
    printf("nb arguments non suffisant\n");
    exit(0);
  }
  //printf("%p\n", buffer);
  strcpy(buffer, argv[1]);
  //printf("%s\n", buffer);
  return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
  int numberOfConnectionDescriptor = socket(AF_INET, SOCK_STREAM, 0);
  struct sockaddr_in myLocalExtremity;
  char buf[1024];
  myLocalExtremity.sin_family = AF_INET;
  myLocalExtremity.sin_port = htons(9999);
  myLocalExtremity.sin_addr.s_addr = htonl(INADDR_ANY);
  if (bind(numberOfConnectionDescriptor, (struct sockaddr *) &myLocalExtremity, sizeof(myLocalExtremity)) < 0) {
    perror("bind");
    exit(EXIT_FAILURE);
  }
  listen(numberOfConnectionDescriptor, 1);
  printf("listening");
  int bytes = 0;
  while (1) {
  }
  return 0;
}


    /*bytes = read(numberOfConnectionDescriptor, buf, sizeof(buf));
    if (bytes > 0) {
      buf[bytes] = 0;
      printf("%s", buf);
    }*/
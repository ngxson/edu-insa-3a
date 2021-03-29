#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <unistd.h>

#include "TD2.h"

int main(int argc, char **argv){
  int numberOfConnectionDescriptor;
  int nDescClientConnection, lenExt;
  struct sockaddr_in myLocalExtremity;
  struct sockaddr_in distantExtremity;
    
  // Création du descripteur dans le domaine Internet pour faire du flux d'octets
  if((numberOfConnectionDescriptor = socket(AF_INET,SOCK_STREAM,FREE_PROTOCOL)) < ZERO){
    perror("Wrong creation of the descriptor for stream on the Internet using the recommanded protocol.\n");
    exit(errno);
  }
  printf("The entry number for the network descriptor is %d\n",numberOfConnectionDescriptor);

  /* Remplissage de la structure sockaddr_in */
  myLocalExtremity.sin_family = AF_INET;
  myLocalExtremity.sin_port = htons(PORT);
  if(inet_pton(AF_INET,LOCAL_COMM,&(myLocalExtremity.sin_addr.s_addr)) <= ZERO){
    perror("Wrong string conversion of the Internet address included in the local extremity.\n");
    exit(errno);
  }
  // Affectation du sockaddr au descripteur
  if((bind(numberOfConnectionDescriptor,(struct sockaddr*)&myLocalExtremity,(socklen_t)sizeof(myLocalExtremity)))< ZERO){
    perror("Cannot bind the local extremity");
    exit(errno);
  }
  // On écoute
  if((listen(numberOfConnectionDescriptor,BUFFER_LEN))<ZERO){
    perror("Cannot wait the incoming connection requests on the connection descriptor");
    exit(errno);
  }

  char buf[64];
  char receivedBuffer[BUFFER_LEN] = {0};
  int nBytesRead, writeResult;

  while(TRUE) {
    lenExt = sizeof(distantExtremity);
    nDescClientConnection = accept(
      numberOfConnectionDescriptor,
      (struct sockaddr *) &distantExtremity,
      &lenExt
    );

    if (nDescClientConnection < ZERO) {
      perror("Cannot accept the incoming connection");
      exit(errno);
    }

    printf("Distance addr=%s port=%d fd=%d\n",
      inet_ntop(AF_INET, &distantExtremity.sin_addr, buf, sizeof(buf)),
      ntohs(distantExtremity.sin_port),
      nDescClientConnection
    );

    while(TRUE) {
      nBytesRead = read(nDescClientConnection, receivedBuffer, BUFFER_LEN);
      if (nBytesRead == 0) {
        printf("!! Connection lost !!\n");
        break; // sortir et retourner vers "accept"
      }
      receivedBuffer[nBytesRead]='\0'; /* car "read" ne marque pas la fin de la chaîne (par un caractère nul), il faut ajouter un caractère nul soi-même  */
      printf("%s", receivedBuffer);

      char begin[] = "Received:";
      char end[] = "\n";
      // écrire la chaine "Received:"
      writeResult = write(nDescClientConnection, begin, sizeof(begin));
      // écrire la chaine receivedBuffer qu'on a recu avant
      writeResult = write(nDescClientConnection, receivedBuffer, sizeof(receivedBuffer));
      // écrire caratère de saute de la ligne
      writeResult = write(nDescClientConnection, end, sizeof(end));

      if (writeResult < ZERO) {
        perror("Cannot write data");
        exit(errno);
      }
    }
  }
}

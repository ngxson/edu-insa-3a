/* (C) Christian Toinard INSA CVL. 2018. To be completed with a consistent management of maxNDescSet... and also prevent holes in the inputNDescSet set */

#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>
#include <sys/select.h>
#include <sys/time.h>
#include <unistd.h>
#include <errno.h>
#include <stdlib.h>

#define BINDFAIL 1
#define KO 2
#define OK 0
#define DISCONNECTED 1

#define MMax(x, y) ((x) > (y) ? x : y)


int messageProcessing(int desc, fd_set *NDescSet, int minNDescSet, int maxNDescSet, int demand)/*5*/
{
	char buf[BUFSIZ];
	int read_ret;

	/* A message must be available on the descriptor number desc */
	if((read_ret = read(desc, buf, sizeof(buf))) > 0)
	{
		buf[read_ret] = '\0';
		printf("Message from the client [%d] : \"%s\"\n", desc, buf);

		/* Must forward the message to all the connected clients */

		for(int i = minNDescSet; i < maxNDescSet + 1; i++)
		{
			if(i != demand) /*TO BE COMPLETED : TEST IF i IS A WRITABLE NDesc */
			{
				if((read_ret = write(i, buf, read_ret)) > 0)
				{
					printf("Forwarded message to client [%d]: \"%s\"\n", i, buf); 
				}

				else
				{
					printf("Writing error on descriptor: %s\n", strerror(errno));
					return KO;
				}
			}
		}
	}

	else if (read_ret == 0)
	{
		printf("End of connexion for client [%d].\n", desc); 
		return DISCONNECTED;/*6*/
	}

	else
	{
		perror("read()");
		exit(EXIT_FAILURE);
	}

	return OK;
}


int main(int argc, char const *argv[])
{
	fd_set inputNDescSet;			// The set of descriptor numbers that correspond to input descriptors
	fd_set activeInputNDescSet; // The active set of descriptor numbers in order to have a working copy of the input set
	int nbActive;			// Count the descriptor numbers that are active 
	int nbFoundActiveNDesc;		// Count the found descriptor numbers that are active 
	int maxNDescSet;				// Gives the maximum descriptor number that is present in the readable set
	int minNDescSet;				// Gives the minimum descriptor number that is present in the readable set

	int demand = socket(AF_INET, SOCK_STREAM, 0);
	if(demand == -1)
	{
		perror("socket()");
		exit(EXIT_FAILURE);
	}

	printf("The descriptor number for waiting the demand of connection: %d.\n", demand);

	struct sockaddr_in extremiteLocale;
	extremiteLocale.sin_family      = AF_INET;
	extremiteLocale.sin_addr.s_addr = INADDR_ANY;
	extremiteLocale.sin_port        = htons(atoi(argv[1])); /*PORT NUMBER PASSED AS THE FIRST ARGUMENT */

	if(bind(demand, (struct sockaddr*)&extremiteLocale, sizeof(extremiteLocale)) != 0)
	{
		perror("bind()");
		return BINDFAIL;
	}

	socklen_t lengthInternetExtremity = sizeof(struct sockaddr_in);
	if(getsockname(demand, (struct sockaddr*)&extremiteLocale, &lengthInternetExtremity) == -1)
	{
		perror("getsockname()");
		exit(EXIT_FAILURE);
	}

	listen(demand, 1);

	FD_ZERO(&inputNDescSet);/*1*/
	FD_SET(demand, &inputNDescSet);/*1*/
	maxNDescSet = demand;/*TO BE COMPLETED*/
	minNDescSet = demand;/*TO BE COMPLETED*/

	printf("Size of 'inputNDescSet': %zu.\n", sizeof(fd_set));

	while(1)
	{
		printf("\n\n");


		printf("The current maximum value for the readable descriptor numbers: %d.\n", maxNDescSet);

		for(int i = minNDescSet; i < maxNDescSet + 1; i++)/*2*/
		{
			if(FD_ISSET(i, &inputNDescSet)) /* TEST IF i IS IN THE INPUT SET*/
			{
				printf("[%d] in inputNDescSet\n", i);
			}

			else
			{
				printf("[%d] is not in inputNDescSet\n", i);
			}
		}

		printf("\n\n");

		FD_ZERO(&activeInputNDescSet);
		memcpy(&activeInputNDescSet, &inputNDescSet, sizeof(fd_set)); //FD_COPY(&inputNDescSet, &activeInputNDescSet/*IN ORDER TO HAVE A WORKING SET CORRESPONDING TO THE INPUT SET i.e. THE WORKING SET WILL CONTAIN THE ACTIVE DESCRIPTORS*/);

		nbActive = select(maxNDescSet + 1, &activeInputNDescSet, NULL, NULL, NULL/*IN ORDER TO GET BACK AN ACTIVE SET WITHIN THE WORKING ACTIVE INPUT SET*/); /*6*/
		nbFoundActiveNDesc = 0;
		int desc = minNDescSet, ear;
		struct sockaddr_in extDist;

		printf("Current count of active descriptor numbers: %d.\n", nbActive);

		while(nbFoundActiveNDesc != nbActive) /* SEARCHING ALL THE ACTIVE DESCRIPTORS */
		{
			if(FD_ISSET(desc, &activeInputNDescSet))
			{
				printf("[%d] est actif\n", desc);

				if(desc == maxNDescSet)/* THE FIRST KIND OF INPUT DESC*/
				{
					ear = accept(demand, (struct sockaddr*)&extDist, &lengthInternetExtremity); /* TO BE COMPLETED */

					printf("A new connection on : %d.\n", ear);

					if(getsockname(ear, (struct sockaddr*)&extDist, &lengthInternetExtremity) == -1)
					{
						perror("getsockname()");
						exit(EXIT_FAILURE);
					}

					printf("The new client extremity: %s:%d.\n", inet_ntoa(extDist.sin_addr), ntohs(extDist.sin_port));

					FD_SET(ear, &inputNDescSet);
					maxNDescSet = MMax(ear, maxNDescSet); 
				}

				else
				{
					switch(messageProcessing(desc, &inputNDescSet, minNDescSet, maxNDescSet, demand))/*5*/
					{
						case DISCONNECTED:/*7*/
							close(desc);
							FD_CLR(desc, &inputNDescSet); /* TO BE COMPLETED */

							if(desc == maxNDescSet)
							{
								maxNDescSet = desc - 1; 
							}
							else /* WHAT IS THE PURPOSE OF THIS CODE */
							{
								FD_SET(dup(maxNDescSet), &inputNDescSet);
								close(maxNDescSet);
								maxNDescSet--;
							}

							printf("The maximum value for the descriptor numbers: %d.\n", maxNDescSet); 
							break;

						default:
							break;
					}
				}

				nbFoundActiveNDesc++;
			}

			else
			{
				printf("[%d] is inactive.\n", desc);
			}

			desc++;
		}
	}
}
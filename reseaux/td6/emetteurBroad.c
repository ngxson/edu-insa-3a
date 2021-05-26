// All Right reserved: this code is written by Christian Toinard : christian.toinard(at)insa-cvl.fr
// Any usage without citation will be prosecuted in accordance with the local law.
#include <sys/errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <signal.h>
#include <net/if.h>
#include <netinet/in.h>
#include <netdb.h>
#include <stdlib.h>
#include <signal.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <sys/ioctl.h>
#include <arpa/inet.h>

#define BUFFERSIZE 1024

typedef void (*sighandler_t)(int);

void catch(void)
{
	exit(EXIT_SUCCESS);
}

int main()
{
  signal(SIGINT,(sighandler_t)catch);

    //Question 2.1
	char buffer[BUFFERSIZE];
	struct ifconf ifc;
	ifc.ifc_len= sizeof(buffer);
	ifc.ifc_buf= buffer;

  int sdemande;
    //Question 2.2
	if ((sdemande = socket(AF_INET, SOCK_DGRAM, 0)) < 0)
	{
		perror("socket()");
		exit(EXIT_FAILURE);
	}

	int on = 1;
	//Question 2.3
	if(setsockopt(sdemande, SOL_SOCKET, SO_BROADCAST, &on, sizeof(on)) < 0)
	{
    perror("setsockopt()");
		exit(EXIT_FAILURE);
	}

	//Question 2.4
	ioctl(sdemande, SIOCGIFCONF, (char*)&ifc);

	//Question 2.7
	struct ifreq *ifr;
	ifr= ifc.ifc_req;

	//Question 2.8
	int n= ifc.ifc_len/sizeof(*ifr);
	for(; --n >= 0 ; ifr++) {

        ioctl(sdemande, SIOCGIFFLAGS, (char*)ifr);


				if(((ifr->ifr_flags & IFF_UP) == 0) || (ifr->ifr_flags & IFF_LOOPBACK) || (ifr->ifr_flags & IFF_POINTOPOINT) || ((ifr->ifr_flags & IFF_BROADCAST) == 0))
        {
            continue;
        }

        //Question 2.10
				ioctl(sdemande, SIOCGIFBRDADDR, (char*)ifr);

        //Question 2.11
        struct sockaddr_in dst;
        bcopy(&ifr->ifr_broadaddr, &dst, sizeof(ifr->ifr_broadaddr));
        dst.sin_family = AF_INET;
        dst.sin_port = htons(5011);;
        //Question 2.12
        sendto(sdemande, "Bonjour", 7, 0, (struct sockaddr*)&dst, sizeof(dst));
	}
	return 0;
}

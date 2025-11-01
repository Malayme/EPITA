#include <stdio.h>
#include <error.h>
#include <stdlib.h>

#include <pthread.h>

void *saluer(void *arg){
    printf("trd : %lu : bonjour %s !\n", pthread_self(), (char *) arg);
    // pthread_exit(NULL);
    return NULL;
}

int main(int argc, char *argv[])
{
    printf("main : pthread_self() = %lu\n", pthread_self());

    //créer un thread par argument
    pthread_t ids[128];
    printf("main : lancement des threads\n");

    for (int i = 1; i < argc; i++)
    {
        int statut = pthread_create(&ids[i], NULL, saluer, argv[i]);
        if(statut != 0)
            error(1, status, "pthread_create");

        printf("main : thread %lu créé\n", ids[i]);
    }

    return 0;
}

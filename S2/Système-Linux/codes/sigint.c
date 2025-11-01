//Ecrire un programme qui capte (catch) SIGINT(ctrl-C) et affiche "SIGINT reçu"

#include <stdio.h>
#include <signal.h>
#include <strings.h>

//gestion routine SIGINT
void sigint_handler(int signal)
{
    if (signal == SIGINT)
    {
        printf("\nSIGINT Intercepté !\n");
    }
}

void set_signal_action(void)
{
    //décla struct sigaction
    struct sigaction act;

    //met à 0 tous les bits pour éviter les surprise
    bzero(&act, sizeof(act));

    //Invoquer handler quand on a le signal
    act.sa_handler = &sigint_handler;

    //Structure à prendreu signal
    sigaction(SIGINT, &act, NULL);
}

int main(void)
{
    //Change m'action à SIGINT
    set_signal_action();

    //Boucle infinie pour pouvoir faire Ctrl-C
    while(1)
        continue;

    return 0;
    
}

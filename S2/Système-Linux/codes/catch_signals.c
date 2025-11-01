#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>


void handle_sigterm(int sig) {
    printf("Received SIGTERM. Cleaning up ....\n", sig);
    exit(0);
}
void handle_usr1(int sig){
    printf("Received SIGUSR1, thanks \n", sig);
}
int main(){
    signal(SIGTERM, handle_sigterm);
    signal(SIGUSR1, handle_usr1);

    while(1){
        printf("Running...\n");
        sleep(2);
    }
}




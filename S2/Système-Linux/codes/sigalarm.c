#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>



void hdl_sigalarm(int sig){
    printf("Time's up! \n");
    exit(0);
}

int main(){
    signal(SIGALRM, hdl_sigalarm);
    alarm(15); //15 seconds
    pause();
}

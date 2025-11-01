#include <stdio.h>
#include <signal.h>
#include <err.h>
#include <unistd.h>

void traitement_signal(int signal) {
    printf("Reception signal %d\n", signal);
}

int main(int argc, char *argv[]) {
    struct sigaction description;

    description.sa_handler = traitement_signal;
    description.sa_flags = 0;
    sigemptyset(&description.sa_mask);

    int retour = sigaction(SIGINT, &description, NULL);

    if (retour == -1) {
        err(1, "sigaction");
    }

    for (int i = 0; 1; i++) {
        sleep(1);
        printf("i = %d\n", i);
    }

    return 0;
}

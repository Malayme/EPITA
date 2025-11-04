#include <stdio.h>
#include <stdlib.h>

struct Arretes{
    int dest;
    int poids;
    struct Arretes* next;
};
struct GraphPonder{
    int value;
    struct Arretes* listeArretes;
};

int bellman(struct GraphPonder* graph){
    int src = graph->value;
    int poids1 = graph->listeArretes->poids;

    int i = 0;
    while( i < t){

    }

}


int main(){



    return 0;

}
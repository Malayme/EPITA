#include <stdio.h>
#include <stdlib.h>

#include "../src/fonctions.h"

// Teste l'initialisation du plateau et vérifie que toutes les cases sont bien vides
int test_init_plateau()
{
    int plateau[Taille_plateau][Taille_plateau];
    int plateau_test[Taille_plateau][Taille_plateau] = {
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}
        };
    // Test initialisation plateau
    initialiser_plateau(plateau);
    int tests = 0;
    for (int i = 0; i < Taille_plateau; i++)
    {
        for (int j = 0; j < Taille_plateau; j++)
        {
            if (plateau[i][j] != plateau_test[i][j])
            {
                tests++;
            }
        }
    }
    if (tests != 0)
    {
        printf("test initialiser_plateau valide : NOK\n");
        return 0;
    }
    printf("test initialiser_plateau valide : OK\n");
    return 1;
}

// Teste la rotation d'une pièce dans le sens horaire et vérifie son exactitude.
int test_turn_piece_H()
{
    struct piece piece_test;
    int piece_1[5][5] = 
    {
        {0,0,1,0,0},
        {0,0,1,0,0},
        {0,0,1,0,0},
        {0,0,1,0,0},
        {0,0,0,0,0}
    };
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            piece_test.piece[i][j] = piece_1[i][j];
        }
    }

    int piece_temp[5][5] = {
        {0,0,0,0,0},
        {0,0,0,0,0},
        {0,1,1,1,1},
        {0,0,0,0,0},
        {0,0,0,0,0}
    };

    turn_piece_H(&piece_test);
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (piece_temp[i][j] !=piece_test.piece[i][j] )
            {
                printf("La piece ne tourne pas correctement das le sens horraire : NOK\n");
                return 0;
            }
        }
    }
    printf("La piece tourne correctement dans le sens horraire : OK\n");
    return 1;
}

// Teste la rotation d'une pièce dans le sens anti-horaire et vérifie son exactitude.
int test_turn_piece_AH()
{
    struct piece piece_test;
    int piece_1[5][5] = 
    {
        {0,0,1,0,0},
        {0,0,1,0,0},
        {0,0,1,0,0},
        {0,0,1,0,0},
        {0,0,0,0,0}
    };
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            piece_test.piece[i][j] = piece_1[i][j];
        }
    }
    int piece_temp[5][5] = {
        {0,0,0,0,0},
        {0,0,0,0,0},
        {1,1,1,1,0},
        {0,0,0,0,0},
        {0,0,0,0,0}
    };
    turn_piece_AH(&piece_test);
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (piece_temp[i][j] !=piece_test.piece[i][j] )
            {
                printf("La piece ne tourne pas correctement das le sens anti horraire : NOK\n");
                return 0;
            }
        }
    }
    printf("La piece tourne correctement dans le sens anti horraire : OK\n");
    return 1;
}

// Teste l'inversion horizontale d'une pièce et vérifie son exactitude.
int test_inverse_piece()
{
    struct piece piece_test;
    int piece_1[5][5] = 
    {
        {0,0,0,0,0},
        {0,1,0,0,0},
        {0,1,1,1,0},
        {0,0,1,0,0},
        {0,0,0,0,0}
    };
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            piece_test.piece[i][j] = piece_1[i][j];
        }
    }

    int piece_temp[5][5] = {
        {0,0,0,0,0},
        {0,0,0,1,0},
        {0,1,1,1,0},
        {0,0,1,0,0},
        {0,0,0,0,0}
    };
    inverse_piece(&piece_test);
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (piece_temp[i][j] !=piece_test.piece[i][j] )
            {
                printf("La piece ne s'inverse pas correctement : NOK\n");
                return 0;
            }
        }
    }
    printf("La piece s'inverse a merveille : OK\n");
    return 1;
}

// Teste la fonction qui détermine le gagnant en fonction des scores.
int test_winner()
{
    int j1 = 1;
    int j2 = 1;
    int j3 = 10;
    int j4 = 1;
    if (Winner(j1,j2,j3,j4) != 3)
    {
        printf("Le calcul de gagnant marche : NOK\n");
        return 0;
    }
    printf("le calcul du gagnant marche : OK\n");
    return 1;
}

// Teste la fonction qui gère les égalités entre joueurs pour le calcul du gagnant.
int test_winner_egalite()
{
    int j1 = 10;
    int j2 = 1;
    int j3 = 10;
    int j4 = 1;

    if (Winner(j1,j2,j3,j4) != 1)
    {
        printf("le calcul du gagnant_egalite marche : NOK\n");
        return 0;
    }
    printf("le calcul du gagnant_egalite marche : OK\n");
    return 1;
}

// Teste le calcul des scores pour chaque joueur en fonction du plateau.
int test_score()
{
    int plateau[24][24] = {
        {1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        {4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3},
    };
    int S1 = 0;
    int S2 = 0;
    int S3 = 0;
    int S4 = 0;
    score(plateau,&S1,&S2,&S3,&S4);
    if (S1 != 1 || S2 != 1 || S3 != 1 || S4 != 1)
    {
        printf("Le calcul du score marche : NOK\n");
        return 0;
    }
    printf("Le calcul du score marche : OK\n");
    return 1;
}

int main(void)
{
    int score = 0;
    score += test_init_plateau();
    score += test_turn_piece_H();
    score += test_turn_piece_AH();
    score += test_inverse_piece();
    score += test_winner();
    score += test_winner_egalite();
    score += test_score();

    

    printf("Score final des tests : %d/7\n", score);

    return 0;
}

II] Algorithme "Divide and Conquier" :

Les algorithmes "Diviser pour régner" s'articule autour de l'idée :
1) Découper le problème en sous-problèmes plus simples,
2) Résoudre les problèmes simples
3) Combinaison des solutions simples pour obtenir une solution au problème initial

L'étape 1), dite "diviser", est effectuée de façon récursive, jusqu'à l'obtention de problèmes avec des solutions évidentes.

Exemple : Tri fusion
Le tri fusion est basée sur l'idée suivante: Etant donnés tabA, tabB, deux tableaux triés, il est simple de les combinés pour avoir un tableau trié.

1) On compare tabA[0] et tabB[0] ce qui nous permet de déterminer tab[0].
2) Ainsi de suite, (à l'infini) => $O(nA +nB)$
-> Comment obtenir des tableaux triés ?

Fusion : 1) On découpe le tableau en divisant sa taille par 2, jusqu'à obtenir des tableaux de taille 1.
2) On recombine les tableaux grâce à la remarque précédente
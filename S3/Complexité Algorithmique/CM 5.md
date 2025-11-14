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
MergeSort

Implémentation : 

```C
int *merge(int *tabA, int nA, int *tabB, int nB){
	int *tabC= malloc(sizeof(int)*(nA + nB));
	int i =0;                     //pour parcourir tabA
	int j=0;                      //pour parcourir tabB
	for(int k=0; k<nA+nB; k++){
		if(i>=nA){
			tabC[k]=tabB[j];
			j++;
		}else if(j>=nB){
			tabC[k]=tabA[i];
		}else if(tabA[i]<tabB[j]){
			tabC[k]=tabA[i];
			i++;	
		}else{
			tabC[k]=tabB[j];
			j++;
		}
	}
	return tabC; //Complexité en \Theta(n)
}
```

```C
int * mergeSort(int * tab, int n){
	if (n <= 1){
		return tab;
	}else{
		int nA = n/2;
		int nB = n-nA;
		int *tabA = malloc(sizeof(int) * nA);
		for(int i=0; i < nA; i++){ tabA[i] = tabB[i]; }
		int *tabB = malloc(sizeof(int) * nB);
		for (int i=0; i < nB; i++){ tabB[i] = tab[i + nA]; }
		
		return merge(mergeSort(tabA, nA), mergeSort(tabB, nB));
	}
}
```
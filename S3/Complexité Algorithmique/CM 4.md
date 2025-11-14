Rappel de calcul de la complexité un algorithme :

```C
void selection(int tab[], int n){
	int temp=0;                             // \Theta(1)
	int indMax=0;                           // \Theta(1)
	for(int i=0; i<n;i++){                  // \Theta(n)
		indMax=0;                           // \Theta(n)
		for(int j=1;j<n-&;j++){             // \Theta(n^2)
			if(tab[j]>tab[indMax]){         // \Theta(n^2)
				indMax=j;                   // O(n^2)
			}
		}
		if(indMax != n-i-1){                // \Theta(n)
			temp=tab[indMax];               // O(n)
			tab[indMax] = tab[n-i-1];       // O(n)
			tab[n-i-1]=temp;                // O(n)
		}
	}
}
```

=> $T(n) = 2\Theta(n^2) + O(n^2) + 2\Theta(n) + 3O(n) +2\Theta(1)$
       $=\Theta(n^2)+O(n^2)+\Theta(n)+O(n)+\Theta(1)$
      $=\Theta(n^2)+O(n^2)$
      $=\Theta(n^2)$ 

```C
int algo1(int n){
	int cpt=0;                              // \Theta(1)
	for(int i=0;i<n;i++){                   // \Theta(n)
		int m=2*n;                          // \Theta(n)
		for(int j=0;j<m;j++){               // \Theta(n^2)
			int even=j%2;                   // \Theta(n^2)
			if(even==0){                    // \Theta(n^2)
				for(int k=0;k<m;k++){       // O(n^3)
					cpt++;                  // O(n^3)
				}
			}
		}
	}
	return cpt;                             // \Theta(1)
}

```

=>$T(n)=2\Theta(1)+2\Theta(n)+3\Theta(n^2)+2O(n^3)$
    $=\Theta(1)+\Theta(n)+\Theta(n^2)+O(n^3)$
     $=\Theta(n^2)+O(n^3)$
     $=O(n^3)$

```C
int binarySearch(int tab[], int n, int value, int first, int last){
	if(first>last){
		return 0;
	}else{
		int middle=(first+last)/2;       //division entière
		if(tab[middle] == value){
			return 1;
		}else if(value<tab[middle]){
			return binarySearch(tab, n, value, first, middle-1);
		}else{
			return binarySearch(tab, n, value, middle+1, last);
		}
	}
}
```

Nombre d'opérations pour un appel de binarySearch():
- l.2: 1 test,
- l.3: 1 return (pas au pire cas)
- l.5: 1 addition, 1 division, 1 déclaration, 1 affectation
- l.6: 1 test
- l.7: 1 return (qui ne correspond pas au pire cas)
- l.8: 1 test,
- l.9, 11: 1 opération arithmétique, 1 appel, 1 return
------------------
Au total, 10 opérations  élémentaires pour chaque appel

Nombre d'appels à binarySearch()

On définit la suite $S(n)$ telle que $S(n)$ le nombre d'appels à binarySearch() pour une instance de taille n.
On détermine la relation de récurrence vérifiée par $S(n)$.
$S(n)=1 + S(\frac{n}{2})$ (partie entière).
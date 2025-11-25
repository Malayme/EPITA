$O(g(n)) = {f(n) / \exists c \in \mathbf{R}_*^+, \exists n_0 \in \mathbf{N} / \forall n >= n_0, 0 =< f(n) =< c * g(n)}$ 

Exemple : $12n^3 + 5n^2 + 6 = O(n^3)$ 
On considère $n >= 1$, on a alors : 
$6 <= 6*n^3$ et
$5n^2 <= 5n^3$ et
$12n^3 <= 12n^3$
Donc : $12n^3 + 5n^2 + 6 <= 23n^3$

Exo : $4n^4 + 6n^2 +17n = O(n^4)$
Pour $n >= 1$, on a :
$4n^4 <= 4n^4$ et
$6n^2 <= 6n^4$ et
$17n <= 17n^4$

$4n^4 + 6n^2 + 17n <= 27n^4$ , Pour $n_0 = 1$ et $c = 27$ 

**Propriétés de $0(.)$ :**
(1) $\lambda = O(1); \lambda \in \mathbf{R}_*^+$
(2) $f(n) = O(f(n))$
(3) $O(f(n)) + O(g(n)) = O(f(n) + g(n))$
(4) $O(f(n)) + g(n) = O(max(f(n); g(n))$ 
(5) $O(f(n)) * O(g(n)) = O(f(n)*g(n))$
(6) $O(\lambda f(n)) = O(f(n))$ 

Exemple : $4n^4 + 6n^2 +17n = O(n^4)$ 
$4n^4 = O(4n^4) = 0(n^4)$ (propriété 2 et 6)
$6n^2 = O(6n^2) = O(n^2)$ (propriété 2 et 6)
$17n = O(17n) = O(n)$ (propriété 2 et 6)

$4n^4 + 6n^2 + 17n = O(n^4) + O(n^2) + O(n)$
             $= O(n^4 + n^2 + n)$ 
            $= O(max(n^4; n^2; n))$ 
             $= O(n^4)$

Exo : 1) Montrer que : $5n^2 + 6n + 7 = O(n^2)$

$5n^2 = O(n^2)$
$6n = O(n)$
$7 = O(1)$ 

Donc : $O(n^2 + n + 1) = O(max(n^2; n; 1)) = O(n^2)$

2) Simplifier : $O(10n^2+n) + O(n^3+3n)$
$= O(10n^2 + n + n^3 + 3n)$ 
$= O(n^3 + 10n^2 + 4n)$
$= O(n^3)$ (le max, avec grand n)

3) Simplifier : $O(n) + O(1000 log(n))$
$= O(n) + O(log(n))$
$= O(n + log(n))$
$= O(n)$

## "Omega" $\Omega (g(n))$
Soit $g(n)$, une fonction à réelles positives;
$\Omega(g(n))$ : l'ensemble des fonctions qui sont plus grandes que $g(n)$; à un coefficient près; à partir d'un certain rang.

$\Omega (g(n))$ : ${f(n) / \exists c \in \mathbf{R}_*^+, \exists n_0 \in \mathbf{N} / \forall n >= n_0; 0 <= c * g(n <= f(n))}$

Exemple : 

(1) $n = \Omega (n)$
Pour $n_0 = 1$, et $c =1$, on a : $\forall n >= n_0, 0 <= 1n <= n$
(2) $n^2 = \Omega (n)$
Pour $n_0 = 1$, et $c = 1$, on a : $\forall n >= n_0, 0 <= 1n <= n^2$
(3) $10n^3 + 5n^2 + n = \Omega(n^3)$
Pour $n_0$ et $c=1$, $\forall n >= n_0, 1n^3 <= 10n^3+5n^2+n$ 
$n^3 <= n^3+5n^2+n$ 

## "Theta" $\Theta (g(n))$ 
Soit $g(n)$, une fonction à valeurs réelles positives.
$\Theta(g(n))$: l'ensemble des fonctions qui ont le même comportement asymptotique que $g(n)$
$\Theta (g(n)) = {f(n) / \exists c_1 \in \mathbf{R}_+^* , \exists c_2 \in \mathbf{R}_+^* , \exists n_0 \in \mathbf{N} / \forall n >= n_à, 0 <= c_1 * g(n) <= f(n) <= c_2*g(n)}$

On a: $\Theta(g(n))=\Omega(g(n))\cap\Omega(g(n))$

## Analyse de la complexité avec O, $\Theta$ 
On peut analyser la complexité d'un algorithme en associant à chaque ligne $O(1), O(n), O(n^2)$... ou $\Theta(1),\Theta(n),\Theta(n^2)$...

```C
void insertionSort(int tab[], int n){
	int tpr = 0;                   // \Theta(1)  
	int ind = 0;                   //  \Theta(1)
	for (int i =1; i<n; i++){      // \Theta(n)
		ind = 1;                   // \Theta(n)
		while(ind >0 && tab [ind-1] > tab[ind]){       // O(n^2)
			tpr = tab[ind];            // O(n^2)
			tab[ind] = tab[ind-1];     // O(n^2)
			tab[ind-1] = tpr;          // O(n^2)
			ind --;                    // O(n^2)
			}
	}
}
```

La complexité totale de l'algorithme correspond à la somme des complexités de chaque ligne.
$T(n) = 2\Theta(1)+2\Theta(n)+5O(n^2)$ 
    $=\Theta(n)+O(n^2)$
    $=O(n^2)$ 



Pour résumer : Grand O = élément de droite plus grand que élément de gauche; Omega = élément de gauche plus grand que élément de droite; Theta = les deux éléments sont égaux
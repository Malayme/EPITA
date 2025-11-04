Dans le contexte du PCCH, on considère un graphe **pondéré** , orienté ou non.
Soit un graphe orienté et pondéré, $G = (X, U)$.
Pour chaque arc (i, j) $\in$ U, on note $w(i, j)$  le poids associé à l'arc $(i, j)$.
La fonction $w(.;.)$ est appelée ==__fonction de poids__==. 
Le poids d'un chemin  $\mu$ est la somme des poids des arcs de mu : $\sum_{(i,j)}{\in} w(i,j)$.

==__Définition__== : Soit $G = (X,U)$ un graphe orienté et $w(.;.)$ sa fonction de poids.
La recherche du plus court chemin entre deux sommets $i_0$ et $j_0$, consiste à ==__déterminer un chemin $\mu*$__== qui parmi les chemins allant de $i_0$ à $j_0$, possède ==__le poids__== minimal.

Exemple :  [[Schéma1.canvas|Schéma1]] 

==__Condition d'existence__== : 
Un ==__circuit absorbant__== est  un circuit dont le poids est ==__strictement négatif__==. Il existe un plus court chemin dans un graphe $G$, si $G$ ==__ne contient pas de circuit absorbant__==. 
-> Le circuit (4, 7, 6, 4) est un circuit absorbant de poids -3. (poid modifié entre 6 et 4).

$\mu_1 = (1, 4, 7, 6, 8)$ de poids 11.
$\mu_2 = (1, 4, 7, 6, 4, 7, 6, 8)$ de poids 8.
$\mu_2 = (1, 4, 7, 6, 4, 7, 6, 4, 7, 6, 8)$ de poids 5.

=> Lorsqu'il existe un circuit absorbant, il n'y a pas de plus court chemin.

Pour garantir l'existence d'un PCCH, on considère soit les graphes sans circuit (Bellman), soit les graphes sans valeurs négatives (Dijkstra).

==__ATTENTION__== : Il existe beaucoup de référence à un algorithme nommé Bellman-Ford.

Catégorie d'algorithmes: 
- Certains algorithmes calculent les PCCH d'une racine $i_0$ vers tous les autres sommets.
- D'autres algorithmes calculent les PCCH entres tout couple de sommet.

__Algorithme de Bellman :__ 
Dans le cas où le graphe ==__ne contient pas de circuit__==, on peut utiliser l'algorithme de Bellman.

- Ordre topologique des sommets.
		Soit un graphe orienté $G = (X, U)$, un ==__ordre topologique__== de $G$ est une numérotation $V (.)$ tel que $\forall (i, j) \in U$ on a $V(i) < V(j)$. 

Exemple :[[Schéma2.canvas|Schéma2]] 

- l'ordre naturel (1, 2, 3, 4, 5, 6, 7, 8).
n'est pas topologique (7, 6), (3, 2).
- (1, 3, 2, 4, 5, 7, 6, 8)
- (1, 4, 7, 3, 2, 5, 6, 8)

Il existe un ordre topologique dans $G \Leftrightarrow$ il n'existe pas de circuit dans $G$.
L'==ordre suffixe inverse== est un ordre topologique (si le graphe ne contient pas de circuit).

__Principe de l'algorithme de Bellman__.
L'algorithme de Bellman procède à un marquage des sommets: une marque $\lambda(j)$ st calculée durant l'algorithme pour chaque sommet $j$. A la fin de l'algorithme $\lambda(j)$ contient le poids d'un PCCH de $i_0$ vers $j$.

On considère que lordre (1,2, ..., n) est un cercle topologique.
Bellman suit alors les étapes suivantes:
- on marque le sommet 1 avec $\lambda(1) = 0$ .
- A l'itération $j$, on dértermine la marque de sommet $j$ avec : ==$\lambda(j) = min \lambda(i) + w(i, j) i \in N^- (j)$
- A la fin l'algorithme, $\lambda(j)$ contient le pods d'un PCCH de 1 vers $j$. 

$\lambda(4) = min (\lambda(1) + w(1, 3); \lambda(2) + w(2, 4); \lambda(3)+ w(3, 4))$ 
$\lambda(4) = 4$ 

| sommet | $\lambda(.)$ | parent (.) |
| ------ | ------------ | ---------- |
| 1      | 0            | /          |
| 4      | 1            | 1          |
| 7      | 4            | 4          |
| 3      | 2            | 1          |
| 2      | 3            | 3          |
| 5      | 2            | 2          |
| 6      | 6            | 2          |
| 8      | 10           | 6          |
PCCH (1, 3, 2, 6, 8)

Exo : 

1) Déterminer ordre topologique
2) Bellman

1 - (1, 2, 3, 4, 5, 6, 7,  8, 9)
2 - 

| sommet | $\lambda(.)$ | parent (.) |
| ------ | ------------ | ---------- |
| 1      | 0            | /          |
| 2      | 2            | 1          |
| 3      | 9            | 2          |
| 4      | -1           | 1          |
| 5      | 7            | 2          |
| 6      | 4            | 5          |
| 7      | 4            | 4          |
| 8      | 7            | 7          |
| 9      | 6            | 6          |
(1, 2, 5, 6, 9)

Complexité : ordre topologique par DFS : $O(n+n)$
marquage : $O(\sum_{i \in X} d(i)) = O(m) => O(n+m)+O(m)= O(n+m)$   
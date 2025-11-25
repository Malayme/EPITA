Exercice 1:
1) 1 - 2 - 4 - 3 - 5 - 6 - 8 - 10 - 7 - 9 - 11 - 12

| sommet | $\lambda()$ | P() |
| ------ | ----------- | --- |
| 1      | 0           | /   |
| 2      | 2           | 1   |
| 4      | 4           | 2   |
| 3      | 2           | 4   |
| 5      | 2           | 2   |
| 6      | 2           | 4   |
| 8      | 5           | 5   |
| 10     | 8           | 3   |
| 7      | 3           | 10  |
| 9      | 1           | 8   |
| 11     | 4           | 7   |
| 12     | 6           | 11  |
12 - 11 - 7 - 10 - 3 - 4 - 2 - 1
PCCH : 1 - 2 - 4 - 3 - 10 - 7 - 11 - 12
Poids du chemin : 6

## Algorithme de Djikstra
l'algorithme de Dijkstra est adopté aux graphes sans valeurs négatives (mais avec des circuits).
Il utilise des marques ==temporaires== associés aux sommets, ces marques évoluent au cours de l'algorithme et à chaque itération ==une des marques devient définitive==.

Etape 1 : On marque $\lambda(1)=0$ $\lambda(i)= +\infty  \forall i \ne 1$
Etape Quelconque:
On détermine le sommet i avec une marque temporaire minimale, et cette marque devient définitive.
On fait évaluer la marque des successeurs de i, avec : $\forall j \in N^+ (i)$
											$\lambda(j)=min(\lambda(j); \lambda(i)+\omega(i,j))$

A chaque itération, l'ensemble des sommets X est découpé en l'ensemble des sommets avec marque définitive, S et l'ensemble des marques temporaire, X \ S.

-------------------------------- 
$\lambda(*)$ : marque définitive
$\lambda(p)$ : p: prédecesseur

| Itération | $\lambda(1)$ | $\lambda(2)$ | $\lambda(3)$ | $\lambda(4)$ | $\lambda(5)$ | $\lambda(6)$ | $\lambda(7)$ | $\lambda(8)$ | Sommet selectionné |
| --------- | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------------ |
| 1         | $0^*$ (1)    | $\infty$     | $\infty$     | $\infty$     | $\infty$     | $\infty$     | $\infty$     | $\infty$     | 1                  |
| 2         | /            | 4 (1)        | 2 (1)        | $1^*$ (1)    | $\infty$     | $\infty$     | $\infty$     | $\infty$     | 4                  |
| 3         | /            | 4(1)         | 2$^*$ (1)    | /            | $\infty$     | $\infty$     | 4(4)         | $\infty$     | 3                  |
| 4         | /            | 3$^*$(3)     | /            | /            | $\infty$     | 7(3)         | 4(4)         | $\infty$     | 2                  |
| 5         | /            | /            | /            | /            | 4$^*$(2)     | 6(2)         | 4(4)         | $\infty$     | 5                  |
| 6         | /            | /            | /            | /            | /            | 6(2)         | 4$^*$(4)     | 14(5)        | 7                  |
| 7         | /            | /            | /            | /            | /            | 6$^*$(2)     | /            | 11(7)        | 6                  |
| 8         | /            | /            | /            | /            | /            | /            | /            | 10$^*$(6)    | 8                  |
PCCH : 1-3-2-6-8

Exercice 2

1) Djikstra
2) 1 - 2 - 3 - 4 - 9; Poids Total = 13

Exercice 3


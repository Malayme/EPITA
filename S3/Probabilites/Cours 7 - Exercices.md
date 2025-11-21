Exercice 1 : 
Soit X une variable aléatoire discrète admettant un moment d’ordre 2. Vérifier que la formule $Var(X) := E((X − E(X))^2)$ est bien définie.

$E(X-E(X))^2)=E(X^2-2XE(X)+E(X)^2)$
            $= E(X^2)-E(2XE(X))+E(E(X)^2)$
            $=E(X^2)-2E(X)E(X)+E(X)^2$
            $=E(X^2)-2E(X)^2+E(X)^2$
            $=E(X^2)-E(X)^2$
-> bien défini

Comm X a un moment d'ordre 2, X a un moment d'ordre 1, et la formule est bien défini.

Exercice 2 : Soit X une variable aléatoire discrète admettant un moment d’ordre 2. Montrer que si X est constante alors $Var(X) = 0$.

Soit $k \in R$ tq  $X = k$  alors $Var(X)=E(k^2)-E(k)^2$
                            $=k^2 -k^2$
                            $= 0$

Exercice 3.
On jette deux dés équilibrés à 6 faces. On note S la variable aléatoire qui calcule la somme des résultats des lancers obtenus. 
1. Quel est l’univers de cette expérience ? 
2. Déterminer la loi de probabilité de S. 
3. Calculer $F_S (5)$. 
4. Calculer l’espérance et la variance du double de S.

L'univers de cette expérience est de 2 à 12. $S(\Omega)=[2, 12]$ (interval entier)
$P(S=2)=1/36$
$P(S=3)=2/36$
$P(S=4)=3/36$
$P(S=5)=4/36$
$P(S=6)=5/36$
$P(S=7)=6/36$
$P(S=8)= 5/36$
$P(S=9)=4/36$
$P(S=10)=3/36$
$P(S=11)=2/36$
$P(S=12)=1/36$



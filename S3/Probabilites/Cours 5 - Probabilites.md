Exercice 1 :
1. Combien existe-t-il de nombre entier s’écrivant avec exactement k chiffres significatifs en base 2 ? Remarque : Lorsqu’on lit les nombres de gauche à droite, un chiffre significatif est un chiffre placé à droite du premier chiffre non nul. 
Il existe : $2^{k-1}$ possibilités

2. Combien existe-t-il de nombres entiers s’écrivant avec au plus k chiffres significatifs en base 2 ?
Il existe : $\sum_{i=1}^k 2^{i-1} = \sum_{i=0}^{k-1} 2^i$
3. Comment répondre rapidement à la question 2 sans faire de somme ? 
$2^k$ : nb de nb sur k bits; -1 : on enlève le zéro. 
4. Faire le lien avec l’ensemble des parties.
Soit $\Omega$ = {$\omega_1, ..., \omega_k$} un ensemble. 
On veut créer un sous-ensemble $\mathbf{A} \subset \Omega$.
Pour chaque sous-ensemble $\omega_i \in \mathbf{A}$.
On peut associer a $\mathbf{A}$ un vecteur $(b_1,...,b_k)$ tq $b_i=1$ si $\omega_i \in \mathbf{A}$ et $b_i=0$ sinon.
Comme vu a la Q.2, il existe $2^k$ vecteurs de ce type (on compte le vecteur nul, qui correspond a $\emptyset$).
On en déduit que : $Card(P(\Omega))=2^k$.

Exercice 2 : 
On considère un jeu de pile ou face infini : on tire une pièce à pile ou face une infinité de fois. Proposer un univers pour cette expérience.
$\Omega=$ {pile, face}$^\mathbf{N}$

Exercice 3 : 
On jette deux fois un dé équilibré à 6 faces (numérotées de 1 à 6). On considère les évènements E : "La somme des points obtenus est paire." F : "Le 3 est obtenu au moins une fois." 
1. Calculer P(E) et P(F ).
On note : $\mathbf{E_1}$ : "de 1 pair"
$\mathbf{E_2}$ : "de 2 pair"
On a : $\mathbf{P(E)}=\mathbf{P(E_1 \cap E_2 \cup \overline{E}_1 \cap \overline{E}_2)}$ (union disjointe)
		   $=\mathbf{P(E_1 \cap E_2)} + \mathbf{P(\overline{E}_1 \cap \overline{E}_2)}$
		   $= \frac{9}{36} + \frac{9}{36}$
		   $=\frac{1}{2}$
On note : 
$\mathbf{F}_1$: "de $1=3$"
$\mathbf{F}_2$: "de $2=3$"
alors : $\mathbf{P(F)} = \mathbf{P(F_1 \cup F_2)}$
        $= \mathbf{P(F_1)} + \mathbf{P(F_2)} - \mathbf{P(F_1 \cap F_2)}$
           $=\frac{1}{6} + \frac{1}{6} - \frac{1}{36}$
         $=\frac{11}{36}$
         
2. Donner la signification et la probabilité des évènements E ∩ F , E ∪ F , E ∩ $\overline{F}$ , E ∩ $\overline{F}$ ∪ $\overline{E}$.
$\mathbf{P(E \cap F)}= \frac{5}{36}$
$\mathbf(E \cup F)= \mathbf{P(E)} + \mathbf{P(F)}-\mathbf{P(E \cap F)}$
     $= \frac{1}{2} + \frac{11}{36} - \frac{5}{36}$
     $=\frac{4}{6}$
     $=\frac{2}{3}$
$(E \cap \overline{F})$ : $E= E \cap F \cup E \cap \overline{F}$
donc $\mathbf{P(E)} = \mathbf{P(E \cap F \cup E \cap \overline{F})}$
          $= \mathbf{P(E \cap F)} + \mathbf{P(E \cap \overline{F})}$
    alors $=\mathbf{P(E \cap \overline{F})} = \mathbf{P(E)}-\mathbf{P(E \cap F)}$
         $= \frac{1}{2}-\frac{5}{36}$
         $=\frac{13}{36}$
$E \cap \overline{F} \cup E = \mathbf{P(E \cap \overline{F})} + \mathbf{P(\overline{E})}$
         $= \frac{13}{36} + 1 - \mathbf{P(E)}$
         $=\frac{13}{36}+\frac{36}{36}-\frac{18}{36}$
         $=\frac{31}{36}$
Exercice 4 : Une urne contient 2 boules blanches et quatre boules noires. On tire successivement et au hasard toutes les boules de l’urne. Quelle est la probabilité que toutes les boules blanches soient tirées lors des 4 premiers tirages ?

Nombre de tirage total : $\frac{6!}{2! * 4!} = 15$
On note : 
$E$ : "2 b. blanches sur 4 premiers tirages"
$\overline{E}$ : "au moins 1 b. blanche sur 2 derniers tirages"
G : "2 b. blanche sur """""""""""""""""""""""""""""

On a $\mathbf{P(E)} = 1 - \mathbf{P(\overline{E})}$
         $=1- \mathbf{P(F \cup G)}$
         $= 1- (\mathbf{P(F}) + \mathbf{P(G)})$
         $= 1- \frac{8}{15} - \frac{1}{15}$
         $=\frac{6}{15}$

Exercice 5 : Soit Ω un ensemble de cardinal n ∈ N∗. Montrer qu’il y a $2^{n−1}$ éléments de cardinal pair dans P(Ω).
On a vu a l'ex 1 que $Card(P(\Omega))=2^n$
On avait representer les ss-ens de $\Omega$ par des nbs de $n$ chiffres en base 2.
Un nombre est pair en base 2 si son chiffre des unites est nul.
En faisant ce chiffre a 0, on garde $2^{n-1}$, d'ou le resultat.








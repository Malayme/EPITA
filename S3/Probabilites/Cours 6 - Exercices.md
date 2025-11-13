Exercice 1 : Dans une urne on a r ∈ N boules rouges et b ∈ N boules blanches. On tire deux boules sans remise. Quelle est la probabilité d’obtenir deux boules rouges ? Répondre avec deux méthodes : une utilisant les probabilités conditionnelles, l’autre non.

 Methode 1 : Probabilites Conditionnelles 
On definit :
$R_1$ : "boule rouge tirage 1"
$R_2$ : "boule rouge tirage 2"
$P(R_1 \cap R_2)=P(R_1)P(R_2 | R_1)$
          $=\frac{r}{r+b} \frac{r-1}{r+b-1}$

Methode 2 : Raisonnement avec arrangements 

$P(R_1 \cap R_2) \frac{r}{r+b}\frac{r-1}{r+b-1} = \frac{A_{2}{^r}}{A_{2}^{r+b}}$

Exercice 2 : 1. Démontrer soigneusement la formule de Bayes. 2. Dans une salle de classe il y a 40% d’étudiantes et 60% d’étudiants. Une étudiante sur trois porte des lunettes, un étudiant sur deux porte des lunettes. Quelle est la probabilité qu’une personne portant des lunettes prise au hasard soit une étudiante ?

1. Soient $(\Omega, P)$ un esp. proba. $A, B_1,...,B_n \subset \Omega$ de proba non nulles et tq $(B_1,...,B_n)$ partitionne $\Omega$ 
Soit $j \in [ 1~;~n ]$ 
$P(B_j|A)=\frac{P(B_j \cap A)}{P(A)}$  => proba conditionnelle au numerateur et proba totale au denominateur
        $=\frac{P(A|B_j)P(B_j)}{\sum_{i=1}^{n} P(A|B_i)P(B_i)}$

Formule de Bayes : $P(B_j | A) = \frac{P(A|B_j)P(B_j)}{\sum^{n}_{i=1}P(A|B_i)P(B_i)}$
2. On pose :
$E$ : "etre etudiante"
$L$ : "porter des lunettes"
On a : $P(E)=\frac{2}{5}$
$P(\overline{E})=\frac{3}{5}$
$P(E \cap L)=\frac{1}{3}$
$P(\overline{E} \cap L)=\frac{1}{2}$

On cherche : $P(E|L)$
On a :
$P(E|L)= \frac{P(E \cap L)}{P(L)}$
       $=\frac{P(L|E)P(E)}{P(L|E)P(E)+P(L|\overline{E})P(\overline{E})}$
       $=\frac{\frac{1}{3} * \frac{2}{5}}{\frac{1}{3}*\frac{2}{5}+\frac{1}{2}*\frac{3}{5}}$

Exercice 3 : Une urne contient 12 jetons numérotés de 1 à 12. On tire un jeton au hasard et on considère les évènements : A : "Le jeton porte un numéro pair." B : "Le jeton porte un numéro multiple de 3." 1. A et B sont-ils indépendants ? 2. On ajoute un treizième jeton numéroté 13, sans changer A ni B. A et B sont-ils indépendants ?

1. On a : $P(A)=\frac{6}{12} = \frac{1}{2}$
$P(B) = \frac{4}{12} = \frac{1}{3}$
et $P(A \cap B)=\frac{2}{12}=\frac{1}{6}$
alors $P(A)P(B)=\frac{1}{2}*\frac{1}{3} = \frac{1}{6}= P(A \cap B)$$
ainsi $A$ et $B$ sont independants.

2. On a : $P(A) = \frac{6}{13}$
$P(B)=\frac{4}{13}$
et $P(A \cap B) = \frac{2}{13}$
alors $P(A)P(B)=\frac{6}{13}*\frac{4}{13}= \frac{24}{169} \neq P(A \cap B)$
donc A, B pas independants.

Exercice 4 : Une urne contient 4 jetons : un rouge, un jaune, un vert et un tricolore rouge-jaune-vert. On tire un jeton au hasard et on définie les évènements : A : "Il y a du rouge sur le jeton tiré." B : "Il y a du jaune sur le jeton tiré." C : "Il y a du vert sur le jeton tiré." 1. Montrer que A, B et C sont indépendants deux à deux. 2. Sont-ils mutuellement indépendants ?

1. On a : $P(A) = \frac{2}{4} = \frac{1}{2}$
$P(A \cap B) = P(A \cap B)= P(B \cap C)= \frac{1}{4}$
ainsi $P(A)P(B) = P(A \cap B)$
$P(A)P(C)=P(A \cap C)$
$P(B)P(C) = P(B \cap C)$

donc A, B, C sont 2 a 2 inde

2. On a $P(A \cap B \cap C)=\frac{1}{4} \neq P(A)P(B)P(C)$ donc A, B, C ne sont pas mut. independants.

Exercice 5 : On considère un lot de pièces métalliques rectangulaires. Elles sont destinées à être assemblées ensembles. Toutefois certaines sont mal proportionnées et ne sont donc pas utilisables. Plus précisément : • 3% sont inutilisables car trop longues. • 5% sont inutilisables car trop larges. • 2% sont inutilisables car à le fois trop longues et trop larges. On prend une pièce au hasard, quelle est la probabilité quelle soit utilisable ?

On note A : 'piece trop longue', B : 'piece trop large'
On a : $P(A) = \frac{3}{100}, P(B)=\frac{5}{100}$
$P(A \cap B)=\frac{2}{100}$
On cherche : $P(\overline{A \cup B})$
On a : $P(\overline{A \cup B})=1- P(A \cup B)$
             $= 1-(P(A)+P(B)-P(A\cap B))$
             $= \frac{94}{100}$

Exercice 6 : Une urne contient n boules dont b boules blanches et r boules rouges. On tire une première boule, on la remet dans l’urne et on ajoute une seconde boule de la même couleur dans l’urne. On tire ensuite une seconde boule. 1. Décrire l’univers Ω de cette expérience. 2. Quelle est la probabilité de tirer deux boules blanches ? 3. Quelle est la probabilité que la seconde boule tirée soit blanche ? 4. Sachant que la seconde boule tirée est blanche, quelle est la probabilité que la première boule tirée est été blanche ?

1. $\Omega=${$(B, B), (R,R), (R, B), (B,R)$}
2. On note : $B_1$ : "boule 1 blanche"
$B_2$ : "boule 2 blanche"
alors $P(B_1 \cap B_2)= \frac{b}{n} \frac{b+1}{n+1} = \frac{b^2 + b}{n^2 +n}$
3. $P(B_2)=P((B_2 \cap B_1) \cup (B_2 \cap \overline{B_1}))$
        $=P(B_2 \cap B_1) + P(B_2 \cap \overline{B_1})$
        $= \frac{b^2 +b}{n^2 + n} + \frac{r}{n} \frac{b}{n+1}$ 
4. On cherche $P(B_1 | B_2)$
$P(B_1 | B_2)= \frac{P(B_1 \cap B_2)}{P(B_2)}$
     $=\frac{\frac{b^{2}+b}{n^{2}+n}}{\frac{b^{2}+(1+r)b}{n^{2}+n}}$
       $=\frac{b+1}{b+1+r}$
       $=\frac{b+1}{n+1}$    

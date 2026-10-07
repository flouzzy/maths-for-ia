## Exercice 7 : L'ensemble de Cantor et la limite de probabilité
$\bigstar\bigstar\bigstar\bigstar\star$

### Énoncé

On construit l'ensemble de Cantor $C$ sur $[0, 1]$.
- Étape 0 : On part de $I_0 = [0, 1]$. La longueur est $L_0 = 1$.
- Étape 1 : On enlève le tiers central ouvert $]1/3, 2/3[$. Il reste $I_1 = [0, 1/3] \cup [2/3, 1]$.
- Étape $n$ : On enlève le tiers central de chaque segment restant à l'étape $n-1$ pour former $I_n$.
L'ensemble de Cantor est défini par l'intersection infinie : $C = \bigcap_{n=0}^\infty I_n$.
En utilisant les axiomes de Kolmogorov sur la mesure de Lebesgue $\lambda$ (où $\lambda([a,b]) = b-a$), calculer la probabilité $\mathbb{P}(C)$ de tirer un nombre au hasard dans l'ensemble de Cantor.


### Correction Détaillée

**Étape 1 : Analyser la suite des événements $I_n$.**
L'événement $I_n$ représente l'union de tous les intervalles restants à l'étape $n$.
On tire un réel uniformly dans $[0, 1]$, donc la probabilité $\mathbb{P}(I_n)$ correspond à la somme des longueurs des intervalles constituant $I_n$.
- À l'étape 0 : $\mathbb{P}(I_0) = 1$.
- À l'étape 1 : On enlève un tiers de la longueur de chaque intervalle, donc il reste $2/3$ de la longueur. $I_1$ est composé de 2 segments de longueur $1/3$. $\mathbb{P}(I_1) = 2 \times (1/3) = 2/3$.
- À l'étape 2 : $I_2$ est composé de 4 segments de longueur $1/9$. $\mathbb{P}(I_2) = 4 \times (1/9) = (2/3)^2$.
Par une récurrence immédiate, à l'étape $n$, $I_n$ est composé de $2^n$ segments, chacun de longueur $(1/3)^n$.
Donc la probabilité (la longueur totale) est :
$\mathbb{P}(I_n) = 2^n \times \left(\frac{1}{3}\right)^n = \left(\frac{2}{3}\right)^n$.

**Étape 2 : Appliquer le théorème de continuité descendante.**
Par construction, l'ensemble à l'étape $n$ est strictement inclus dans l'ensemble à l'étape $n-1$.
Ainsi, la suite d'événements $(I_n)_{n \in \mathbb{N}}$ est décroissante :
$I_0 \supset I_1 \supset I_2 \dots$
L'ensemble de Cantor $C$ est l'intersection dénombrable décroissante de ces ensembles : $C = \bigcap_{n=0}^\infty I_n$.
D'après l'axiome de $\sigma$-additivité, qui induit la continuité descendante, la probabilité de l'intersection est la limite des probabilités :
$\mathbb{P}(C) = \mathbb{P}\left(\bigcap_{n=0}^\infty I_n\right) = \lim_{n \to \infty} \mathbb{P}(I_n)$.
$\mathbb{P}(C) = \lim_{n \to \infty} \left(\frac{2}{3}\right)^n$.

**Étape 3 : Conclusion.**
Puisque $\frac{2}{3} < 1$, la suite géométrique converge vers $0$.
$\mathbb{P}(C) = 0$.
Bien que l'ensemble de Cantor contienne une infinité non-dénombrable de points (il a la puissance du continu, comme $\mathbb{R}$), sa "taille" géométrique (sa probabilité sous la mesure de Lebesgue) est rigoureusement nulle.

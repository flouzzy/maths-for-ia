# Exercice 6 : Lemme de Fatou pour une suite d'indicatrices

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $(A_n)_{n \in \mathbb{N}}$ une suite d'ensembles mesurables dans un espace mesuré $(X, \mathcal{A}, \mu)$. Démontrer directement à partir des propriétés de la mesure (sans invoquer le Lemme de Fatou général) que $\mu(\liminf_{n \to \infty} A_n) \leq \liminf_{n \to \infty} \mu(A_n)$.

**Démonstration :**
Rappelons la définition de la limite inférieure d'une suite d'ensembles :
$A = \liminf_{n \to \infty} A_n = \bigcup_{k=1}^\infty \bigcap_{n=k}^\infty A_n$.
Cette définition s'interprète comme l'ensemble des éléments qui appartiennent à presque tous les $A_n$ (à tous à partir d'un certain rang).
Définissons la suite d'ensembles emboîtés $B_k = \bigcap_{n=k}^\infty A_n$.
Par définition de l'intersection, la suite $(B_k)$ est croissante pour l'inclusion : $B_k \subseteq B_{k+1}$.
De plus, $A = \bigcup_{k=1}^\infty B_k$.
D'après le théorème de continuité monotone croissante de la mesure :
$$\mu(A) = \mu\left(\bigcup_{k=1}^\infty B_k\right) = \lim_{k \to \infty} \mu(B_k)$$
Analysons le terme $\mu(B_k)$. Par construction de l'intersection, pour tout $n \geq k$, on a $B_k \subseteq A_n$.
La monotonie de la mesure implique donc que pour tout $n \geq k$, $\mu(B_k) \leq \mu(A_n)$.
Puisque cette inégalité est vraie pour tout $n \geq k$, $\mu(B_k)$ minore l'ensemble des valeurs $\{\mu(A_n) \mid n \geq k\}$.
Par conséquent, $\mu(B_k)$ est inférieur ou égal à la borne inférieure de cet ensemble :
$$\mu(B_k) \leq \inf_{n \geq k} \mu(A_n)$$
Prenons maintenant la limite lorsque $k \to \infty$ des deux côtés de cette inégalité.
Le terme de gauche tend vers $\mu(A)$ par continuité croissante.
Le terme de droite est précisément la définition de la limite inférieure d'une suite numérique. Ainsi :
$$\lim_{k \to \infty} \mu(B_k) \leq \lim_{k \to \infty} \left( \inf_{n \geq k} \mu(A_n) \right)$$
Ce qui s'écrit formellement :
$$\mu(\liminf_{n \to \infty} A_n) \leq \liminf_{n \to \infty} \mu(A_n)$$
C'est l'essence géométrique du Lemme de Fatou.

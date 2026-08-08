## Exercice 8 : L'espace des suites bornées \quad $\bigstar\bigstar\bigstar$

**Énoncé :** Sur l'espace $l^\infty(\mathbb{R})$ des suites réelles bornées, on définit $d(u, v) = \sup_{n \in \mathbb{N}} |u_n - v_n|$. Démontrer que la convergence pour cette distance implique la convergence uniforme des suites.

**Correction :** Soit $(u^{(k)})_{k \in \mathbb{N}}$ une suite d'éléments de $l^\infty(\mathbb{R})$ (donc une suite de suites) convergeant vers une suite $v$ pour la distance $d$.
Par définition de la convergence métrique :
$\forall \epsilon > 0, \exists K \in \mathbb{N}, \forall k \ge K, d(u^{(k)}, v) < \epsilon$.
En remplaçant $d$ par sa définition :
$\forall k \ge K, \sup_{n \in \mathbb{N}} |u^{(k)}_n - v_n| < \epsilon$.
Par définition du supremum, cela implique que pour chaque indice scalaire $n$, l'écart est majoré par le supremum :
$\forall k \ge K, \forall n \in \mathbb{N}, |u^{(k)}_n - v_n| \le \sup_{m} |u^{(k)}_m - v_m| < \epsilon$.
L'entier $K$ dépend uniquement de $\epsilon$ et est parfaitement indépendant de l'indice $n$. C'est l'exacte définition formelle de la convergence uniforme d'une suite de fonctions (ici définies sur $\mathbb{N}$).

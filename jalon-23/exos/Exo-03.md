# Exercice 3 : L'astuce du coefficient nul et le changement de variable

**Énoncé :**
Étudier la série entière $\sum_{n \geq 0} \frac{z^{2n}}{4^n}$. Déterminer son rayon de convergence $R$.

**Correction détaillée :**
Prudence ! Le terme général de la série ne se présente pas sous la forme canonique $\sum a_k z^k$ pour tous les entiers. En effet, en posant l'indice canonique $k$, les coefficients $a_k$ sont nuls pour tous les indices impairs $k$.
La règle de d'Alembert n'est donc pas applicable directement à la suite $(a_k)$, puisque les quotients $a_{k+1}/a_k$ impliqueraient des divisions par zéro.
Nous contournons la pathologie en posant un changement de variable formel.
Soit $w = z^2$. La série de fonctions devient une nouvelle série entière de la variable $w$ :
$$ S(w) = \sum_{n \geq 0} \frac{w^n}{4^n} $$
Le coefficient général pour la variable $w$ est $b_n = \frac{1}{4^n}$. Ces coefficients sont non nuls, nous appliquons d'Alembert sur $b_n$.
$$ \left| \frac{b_{n+1}}{b_n} \right| = \frac{1/4^{n+1}}{1/4^n} = \frac{4^n}{4^{n+1}} = \frac{1}{4} $$
La limite est trivialement $L = 1/4$. Le rayon de convergence pour la variable $w$ est $R_w = 4$.
La condition de convergence absolue s'écrit donc géométriquement :
$$ |w| < 4 $$
Revenons à la variable originale $z$. Sachant que $w = z^2$, nous obtenons l'inégalité équivalente :
$$ |z^2| < 4 \iff |z|^2 < 4 \iff |z| < 2 $$
Par définition du rayon de convergence sur la variable $z$, le suprémum des modules assurant la convergence absolue est bien 2.
Le rayon de convergence de la série originale est par conséquent $R = 2$.

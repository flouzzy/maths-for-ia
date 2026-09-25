# Exercice 5 : Inégalité de Tchebychev et espace de Schwartz $\star\star\star\star\mathstrut$

**Énoncé :**
Montrer que l'espace de Schwartz $\mathcal{S}(\mathbb{R})$ des fonctions à décroissance rapide est dense dans $L^p(\mathbb{R})$ pour $1 \le p < \infty$.

**Correction détaillée :**
L'espace de Schwartz $\mathcal{S}(\mathbb{R})$ est constitué des fonctions infiniment dérivables dont toutes les dérivées décroissent plus vite que n'importe quelle puissance de l'inverse de la distance.
1. On sait par les théorèmes fondamentaux que l'espace des fonctions infiniment dérivables à support compact $C_c^\infty(\mathbb{R}) = \mathcal{D}(\mathbb{R})$ est dense dans $L^p(\mathbb{R})$.
2. Une fonction à support compact est nulle en dehors d'un certain segment. Par conséquent, elle appartient trivialement à $\mathcal{S}(\mathbb{R})$ car en dehors du compact, la fonction et toutes ses dérivées sont strictement nulles, vérifiant ainsi la condition de décroissance plus rapide que n'importe quel polynôme inverse.
3. Donc, l'inclusion suivante est stricte : $\mathcal{D}(\mathbb{R}) \subset \mathcal{S}(\mathbb{R}) \subset L^p(\mathbb{R})$.
*(L'inclusion $\mathcal{S}(\mathbb{R}) \subset L^p(\mathbb{R})$ est justifiée car une fonction de $\mathcal{S}(\mathbb{R})$ est bornée, disons par $C$, et décroît au moins comme $|x|^{-2}$ pour $|x| \ge 1$. Ainsi $|f(x)|^p$ est intégrable près de l'infini).*
4. Soit $f \in L^p(\mathbb{R})$ et $\varepsilon > 0$. Puisque $\mathcal{D}(\mathbb{R})$ est dense dans $L^p(\mathbb{R})$, il existe $\varphi \in \mathcal{D}(\mathbb{R})$ telle que $\|f - \varphi\|_p < \varepsilon$.
5. Comme $\varphi \in \mathcal{D}(\mathbb{R}) \subset \mathcal{S}(\mathbb{R})$, on a trouvé un élément de l'espace de Schwartz à une distance $\varepsilon$ de $f$.
La densité de $\mathcal{S}(\mathbb{R})$ dans $L^p(\mathbb{R})$ est donc une conséquence immédiate de la densité de $\mathcal{D}(\mathbb{R})$. $\blacksquare$

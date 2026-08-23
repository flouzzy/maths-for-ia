## Exercice 7 : Continuité des translations $\quad \bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Pour $f \in L^1(\mathbb{R}, \lambda)$ positive, montrer que $\lim_{h \to 0} \int |f(x+h) - f(x)| d\lambda = 0$.

**Correction :**
Le résultat est d'abord vrai pour les fonctions continues à support compact $C_c(\mathbb{R})$.
Soit $f \in C_c(\mathbb{R})$. Elle est uniformément continue, donc $\sup_x |f(x+h) - f(x)| \to 0$.
Comme le support est contenu dans un segment compact $K$, pour $h$ assez petit, les supports de $x \mapsto f(x+h)$ restent dans un compact un peu plus grand $K'$.
Ainsi, $\int |f(x+h) - f(x)| d\lambda \le \lambda(K') \sup_x |f(x+h) - f(x)| \to 0$.
Pour $f \in L^1(\mathbb{R})$ quelconque, on utilise la densité de $C_c(\mathbb{R})$ dans $L^1$.
Soit $\epsilon > 0$. Il existe $g \in C_c(\mathbb{R})$ telle que $\|f-g\|_1 < \epsilon / 3$.
Alors $\int |f(x+h) - f(x)| \le \int |f(x+h) - g(x+h)| + \int |g(x+h) - g(x)| + \int |g(x) - f(x)|$.
Le premier terme est par changement de variable $\|f-g\|_1 < \epsilon/3$. Le dernier aussi.
Le terme du milieu tend vers 0, donc est $< \epsilon/3$ pour $h$ petit. Le tout est $< \epsilon$.

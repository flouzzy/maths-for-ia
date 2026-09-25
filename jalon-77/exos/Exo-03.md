# Exercice 3 : Continuité des translations dans $L^p$ $\star\star\star\mathstrut\mathstrut$

**Énoncé :**
Soit $f \in L^p(\mathbb{R})$ avec $1 \le p < \infty$. Pour $h \in \mathbb{R}$, on définit la fonction translatée $\tau_h f(x) = f(x - h)$.
Démontrer que $\lim_{h \to 0} \|\tau_h f - f\|_p = 0$.

**Correction détaillée :**
Cette propriété fondamentale exprime la continuité uniforme de l'opérateur de translation sur $L^p$. La preuve utilise la densité de $C_c(\mathbb{R})$.
**Étape 1 : Cas des fonctions continues à support compact.**
Supposons d'abord que $g \in C_c(\mathbb{R})$. Soit $K$ le support de $g$. $K$ est un compact, donc par le théorème de Heine, $g$ est uniformément continue sur $\mathbb{R}$.
Pour tout $\varepsilon > 0$, il existe $\delta > 0$ tel que pour tout $|h| < \delta$ et tout $x \in \mathbb{R}$, on a $|g(x-h) - g(x)| < \varepsilon$.
De plus, si $|h| < 1$, le support de $\tau_h g - g$ est inclus dans le compact $K' = K + [-1, 1]$.
Ainsi, pour $|h| < \min(\delta, 1)$, on majore la norme $L^p$ :
$$ \|\tau_h g - g\|_p^p = \int_{K'} |g(x-h) - g(x)|^p \, dx \le \int_{K'} \varepsilon^p \, dx = \varepsilon^p \lambda(K') $$
Comme $\lambda(K')$ est finie, en faisant tendre $\varepsilon$ vers $0$, on obtient que $\lim_{h \to 0} \|\tau_h g - g\|_p = 0$.
**Étape 2 : Cas d'une fonction $f \in L^p(\mathbb{R})$ quelconque.**
Soit $\varepsilon > 0$. Par le théorème de densité, il existe $g \in C_c(\mathbb{R})$ telle que $\|f - g\|_p < \frac{\varepsilon}{3}$.
Par l'invariance de la mesure de Lebesgue par translation, $\|\tau_h f - \tau_h g\|_p = \|\tau_h(f - g)\|_p = \|f - g\|_p < \frac{\varepsilon}{3}$.
En utilisant l'inégalité de Minkowski, on a :
$$ \|\tau_h f - f\|_p \le \|\tau_h f - \tau_h g\|_p + \|\tau_h g - g\|_p + \|g - f\|_p $$
D'où $\|\tau_h f - f\|_p < \frac{2\varepsilon}{3} + \|\tau_h g - g\|_p$.
D'après l'étape 1, il existe $\eta > 0$ tel que pour $|h| < \eta$, $\|\tau_h g - g\|_p < \frac{\varepsilon}{3}$.
Par conséquent, pour $|h| < \eta$, on a $\|\tau_h f - f\|_p < \varepsilon$. La limite est bien démontrée. $\blacksquare$

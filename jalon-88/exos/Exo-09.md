# Exercice 9 : Indépendance de variables à densité (Loi Normale)

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soient $X$ et $Y$ deux variables aléatoires à densité indépendantes, suivant la loi normale centrée réduite $\mathcal{N}(0,1)$.
Leur densité de probabilité commune est $f(x) = \frac{{1}}{{\sqrt{{2\pi}}}}e^{{-x^2/2}}$.
On définit deux nouvelles variables aléatoires :
$$ U = X + Y $$
$$ V = X - Y $$
Démontrer rigoureusement que $U$ et $V$ sont des variables aléatoires indépendantes.

---
**Correction détaillée :**

Pour des variables aléatoires à densité, démontrer leur indépendance revient à montrer que la densité conjointe de la paire $(U, V)$ est égale au produit des densités marginales de $U$ et $V$.

1. **Densité conjointe de $(X,Y)$ :**
Par indépendance de $X$ et $Y$, la densité conjointe du vecteur $(X,Y)$ est le produit des densités marginales :
$$ f_{{X,Y}}(x,y) = f(x)f(y) = \frac{{1}}{{2\pi}} e^{{-x^2/2}} e^{{-y^2/2}} = \frac{{1}}{{2\pi}} e^{{-\frac{{1}}{{2}}(x^2+y^2)}} $$

2. **Changement de variable (Méthode de la transformation) :**
Considérons l'application $\Phi : \mathbb{R}^2 \to \mathbb{R}^2$ définie par $\Phi(x,y) = (x+y, x-y) = (u,v)$.
C'est une application linéaire représentée par la matrice :
$$ J = \begin{{pmatrix}} 1 & 1 \\ 1 & -1 \end{{pmatrix}} $$
Calculons le déterminant jacobien de cette transformation : $\det(J) = (1)(-1) - (1)(1) = -2$.
Le jacobien de la transformation inverse est l'inverse absolu de ce déterminant, c'est-à-dire $|J^{{-1}}| = 1 / |\det(J)| = 1/2$.
Le système s'inverse facilement pour exprimer $x$ et $y$ en fonction de $u$ et $v$ :
$$ x = \frac{{u+v}}{{2}} $$
$$ y = \frac{{u-v}}{{2}} $$

3. **Calcul de la densité conjointe de $(U,V)$ :**
En appliquant la formule du changement de variable pour les densités :
$$ f_{{U,V}}(u,v) = f_{{X,Y}}(x(u,v), y(u,v)) \times |J^{{-1}}| $$
Substituons les expressions :
$$ f_{{U,V}}(u,v) = \frac{{1}}{{2\pi}} \exp\left( -\frac{{1}}{{2}} \left[ \left(\frac{{u+v}}{{2}}\right)^2 + \left(\frac{{u-v}}{{2}}\right)^2 \right] \right) \times \frac{{1}}{{2}} $$
Simplifions la forme quadratique dans l'exponentielle :
$$ \left(\frac{{u+v}}{{2}}\right)^2 + \left(\frac{{u-v}}{{2}}\right)^2 = \frac{{u^2 + 2uv + v^2}}{{4}} + \frac{{u^2 - 2uv + v^2}}{{4}} = \frac{{2u^2 + 2v^2}}{{4}} = \frac{{u^2 + v^2}}{{2}} $$
En reportant dans la densité :
$$ f_{{U,V}}(u,v) = \frac{{1}}{{4\pi}} \exp\left( -\frac{{1}}{{2}} \frac{{u^2 + v^2}}{{2}} \right) = \frac{{1}}{{4\pi}} \exp\left( -\frac{{u^2}}{{4}} - \frac{{v^2}}{{4}} \right) $$

4. **Factorisation de la densité conjointe :**
Séparons les termes en $u$ et en $v$ :
$$ f_{{U,V}}(u,v) = \left( \frac{{1}}{{\sqrt{{4\pi}}}} e^{{-u^2/4}} \right) \times \left( \frac{{1}}{{\sqrt{{4\pi}}}} e^{{-v^2/4}} \right) $$

5. **Conclusion :**
Nous observons que la densité conjointe de $(U,V)$ se factorise sous la forme $g(u)h(v)$.
Cette séparation prouve irréfutablement que les variables $U$ et $V$ sont **indépendantes**.
De plus, par identification de la formule de la loi normale, on reconnait les densités marginales, prouvant au passage que $U \sim \mathcal{N}(0,2)$ et $V \sim \mathcal{N}(0,2)$. $\blacksquare$

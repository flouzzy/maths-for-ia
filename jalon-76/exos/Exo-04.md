# Exercice 4 : Espace $L^2$ (★★☆☆☆)

**Énoncé :**
Soit $f \in L^2(\mathbb{R})$. Montrer que pour tout $a \in \mathbb{R}$, l'opérateur de translation $T_a f(x) = f(x - a)$ est une isométrie de $L^2(\mathbb{R})$.

**Correction Détaillée :**
*Analyse de l'énoncé :* Il faut démontrer que $\|T_a f\|_{L^2} = \|f\|_{L^2}$.

*Résolution pas-à-pas :*
Soit $f \in L^2(\mathbb{R})$. Par définition :
$$ \|T_a f\|^2 = \int_{-\infty}^{\infty} |f(x - a)|^2 dx $$

On effectue le changement de variable $u = x - a$.
Alors $du = dx$. Les bornes d'intégration restent $-\infty$ et $+\infty$ car la translation est une bijection de $\mathbb{R}$ dans $\mathbb{R}$.
$$ \int_{-\infty}^{\infty} |f(x - a)|^2 dx = \int_{-\infty}^{\infty} |f(u)|^2 du $$
Ce qui est exactement $\|f\|^2$.

Donc $\|T_a f\|^2 = \|f\|^2$, et puisque les normes sont positives, $\|T_a f\| = \|f\|$. L'opérateur préserve la norme, c'est une isométrie.

# Exercice 10 : Non-compacité de la boule unité dans un espace de dimension infinie

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Cet exercice illustre pourquoi le théorème de Riesz impose qu'en dimension infinie, la boule unité fermée n'est jamais compacte.
Considérons l'espace vectoriel normé $\mathcal{C}([0, 1])$ muni de la norme uniforme $\| \cdot \|_\infty$.
Soit $\mathcal{B}$ la boule unité fermée, définie par $\mathcal{B} = \{ f \in \mathcal{C}([0, 1]) \mid \|f\|_\infty \le 1 \}$.
Considérons la suite de fonctions "en tente" (ou "dents de scie pointues") définie par :
$$ f_n(x) = \begin{cases} n x & \text{si } x \in [0, 1/n] \\ 2 - nx & \text{si } x \in [1/n, 2/n] \\ 0 & \text{si } x \in [2/n, 1] \end{cases} $$

1. Vérifier que $f_n \in \mathcal{B}$.
2. Montrer que pour $m \neq n$ (avec $m \ge 2n$), $\|f_m - f_n\|_\infty = 1$.
3. En déduire par l'absurde que $\mathcal{B}$ n'est pas compacte, c'est-à-dire qu'on ne peut extraire aucune sous-suite convergente de $(f_n)$.
4. Quel critère du théorème d'Arzelà-Ascoli manque pour que $\mathcal{B}$ soit compacte ?

## Résolution Détaillée

### 1. Appartenance à la boule unité fermée

La fonction $f_n$ est affine par morceaux et continue (raccordement parfait : $f_n(1/n) = n(1/n) = 1$ et $f_n(2/n) = 2 - 2 = 0$).
Le maximum géométrique du "pic" de la tente est situé en $x = 1/n$ avec $f_n(1/n) = 1$.
La fonction est positive. Donc $\|f_n\|_\infty = \sup_{x \in [0, 1]} |f_n(x)| = 1 \le 1$.
Ainsi, chaque $f_n$ appartient bien à la boule unité fermée $\mathcal{B}$.

### 2. Distance mutuelle entre les pics

Soient $m, n \in \mathbb{N}^*$ avec $m > 2n$.
Évaluons la distance $\|f_m - f_n\|_\infty = \sup_{x \in [0, 1]} |f_m(x) - f_n(x)|$.
Le support de $f_m$ (l'ensemble où elle est non nulle) est strictement inclus dans $[0, 2/m]$.
Comme $m > 2n \iff 1/n > 2/m$, le support entier du pic de $f_m$ se trouve à gauche du sommet du pic de $f_n$ (situé en $1/n$).
Évaluons l'écart aux deux sommets :
- Au point $x = 1/n$ : $f_n(1/n) = 1$. À ce point, $1/n > 2/m$, donc $f_m(1/n) = 0$. La différence est $|0 - 1| = 1$.
- Au point $x = 1/m$ : $f_m(1/m) = 1$. Évaluons $f_n(1/m)$. Puisque $1/m < 1/n$, nous sommes dans la branche croissante de $f_n$, donc $f_n(1/m) = n(1/m) = n/m$. L'écart vaut $1 - n/m > 1 - 1/2 = 1/2$.
En $x = 1/n$, l'écart absolu vaut 1.
Puisque les deux fonctions sont à valeurs dans $[0, 1]$, leur différence ne peut pas excéder 1 en valeur absolue.
Le supremum de l'écart est donc atteint en $1/n$ :
$$ \|f_m - f_n\|_\infty = 1 $$

### 3. Non-compacité de la boule

Supposons par l'absurde que la boule unité fermée $\mathcal{B}$ soit compacte.
Alors la suite $(f_n)$ (entièrement contenue dans $\mathcal{B}$) devrait posséder une sous-suite $(f_{\phi(k)})_{k\in\mathbb{N}}$ convergente.
Or, toute suite convergente dans un espace métrique est une suite de Cauchy.
Il devrait donc exister un rang $K$ tel que pour tous $p, q \ge K$, $\|f_{\phi(p)} - f_{\phi(q)}\|_\infty < 1/2$.
Mais d'après la question 2, pour des indices arbitrairement grands de la sous-suite (en choisissant $p$ tel que $\phi(p) > 2\phi(q)$), l'écart mutuel est exactement 1, ce qui contredit formellement la condition de Cauchy.
La contradiction détruit l'hypothèse : la boule unité $\mathcal{B}$ d'un espace fonctionnel de dimension infinie **n'est jamais un compact**.

### 4. Violation d'Arzelà-Ascoli

Si $\mathcal{B}$ était compacte, selon Arzelà-Ascoli, elle serait uniformément équicontinue.
Vérifions le critère d'équicontinuité en 0.
La pente à l'origine de $f_n$ est $n$. Ainsi $|f_n(1/n) - f_n(0)| = 1$.
Pour tout $\delta > 0$, il existe un indice $n$ tel que $1/n < \delta$. On évalue à cet instant $x=1/n$ (distance à 0 inférieure à $\delta$), mais le saut vaut toujours 1.
Il est donc impossible de trouver un module de continuité uniforme : l'équicontinuité, pivot central du Théorème d'Arzelà-Ascoli, est irrémédiablement violée par cette suite de "tentes" infiniment acérées. $\blacksquare$

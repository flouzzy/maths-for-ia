# Exercice 1 : Convergence normale basique

**Difficulté :** $\star$

**Énoncé :**
Étudier la convergence (simple, absolue, uniforme, normale) de la série de fonctions $\sum f_n$ définie sur $\mathbb{R}$ par $f_n(x) = \frac{\sin(nx)}{n^3}$.

**Démonstration :**
1. **Convergence simple et absolue :**
   Soit $x \in \mathbb{R}$. On majore la valeur absolue du terme général :
   $$ |f_n(x)| = \left| \frac{\sin(nx)}{n^3} \right| \le \frac{1}{n^3} $$
   La série numérique $\sum \frac{1}{n^3}$ est une série de Riemann avec $\alpha = 3 > 1$. Elle est donc convergente.
   Par comparaison de séries à termes positifs, la série $\sum |f_n(x)|$ converge. Ainsi, la série $\sum f_n(x)$ converge absolument, ce qui implique qu'elle converge simplement sur $\mathbb{R}$.

2. **Convergence normale :**
   Calculons la norme infinie de $f_n$ sur $\mathbb{R}$ :
   $$ \|f_n\|_{\infty, \mathbb{R}} = \sup_{x \in \mathbb{R}} \left| \frac{\sin(nx)}{n^3} \right| $$
   Puisque $|\sin(nx)|$ atteint la valeur 1 (par exemple pour $nx = \frac{\pi}{2}$, soit $x = \frac{\pi}{2n}$), on a :
   $$ \|f_n\|_{\infty, \mathbb{R}} = \frac{1}{n^3} $$
   La série des normes infinies $\sum \|f_n\|_{\infty, \mathbb{R}} = \sum \frac{1}{n^3}$ converge.
   Par définition, la série $\sum f_n$ converge **normalement** sur $\mathbb{R}$.

3. **Convergence uniforme :**
   D'après le théorème fondamental, toute série normalement convergente sur un ensemble est uniformément convergente sur cet ensemble. Donc $\sum f_n$ converge uniformément sur $\mathbb{R}$.
$\blacksquare$

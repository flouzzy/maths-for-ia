# Exercice 5

**Difficulté :** $\star\star\star\star\star$

**Énoncé :**
Soit $E = (\mathcal{C}([0,1], \mathbb{R}), \|\cdot\|_\infty)$. Soit $T : E \to \mathbb{R}$ la forme linéaire définie par $T(f) = \int_0^{1/2} f(t)dt - \int_{1/2}^1 f(t)dt$. Calculer la norme de cet opérateur $\|T\|_{E'}$ et montrer qu'il n'existe aucune fonction $f \in E$ de norme 1 telle que $T(f) = \|T\|_{E'}$.

**Correction Détaillée :**
1. **Majoration de la forme linéaire :** Pour toute fonction $f \in E$, appliquons l'inégalité triangulaire et la propriété de l'intégrale :
   $$ |T(f)| \le \left|\int_0^{1/2} f(t)dt\right| + \left|\int_{1/2}^1 f(t)dt\right| \le \int_0^{1/2} |f(t)|dt + \int_{1/2}^1 |f(t)|dt = \int_0^1 |f(t)|dt. $$
2. On majore l'intégrande par la norme uniforme :
   $$ \int_0^1 |f(t)|dt \le \int_0^1 \|f\|_\infty dt = \|f\|_\infty. $$
3. Ainsi, pour toute fonction $f$, $|T(f)| \le \|f\|_\infty$. Ceci montre que $T$ est continue et que $\|T\| \le 1$.
4. **Calcul exact du supremum :** Pour montrer que $\|T\| = 1$, il faut approcher cette borne par une suite de fonctions continues. Définissons la suite $f_n$ pour $n \ge 3$ :
   - $f_n(t) = 1$ sur $[0, \frac{1}{2} - \frac{1}{n}]$
   - $f_n(t) = -1$ sur $[\frac{1}{2} + \frac{1}{n}, 1]$
   - $f_n$ est affine et continue sur $[\frac{1}{2} - \frac{1}{n}, \frac{1}{2} + \frac{1}{n}]$, passant de 1 à -1 (droite de pente $-n$).
5. Chaque $f_n$ est continue, et $\|f_n\|_\infty = 1$.
6. Calculons $T(f_n)$ :
   $$ \int_0^{1/2} f_n(t)dt = \left(\frac{1}{2} - \frac{1}{n}\right) \times 1 + \frac{1}{2} \times \frac{1}{n} \times 1 = \frac{1}{2} - \frac{1}{2n}. $$
   L'intégrale sur $[\frac{1}{2}, 1]$ par symétrie est $-\left(\frac{1}{2} - \frac{1}{2n}\right)$.
   Donc $T(f_n) = \left(\frac{1}{2} - \frac{1}{2n}\right) - \left(-\frac{1}{2} + \frac{1}{2n}\right) = 1 - \frac{1}{n}$.
7. Lorsque $n \to \infty$, $T(f_n) \to 1$. Comme $|T(f_n)| / \|f_n\|_\infty \to 1$, la borne supérieure est bien $\|T\| = 1$.
8. **Non-atteinte du supremum :** Supposons qu'il existe $f \in E$ continue avec $\|f\|_\infty = 1$ et $T(f) = 1$.
9. L'équation $T(f) = \int_0^{1/2} f(t)dt - \int_{1/2}^1 f(t)dt = 1$ implique, puisque $f(t) \le 1$, que l'on doit avoir $\int_0^{1/2} f(t)dt = 1/2$ et $\int_{1/2}^1 f(t)dt = -1/2$.
10. Pour qu'une fonction continue bornée par 1 ait une moyenne de 1 sur $[0, 1/2]$, elle doit être constamment égale à 1 sur ce segment. De même, elle doit être constamment égale à -1 sur $[1/2, 1]$.
11. Mais alors $f(1/2) = 1$ (par limite à gauche) et $f(1/2) = -1$ (par limite à droite), ce qui contredit la continuité de $f$ en $1/2$.
12. En conclusion, il n'existe aucune telle fonction $f$. L'opérateur n'atteint pas sa norme, un phénomène spécifique aux espaces de Banach de dimension infinie non réflexifs (ici $\mathcal{C}([0,1])$).

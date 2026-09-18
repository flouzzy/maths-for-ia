# Exercice 2 : Inclusions des espaces Lp sur un espace de probabilité

**Difficulté :** $\bigstar\bigstar\star\star\star$

## Énoncé

Soit $(X, \mathcal{F}, \mathbb{P})$ un espace de probabilité ($\mathbb{P}(X) = 1$).
Soit $f \in L^2(X, \mathbb{P})$.

1. En utilisant l'inégalité de Cauchy-Schwarz pour les intégrales, montrer que $f \in L^1(X, \mathbb{P})$.
2. Établir l'inégalité explicite entre $\|f\|_1$ et $\|f\|_2$.
3. Est-il vrai que $L^1(X, \mathbb{P}) \subset L^2(X, \mathbb{P})$ ? Justifier avec un contre-exemple sur $]0, 1]$ muni de la mesure de Lebesgue.

---

## Correction détaillée

1. **Application de Cauchy-Schwarz :**
   L'inégalité de Cauchy-Schwarz stipule que pour $f, g \in L^2$, $|\int f g| \le \|f\|_2 \|g\|_2$.
   Posons $g = \mathbf{1}_X$. Comme $\mathbb{P}(X) = 1$, on a :
   $$ \|g\|_2 = \left( \int_X 1^2 \, d\mathbb{P} \right)^{1/2} = \sqrt{\mathbb{P}(X)} = 1 $$
   Donc $g \in L^2(X, \mathbb{P})$.
   On applique l'inégalité avec $|f|$ et $g$ :
   $$ \int_X |f| \times 1 \, d\mathbb{P} \le \left( \int_X |f|^2 \, d\mathbb{P} \right)^{1/2} \left( \int_X 1^2 \, d\mathbb{P} \right)^{1/2} $$
   $$ \|f\|_1 \le \|f\|_2 \times 1 < +\infty $$
   Ainsi, $f$ est intégrable, donc $f \in L^1(X, \mathbb{P})$.

2. **Inégalité :**
   La ligne précédente prouve directement que :
   $$ \|f\|_1 \le \|f\|_2 $$
   Ceci illustre le fait géométrique fondamental : sur un espace fini (de masse 1), les moments d'ordre supérieur dominent les moments d'ordre inférieur. $L^2 \subset L^1$.

3. **Contre-exemple pour l'inclusion réciproque :**
   Non, l'inclusion réciproque est fausse.
   Prenons $X = ]0, 1]$ avec la mesure de Lebesgue (qui est bien une probabilité car $\lambda(]0, 1]) = 1$).
   Considérons $f(x) = x^{-1/2}$.
   $$ \|f\|_1 = \int_0^1 x^{-1/2} \, dx = [2\sqrt{x}]_0^1 = 2 < +\infty $$
   Donc $f \in L^1$.
   $$ \|f\|_2^2 = \int_0^1 (x^{-1/2})^2 \, dx = \int_0^1 \frac{1}{x} \, dx = [\ln x]_0^1 = +\infty $$
   Donc $f \notin L^2$. Ainsi, $L^1 \not\subset L^2$.

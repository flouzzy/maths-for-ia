# Exercice 5 : Opérateur de translation temporelle et isométrie
$\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $f \in L^2(\mathbb{R})$ et $a \in \mathbb{R}$. Soit $\tau_a f$ l'opérateur de translation défini par $(\tau_a f)(t) = f(t-a)$.
1. Montrer que $\tau_a$ est une isométrie sur $L^2(\mathbb{R})$.
2. Déterminer la transformée de Fourier de $\tau_a f$ en fonction de $\hat{f}$.
3. Montrer que la multiplication par $e^{-i\xi a}$ dans le domaine fréquentiel est une isométrie sur $L^2(\mathbb{R})$.
4. Vérifier la cohérence de ces résultats avec le théorème de Plancherel.

---
**Correction :**
**Question 1 : $\tau_a$ est une isométrie sur $L^2(\mathbb{R})$**
Calculons la norme $L^2$ de $\tau_a f$ :
$$ \|\tau_a f\|_2^2 = \int_{-\infty}^{+\infty} |f(t-a)|^2 dt $$
Effectuons le changement de variable $u = t - a$, $du = dt$ :
$$ \|\tau_a f\|_2^2 = \int_{-\infty}^{+\infty} |f(u)|^2 du = \|f\|_2^2 $$
Puisque $\|\tau_a f\|_2 = \|f\|_2$ pour tout $f \in L^2(\mathbb{R})$, l'opérateur linéaire $\tau_a$ est une isométrie.

**Question 2 : Transformée de Fourier de $\tau_a f$**
Pour des fonctions $f \in L^1 \cap L^2$, on calcule :
$$ \widehat{\tau_a f}(\xi) = \int_{-\infty}^{+\infty} f(t-a) e^{-i\xi t} dt $$
Posons $u = t - a \implies t = u + a, dt = du$ :
$$ \widehat{\tau_a f}(\xi) = \int_{-\infty}^{+\infty} f(u) e^{-i\xi (u+a)} du = e^{-i\xi a} \int_{-\infty}^{+\infty} f(u) e^{-i\xi u} du = e^{-i\xi a} \hat{f}(\xi) $$
Par prolongement par densité, cette relation reste vraie presque partout pour $f \in L^2(\mathbb{R})$.

**Question 3 : Multiplication par $e^{-i\xi a}$ est une isométrie**
Soit l'opérateur $M_a : g(\xi) \mapsto e^{-i\xi a} g(\xi)$ agissant sur $L^2(\mathbb{R})$.
$$ \|M_a g\|_2^2 = \int_{-\infty}^{+\infty} |e^{-i\xi a} g(\xi)|^2 d\xi = \int_{-\infty}^{+\infty} |e^{-i\xi a}|^2 |g(\xi)|^2 d\xi $$
Puisque $|e^{-i\xi a}| = 1$ pour tout $\xi \in \mathbb{R}$, on a :
$$ \|M_a g\|_2^2 = \int_{-\infty}^{+\infty} 1 \cdot |g(\xi)|^2 d\xi = \|g\|_2^2 $$
Donc $M_a$ est une isométrie sur $L^2(\mathbb{R})$.

**Question 4 : Cohérence avec Plancherel**
Appliquons Plancherel à $\tau_a f$ :
$$ \|\widehat{\tau_a f}\|_2^2 = 2\pi \|\tau_a f\|_2^2 $$
D'après la question 2, le terme de gauche est $\|M_a \hat{f}\|_2^2$, qui par la question 3 vaut $\|\hat{f}\|_2^2$.
D'après la question 1, le terme de droite est $2\pi \|f\|_2^2$.
On retrouve donc exactement $\|\hat{f}\|_2^2 = 2\pi \|f\|_2^2$, ce qui est la relation de Plancherel pour $f$. La structure isométrique globale est donc parfaitement cohérente et commutative.

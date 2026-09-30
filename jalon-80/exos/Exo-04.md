\subsection*{Exercice 4 : Propriétés de translation spatiale \quad $\bigstar\bigstar\bigstar\star\star$}

Soit $f \in L^1(\mathbb{R})$ et $a \in \mathbb{R}$.
On définit l'opérateur de translation $\tau_a$ par $(\tau_a f)(t) = f(t-a)$.
Montrer que $\widehat{\tau_a f}(\xi) = e^{-ia\xi} \hat{f}(\xi)$.

---
**Correction :**

Par définition de la transformée de Fourier appliquée à la fonction $\tau_a f$ :
$$ \widehat{\tau_a f}(\xi) = \int_{-\infty}^{+\infty} (\tau_a f)(t) e^{-i\xi t} \, dt = \int_{-\infty}^{+\infty} f(t-a) e^{-i\xi t} \, dt $$
Effectuons le changement de variable $u = t - a$, ce qui implique $t = u + a$ et $dt = du$. Les bornes de l'intégrale de $-\infty$ à $+\infty$ restent inchangées.
$$ \widehat{\tau_a f}(\xi) = \int_{-\infty}^{+\infty} f(u) e^{-i\xi (u+a)} \, du $$
Par les propriétés de l'exponentielle :
$$ e^{-i\xi (u+a)} = e^{-i\xi u} e^{-i\xi a} $$
Puisque le terme $e^{-i\xi a}$ ne dépend pas de la variable d'intégration $u$, on peut le sortir de l'intégrale :
$$ \widehat{\tau_a f}(\xi) = e^{-i\xi a} \int_{-\infty}^{+\infty} f(u) e^{-i\xi u} \, du $$
On reconnaît l'expression exacte de la transformée de Fourier de $f$ :
$$ \widehat{\tau_a f}(\xi) = e^{-ia\xi} \hat{f}(\xi) $$
Ce résultat fondamental montre qu'une translation dans le domaine temporel correspond à un déphasage linéaire dans le domaine fréquentiel.

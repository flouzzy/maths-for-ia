## Exercice 3 : Construction de la fonction identité avec des sigmoïdes \quad $\bigstar\bigstar\star\star\star$

Montrer qu'en utilisant des combinaisons linéaires de sigmoïdes $\sigma(x) = \frac{1}{1+e^{-x}}$, on peut approcher la fonction identité $f(x) = x$ sur l'intervalle $[-1, 1]$ avec une erreur arbitrairement petite $\epsilon > 0$.

**Correction :**
Le développement limité de $\sigma(x)$ au voisinage de 0 donne $\sigma(x) = \frac{1}{2} + \frac{1}{4}x + \mathcal{O}(x^3)$.
On considère la combinaison $G_h(x) = \frac{\sigma(h x) - \sigma(-h x)}{2}$.
On a $\sigma(hx) = \frac{1}{2} + \frac{h x}{4} + \mathcal{O}(h^3 x^3)$ et $\sigma(-hx) = \frac{1}{2} - \frac{h x}{4} + \mathcal{O}(h^3 x^3)$.
Donc $G_h(x) = \frac{h x}{4} + \mathcal{O}(h^3 x^3)$.
En multipliant par $\frac{4}{h}$, on obtient $\tilde{G}_h(x) = \frac{4}{h} G_h(x) = x + \mathcal{O}(h^2 x^3)$.
Sur le compact $[-1, 1]$, $|x^3| \le 1$. L'erreur est en $\mathcal{O}(h^2)$.
En choisissant $h$ suffisamment petit tel que l'erreur maximale soit inférieure à $\epsilon$, on a bien approché la fonction identité uniformément sur $[-1, 1]$.

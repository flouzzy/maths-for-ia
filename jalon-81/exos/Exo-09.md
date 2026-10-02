## Exercice 9 : Propriété de lissage du projecteur idéal \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit un signal $f \in L^2(\mathbb{R})$. On définit le signal filtré $f_c$ tel que $\hat{f}_c(\xi) = \hat{f}(\xi) \mathbf{1}_{[-\omega_c, \omega_c]}(\xi)$.
1. Montrer que $f_c \in L^2(\mathbb{R})$.
2. Montrer que $f_c$ est une fonction continue.
3. Calculer l'erreur d'approximation $\|f - f_c\|_2^2$ en fonction de la queue du spectre de $f$.

**Correction :**
1. **Filtrage dans $L^2$ :**
Puisque $f \in L^2$, $\hat{f} \in L^2$ par l'isomorphisme de Plancherel.
L'indicatrice $\mathbf{1}_{[-\omega_c, \omega_c]}$ est une fonction bornée (par 1).
Le produit de $\hat{f}$ par une fonction bornée reste dans $L^2$. Donc $\hat{f}_c \in L^2$.
Par la surjectivité de l'isomorphisme de Fourier, il existe une unique $f_c \in L^2$ correspondant à cette transformée.

2. **Continuité par injection :**
Nous avons $\hat{f}_c \in L^2$. De plus, le support de $\hat{f}_c$ est compact (inclus dans $[-\omega_c, \omega_c]$).
Or, par Cauchy-Schwarz sur cet intervalle compact :
$$ \int_{-\omega_c}^{\omega_c} |\hat{f}_c(\xi)| d\xi \le \left( \int_{-\omega_c}^{\omega_c} 1^2 d\xi \right)^{1/2} \left( \int_{-\omega_c}^{\omega_c} |\hat{f}_c(\xi)|^2 d\xi \right)^{1/2} = \sqrt{2\omega_c} \|\hat{f}_c\|_{L^2} < \infty $$
Donc $\hat{f}_c \in L^1(\mathbb{R})$.
Or, le théorème d'inversion implique que si $\hat{f}_c \in L^1$, alors son inverse de Fourier (qui est $f_c$) est une fonction continue tendant vers zéro à l'infini (lemme de Riemann-Lebesgue).
Donc, un filtrage passe-bas idéal "régularise" n'importe quel signal $L^2$ en un signal continu (il élimine les singularités arbitrairement pointues portées par les hautes fréquences).

3. **Erreur d'énergie :**
L'erreur est le signal $e = f - f_c$.
Sa transformée est $\hat{e}(\xi) = \hat{f}(\xi) - \hat{f}_c(\xi) = \hat{f}(\xi)(1 - \mathbf{1}_{[-\omega_c, \omega_c]}(\xi))$.
Cela correspond à la partie hors bande du signal : $\hat{e}(\xi) = \hat{f}(\xi)$ pour $|\xi| > \omega_c$ et $0$ sinon.
L'énergie de l'erreur dans le domaine temporel se calcule par Plancherel :
$$ \|f - f_c\|_2^2 = \frac{1}{2\pi} \|\hat{f} - \hat{f}_c\|_2^2 = \frac{1}{2\pi} \int_{|\xi| > \omega_c} |\hat{f}(\xi)|^2 d\xi $$
Cette expression quantifie précisément l'énergie perdue par la troncature fréquentielle. Comme $\hat{f} \in L^2$, les "restes d'intégrales convergentes" tendent vers 0, donc $\|f - f_c\|_2 \to 0$ lorsque $\omega_c \to +\infty$.

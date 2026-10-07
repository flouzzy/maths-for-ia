# Exercice 3 : Inversion dans L2
**Difficulté :** $\bigstar\bigstar\star\star\star$

## Énoncé

On sait que pour un certain signal $f \in L^2(\mathbb{R})$, sa transformée de Fourier vaut $\hat{f}(\xi) = e^{-|\xi|}$.
Trouver le signal temporel $f(t)$ presque partout.

**Correction :**
L'opérateur de Fourier dans $L^2$ possède un inverse défini par $f(t) = \frac{1}{2\pi} \int_{-\infty}^\infty \hat{f}(\xi) e^{i\xi t} d\xi$.
Ici $\hat{f}(\xi) = e^{-|\xi|}$ est dans $L^1 \cap L^2$. Nous pouvons effectuer l'intégrale classique.
$f(t) = \frac{1}{2\pi} \int_{-\infty}^\infty e^{-|\xi|} e^{i\xi t} d\xi$.
Par analogie absolue avec l'exercice 1, mais en échangeant les rôles de $t$ et $\xi$ et en considérant le signe devant le $i$ :
L'intégrale $\int_{-\infty}^\infty e^{-|\xi|} e^{i\xi t} d\xi$ donne $\frac{2}{1+t^2}$.
Donc $f(t) = \frac{1}{2\pi} \frac{2}{1+t^2} = \frac{1}{\pi(1+t^2)}$.

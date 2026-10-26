# Exercice 04 : Loi de Cauchy
Difficulté : $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $X$ une variable aléatoire suivant la loi de Cauchy standard, de densité $f(x) = \frac{1}{\pi(1+x^2)}$.
1. Justifier pourquoi on ne peut pas utiliser la formule des moments pour cette loi.
2. On admet que $\phi_X(t) = e^{-|t|}$. Montrer que si $X_1, \dots, X_n$ sont des V.A. indépendantes de loi de Cauchy standard, alors la moyenne empirique $\bar{X}_n = \frac{1}{n}\sum_{k=1}^n X_k$ suit également une loi de Cauchy standard.

**Correction pas à pas :**
1. L'espérance de la loi de Cauchy nécessiterait que l'intégrale $\int_{-\infty}^{+\infty} \frac{|x|}{\pi(1+x^2)} dx$ converge.
   Or, au voisinage de l'infini, $\frac{|x|}{1+x^2} \sim \frac{1}{|x|}$, dont l'intégrale diverge (intégrale de Riemann divergente).
   Comme le moment d'ordre 1 n'existe pas, la fonction caractéristique n'est pas dérivable en $0$.
   En effet, $\phi_X(t) = e^{-|t|}$ n'est pas dérivable en $t=0$, ce qui est parfaitement cohérent avec l'absence de moment.
2. Posons $S_n = \sum_{k=1}^n X_k$. Par indépendance des $X_k$,
   $\phi_{S_n}(t) = \prod_{k=1}^n \phi_{X_k}(t) = (\phi_X(t))^n = (e^{-|t|})^n = e^{-n|t|}$.
3. La variable étudiée est $\bar{X}_n = \frac{1}{n} S_n$.
   En utilisant la propriété de la dilatation (démontrée dans l'exercice 3) avec $a = \frac{1}{n}$ et $b=0$ :
   $\phi_{\bar{X}_n}(t) = \phi_{S_n}\left(\frac{t}{n}\right) = e^{-n\left|\frac{t}{n}\right|} = e^{-|t|}$.
4. La fonction caractéristique de $\bar{X}_n$ est exactement $e^{-|t|}$, qui est la fonction caractéristique de la loi de Cauchy standard.
   Par injectivité de la transformée de Fourier (Théorème d'inversion), on conclut rigoureusement que $\bar{X}_n$ suit une loi de Cauchy standard.
   C'est une singularité remarquable : moyenner un très grand nombre de variables de Cauchy ne réduit pas la variance (car elle n'existe pas), la dispersion reste la même qu'une seule variable !

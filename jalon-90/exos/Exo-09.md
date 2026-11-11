# Exercice 09

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Absence de convergence $L^p$ pour la loi de Cauchy

Considérons une suite $(X_n)$ de variables indépendantes suivant la loi de Cauchy standard.
La densité de $X_i$ est $f(x) = \frac{1}{\pi(1+x^2)}$.
Posons la moyenne empirique $S_n = \frac{1}{n} \sum_{i=1}^n X_i$.
Montrez rigoureusement que $S_n$ ne converge ni en probabilité, ni presque sûrement vers la constante 0, ruinant l'intuition de la loi des grands nombres.

**Correction exhaustive :**
La loi des grands nombres s'applique aux variables aléatoires admettant une espérance (une norme $L^1$ finie). Or, l'intégrale pour l'espérance de la loi de Cauchy vaut :
$$ \int_{-\infty}^{\infty} |x| \frac{1}{\pi(1+x^2)} dx $$
L'intégrande se comporte comme $\frac{1}{|x|}$ à l'infini. L'intégrale de Riemann d'une fonction de la forme $\frac{1}{x^a}$ avec $a \le 1$ est divergente. La loi de Cauchy ne possède donc pas de moment d'ordre 1.
Pour étudier la somme, utilisons l'outil fondamental des probabilités additives : la fonction caractéristique.
La fonction caractéristique de la loi de Cauchy standard est connue et vaut :
$$ \phi_{X_1}(t) = \mathbb{E}[e^{itX_1}] = e^{-|t|} $$
Par indépendance des $X_i$, la fonction caractéristique de la somme s'obtient par multiplication :
$$ \phi_{\sum_{i=1}^n X_i}(t) = \prod_{i=1}^n \phi_{X_i}(t) = (e^{-|t|})^n = e^{-n|t|} $$
Appliquons la transformation linéaire due au coefficient $1/n$ : pour toute variable aléatoire $Y$ et scalaire $c$, $\phi_{cY}(t) = \phi_Y(ct)$.
$$ \phi_{S_n}(t) = \phi_{\frac{1}{n}\sum X_i}(t) = \phi_{\sum X_i}\left(\frac{t}{n}\right) = e^{-n\left|\frac{t}{n}\right|} = e^{-|t|} $$
Incroyablement, la fonction caractéristique de $S_n$ reste rigoureusement identique à celle de $X_1$ !
Puisque la fonction caractéristique détermine univoquement la loi d'une variable aléatoire (Théorème d'inversion de Fourier-Lévy), la variable empirique $S_n$ suit elle-même une loi de Cauchy standard pour tout $n$.
$$ S_n \sim \text{Cauchy}(0, 1) $$
Par conséquent, la suite des distributions de $S_n$ ne s'écrase pas vers un dirac en 0. Elle converge en loi vers une variable $X \sim \text{Cauchy}(0, 1)$ non-dégénérée.
Puisque la limite en loi n'est pas constante, et que la convergence en probabilité vers une variable impliquerait la convergence en loi vers cette même variable dégénérée, on conclut de manière absolue que $S_n$ ne converge **pas** en probabilité vers 0 (ni vers aucune constante).
A fortiori, puisqu'elle ne converge pas en probabilité, elle ne peut pas converger presque sûrement vers 0, pulvérisant ainsi l'idée naïve d'une stabilisation algorithmique de ces données.

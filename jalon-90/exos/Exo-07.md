---
uuid: "jalon-90-exo-07"
title: "Convergence des suites de Cauchy en probabilité"
---

# Exercice 7 : Convergence des suites de Cauchy en probabilité (Difficulté $\bigstar\bigstar\bigstar\bigstar\star$)

Démontrer que si une suite de variables aléatoires $(X_n)$ est de Cauchy en probabilité, alors il existe une variable aléatoire $X$ telle que $(X_n)$ converge en probabilité vers $X$.
*Rappel : $(X_n)$ est de Cauchy en probabilité si pour tout $\epsilon > 0$ et $\eta > 0$, il existe un entier $N$ tel que pour tout $n, m \geq N$, $\mathbb{P}(|X_n - X_m| > \epsilon) < \eta$.*

## Correction Pas-à-Pas

1. **Extraction d'une sous-suite à convergence rapide :**
   Appliquons la définition de la suite de Cauchy avec des choix précis de paramètres $\epsilon_k = 2^{-k}$ et $\eta_k = 2^{-k}$.
   Pour chaque entier $k \geq 1$, il existe un indice $n_k$ tel que pour tous $n, m \geq n_k$, on a :
   $$ \mathbb{P}(|X_n - X_m| > 2^{-k}) < 2^{-k} $$
   Nous pouvons construire la séquence des entiers $(n_k)_{k \ge 1}$ de manière à ce qu'elle soit strictement croissante : $n_1 < n_2 < \dots < n_k < \dots$.
   En particulier, pour les éléments consécutifs de la sous-suite $X_{n_k}$ et $X_{n_{k+1}}$, puisque $n_{k+1} > n_k \geq n_k$, nous avons :
   $$ \mathbb{P}(|X_{n_{k+1}} - X_{n_k}| > 2^{-k}) < 2^{-k} $$

2. **Utilisation du lemme de Borel-Cantelli :**
   Considérons l'événement $A_k = \{ |X_{n_{k+1}} - X_{n_k}| > 2^{-k} \}$.
   La somme des probabilités de ces événements est :
   $$ \sum_{k=1}^\infty \mathbb{P}(A_k) < \sum_{k=1}^\infty 2^{-k} = 1 < \infty $$
   La série étant convergente, le premier lemme de Borel-Cantelli garantit que :
   $$ \mathbb{P}\left(\limsup_{k \to \infty} A_k\right) = 0 $$
   Cela signifie qu'avec une probabilité $1$, l'événement $A_k$ ne se réalise qu'un nombre fini de fois.
   Il existe donc un ensemble $\Omega_0 \subset \Omega$ tel que $\mathbb{P}(\Omega_0) = 1$, et pour tout $\omega \in \Omega_0$, il existe un entier $K(\omega)$ tel que pour tout $k \geq K(\omega)$ :
   $$ |X_{n_{k+1}}(\omega) - X_{n_k}(\omega)| \leq 2^{-k} $$

3. **Convergence ponctuelle de la sous-suite :**
   Pour $\omega \in \Omega_0$, la série télescopique $\sum (X_{n_{k+1}}(\omega) - X_{n_k}(\omega))$ est absolument convergente car elle est majorée par la série géométrique $\sum 2^{-k}$.
   Une série dont le terme général est l'incrément d'une suite converge si et seulement si la suite elle-même converge.
   Par conséquent, pour tout $\omega \in \Omega_0$, la suite des valeurs réelles $(X_{n_k}(\omega))_{k \ge 1}$ est de Cauchy dans $\mathbb{R}$, un espace complet. Elle converge donc vers une limite finie.
   Définissons la variable aléatoire $X$ par :
   $$ X(\omega) = \lim_{k \to \infty} X_{n_k}(\omega) \text{ si } \omega \in \Omega_0, \text{ et } X(\omega) = 0 \text{ sinon.} $$
   Nous avons ainsi démontré que $X_{n_k} \xrightarrow{p.s.} X$.

4. **Convergence de la suite complète en probabilité :**
   Puisque la sous-suite converge presque sûrement, elle converge également en probabilité :
   $X_{n_k} \xrightarrow{\mathbb{P}} X$.
   Montrons que la suite complète converge vers $X$. Fixons $\epsilon > 0$. Par l'inégalité triangulaire :
   $$ |X_n - X| \leq |X_n - X_{n_k}| + |X_{n_k} - X| $$
   Pour que $|X_n - X| > \epsilon$, il faut qu'au moins l'un des deux termes dépasse $\epsilon/2$.
   $$ \mathbb{P}(|X_n - X| > \epsilon) \leq \mathbb{P}\left(|X_n - X_{n_k}| > \frac{\epsilon}{2}\right) + \mathbb{P}\left(|X_{n_k} - X| > \frac{\epsilon}{2}\right) $$
   L'hypothèse initiale stipule que $(X_n)$ est de Cauchy en probabilité. Il existe un rang $N$ pour le premier terme. Pour tout $n \geq N$ et en choisissant $n_k \geq N$, ce terme devient arbitrairement petit. Le second terme devient arbitrairement petit car la sous-suite converge.
   Ainsi, $\lim_{n \to \infty} \mathbb{P}(|X_n - X| > \epsilon) = 0$.
   La suite converge en probabilité.
   $\blacksquare$


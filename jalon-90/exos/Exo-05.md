---
uuid: "jalon-90-exo-05"
title: "Convergence $L^p$ et dommage collatéral"
---

# Exercice 5 : Convergence $L^p$ et dommage collatéral (Difficulté $\bigstar\bigstar\bigstar\star\star$)

Soit $p > q \geq 1$. Montrer que si une suite $(X_n)$ converge vers $X$ dans l'espace $L^p$, alors elle converge également dans $L^q$. L'inverse est-il vrai ?

## Correction Pas-à-Pas

1. **Convergence $L^p \implies L^q$ :**
   Supposons $X_n \xrightarrow{L^p} X$. Cela signifie que $\mathbb{E}\left[|X_n - X|^p\right] \to 0$.
   Nous voulons montrer que $\mathbb{E}\left[|X_n - X|^q\right] \to 0$.
   Puisque l'espace de probabilité $\Omega$ est de mesure totale $\mathbb{P}(\Omega) = 1 < \infty$, nous pouvons utiliser l'inégalité de Jensen ou l'inégalité de Hölder pour les moments.
   La fonction $\phi(x) = x^{p/q}$ est convexe sur $\mathbb{R}^+$ car $p/q > 1$.
   Considérons la variable aléatoire positive $Y_n = |X_n - X|^q$.
   D'après l'inégalité de Jensen :
   $$ \phi(\mathbb{E}[Y_n]) \leq \mathbb{E}[\phi(Y_n)] $$
   En substituant :
   $$ \left( \mathbb{E}\left[|X_n - X|^q\right] \right)^{p/q} \leq \mathbb{E}\left[ \left(|X_n - X|^q\right)^{p/q} \right] $$
   $$ \left( \mathbb{E}\left[|X_n - X|^q\right] \right)^{p/q} \leq \mathbb{E}\left[ |X_n - X|^p \right] $$
   En élevant à la puissance $q/p$ :
   $$ \mathbb{E}\left[|X_n - X|^q\right] \leq \left( \mathbb{E}\left[ |X_n - X|^p \right] \right)^{q/p} $$
   Puisque $\mathbb{E}\left[ |X_n - X|^p \right] \to 0$, le membre de droite tend vers $0^{q/p} = 0$.
   Ainsi, $\lim_{n \to \infty} \mathbb{E}\left[|X_n - X|^q\right] = 0$.
   $X_n \xrightarrow{L^q} X$.

2. **Réciproque : $L^q \implies L^p$ (Faux) :**
   Construisons un contre-exemple. Soit $p = 2$ et $q = 1$.
   Considérons $X = 0$ et $X_n$ définie par :
   $$ \mathbb{P}(X_n = n) = \frac{1}{n \sqrt{n}}, \quad \mathbb{P}(X_n = 0) = 1 - \frac{1}{n \sqrt{n}} $$
   Calcul de la norme $L^1$ :
   $$ \mathbb{E}[|X_n|] = n \cdot \frac{1}{n \sqrt{n}} = \frac{1}{\sqrt{n}} $$
   La limite est $0$, donc $X_n \xrightarrow{L^1} 0$.

   Calcul de la norme $L^2$ (carrée) :
   $$ \mathbb{E}[|X_n|^2] = n^2 \cdot \frac{1}{n \sqrt{n}} = \frac{n^2}{n^{1.5}} = n^{0.5} = \sqrt{n} $$
   La limite est $+\infty$. La suite ne converge pas dans $L^2$.
   L'implication inverse est donc fausse.
   $\blacksquare$


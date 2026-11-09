---
uuid: "jalon-90-exo-02"
title: "Convergence en probabilité versus $L^1$"
---

# Exercice 2 : Convergence en probabilité versus $L^1$ (Difficulté $\bigstar\star\star\star\star$)

Soit $(X_n)_{n \geq 1}$ une suite de variables aléatoires vérifiant $\mathbb{P}(X_n = n) = 1/\sqrt{n}$ et $\mathbb{P}(X_n = 0) = 1 - 1/\sqrt{n}$.

1. Étudier la convergence de la suite $(X_n)$ en probabilité.
2. Étudier la convergence de la suite $(X_n)$ dans l'espace $L^1$.

## Correction Pas-à-Pas

1. **Convergence en probabilité :**
   Soit $\epsilon > 0$. Fixons $n$ suffisamment grand pour que $n > \epsilon$.
   La probabilité que $X_n$ s'éloigne de $0$ de plus de $\epsilon$ est :
   $$ \mathbb{P}(|X_n - 0| > \epsilon) = \mathbb{P}(X_n = n) = \frac{1}{\sqrt{n}} $$
   Calculons la limite lorsque $n \to \infty$ :
   $$ \lim_{n \to \infty} \frac{1}{\sqrt{n}} = 0 $$
   Par définition, cela signifie que la suite $(X_n)$ converge en probabilité vers la variable aléatoire constante $0$ :
   $$ X_n \xrightarrow{\mathbb{P}} 0 $$

2. **Convergence dans $L^1$ :**
   Calculons l'espérance de la valeur absolue de l'écart par pour à $0$ :
   $$ \mathbb{E}\left[|X_n - 0|\right] = \mathbb{E}[X_n] = n \cdot \mathbb{P}(X_n = n) + 0 \cdot \mathbb{P}(X_n = 0) $$
   $$ \mathbb{E}[X_n] = n \times \frac{1}{\sqrt{n}} = \sqrt{n} $$
   Calculons la limite lorsque $n \to \infty$ :
   $$ \lim_{n \to \infty} \sqrt{n} = +\infty $$
   L'espérance ne tend pas vers zéro (elle diverge vers $+\infty$).
   La suite $(X_n)$ ne converge donc **pas** dans $L^1$.
   $\blacksquare$


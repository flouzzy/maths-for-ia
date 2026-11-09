---
uuid: "jalon-90-exo-06"
title: "Théorème de Slutsky (Version simple)"
---

# Exercice 6 : Théorème de Slutsky (Version simple) (Difficulté $\bigstar\bigstar\bigstar\star\star$)

Soit $(X_n)$ une suite convergeant en loi vers une variable $X$. Soit $(Y_n)$ une suite convergeant en probabilité vers une constante $c$.
Démontrer que la suite définie par la somme $X_n + Y_n$ converge en loi vers $X + c$.

## Correction Pas-à-Pas

1. **Objectif :**
   Nous devons montrer que pour toute fonction $f : \mathbb{R} \to \mathbb{R}$ uniformément continue et bornée (une réduction classique autorisée pour la convergence en loi), on a :
   $$ \lim_{n \to \infty} \mathbb{E}[f(X_n + Y_n)] = \mathbb{E}[f(X + c)] $$

2. **Décomposition de l'erreur :**
   Nous écrivons la différence :
   $$ |\mathbb{E}[f(X_n + Y_n)] - \mathbb{E}[f(X + c)]| \leq |\mathbb{E}[f(X_n + Y_n)] - \mathbb{E}[f(X_n + c)]| + |\mathbb{E}[f(X_n + c)] - \mathbb{E}[f(X + c)]| $$

3. **Traitement du deuxième terme :**
   Définissons la fonction $g(x) = f(x + c)$. Puisque $f$ est continue et bornée, $g$ l'est aussi.
   Par l'hypothèse de convergence en loi de $X_n$ vers $X$, nous avons par définition :
   $$ \lim_{n \to \infty} \mathbb{E}[g(X_n)] = \mathbb{E}[g(X)] $$
   Donc $|\mathbb{E}[f(X_n + c)] - \mathbb{E}[f(X + c)]| \to 0$.

4. **Traitement du premier terme :**
   Nous devons majorer $\mathbb{E}[|f(X_n + Y_n) - f(X_n + c)|]$.
   Soit $M$ la borne de $f$.
   Puisque $f$ est uniformément continue, pour tout $\epsilon > 0$, il existe $\delta > 0$ tel que $|u - v| \leq \delta \implies |f(u) - f(v)| \leq \epsilon$.
   Considérons l'événement $A_n = \{ |Y_n - c| > \delta \}$.
   Sur le complémentaire $A_n^c$, on a $|(X_n + Y_n) - (X_n + c)| = |Y_n - c| \leq \delta$, donc l'écart des fonctions est inférieur à $\epsilon$.
   Décomposons l'espérance :
   $$ \mathbb{E}[|f(X_n + Y_n) - f(X_n + c)|] \leq \mathbb{E}[\epsilon \cdot \mathbf{1}_{A_n^c}] + \mathbb{E}[2M \cdot \mathbf{1}_{A_n}] $$
   $$ \mathbb{E}[|f(X_n + Y_n) - f(X_n + c)|] \leq \epsilon \cdot 1 + 2M \cdot \mathbb{P}(A_n) $$
   Par l'hypothèse de convergence en probabilité de $Y_n$ vers $c$, la probabilité $\mathbb{P}(A_n) = \mathbb{P}(|Y_n - c| > \delta)$ tend vers $0$ lorsque $n \to \infty$.
   La limite supérieure de ce terme est donc $\epsilon$. Puisque $\epsilon$ est arbitraire, la limite exacte est $0$.

5. **Conclusion finale :**
   Les deux composantes de l'erreur tendent vers $0$.
   $$ \lim_{n \to \infty} \mathbb{E}[f(X_n + Y_n)] = \mathbb{E}[f(X + c)] $$
   Ainsi, $X_n + Y_n \xrightarrow{\mathcal{L}} X + c$.
   $\blacksquare$


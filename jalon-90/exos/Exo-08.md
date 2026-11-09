---
uuid: "jalon-90-exo-08"
title: "Application du Lemme de Fatou aux modes de convergence"
---

# Exercice 8 : Application du Lemme de Fatou aux modes de convergence (Difficulté $\bigstar\bigstar\bigstar\bigstar\star$)

Soit $(X_n)$ une suite de variables aléatoires positives convergeant en probabilité vers une variable $X$.
Démontrer l'équivalent du lemme de Fatou pour la convergence en probabilité :
$$ \mathbb{E}[X] \leq \liminf_{n \to \infty} \mathbb{E}[X_n] $$

## Correction Pas-à-Pas

1. **Extraction d'une sous-suite convergente :**
   On pose $L = \liminf_{n \to \infty} \mathbb{E}[X_n]$. Si $L = +\infty$, l'inégalité est immédiate. On suppose donc $L < +\infty$.
   Par définition de la limite inférieure, il existe une sous-suite $(X_{n_k})$ telle que :
   $$ \lim_{k \to \infty} \mathbb{E}[X_{n_k}] = \liminf_{n \to \infty} \mathbb{E}[X_n] $$

2. **Propriété de Riesz pour la convergence en probabilité :**
   Puisque la suite originelle $(X_n)$ converge en probabilité vers $X$, toute sous-suite de $(X_n)$ converge également en probabilité vers $X$.
   C'est le cas pour la sous-suite $(X_{n_k})$.
   D'après le théorème de Riesz-Weyl (réciproque partielle), si une suite converge en probabilité, on peut en extraire une sous-suite qui converge presque sûrement.
   Il existe donc une sous-sous-suite $(X_{n_{k_j}})_{j \ge 1}$ telle que :
   $$ X_{n_{k_j}} \xrightarrow{p.s.} X $$

3. **Application du Lemme de Fatou classique :**
   La suite $(X_{n_{k_j}})$ est une suite de variables aléatoires positives qui converge presque sûrement (donc presque partout par rapport à la mesure $\mathbb{P}$) vers $X$.
   Le lemme de Fatou standard de la théorie de l'intégration stipule que pour une telle convergence p.s. (ou ponctuelle p.p.) :
   $$ \mathbb{E}[X] = \mathbb{E}\left[ \liminf_{j \to \infty} X_{n_{k_j}} \right] \leq \liminf_{j \to \infty} \mathbb{E}\left[ X_{n_{k_j}} \right] $$

4. **Clôture de la preuve :**
   Puisque la sous-suite des espérances $(\mathbb{E}[X_{n_{k_j}}])$ est extraite de la sous-suite $(\mathbb{E}[X_{n_k}])$ qui converge vers la limite inférieure $L$, on a :
   $$ \liminf_{j \to \infty} \mathbb{E}\left[ X_{n_{k_j}} \right] = \lim_{k \to \infty} \mathbb{E}[X_{n_k}] = \liminf_{n \to \infty} \mathbb{E}[X_n] $$
   En substituant ce résultat dans l'inégalité précédente :
   $$ \mathbb{E}[X] \leq \liminf_{n \to \infty} \mathbb{E}[X_n] $$
   L'inégalité est démontrée.
   $\blacksquare$


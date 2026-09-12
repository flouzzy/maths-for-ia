---
uuid: "jalon-68"
title: "Lemme de Fatou et fonctions de signe quelconque"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[jalon-67/Jalon-67.md|Jalon 67 (Démonstration du théorème de convergence monotone)]]"
next: "[[Jalon 69 (Démonstration complète du théorème de convergence dominée de Lebesgue.).md]]"
---

# Jalon 68 : Lemme de Fatou et fonctions de signe quelconque

## 1. Présentation du concept clé

Le lemme de Fatou est un outil fondamental de l'intégration de Lebesgue. Il stipule que pour une suite de fonctions mesurables positives, l'intégrale de la limite inférieure est toujours majorée par la limite inférieure des intégrales. Cela traduit le fait qu'à la limite, de la masse peut disparaître (vers l'infini ou en s'échappant vers un point de manière singulière), mais elle ne peut pas se créer ex nihilo.


## 2. Formalisation

### A. Le Lemme de Fatou

> **Lemme de Fatou :**
> Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables de $X$ dans $[0, +\infty]$. Alors :
> $$\int_X \left( \liminf_{n \to \infty} f_n \right) d\mu \le \liminf_{n \to \infty} \int_X f_n d\mu$$

### B. Fonctions de signe quelconque

Soit $f : X \to \mathbb{R}$ une fonction mesurable. On définit :
- Partie positive : $f^+(x) = \max(f(x), 0)$
- Partie négative : $f^-(x) = \max(-f(x), 0)$
On a alors $f = f^+ - f^-$ and $|f| = f^+ + f^-$.

> **Définition (Intégrabilité) :**
> On dit que $f$ est **intégrable** (ou appartient à $\mathcal{L}^1(\mu)$) si les intégrales de $f^+$ et $f^-$ sont finies. L'intégrale de $f$ est alors définie par :
> $$\int_X f d\mu = \int_X f^+ d\mu - \int_X f^- d\mu$$

## 3. Démonstrations

### Démonstration du Lemme de Fatou

1. **Cadre :** Posons $g_k = \inf_{n \ge k} f_n$. La suite $(g_k)$ est une suite croissante de fonctions mesurables positives.
2. **Limite :** Par définition, $\lim_{k \to \infty} g_k = \liminf f_n$.
3. **Application du TCM (Beppo Levi) :** D'après le Jalon 67 :
   $$\int \liminf f_n = \int \lim g_k = \lim \int g_k$$
4. **Inégalité sur l'infimum :** Pour tout $n \ge k$, on a $g_k \le f_n$.
   Par croissance de l'intégrale : $\int g_k \le \int f_n$ pour tout $n \ge k$.
   Donc $\int g_k \le \inf_{n \ge k} \int f_n$.
5. **Passage à la limite :**
   $$\lim_{k \to \infty} \int g_k \le \lim_{k \to \infty} \left( \inf_{n \ge k} \int f_n \right) = \liminf \int f_n$$
6. **Conclusion :** $\int \liminf f_n \le \liminf \int f_n$.

## 4. Exercices d'Application

### Exercice 1 : Inégalité stricte dans Fatou
**Énoncé :** Soit $f_n = n \mathbf{1}_{]0, 1/n[}$ sur $\mathbb{R}$ avec la mesure de Lebesgue.
1. Calculer $\int f_n d\lambda$.
2. Calculer $f = \liminf f_n$.
3. Vérifier le lemme de Fatou.
**Correction Détaillée :**
1. $\int f_n = n \cdot \lambda(]0, 1/n[) = n \cdot (1/n) = 1$. La limite des intégrales est donc 1.
2. Pour tout $x > 0$, $1/n$ finit par être plus petit que $x$, donc $f_n(x) = 0$ pour $n$ assez grand. Pour $x \le 0$, $f_n(x)=0$. Donc $f(x) = 0$ partout. $\int f = 0$.
3. On a bien $0 \le 1$. L'inégalité est stricte. Ici, la "masse" (l'aire de 1) s'est échappée vers l'origine en devenant infiniment haute et fine, elle a disparu à la limite.

### Exercice 2 : Niveau Avancé (Intégrabilité)
**Énoncé :** Montrer que $f$ est intégrable si et seulement si $|f|$ est intégrable.
**Correction Détaillée :**
1. **Sens ($\implies$) :** Si $f$ est intégrable, alors $\int f^+$ et $\int f^-$ sont finies. Comme $|f| = f^+ + f^-$, par linéarité $\int |f| = \int f^+ + \int f^-$, qui est une somme de deux nombres finis.
2. **Sens ($\impliedby$) :** Comme $0 \le f^+ \le |f|$ and $0 \le f^- \le |f|$, par croissance, si $\int |f| < \infty$, alors les deux intégrales sont finies.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** En IA, on manipule souvent des **récompenses** (Rewards) en Reinforcement Learning qui peuvent être positives ou négatives. La définition de l'espérance du gain total nécessite ce cadre.
- **Example Concret :**
    - **Optimisation de Portefeuille :** On intègre des rendements qui peuvent être négatifs (pertes). L'intégrabilité garantit que le risque moyen est calculable.
    - **Fonctions de score (Log-Likelihood) :** La log-vraisemblance $\ln(p(x))$ est presque toujours négative (car $p(x) \le 1$). Pour calculer l'information de Fisher ou l'entropie, on utilise la décomposition en parties positives et négatives.
    - **Stabilité des Algorithmes :** Le lemme de Fatou est utilisé pour prouver que si une suite de modèles a une erreur moyenne qui converge, alors le modèle limite ne peut pas être "pire" que la limite de l'erreur. C'est une garantie de sécurité pour la convergence des algorithmes stochastiques.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[jalon-67/Jalon-67.md|Jalon 67 (Démonstration du théorème de convergence monotone)]], [[Jalon 66 (Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives.).md]]
- **Concepts Futurs dépendants :** [[Jalon 69 (Démonstration complète du théorème de convergence dominée de Lebesgue.).md]], [[Jalon 73 (Définition des espaces Lp).md]]

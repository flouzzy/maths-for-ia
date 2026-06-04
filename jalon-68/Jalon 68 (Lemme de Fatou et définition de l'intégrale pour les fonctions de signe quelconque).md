---
uuid: "jalon-68"
title: "Lemme de Fatou et fonctions de signe quelconque"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 67 (Démonstration du théorème de convergence monotone).md]]"
next: "[[Jalon 69 (Démonstration complète du théorème de convergence dominée de Lebesgue.).md]]"
---

# Jalon 68 : Lemme de Fatou et fonctions de signe quelconque

## 1. Présentation du concept clé

- **La Métaphore :**
    - **Le Lemme de Fatou :** Imaginez des athlètes qui sautent en hauteur. Chaque athlète fait plusieurs essais ($f_n$). La "performance minimale garantie" de l'équipe à la fin ($\liminf f_n$) ne peut pas être plus grande que la moyenne des performances au fil du temps. Autrement dit, si de la "masse" s'échappe vers l'infini ou s'évapore dans des oscillations folles, l'intégrale de la limite sera plus petite que la limite des intégrales. On peut perdre de l'information à la limite, mais on n'en gagne jamais par magie.
    - **Le Signe Quelconque :** Imaginez un compte bancaire. Vous avez des rentrées d'argent (le côté positif $f^+$) et des dépenses (le côté négatif $f^-$). Pour savoir si vous êtes globalement riche ou pauvre, vous calculez séparément le total de ce que vous avez gagné et le total de ce que vous avez dépensé, puis vous faites la soustraction. Si les deux totaux sont finis, votre situation est bien définie.
- **Le "Pourquoi on a inventé ça" :** Jusqu'ici, on ne savait intégrer que des fonctions positives. Mais en physique ou en finance, les flux peuvent être négatifs. Il fallait donc étendre la définition de Lebesgue tout en gardant une cohérence mathématique absolue.
- **Visualisation :** On découpe une fonction qui ondule au-dessus et en dessous de l'axe des abscisses en deux fonctions strictement positives. L'intégrale totale est l'aire au-dessus moins l'aire en dessous.

## 2. Formalisation & Rigueur Académique

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

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

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

## 4. Exercices d'Application & Pratique de Concours

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

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** En IA, on manipule souvent des **récompenses** (Rewards) en Reinforcement Learning qui peuvent être positives ou négatives. La définition de l'espérance du gain total nécessite ce cadre.
- **Example Concret :**
    - **Optimisation de Portefeuille :** On intègre des rendements qui peuvent être négatifs (pertes). L'intégrabilité garantit que le risque moyen est calculable.
    - **Fonctions de score (Log-Likelihood) :** La log-vraisemblance $\ln(p(x))$ est presque toujours négative (car $p(x) \le 1$). Pour calculer l'information de Fisher ou l'entropie, on utilise la décomposition en parties positives et négatives.
    - **Stabilité des Algorithmes :** Le lemme de Fatou est utilisé pour prouver que si une suite de modèles a une erreur moyenne qui converge, alors le modèle limite ne peut pas être "pire" que la limite de l'erreur. C'est une garantie de sécurité pour la convergence des algorithmes stochastiques.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 67 (Démonstration du théorème de convergence monotone).md]], [[Jalon 66 (Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives.).md]]
- **Concepts Futurs dépendants :** [[Jalon 69 (Démonstration complète du théorème de convergence dominée de Lebesgue.).md]], [[Jalon 73 (Définition des espaces Lp).md]]

---
uuid: "jalon-30"
title: "Trigonalisation d'endomorphismes et décomposition de Dunford"
year: 1
trimester: 3
tags:
  - math/algebre-lineaire
  - ia/reduction-avancee
prev: "[[Jalon 29 (Éléments propres).md]]"
next: "[[Jalon 31 (Introduction à la réduction de Jordan et structure des nilpotents.).md]]"
---

# Jalon 30 : Trigonalisation d'endomorphismes et décomposition de Dunford

## 1. L'Intuition Première (Niveau 12 ans)
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** 
  - **Trigonalisation :** Parfois, une transformation ne peut pas être diagonalisée (on ne peut pas trouver une base où elle n'est que des étirements sur les axes). La trigonalisation, c'est trouver une base où la transformation est "presque" diagonale : elle se comporte comme des étirements sur les axes principaux, avec des petits effets de cisaillement en plus (les nombres au-dessus de la diagonale).
  - **Décomposition de Dunford :** C'est le théorème du "diviser pour régner". Il dit que toute transformation un peu complexe peut être séparée en deux parties : une partie parfaitement "simple" (diagonalisable) et une partie "nuisible" (nilpotente, qui finit par disparaître si on la met à une puissance suffisante) qui commutent ensemble.
- **Le "Pourquoi on a inventé ça" :** Les matrices non diagonalisables sont un cauchemar pour le calcul des puissances ou de l'exponentielle de matrice. La décomposition de Dunford permet de traiter ces deux types de comportements séparément, simplifiant ainsi drastiquement les calculs.
- **Visualisation :** Une matrice triangulaire, c'est comme une transformation qui étire les axes, mais où chaque axe peut "tirer" sur les axes précédents.

## 2. Formalisation & Rigueur Académique
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
1. **Trigonalisation :** $f$ est trigonalisable s'il existe une base $\mathcal{B}$ telle que $\text{Mat}_{\mathcal{B}}(f)$ soit triangulaire supérieure.
2. **Décomposition de Dunford :** Soit $f \in \mathcal{L}(E)$ dont le polynôme caractéristique est scindé. Il existe un unique couple $(d, n)$ tel que $f = d + n$, avec $d$ diagonalisable, $n$ nilpotent, et $d \circ n = n \circ d$.

### B. Théorèmes, Propositions & Lemmes
> **Théorème (Trigonalisation) :**
> $f$ est trigonalisable $\iff \chi_f$ est scindé sur $\mathbb{K}$.

> **Propriété de Dunford :**
> Les éléments $d$ et $n$ sont des polynômes en $f$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas
### Démonstration : Existence de la trigonalisation (par récurrence)
1. **Initialisation :** $n=1$, trivial.
2. **Hérédité :** Soit $f$ de dimension $n$ avec $\chi_f$ scindé. Soit $\lambda$ une valeur propre et $e_1$ un vecteur propre associé.
3. **Réduction :** Soit $F = \text{Vect}(e_1)$. On passe au quotient $E/F$. $f$ induit $\bar{f}$ sur $E/F$.
4. **Récurrence :** $\chi_{\bar{f}}$ est scindé. Il existe une base de $E/F$ trigonalisant $\bar{f}$.
5. **Conclusion :** En relevant cette base dans $E$, on obtient une base de trigonalisation.

## 4. Exercices d'Application
### Exercice 1 : Dunford
$A = \begin{pmatrix} 1 & 1 \ 0 & 1 \end{pmatrix}$. $D = I_2$, $N = \begin{pmatrix} 0 & 1 \ 0 & 0 \end{pmatrix}$. $A = D + N$.

## 5. Ancrage & Application en IA
*   **Les systèmes dynamiques** (RNNs) utilisent la décomposition de Dunford pour analyser la stabilité à long terme : la partie diagonale donne le taux de croissance (exponentiel), la partie nilpotente donne la croissance polynomiale.

## 6. Liens Obsidian
- [[Jalon 29 (Éléments propres).md]], [[Jalon 31 (Introduction à la réduction de Jordan et structure des nilpotents.).md]]

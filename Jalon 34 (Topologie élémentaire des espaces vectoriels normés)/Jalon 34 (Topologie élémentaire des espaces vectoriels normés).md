---
uuid: "jalon-34"
title: "Topologie élémentaire des espaces vectoriels normés"
year: 1
trimester: 3
tags:
  - math/analyse
  - ia/regularisation
prev: "[[Jalon 33 (Formes quadratiques).md]]"
next: "[[Jalon 35 (Caractérisation séquentielle des ouverts).md]]"
---

# Jalon 34 : Topologie élémentaire des espaces vectoriels normés

## 1. Présentation du concept clé

- **La Métaphore :** Comment mesurer la distance entre deux points ? Si vous êtes un oiseau, vous volez en ligne droite (c'est la distance "normale"). Si vous êtes un taxi à New York, vous devez suivre les rues perpendiculaires (c'est la distance "Manhattan"). Une **norme**, c'est simplement une règle du jeu pour mesurer une "taille" ou une "distance". Selon la règle choisie, la forme d'un "cercle" change : il peut être rond, carré ou en forme de losange !
- **Le "Pourquoi on a inventé ça" :** En mathématiques, on veut savoir si une suite de nombres ou de fonctions s'approche d'une cible. Pour dire "proche", il faut pouvoir mesurer l'écart. Les espaces vectoriels normés (EVN) fournissent le cadre rigoureux pour parler de limites, de continuité et de convergence sans avoir besoin d'un dessin.
- **Visualisation :** Dessinez l'ensemble des points à distance 1 de l'origine. Avec la norme usuelle, c'est un cercle. Avec la norme "Manhattan" (somme des valeurs absolues), c'est un losange tourné à 45°. Avec la norme "Maximum", c'est un carré.

## 2. Formalisation

### A. Définitions Formelles

Soit $E$ un espace vectoriel sur $\mathbb{K} = \mathbb{R}$ ou $\mathbb{C}$.

> **Définition 1 (Norme) :**
> On appelle **norme** sur $E$ une application $N : E \to \mathbb{R}_+$ (souvent notée $\| \cdot \|$) vérifiant les trois axiomes suivants :
> 1. **Séparation :** $\forall x \in E, \quad \|x\| = 0 \iff x = 0_E$.
> 2. **Homogénéité :** $\forall \lambda \in \mathbb{K}, \forall x \in E, \quad \|\lambda x\| = |\lambda| \cdot \|x\|$.
> 3. **Inégalité Triangulaire :** $\forall x, y \in E, \quad \|x + y\| \le \|x\| + \|y\|$.

> **Définition 2 (Boules) :**
> Soit $a \in E$ et $r > 0$.
> - Boule ouverte : $B(a, r) = \{ x \in E \mid \|x - a\| < r \}$.
> - Boule fermée : $\bar{B}(a, r) = \{ x \in E \mid \|x - a\| \le r \}$.

> **Définition 3 (Équivalence des normes) :**
> Deux normes $N_1$ et $N_2$ sur $E$ sont dites **équivalentes** s'il existe deux constantes $C_1, C_2 > 0$ telles que :
> $$\forall x \in E, \quad C_1 N_1(x) \le N_2(x) \le C_2 N_1(x)$$

### B. Théorèmes Fondamentaux

> **Théorème de l'Équivalence (Dimension Finie) :**
> Sur un espace vectoriel de dimension finie, toutes les normes sont équivalentes.

> **Propriété (Continuité de la norme) :**
> Toute norme est une application lipschitzienne (donc continue) sur $E$ pour elle-même :
> $| \|x\| - \|y\| | \le \|x - y\|$.

## 3. Démonstrations

### Démonstration du Théorème d'Équivalence des Normes en Dimension Finie

Nous allons montrer que toute norme $N$ sur $E$ est équivalente à la norme infinie $\| \cdot \|_\infty$ dans une base $\mathcal{B} = (e_1, \dots, e_n)$.

1. **Étape 1 : Majoration de N par $\| \cdot \|_\infty$**
   Soit $x = \sum_{i=1}^n x_i e_i$. Par inégalité triangulaire et homogénéité :
   $$N(x) = N\left( \sum_{i=1}^n x_i e_i \right) \le \sum_{i=1}^n |x_i| N(e_i)$$
   Comme $|x_i| \le \|x\|_\infty$ pour tout $i$, on a :
   $$N(x) \le \left( \sum_{i=1}^n N(e_i) \right) \|x\|_\infty$$
   En posant $C_2 = \sum N(e_i)$, on a $N(x) \le C_2 \|x\|_\infty$. Cela montre que $N$ est continue pour $\| \cdot \|_\infty$.

2. **Étape 2 : Minoration (Utilisation de la compacité)**
   Considérons la sphère unité pour la norme infinie : $S_\infty = \{ x \in E \mid \|x\|_\infty = 1 \}$.
   $S_\infty$ est un ensemble fermé et borné en dimension finie, donc compact (Théorème de Borel-Lebesgue).
   L'application $N$ est continue sur ce compact (d'après l'étape 1). Elle y atteint son minimum $m$.
   Comme $x \in S_\infty$, $x \neq 0$, donc par l'axiome de séparation, $N(x) > 0$. Ainsi $m > 0$.
   Pour tout $x \neq 0$, on a $\frac{x}{\|x\|_\infty} \in S_\infty$, donc :
   $$N\left( \frac{x}{\|x\|_\infty} \right) \ge m \implies N(x) \ge m \|x\|_\infty$$
   En posant $C_1 = m$, on a la minoration.

3. **Conclusion :**
   $C_1 \|x\|_\infty \le N(x) \le C_2 \|x\|_\infty$. Toutes les normes sont équivalentes à $\| \cdot \|_\infty$, donc elles sont toutes équivalentes entre elles par transitivité.

## 4. Exercices d'Application

### Exercice 1 : Comparaison de normes usuelles
**Énoncé :** Sur $\mathbb{R}^n$, on considère $\|x\|_1 = \sum |x_i|$, $\|x\|_2 = \sqrt{\sum x_i^2}$ et $\|x\|_\infty = \max |x_i|$.
Montrer que $\|x\|_\infty \le \|x\|_2 \le \|x\|_1 \le n \|x\|_\infty$.

**Correction Détaillée :**
* *$\|x\|_\infty \le \|x\|_2$ :* Soit $j$ l'indice tel que $|x_j| = \|x\|_\infty$. Alors $\|x\|_2^2 = \sum x_i^2 \ge x_j^2 = \|x\|_\infty^2$. En prenant la racine, c'est démontré.
* *$\|x\|_2 \le \|x\|_1$ :* $\|x\|_1^2 = (\sum |x_i|)^2 = \sum x_i^2 + \sum_{i \neq j} |x_i x_j| \ge \sum x_i^2 = \|x\|_2^2$.
* *$\|x\|_1 \le n \|x\|_\infty$ :* Chaque $|x_i| \le \|x\|_\infty$, on somme $n$ fois, d'où le résultat.

### Exercice 2 : Non-équivalence en dimension infinie
**Énoncé :** Sur $E = \mathcal{C}([0, 1], \mathbb{R})$, montrer que $\|f\|_1 = \int_0^1 |f(t)| dt$ et $\|f\|_\infty = \sup |f(t)|$ ne sont pas équivalentes.

**Correction Détaillée :**
Considérons la suite de fonctions $f_n(t) = t^n$.
$\|f_n\|_\infty = 1$ pour tout $n$.
$\|f_n\|_1 = \int_0^1 t^n dt = \frac{1}{n+1}$.
Si les normes étaient équivalentes, on aurait $C_1 \|f_n\|_\infty \le \|f_n\|_1$, soit $C_1 \le \frac{1}{n+1}$ pour tout $n$. En faisant tendre $n \to \infty$, on obtient $C_1 \le 0$, ce qui contredit $C_1 > 0$.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** En IA, le choix de la norme pour définir la fonction de perte (loss function) ou la régularisation change radicalement le comportement du modèle. C'est ce qu'on appelle la **géométrie de l'apprentissage**.
- **Exemple Concret :**
    - **Régularisation L2 (Ridge) :** Utilise la norme $\|\theta\|_2^2$. Comme la boule unité est ronde, elle tend à réduire uniformément les poids sans les annuler complètement.
    - **Régularisation L1 (Lasso) :** Utilise la norme $\|\theta\|_1$. Comme la boule unité a des pointes sur les axes (forme de losange), le minimum de la fonction de perte a de fortes chances de se trouver sur un axe, forçant certains poids à être **exactement nuls**. C'est fondamental pour la **sélection de variables** (sparse models).

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 7 (Espaces vectoriels abstraits).md]], [[Jalon 26 (Espaces euclidiens).md]]
- **Concepts Futurs dépendants :** [[Jalon 35 (Caractérisation séquentielle des ouverts).md]], [[Jalon 56 (Espaces métriques complets).md]]

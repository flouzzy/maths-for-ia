---
uuid: "jalon-13"
title: "Structure de R, axiome de la borne supérieure et propriété d'Archimède"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/continuite-numerique
prev: "[[Jalon 12 (Livrable IA).md]]"
next: "[[Jalon 14 (Suites réelles et complexes).md]]"
---
# Jalon 13 : Structure de $\mathbb{R}$, axiome de la borne supérieure et propriété d'Archimède

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Imaginez une règle graduée infiniment longue. Si vous n'utilisez que des nombres entiers (1, 2, 3), il y a des trous géants entre les marques. Si vous utilisez des fractions (1/2, 2/3), la règle semble pleine, mais en fait, elle est encore pleine de micro-trous invisibles (comme $\sqrt{2}$ ou $\pi$). L'ensemble des nombres réels ($\mathbb{R}$), c'est la règle **parfaite** : il n'y a absolument aucun trou. C'est comme une ligne de soie continue. L'**axiome de la borne supérieure**, c'est la garantie que si vous essayez de monter un escalier de nombres sans fin, il y a toujours un plafond (une limite) que vous allez toucher ou frôler de très près.
- **Le "Pourquoi on a inventé ça" :** Les Grecs ont découvert avec horreur que la diagonale d'un carré de côté 1 ne pouvait pas s'écrire comme une fraction. Il fallait inventer un nouveau monde de nombres pour que la géométrie et le calcul s'entendent. Sans $\mathbb{R}$, on ne pourrait pas définir la notion de "limite" ou de "courbe lisse".
- **Visualisation :** Imaginez zoomer indéfiniment sur la droite numérique. Avec les fractions, vous finiriez par tomber dans le vide. Avec les réels, peu importe la puissance de votre microscope, vous verrez toujours une ligne pleine.

## 2. Formalisation
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
1. **Corps Totalement Ordonné :** $\mathbb{R}$ est un corps muni d'une relation d'ordre total $\le$ compatible avec les opérations $+$ et $\times$.
2. **Majorant / Borne Supérieure :** Soit $A \subset \mathbb{R}$ une partie non vide.
   - $M \in \mathbb{R}$ est un **majorant** de $A$ si $\forall x \in A, x \le M$.
   - $S \in \mathbb{R}$ est la **borne supérieure** de $A$ (notée $\sup A$) si $S$ est le plus petit des majorants de $A$.
3. **Axiome de la Borne Supérieure :** Toute partie de $\mathbb{R}$ non vide et majorée admet une borne supérieure dans $\mathbb{R}$.
4. **Propriété d'Archimède :** $\mathbb{R}$ est archimédien : $\forall x \in \mathbb{R}, \forall \epsilon > 0, \exists n \in \mathbb{N}, n\epsilon > x$.

### B. Théorèmes, Propositions & Lemmes
> **Caractérisation de la borne supérieure :**
> $S = \sup A \iff \begin{cases} \forall x \in A, x \le S \\ \forall \epsilon > 0, \exists x_\epsilon \in A, S - \epsilon < x_\epsilon \end{cases}$

> **Théorème de la densité de $\mathbb{Q}$ dans $\mathbb{R}$ :**
> Entre deux nombres réels distincts, il existe toujours un nombre rationnel.
> $$\forall x, y \in \mathbb{R}, x < y \Rightarrow \exists q \in \mathbb{Q}, x < q < y$$

## 3. Démonstrations
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : La partie entière et le caractère archimédien
Démontrons l'existence et l'unicité de la partie entière d'un réel $x$, notée $\lfloor x \rfloor$.
Théorème : $\forall x \in \mathbb{R}, \exists ! n \in \mathbb{Z}, n \le x < n+1$.

1. **Initialisation / Cadre :** Soit $x \in \mathbb{R}$.
   - Considérons l'ensemble $E = \{ k \in \mathbb{Z} \mid k \le x \}$.
   - Pour prouver l'existence de $n$, nous devons montrer que $E$ possède un plus grand élément.

2. **Étape 1 : Montrons que $E$ est non vide**
   - Si $x \ge 0$, alors $0 \in E$ (car $0 \in \mathbb{Z}$ et $0 \le x$).
   - Si $x < 0$, par la propriété d'Archimède appliquée à $-x$ et $\epsilon=1$, il existe $m \in \mathbb{N}$ tel que $m \cdot 1 > -x$, soit $-m < x$. Comme $-m \in \mathbb{Z}$, alors $-m \in E$.
   $E$ est donc non vide dans tous les cas.

3. **Étape 2 : Montrons que $E$ est majoré**
   - Par définition de $E$, tout élément $k \in E$ vérifie $k \le x$.
   - $E$ est donc majoré par $x$.

4. **Étape 3 : Application de l'axiome de la borne supérieure**
   - $E \subset \mathbb{Z} \subset \mathbb{R}$, $E \neq \emptyset$ et $E$ majoré.
   - D'après l'axiome de la borne supérieure, $E$ admet une borne supérieure $S = \sup E$.
   - Par caractérisation du $\sup$, il existe $n \in E$ tel que $S - 1 < n \le S$.
   - Montrons que $n$ est le plus grand élément de $E$.
   - Supposons qu'il existe $k \in E$ tel que $k \ge n+1$.
   - Alors $k > S$ (car $n+1 > S$), ce qui contredit le fait que $S$ est un majorant de $E$.
   - Donc $\forall k \in E, k \le n$. $n = \max E$.

5. **Conclusion :**
   - Puisque $n \in E$, $n \le x$.
   - Comme $n = \max E$, alors $n+1 \notin E$, ce qui impose $n+1 > x$.
   - On a bien $n \le x < n+1$. L'unicité est immédiate par l'écart de 1 entre deux entiers distincts.

## 4. Exercices d'Application
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Application Directe (Calcul de borne sup)
**Énoncé :** Soit $A = \{ 1 - \frac{1}{n} \mid n \in \mathbb{N}^* \}$. Déterminer $\sup A$ et $\inf A$.
**Correction Détaillée :**
1. **Infimum :** La suite $(1 - 1/n)$ est croissante. Son premier terme est pour $n=1 : 1-1=0$. Comme la suite croît, $0$ est le plus petit élément. $\inf A = \min A = 0$.
2. **Supremum :** Pour tout $n \ge 1, \frac{1}{n} > 0 \implies 1 - \frac{1}{n} < 1$. Donc $1$ est un majorant.
   - Soit $\epsilon > 0$. Cherchons $n$ tel que $1 - \frac{1}{n} > 1 - \epsilon$.
   - $1 - \frac{1}{n} > 1 - \epsilon \iff \frac{1}{n} < \epsilon \iff n > \frac{1}{\epsilon}$.
   - Par la propriété d'Archimède, un tel entier $n$ existe toujours.
**Conclusion :** $\sup A = 1$. (Note : $1 \notin A$).

### Exercice 2 : Niveau Avancé (Somme de bornes supérieures)
**Énoncé :** Soient $A$ et $B$ deux parties non vides et majorées de $\mathbb{R}$. On note $A+B = \{ a+b \mid a \in A, b \in B \}$. Montrer que $\sup(A+B) = \sup A + \sup B$.
**Correction Détaillée :**
1. **Majorant :** Soit $x \in A+B$. Alors $x = a+b$ avec $a \le \sup A$ and $b \le \sup B$.
   - $x = a+b \le \sup A + \sup B$. Donc $\sup A + \sup B$ est un majorant de $A+B$.
   - Par définition du $\sup$, on a $\sup(A+B) \le \sup A + \sup B$.
2. **Optimalité :** Soit $\epsilon > 0$.
   - Il existe $a \in A$ tel que $a > \sup A - \epsilon/2$.
   - Il existe $b \in B$ tel que $b > \sup B - \epsilon/2$.
   - Alors $a+b \in A+B$ et $a+b > (\sup A + \sup B) - \epsilon$.
   - Cela montre que n'importe quel nombre strictement plus petit que $\sup A + \sup B$ n'est pas un majorant de $A+B$.
**Conclusion :** Par caractérisation, $\sup(A+B) = \sup A + \sup B$.

## 5. Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
- **Le Pont Théorique :** Les algorithmes d'optimisation (comme la descente de gradient) reposent sur l'existence de bornes inférieures (le minimum de la fonction de perte). Sans la structure complète de $\mathbb{R}$, on ne pourrait jamais garantir qu'une suite de poids "converge" vers un nombre réel précis.
- **Exemple Concret :** En **Deep Learning**, lors de la **Normalisation (Batch Norm / Layer Norm)**, on manipule des statistiques (moyenne, variance) qui sont des nombres réels. La stabilité numérique des calculs en virgule flottante (Float32/Float16) est une approximation informatique de la structure de $\mathbb{R}$. Comprendre que $\mathbb{R}$ n'a pas de "trous" permet de justifier l'utilisation du calcul différentiel pour ajuster les neurones de manière continue.

## 6. Liens Sémantiques
- **Concepts Précédents requis :** [[Jalon 3 (Quantification)]], [[Jalon 6 (Relations d'équivalence)]]
- **Concepts Futurs dépendants :** [[Jalon 14 (Suites réelles et complexes)]], [[Jalon 18 (Continuité des fonctions d'une variable réelle)]], [[Jalon 34 (Topologie élémentaire des espaces vectoriels normés)]]

---
uuid: "jalon-20"
title: "Dérivées successives, formules de Taylor-Lagrange, Taylor-Young et développements limités"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/approximation-locale
prev: "[[Jalon 19 (Dérivabilité).md]]"
next: "[[Jalon 21 (Suites de fonctions).md]]"
---

# Jalon 20 : Dérivées successives, formules de Taylor-Lagrange, Taylor-Young et développements limités

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Imaginez que vous vouliez copier un tableau célèbre (comme la Joconde). 
  - La **Dérivée première**, c'est copier la couleur globale. 
  - La **Dérivée seconde**, c'est copier les ombres et les reliefs. 
  - Les **Dérivées suivantes**, c'est copier les micro-détails, les craquelures, la texture de la toile. 
  Plus vous avez de détails (de dérivées), plus votre copie ressemble à l'original. Les **Formules de Taylor**, c'est la recette qui vous dit : "Pour ressembler parfaitement à l'original près de ce point, mélangez $x$ doses de couleur, $y$ doses d'ombre, $z$ doses de texture...". Un **Développement Limité**, c'est une "copie simplifiée" qui est parfaite si on regarde de très près, mais qui devient floue si on s'éloigne.
- **Le "Pourquoi on a inventé ça" :** Les fonctions compliquées (comme $\sin(x)$ ou $e^x$) sont difficiles à calculer à la main ou par un ordinateur simple. Taylor a découvert qu'on peut remplacer n'importe quelle fonction lisse par un **polynôme** (une simple somme de puissances), beaucoup plus facile à manipuler.
- **Visualisation :** Imaginez une courbe complexe. Taylor-Young nous donne une parabole, puis une courbe de degré 3, 4... qui "épouse" la forme de la courbe originale de plus en plus loin autour du point de contact.

## 2. Formalisation
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soit $I$ un intervalle ouvert et $f : I \to \mathbb{R}$.
1. **Dérivées successives :** On définit par récurrence $f^{(0)} = f$ et $f^{(n+1)} = (f^{(n)})'$.
2. **Classe $C^n$ :** $f$ est de classe $C^n$ si elle est $n$ fois dérivable et si $f^{(n)}$ est continue.
3. **Polynôme de Taylor :** Le polynôme de Taylor de $f$ à l'ordre $n$ en $a$ est :
   $$P_{n,a}(x) = \sum_{k=0}^n \frac{f^{(k)}(a)}{k!} (x-a)^k$$

### B. Théorèmes, Propositions & Lemmes
> **Formule de Taylor-Young (Approximation locale) :**
> Si $f$ est de classe $C^n$ au voisinage de $a$, alors :
> $$f(x) = P_{n,a}(x) + o((x-a)^n) \quad \text{quand } x \to a$$

> **Formule de Taylor-Lagrange (Approximation globale) :**
> Si $f$ est de classe $C^{n+1}$ sur $[a, b]$, il existe $c \in ]a, b[$ tel que :
> $$f(b) = P_{n,a}(b) + \frac{f^{(n+1)}(c)}{(n+1)!} (b-a)^{n+1}$$

> **Développement Limité (DL) :** $f$ admet un DL à l'ordre $n$ en $a$ s'il existe des réels $a_0, ..., a_n$ tels que $f(x) = \sum_{k=0}^n a_k(x-a)^k + o((x-a)^n)$.

## 3. Démonstrations
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : Formule de Taylor-Lagrange à l'ordre 1 (TAF généralisé)
Montrons que $f(b) = f(a) + f'(a)(b-a) + \frac{f''(c)}{2}(b-a)^2$.

1. **Initialisation / Cadre :** Soit $f$ de classe $C^2$ sur $[a, b]$.
   Considérons la fonction auxiliaire $\phi(t)$ définie sur $[a, b]$ par :
   $$\phi(t) = f(b) - \left( f(t) + (b-t)f'(t) + K \frac{(b-t)^2}{2} \right)$$
   où $K$ est une constante choisie telle que $\phi(a) = 0$.

2. **Étape 1 : Détermination de $K$**
   $\phi(a) = 0 \implies f(b) - f(a) - (b-a)f'(a) - K \frac{(b-a)^2}{2} = 0$.
   $$K = \frac{f(b) - f(a) - (b-a)f'(a)}{\frac{(b-a)^2}{2}}$$

3. **Étape 2 : Application du théorème de Rolle à $\phi$**
   - $\phi$ est continue sur $[a, b]$ et dérivable sur $]a, b[$.
   - $\phi(b) = f(b) - (f(b) + 0 + 0) = 0$.
   - $\phi(a) = 0$ par construction.
   D'après le théorème de Rolle, il existe $c \in ]a, b[$ tel que $\phi'(c) = 0$.

4. **Étape 3 : Calcul de la dérivée $\phi'(t)$**
   Dérivons $\phi(t) = f(b) - f(t) - (b-t)f'(t) - K \frac{(b-t)^2}{2}$ :
   $\phi'(t) = 0 - f'(t) - [ -f'(t) + (b-t)f''(t) ] - K \frac{2(b-t)(-1)}{2}$
   $\phi'(t) = -f'(t) + f'(t) - (b-t)f''(t) + K(b-t)$
   $\phi'(t) = (b-t) [ K - f''(t) ]$.

5. **Étape 4 : Conclusion en $c$**
   Comme $\phi'(c) = 0$ et $c < b$ (donc $b-c \neq 0$), on a :
   $K - f''(c) = 0 \implies K = f''(c)$.

6. **Étape 5 : Réassemblage final**
   Remplaçons $K$ dans l'expression de $\phi(a) = 0$ :
   $f(b) = f(a) + (b-a)f'(a) + f''(c) \frac{(b-a)^2}{2}$.
   Le théorème est démontré.

## 4. Exercices d'Application
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Calcul de DL (Composition)
**Énoncé :** Calculer le DL à l'ordre 3 en 0 de $f(x) = e^{\sin(x)}$.
**Correction Détaillée :**
1. DL de $\sin(x)$ en 0 à l'ordre 3 : $\sin(x) = x - \frac{x^3}{6} + o(x^3)$.
2. Posons $u = \sin(x)$. Quand $x \to 0, u \to 0$.
3. DL de $e^u$ en 0 à l'ordre 3 : $e^u = 1 + u + \frac{u^2}{2} + \frac{u^3}{6} + o(u^3)$.
4. Substituons $u$ :
   $f(x) = 1 + (x - \frac{x^3}{6}) + \frac{(x - \frac{x^3}{6})^2}{2} + \frac{(x - \frac{x^3}{6})^3}{6} + o(x^3)$.
5. Développons les puissances en ne gardant que les termes de degré $\le 3$ :
   - $(x - \frac{x^3}{6})^2 = x^2 - 2 \frac{x^4}{6} + ... = x^2 + o(x^3)$.
   - $(x - \frac{x^3}{6})^3 = x^3 + o(x^3)$.
6. Sommons :
   $f(x) = 1 + x - \frac{x^3}{6} + \frac{x^2}{2} + \frac{x^3}{6} + o(x^3)$.
   $f(x) = 1 + x + \frac{x^2}{2} + 0x^3 + o(x^3)$.
**Conclusion :** $e^{\sin(x)} = 1 + x + \frac{x^2}{2} + o(x^3)$.

### Exercice 2 : Niveau Avancé (Étude d'extremum)
**Énoncé :** Soit $f$ de classe $C^2$. Montrer que si $f'(a) = 0$ et $f''(a) > 0$, alors $f$ admet un minimum local en $a$.
**Correction Détaillée :**
1. Appliquons la formule de Taylor-Young à l'ordre 2 en $a$ :
   $f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2}(x-a)^2 + o((x-a)^2)$.
2. Comme $f'(a) = 0$, on a $f(x) - f(a) = \frac{f''(a)}{2}(x-a)^2 + (x-a)^2 \epsilon(x)$ avec $\lim_{x \to a} \epsilon(x) = 0$.
3. Factorisons : $f(x) - f(a) = (x-a)^2 \left[ \frac{f''(a)}{2} + \epsilon(x) \right]$.
4. Comme $f''(a) > 0$, alors $\frac{f''(a)}{2} > 0$.
5. Par définition de la limite, il existe un intervalle autour de $a$ tel que $|\epsilon(x)| < \frac{f''(a)}{4}$.
6. Dans cet intervalle, le terme entre crochets est strictement positif (car $\frac{f''(a)}{2} - \frac{f''(a)}{4} = \frac{f''(a)}{4} > 0$).
7. Comme $(x-a)^2 \ge 0$, alors $f(x) - f(a) \ge 0$ pour tout $x$ proche de $a$.
**Conclusion :** $f(a)$ est un minimum local.

## 5. Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
- **Le Pont Théorique :** En IA, la formule de Taylor à l'ordre 2 est le fondement des **Méthodes de Second Ordre** (comme la méthode de Newton ou L-BFGS).
- **Exemple Concret :** Pour optimiser une fonction de perte $L(W)$, on utilise souvent la **Matrice Hessienne** (les dérivées secondes). La formule de Taylor nous dit :
  $$L(W + \Delta W) \approx L(W) + \nabla L^T \Delta W + \frac{1}{2} \Delta W^T H \Delta W$$
  Si on veut que l'erreur diminue le plus vite possible, on ne regarde pas juste la pente ($\nabla L$), mais aussi la courbure ($H$). C'est ce qui permet aux algorithmes de type **Adam** ou **RMSProp** d'ajuster dynamiquement le pas d'apprentissage : ils utilisent une approximation de cette courbure pour savoir s'ils sont dans un virage serré ou sur une longue ligne droite.

## 6. Liens Sémantiques
- **Concepts Précédents requis :** [[Jalon 19 (Dérivabilité)]]
- **Concepts Futurs dépendants :** [[Jalon 23 (Séries entières)]], [[Jalon 47 (Dérivées partielles d'ordre deux)]], [[Jalon 122 (Notion de sous-gradient)]], [[Jalon 131 (Algorithmes d'optimisation de second ordre en grande dimension)]]

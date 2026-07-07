---
uuid: "jalon-21"
title: "Suites de fonctions, étude de la convergence simple et de la convergence uniforme"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/convergence-algorithmique
prev: "[[Jalon-20.md]]"
next: "[[Jalon 22 (Séries de fonctions).md]]"
---

# Jalon 21 : Suites de fonctions, étude de la convergence simple et de la convergence uniforme

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Imaginez que vous regardiez un dessin animé. Chaque image du film est une fonction. 
  - La **Convergence Simple**, c'est comme si vous fixiez un seul pixel de l'écran. Si, au fil du film, la couleur de ce pixel finit par se stabiliser, on dit qu'il y a convergence simple en ce point. Mais attention : un pixel peut se stabiliser très vite alors qu'un autre pixel à côté continue de changer pendant des heures !
  - La **Convergence Uniforme**, c'est le cas idéal : c'est quand l'image *entière* se stabilise d'un coup, partout en même temps, à la même vitesse. C'est la garantie que si chaque image du film est nette, l'image finale sera nette aussi. Sans convergence uniforme, l'image finale pourrait être toute floue ou cassée, même si chaque image intermédiaire était parfaite.
- **Le "Pourquoi on a inventé ça" :** Les mathématiciens ont découvert avec horreur que si on additionne une infinité de fonctions continues, le résultat peut être une fonction discontinue ! La convergence uniforme est le "garde-fou" qui permet de transférer les propriétés (continuité, dérivabilité) des fonctions d'une suite vers leur limite.
- **Visualisation :** Imaginez un tuyau de plus en plus fin autour de la courbe limite. La convergence est uniforme si, après un certain temps, TOUTE la courbe de votre fonction rentre entièrement dans le tuyau.

## 2. Formalisation
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soit $D \subset \mathbb{R}$ et $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions de $D$ dans $\mathbb{R}$ (ou $\mathbb{C}$).
1. **Convergence Simple (CS) :** La suite $(f_n)$ converge simplement vers $f$ sur $D$ si :
   $$\forall x \in D, \lim_{n \to \infty} f_n(x) = f(x)$$
   $$\forall x \in D, \forall \epsilon > 0, \exists N_{x,\epsilon} \in \mathbb{N}, \forall n \ge N_{x,\epsilon}, |f_n(x) - f(x)| < \epsilon$$
2. **Convergence Uniforme (CU) :** La suite $(f_n)$ converge uniformément vers $f$ sur $D$ si :
   $$\lim_{n \to \infty} \left( \sup_{x \in D} |f_n(x) - f(x)| \right) = 0$$
   $$\forall \epsilon > 0, \exists N_\epsilon \in \mathbb{N}, \forall n \ge N_\epsilon, \forall x \in D, |f_n(x) - f(x)| < \epsilon$$
   (Note : $N$ ne dépend plus de $x$).

### B. Théorèmes, Propositions & Lemmes
> **Théorème de Continuité (Double Limite) :**
> Si $(f_n)$ est une suite de fonctions continues sur $D$ et si $(f_n)$ converge **uniformément** vers $f$ sur $D$, alors $f$ est continue sur $D$.

> **Théorème d'Interversion Limite-Intégrale :**
> Si $(f_n)$ converge uniformément vers $f$ sur $[a, b]$, alors :
> $$\lim_{n \to \infty} \int_a^b f_n(t)dt = \int_a^b (\lim_{n \to \infty} f_n(t))dt = \int_a^b f(t)dt$$

> **Théorème de Dérivation :**
> Si $(f_n)$ est de classe $C^1$, si $(f_n(x_0))$ converge pour au moins un $x_0$, et si $(f'_n)$ converge **uniformément** vers $g$, alors $(f_n)$ converge uniformément vers $f$ et $f' = g$.

## 3. Démonstrations
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : La limite uniforme de fonctions continues est continue
Soit $(f_n)$ convergeant uniformément vers $f$ sur $D$. On suppose chaque $f_n$ continue en $x_0 \in D$. Montrons que $f$ est continue en $x_0$.

1. **Initialisation / Cadre :** Soit $\epsilon > 0$.
   Nous voulons montrer qu'il existe $\delta > 0$ tel que pour $|x - x_0| < \delta$, $|f(x) - f(x_0)| < \epsilon$.
   Utilisons l'astuce de la "décomposition en trois" (introduction des $f_n$) :
   $$|f(x) - f(x_0)| = |f(x) - f_n(x) + f_n(x) - f_n(x_0) + f_n(x_0) - f(x_0)|$$

2. **Étape 1 : Choix de $n$ par la Convergence Uniforme**
   Par convergence uniforme, il existe un rang $N$ tel que pour tout $n \ge N$ et pour TOUT $x \in D$ :
   $$|f_n(x) - f(x)| < \frac{\epsilon}{3}$$
   Fixons un tel entier $n \ge N$. Cette majoration est donc valable pour $x$ et pour $x_0$ :
   - $|f_n(x) - f(x)| < \epsilon/3$ (Partie 1)
   - $|f_n(x_0) - f(x_0)| < \epsilon/3$ (Partie 3)

3. **Étape 2 : Choix de $\delta$ par la continuité de $f_n$**
   L'entier $n$ étant fixé, la fonction $f_n$ est continue en $x_0$.
   Par définition de la continuité de $f_n$, il existe $\delta > 0$ tel que :
   $$\forall x \in D, |x - x_0| < \delta \implies |f_n(x) - f_n(x_0)| < \frac{\epsilon}{3} \quad \text{(Partie 2)}$$

4. **Étape 3 : Sommation des majorations**
   En utilisant l'inégalité triangulaire $|a+b+c| \le |a| + |b| + |c|$ :
   $|f(x) - f(x_0)| \le |f(x) - f_n(x)| + |f_n(x) - f_n(x_0)| + |f_n(x_0) - f(x_0)|$.
   Pour $|x - x_0| < \delta$, on a :
   $|f(x) - f(x_0)| < \frac{\epsilon}{3} + \frac{\epsilon}{3} + \frac{\epsilon}{3} = \epsilon$.

5. **Conclusion :**
   Nous avons trouvé un $\delta$ tel que $|f(x) - f(x_0)| < \epsilon$. La fonction limite $f$ est donc continue en $x_0$.

## 4. Exercices d'Application
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : CS mais pas CU (Contre-exemple classique)
**Énoncé :** Soit $f_n(x) = x^n$ sur $D = [0, 1]$. Étudier la convergence de la suite.
**Correction Détaillée :**
1. **Convergence Simple :**
   - Si $x \in [0, 1[$, $\lim_{n \to \infty} x^n = 0$.
   - Si $x = 1$, $\lim_{n \to \infty} 1^n = 1$.
   - La fonction limite est $f(x) = 0$ si $x < 1$ et $f(1) = 1$.
2. **Convergence Uniforme ?**
   - Les fonctions $f_n$ sont toutes continues sur $[0, 1]$.
   - La fonction limite $f$ est discontinue en 1.
   - Si la convergence était uniforme, la limite $f$ devrait être continue (théorème précédent).
**Conclusion :** La convergence n'est pas uniforme sur $[0, 1]$. (Elle l'est par contre sur tout segment $[0, a]$ avec $a < 1$).

### Exercice 2 : Niveau Avancé (Convergence vers l'exponentielle)
**Énoncé :** Démontrer que la suite $f_n(x) = (1 + \frac{x}{n})^n$ converge uniformément vers $e^x$ sur tout segment $[a, b]$.
**Correction Détaillée :**
1. **Convergence Simple :** $\ln(f_n(x)) = n \ln(1 + x/n) = n (x/n - x^2/(2n^2) + o(1/n^2)) = x - x^2/(2n) + o(1/n)$.
   - $\lim_{n \to \infty} \ln(f_n(x)) = x \implies \lim f_n(x) = e^x$.
2. **Convergence Uniforme :** Étudions l'écart $E_n(x) = |e^x - (1+x/n)^n|$.
   - Sur $[a, b]$, on utilise l'inégalité $0 \le e^u - (1+u/n)^n \le \frac{u^2 e^u}{2n}$ (prouvable par étude de fonction).
   - $\sup_{x \in [a, b]} E_n(x) \le \frac{M^2 e^M}{2n}$ où $M = \max(|a|, |b|)$.
   - Comme $\frac{M^2 e^M}{2n} \to 0$ quand $n \to \infty$, le supremum de l'écart tend vers 0.
**Conclusion :** La convergence est uniforme sur tout compact de $\mathbb{R}$.

## 5. Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
- **Le Pont Théorique :** En IA, la convergence uniforme est la condition sine qua non de la **Généralisation**. On veut que l'erreur mesurée sur les données d'entraînement (une fonction de $n$ exemples) converge uniformément vers l'erreur réelle sur toutes les données possibles.
- **Exemple Concret :** Dans la **Théorie de l'Apprentissage Statistique (Vapnik-Chervonenkis)**, on définit des classes de fonctions (ex: tous les réseaux de neurones d'une certaine architecture). On prouve que pour que l'apprentissage soit fiable, la convergence de l'erreur doit être uniforme sur toute la classe de fonctions. C'est ce qu'on appelle une **Borne de Généralisation Uniforme**. Si la convergence n'était que simple, il existerait toujours une fonction du réseau qui "triche" sur les données d'entraînement sans être bonne en réalité (Overfitting).

## 6. Liens Sémantiques
- **Concepts Précédents requis :** [[Jalon 14 (Suites réelles et complexes)]], [[Jalon 18 (Continuité des fonctions d'une variable réelle)]]
- **Concepts Futurs dépendants :** [[Jalon 22 (Séries de fonctions)]], [[Jalon 59 (Topologie des espaces de fonctions)]], [[Jalon 137 (Preuve des bornes de generalisation universelles de Vapnik via la dimension VC)]]

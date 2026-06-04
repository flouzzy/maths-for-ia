---
uuid: "jalon-18"
title: "Continuité des fonctions d'une variable réelle, théorème des valeurs intermédiaires et compacité locale"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/surfaces-decision
prev: "[[Jalon 17 (Séries absolument convergentes).md]]"
next: "[[Jalon 19 (Dérivabilité).md]]"
---

# Jalon 18 : Continuité des fonctions d'une variable réelle, théorème des valeurs intermédiaires et compacité locale

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Imaginez que vous dessiniez une courbe avec un crayon sur une feuille de papier. La **Continuité**, c'est simplement la règle d'or : vous n'avez pas le droit de lever le crayon. Si vous devez passer de la gauche à la droite de la feuille, votre trait doit être ininterrompu. Le **Théorème des Valeurs Intermédiaires (TVI)**, c'est comme dire que si vous commencez à dessiner en bas de la feuille et que vous finissez en haut, votre crayon a forcément dû traverser la ligne du milieu à un moment donné. Vous ne pouvez pas vous téléporter !
- **Le "Pourquoi on a inventé ça" :** Dans la nature, peu de choses changent instantanément. La température, la position d'une voiture, ou la croissance d'une plante sont des phénomènes continus. Les mathématiciens ont eu besoin de définir cette notion pour garantir que si on cherche une solution (un point où une fonction vaut zéro), elle existe vraiment.
- **Visualisation :** Imaginez un élastique tendu. Si vous tirez sur un point, les points voisins suivent le mouvement. C'est la continuité : des causes proches produisent des effets proches.

## 2. Formalisation & Rigueur Académique
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soit $I$ un intervalle de $\mathbb{R}$ et $f : I \to \mathbb{R}$.
1. **Continuité en un point $x_0 \in I$ :** $f$ est continue en $x_0$ si :
   $$\forall \epsilon > 0, \exists \delta > 0, \forall x \in I, |x - x_0| < \delta \Rightarrow |f(x) - f(x_0)| < \epsilon$$
2. **Continuité sur un intervalle :** $f$ est continue sur $I$ si elle est continue en tout point $x_0 \in I$.
3. **Continuité Uniforme :** $f$ est uniformément continue sur $I$ si :
   $$\forall \epsilon > 0, \exists \delta > 0, \forall (x, y) \in I^2, |x - y| < \delta \Rightarrow |f(x) - f(y)| < \epsilon$$
   (Ici, $\delta$ ne dépend que de $\epsilon$, pas du point choisi).

### B. Théorèmes, Propositions & Lemmes
> **Théorème des Valeurs Intermédiaires (TVI) :**
> Soit $f$ continue sur un intervalle $[a, b]$. Pour tout réel $y$ compris entre $f(a)$ et $f(b)$, il existe au moins un réel $c \in [a, b]$ tel que $f(c) = y$.

> **Théorème de Heine :**
> Toute fonction continue sur un segment $[a, b]$ (fermé borné) est uniformément continue sur ce segment.

> **Théorème des Bornes Atteintes (Weierstrass) :**
> L'image d'un segment $[a, b]$ par une fonction continue $f$ est un segment $[m, M]$. La fonction est bornée et atteint ses bornes.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : Théorème des Valeurs Intermédiaires (par dichotomie)
Soit $f : [a, b] \to \mathbb{R}$ continue telle que $f(a) < 0 < f(b)$. Montrons qu'il existe $c \in [a, b]$ tel que $f(c) = 0$.

1. **Initialisation / Cadre :** 
   - Posons $a_0 = a$ et $b_0 = b$.
   - Nous allons construire deux suites $(a_n)$ et $(b_n)$ par récurrence.

2. **Étape 1 : Construction des suites**
   Supposons $a_n$ et $b_n$ définis tels que $f(a_n) \le 0$ et $f(b_n) \ge 0$.
   - Soit $m_n = \frac{a_n + b_n}{2}$ le milieu du segment $[a_n, b_n]$.
   - Si $f(m_n) = 0$, alors $c = m_n$ et la preuve est finie.
   - Si $f(m_n) < 0$, on pose $a_{n+1} = m_n$ et $b_{n+1} = b_n$. On a bien $f(a_{n+1}) < 0$ et $f(b_{n+1}) \ge 0$.
   - Si $f(m_n) > 0$, on pose $a_{n+1} = a_n$ et $b_{n+1} = m_n$. On a bien $f(a_{n+1}) \le 0$ et $f(b_{n+1}) > 0$.

3. **Étape 2 : Convergence des suites**
   - La suite $(a_n)$ est croissante et $(b_n)$ est décroissante.
   - Leur différence est $b_n - a_n = \frac{b-a}{2^n}$, qui tend vers 0.
   - D'après le théorème des suites adjacentes, les deux suites convergent vers une limite commune $c \in [a, b]$.

4. **Étape 3 : Utilisation de la continuité**
   - Puisque $f$ est continue en $c$, alors $\lim_{n \to \infty} f(a_n) = f(c)$ et $\lim_{n \to \infty} f(b_n) = f(c)$.
   - Or, pour tout $n$, $f(a_n) \le 0$. Par passage à la limite dans les inégalités larges, on a $f(c) \le 0$.
   - De même, pour tout $n$, $f(b_n) \ge 0$. Par passage à la limite, on a $f(c) \ge 0$.

5. **Conclusion :**
   - $f(c) \le 0$ et $f(c) \ge 0 \implies f(c) = 0$.
   - Le point $c$ existe bien. Le théorème est démontré.

## 4. Exercices d'Application & Pratique de Concours
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Point Fixe (Application du TVI)
**Énoncé :** Soit $f : [0, 1] \to [0, 1]$ une fonction continue. Démontrer qu'il existe $c \in [0, 1]$ tel que $f(c) = c$.
**Correction Détaillée :**
1. Considérons la fonction auxiliaire $g(x) = f(x) - x$.
2. Puisque $f$ est continue sur $[0, 1]$ et que $x \mapsto x$ est continue, alors $g$ est continue sur $[0, 1]$.
3. Calculons les valeurs aux bornes :
   - $g(0) = f(0) - 0 = f(0)$. Comme $f([0, 1]) \subset [0, 1]$, alors $f(0) \ge 0$. Donc $g(0) \ge 0$.
   - $g(1) = f(1) - 1$. Comme $f(1) \le 1$, alors $f(1) - 1 \le 0$. Donc $g(1) \le 0$.
4. Si $g(0)=0$ ou $g(1)=0$, le point fixe est 0 ou 1.
5. Sinon, $g(1) < 0 < g(0)$. D'après le TVI, il existe $c \in ]0, 1[$ tel que $g(c) = 0$.
6. $g(c) = 0 \iff f(c) - c = 0 \iff f(c) = c$.
**Conclusion :** Toute fonction continue d'un segment dans lui-même admet au moins un point fixe.

### Exercice 2 : Niveau Avancé (Continuité Uniforme)
**Énoncé :** Démontrer que la fonction $f(x) = \sqrt{x}$ est uniformément continue sur $[0, +\infty[$.
**Correction Détaillée :**
1. Sur $[0, 1]$ : $f$ est continue sur un segment fermé borné. D'après le théorème de Heine, $f$ est uniformément continue sur $[0, 1]$.
2. Sur $[1, +\infty[$ : Étudions $|f(x) - f(y)| = |\sqrt{x} - \sqrt{y}|$.
   - On a $|\sqrt{x} - \sqrt{y}| = \frac{|x-y|}{\sqrt{x} + \sqrt{y}}$.
   - Comme $x \ge 1$ and $y \ge 1$, alors $\sqrt{x} + \sqrt{y} \ge 2$.
   - Donc $|\sqrt{x} - \sqrt{y}| \le \frac{1}{2} |x-y|$.
   - La fonction est Lipschitzienne de rapport 1/2 sur $[1, +\infty[$, ce qui implique l'uniforme continuité.
3. Recollement : $f$ étant uniformément continue sur deux intervalles dont l'intersection n'est pas vide et qui recouvrent $[0, +\infty[$, elle l'est sur l'union.
**Conclusion :** $f(x) = \sqrt{x}$ est bien uniformément continue.

## 5. Ancrage & Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
- **Le Pont Théorique :** En IA, la continuité garantit que de petites modifications des données d'entrée (images, texte) n'entraînent pas de changements brutaux et imprévisibles dans la prédiction. C'est la base de la **Robustesse**.
- **Exemple Concret :** Dans la génération d'images par **GAN (Generative Adversarial Networks)** ou **Auto-encodeurs**, on manipule un "Espace Latent". On veut que cet espace soit continu : si on se déplace doucement entre le vecteur d'un "Chien" et celui d'un "Chat", le décodeur doit générer une suite d'images qui se transforment graduellement de l'un à l'autre sans sauter. Si la fonction apprise par le réseau n'était pas continue, le modèle "hallucinerait" des images incohérentes au moindre petit changement de paramètre.

## 6. Liens Sémantiques & Maillage Obsidian
- **Concepts Précédents requis :** [[Jalon 13 (Structure de R)]], [[Jalon 14 (Suites réelles et complexes)]]
- **Concepts Futurs dépendants :** [[Jalon 19 (Dérivabilité)]], [[Jalon 44 (Fonctions de plusieurs variables)]], [[Jalon 52 (Applications continues entre espaces topologiques et définition fine des homéomorphismes.)]]

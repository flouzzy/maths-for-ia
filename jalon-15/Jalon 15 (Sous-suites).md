---
uuid: "jalon-15"
title: "Sous-suites, valeurs d'adhérence et preuve par séparation du théorème de Bolzano-Weierstrass"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/compacite
prev: "[[Jalon-14.md]]"
next: "[[Jalon-16.md]]"
---
# Jalon 15 : Sous-suites, valeurs d'adhérence et preuve par séparation du théorème de Bolzano-Weierstrass

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Imaginez que vous observez une foule qui marche dans une rue. Si vous ne regardez que certaines personnes (par exemple, seulement celles qui portent un chapeau rouge), vous observez une **sous-suite**. Même si la foule entière semble aller dans tous les sens sans direction précise, il se peut que le groupe des "chapeaux rouges" finisse par se regrouper tous devant une boulangerie. Le **théorème de Bolzano-Weierstrass**, c'est la garantie que si une foule est coincée dans une rue fermée (un espace borné), il y aura forcément au moins un petit groupe (une sous-suite) qui finira par s'agglutiner quelque part (converger).
- **Le "Pourquoi on a inventé ça" :** Parfois, une suite est trop chaotique pour converger (pensez à $(-1)^n$). Mais elle contient souvent des morceaux plus sages qui, eux, se stabilisent. C'est essentiel pour trouver des solutions optimales dans des problèmes complexes : on ne trouve pas la solution parfaite d'un coup, mais on s'en rapproche par morceaux.
- **Visualisation :** Imaginez un élastique que vous tendez entre vos mains. Si vous lâchez des grains de sable sur l'élastique, peu importe comment vous les jetez, comme ils sont coincés sur l'élastique, ils finiront par être proches les uns des autres.

## 2. Formalisation
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soit $(u_n)_{n \in \mathbb{N}}$ une suite d'éléments de $E$ ($\mathbb{R}$ ou $\mathbb{C}$).
1. **Sous-suite (ou suite extraite) :** Une suite $(v_k)_{k \in \mathbb{N}}$ est une sous-suite de $(u_n)$ s'il existe une application $\phi : \mathbb{N} \to \mathbb{N}$ **strictement croissante** telle que $\forall k \in \mathbb{N}, v_k = u_{\phi(k)}$.
2. **Valeur d'adhérence :** Un élément $a \in E$ est une valeur d'adhérence de $(u_n)$ s'il existe une sous-suite de $(u_n)$ qui converge vers $a$.
3. **Caractérisation topologique :** $a$ est valeur d'adhérence $\iff \forall \epsilon > 0, \forall N \in \mathbb{N}, \exists n \ge N, |u_n - a| < \epsilon$. (Il y a une infinité de termes de la suite arbitrairement proches de $a$).

### B. Théorèmes, Propositions & Lemmes
> **Théorème de Bolzano-Weierstrass :**
> De toute suite réelle bornée, on peut extraire une sous-suite convergente.
> (Plus généralement : Toute suite dans un ensemble compact admet au moins une valeur d'adhérence).

> **Lien avec la convergence :**
> Une suite bornée converge si et seulement si elle admet une unique valeur d'adhérence.

## 3. Démonstrations
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : Bolzano-Weierstrass par dichotomie (méthode de séparation)
Soit $(u_n)$ une suite réelle bornée. Montrons qu'il existe une sous-suite convergente.

1. **Initialisation / Cadre :** 
   - Puisque $(u_n)$ est bornée, il existe un intervalle $[a_0, b_0]$ tel que $\forall n \in \mathbb{N}, u_n \in [a_0, b_0]$.
   - Posons $I_0 = [a_0, b_0]$ et $L_0 = b_0 - a_0$.
   - Nous allons construire par récurrence une suite d'intervalles emboîtés $(I_k)_{k \in \mathbb{N}}$.

2. **Étape 1 : Construction par dichotomie**
   Supposons $I_k = [a_k, b_k]$ construit tel qu'il contient une infinité de termes de la suite $(u_n)$.
   - Soit $m_k = \frac{a_k + b_k}{2}$ le milieu de $I_k$.
   - L'intervalle $I_k$ est l'union de $[a_k, m_k]$ et $[m_k, b_k]$.
   - Puisque $I_k$ contient une infinité de termes, l'un au moins de ces deux sous-intervalles contient aussi une infinité de termes.
   - On choisit $I_{k+1} = [a_{k+1}, b_{k+1}]$ comme étant ce sous-intervalle (si les deux conviennent, on en choisit un arbitrairement).

3. **Étape 2 : Propriétés des suites $(a_k)$ et $(b_k)$**
   - Par construction, $a_k \le a_{k+1}$ (croissante) et $b_{k+1} \le b_k$ (décroissante).
   - De plus, $b_k - a_k = \frac{b_0 - a_0}{2^k} \to 0$ quand $k \to \infty$.
   - D'après le théorème des segments emboîtés, les suites $(a_k)$ et $(b_k)$ convergent vers une limite commune $l$.

4. **Étape 3 : Extraction de la sous-suite**
   - On définit $\phi(0) = 0$.
   - Pour chaque $k \ge 0$, on choisit $\phi(k+1)$ comme étant le plus petit entier tel que $\phi(k+1) > \phi(k)$ et $u_{\phi(k+1)} \in I_{k+1}$. Un tel entier existe car $I_{k+1}$ contient une infinité de termes.
   - On a alors, pour tout $k$ : $a_k \le u_{\phi(k)} \le b_k$.

5. **Conclusion :**
   - Par le théorème des gendarmes, comme $\lim a_k = l$ et $\lim b_k = l$, alors $\lim_{k \to \infty} u_{\phi(k)} = l$.
   - Nous avons extrait une sous-suite convergente. Le théorème est démontré.

## 4. Exercices d'Application
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Application Directe (Valeurs d'adhérence)
**Énoncé :** Déterminer les valeurs d'adhérence de la suite $u_n = \sin(n \frac{\pi}{2})$.
**Correction Détaillée :**
1. Étudions les premiers termes :
   - $n=0 \implies \sin(0) = 0$
   - $n=1 \implies \sin(\pi/2) = 1$
   - $n=2 \implies \sin(\pi) = 0$
   - $n=3 \implies \sin(3\pi/2) = -1$
   - $n=4 \implies \sin(2\pi) = 0$ (Cycle de période 4).
2. Définissons des extractions :
   - Pour $n = 2k$ : $u_{2k} = \sin(k\pi) = 0$. La sous-suite $(u_{2k})$ converge vers $0$.
   - Pour $n = 4k+1$ : $u_{4k+1} = \sin(2k\pi + \pi/2) = 1$. La sous-suite $(u_{4k+1})$ converge vers $1$.
   - Pour $n = 4k+3$ : $u_{4k+3} = \sin(2k\pi + 3\pi/2) = -1$. La sous-suite $(u_{4k+3})$ converge vers $-1$.
**Conclusion :** Les valeurs d'adhérence sont $\{ -1, 0, 1 \}$.

### Exercice 2 : Niveau Avancé (Densité)
**Énoncé :** Montrer que l'ensemble des valeurs d'adhérence de la suite $u_n = \cos(n)$ est l'intervalle $[-1, 1]$ tout entier. (Admettre que $\mathbb{Z} + 2\pi\mathbb{Z}$ est dense dans $\mathbb{R}$).
**Correction Détaillée :**
1. Soit $l \in [-1, 1]$. Il existe $\theta \in \mathbb{R}$ tel que $\cos(\theta) = l$.
2. Par densité de $\mathbb{Z} + 2\pi\mathbb{Z}$, pour tout $\epsilon > 0$, il existe $n \in \mathbb{Z}$ et $k \in \mathbb{Z}$ tels que $|n - 2\pi k - \theta| < \epsilon$.
3. Comme la fonction $\cos$ est 1-lipschitzienne ($|\cos(x)-\cos(y)| \le |x-y|$), on a :
   $|\cos(n - 2\pi k) - \cos(\theta)| \le |n - 2\pi k - \theta| < \epsilon$.
4. Or $\cos(n - 2\pi k) = \cos(n)$.
5. Donc $|\cos(n) - l| < \epsilon$. Comme on peut trouver de tels $n$ arbitrairement grands (par la structure de groupe dense), $l$ est une valeur d'adhérence.
**Conclusion :** Chaque point de $[-1, 1]$ est limite d'une sous-suite de $\cos(n)$.

## 5. Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
- **Le Pont Théorique :** Le concept de compacité (Bolzano-Weierstrass) est crucial pour garantir l'**existence d'un optimum**. Si on cherche à minimiser une erreur dans un espace de paramètres borné et fermé, Bolzano-Weierstrass nous assure qu'il y a au moins un point d'accumulation où l'erreur est minimale.
- **Exemple Concret :** Dans l'**Initialisation des Poids** des réseaux de neurones, on veut éviter que les signaux ne s'évaporent (Vanishing Gradient) ou n'explosent (Exploding Gradient). On s'assure que la suite des activations à travers les couches reste dans un ensemble compact. Sans cette garantie, l'algorithme d'apprentissage pourrait "diverger" vers l'infini sans jamais rencontrer de valeur d'adhérence (solution stable), rendant l'entraînement impossible.

## 6. Liens Sémantiques
- **Concepts Précédents requis :** [[Jalon 14 (Suites réelles et complexes)]]
- **Concepts Futurs dépendants :** [[Jalon 35 (Caractérisation séquentielle des ouverts)]], [[Jalon 54 (Compacité générale)]], [[Jalon 129 (Optimisation stochastique)]]

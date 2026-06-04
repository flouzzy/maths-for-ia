---
uuid: "jalon-83"
title: "Dérivation au sens des distributions"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 82 (Introduction à la théorie des distributions de Schwartz).md]]"
next: "[[Jalon 84 (Livrable IA).md]]"
---

# Jalon 83 : Dérivation au sens des distributions

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous deviez mesurer la pente d'un escalier.
    - Pour une rampe lisse (une fonction dérivable), c'est facile : il suffit de poser une règle.
    - Mais pour une marche d'escalier (une fonction avec un saut), la pente semble être "infinie" à l'endroit de la cassure, et nulle partout ailleurs. La règle classique ne marche pas.
    - La **Dérivation au sens des distributions**, c'est l'astuce ultime : au lieu de regarder la pente de l'escalier lui-même, on regarde comment l'escalier fait bouger un tapis souple que l'on pose dessus (la fonction test). En mesurant les tensions du tapis, on peut définir une "pente généralisée". Le saut de l'escalier devient un "pic de tension" (un Dirac).
- **Le "Pourquoi on a inventé ça" :** En physique, on a besoin de dériver des signaux qui sautent brusquement (interrupteur ON/OFF). En mathématiques, on veut que TOUT soit dérivable. Avec les distributions, même une fonction discontinue ou une poussière de points (un Dirac) possède une dérivée. Cela permet de résoudre des équations différentielles qui n'avaient pas de solutions auparavant.
- **Visualisation :** La dérivée d'un virage serré est un pic de force. Plus le virage est brusque, plus le pic est haut. À la limite, pour un angle droit, la dérivée est une impulsion infinie.

## 2. Formalisation & Rigueur Académique

### A. Définition de la dérivée d'une distribution

Soit $T \in \mathcal{D}'(\mathbb{R})$ une distribution.

> **Définition (Dérivée distributionnelle) :**
> On appelle **dérivée de T**, notée $T'$, la distribution définie par :
> $$\forall \phi \in \mathcal{D}(\mathbb{R}), \quad \langle T', \phi \rangle = -\langle T, \phi' \rangle$$
> *Généralisation :* Pour la $k$-ième dérivée : $\langle T^{(k)}, \phi \rangle = (-1)^k \langle T, \phi^{(k)} \rangle$.

### B. Formule des Sauts

Soit $f$ une fonction de classe $\mathcal{C}^1$ par morceaux, présentant un saut de hauteur $\sigma$ au point $a$. Soit $\{f'\}$ sa dérivée classique (là où elle existe).

> **Théorème (Formule des sauts) :**
> La dérivée de $f$ au sens des distributions est :
> $$T_f' = T_{\{f'\}} + \sigma \delta_a$$
> La dérivée contient une partie "normale" et une partie "impulsionnelle" due au saut.

### C. Espaces de Sobolev (Introduction)

> **Définition (Espace $H^1$) :**
> L'espace de Sobolev $H^1(\mathbb{R})$ est l'ensemble des fonctions $f \in L^2(\mathbb{R})$ dont la dérivée au sens des distributions $f'$ appartient aussi à $L^2(\mathbb{R})$. Ce sont des fonctions "globalement lisses" même si elles ont des pointes.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : La dérivée de Heaviside est le Dirac

Soit $H(x) = \mathbf{1}_{x>0}$. Montrons que $H' = \delta_0$.

1. **Cadre :** Soit $\phi \in \mathcal{D}(\mathbb{R})$ une fonction test.
2. **Définition de la dérivée :**
   $\langle H', \phi \rangle = -\langle H, \phi' \rangle = - \int_{-\infty}^{+\infty} H(x) \phi'(x) dx$.
3. **Calcul de l'intégrale :**
   Comme $H(x)=0$ pour $x < 0$ et $H(x)=1$ pour $x > 0$ :
   $\langle H', \phi \rangle = - \int_0^{+\infty} \phi'(x) dx$.
4. **Théorème fondamental de l'analyse :**
   $\langle H', \phi \rangle = - [ \phi(x) ]_0^{+\infty}$.
5. **Utilisation du support compact :** Comme $\phi$ est nulle en $+\infty$ :
   $\langle H', \phi \rangle = - (0 - \phi(0)) = \phi(0)$.
6. **Conclusion :**
   On a $\langle H', \phi \rangle = \phi(0) = \langle \delta_0, \phi \rangle$.
   Donc $H' = \delta_0$.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Dérivée de la valeur absolue
**Énoncé :** Calculer la dérivée de $f(x) = |x|$ au sens des distributions.
**Correction Détaillée :**
1. $f(x) = x$ pour $x>0$ et $-x$ pour $x<0$.
2. Dérivée classique $\{f'\}$ : elle vaut $1$ pour $x>0$ et $-1$ pour $x<0$. C'est la fonction signe, $\text{sgn}(x)$.
3. Saut : La fonction est continue en 0 ($f(0^-)=0, f(0^+)=0$), donc le saut $\sigma = 0$.
4. **Résultat :** $|x|' = \text{sgn}(x)$.

### Exercice 2 : Niveau Avancé (Seconde dérivée)
**Énoncé :** Calculer la dérivée seconde de $|x|$.
**Correction Détaillée :**
1. On doit dériver $\text{sgn}(x)$.
2. $\text{sgn}(x)$ est une fonction constante par morceaux avec un saut de hauteur $2$ en $x=0$ (elle passe de -1 à 1).
3. Sa dérivée classique est nulle partout (sauf en 0).
4. Par la formule des sauts : $\text{sgn}' = 0 + 2\delta_0 = 2\delta_0$.
**Conclusion :** $|x|'' = 2\delta_0$. La "pointe" de la valeur absolue génère une impulsion de Dirac dans la dérivée seconde.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Les fonctions d'activation non-lisses (ReLU, Leaky ReLU) sont les briques de base de l'IA. La théorie des distributions justifie mathématiquement que l'on puisse calculer leur gradient.
- **Example Concret :**
    - **Gradient de ReLU :** Pour $\text{ReLU}(x) = \max(0, x)$, sa dérivée est la fonction de Heaviside $H(x)$. En informatique, on décide arbitrairement que $H(0)=0$ ou $1$. La théorie des distributions nous dit que peu importe la valeur en un point isolé, car la "masse" de la dérivée est bien capturée par $H$.
    - **Edge Detection (Détection de contours) :** En vision par ordinateur, un contour est un "saut" de luminosité. Dériver une image (filtre de Sobel) fait apparaître des pics là où il y a des contours. C'est l'application directe de la formule des sauts : la dérivée d'une image discontinue est une distribution riche en informations spatiales.
    - **Physics-Informed Neural Networks (PINNs) :** Pour forcer un réseau à respecter une loi physique (ex: équation de la chaleur), on définit une perte qui contient les dérivées du réseau. Si la solution physique a des chocs (discontinuités), on utilise la dérivation au sens des distributions pour calculer la perte correctement.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 82 (Introduction à la théorie des distributions de Schwartz).md]], [[Jalon 38 (Théorème fondamental de l'analyse).md]]
- **Concepts Futurs dépendants :** [[Jalon 107 (Introduction à la théorie des opérateurs non bornés et résolvante.).md]], [[Jalon 117 (Calcul des variations).md]]

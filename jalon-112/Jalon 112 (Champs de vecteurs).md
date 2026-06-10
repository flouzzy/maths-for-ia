---
uuid: "jalon-112"
title: "Champs de vecteurs et Crochet de Lie"
year: 3
trimester: 10
tags:
  - math/geometrie
  - ia/abstraction
prev: "[[Jalon 111 (Applications différentiables et Fibré tangent).md]]"
next: "[[Jalon 113 (Tenseurs).md]]"
---

# Jalon 112 : Champs de vecteurs et Crochet de Lie

## 1. Présentation du concept clé

- **La Métaphore :**
    - Un **Champ de vecteurs**, c'est comme le vent qui souffle partout sur la Terre. À chaque endroit, le vent a une direction et une force précises.
    - Une **Courbe intégrale**, c'est la trajectoire d'un petit avion en papier lâché dans ce vent. L'avion suit les flèches du champ à chaque instant.
    - Le **Crochet de Lie**, c'est une mesure de "non-commutation". Imaginez que vous fassiez un pas vers le Nord (vent $X$) puis un pas vers l'Est (vent $Y$). Arriverez-vous au même endroit que si vous aviez fait d'abord l'Est puis le Nord ? Sur une surface courbe (ou avec des vents tourbillonnants), la réponse est **NON**. Le crochet de Lie mesure exactement le petit décalage entre ces deux chemins.
- **Le "Pourquoi on a inventé ça" :** Pour comprendre les mouvements complexes. En robotique, pour faire bouger un bras, on active plusieurs moteurs (plusieurs champs de vecteurs). Le crochet de Lie nous dit si la combinaison de ces moteurs permet d'atteindre toutes les positions possibles ou si on est limité.
- **Visualisation :** Un champ de flèches sur une sphère. Le crochet de Lie est un nouveau champ de flèches qui représente le "tourbillon" créé par l'interaction de deux autres champs.

## 2. Formalisation

### A. Champs de vecteurs

Soit $M$ une variété différentielle.

> **Définition 1 (Champ de vecteurs) :**
> Un champ de vecteurs $X$ sur $M$ est une application qui, à chaque point $p \in M$, associe un vecteur tangent $X_p \in T_p M$. De manière équivalente, $X$ est une section du fibré tangent $TM$.
> Un champ agit sur les fonctions lisses $f \in \mathcal{C}^\infty(M)$ comme une dérivation : $(Xf)(p) = X_p(f)$.

### B. Flots et Courbes intégrales

> **Définition 2 (Courbe intégrale) :**
> Une courbe $\gamma : I \to M$ est une courbe intégrale de $X$ si sa vitesse à chaque instant est égale au champ :
> $$\forall t \in I, \quad \gamma'(t) = X_{\gamma(t)}$$
> Le **flot** $\Phi_t(p)$ est l'application qui donne la position à l'instant $t$ en partant de $p$ à l'instant 0.

### C. Le Crochet de Lie

Si on applique deux champs successivement ($X$ puis $Y$), l'opération $X(Yf)$ n'est pas une dérivation (elle ne respecte pas la règle de Leibniz pour le produit). Mais leur différence l'est.

> **Définition 3 (Crochet de Lie) :**
> On appelle **crochet de Lie** de deux champs $X$ et $Y$ l'unique champ de vecteurs $[X, Y]$ tel que :
> $$\forall f \in \mathcal{C}^\infty(M), \quad [X, Y]f = X(Yf) - Y(Xf)$$

## 3. Démonstrations

### Démonstration : Le crochet de Lie est une dérivation

Vérifions que $[X, Y]$ satisfait la règle de Leibniz $[X, Y](gh) = ([X, Y]g)h + g([X, Y]h)$.

1. **Développement :**
   $[X, Y](gh) = X(Y(gh)) - Y(X(gh))$.
2. **Application de Leibniz pour Y :**
   $X(Y(gh)) = X( (Yg)h + g(Yh) ) = X(Yg)h + (Yg)(Xh) + (Xg)(Yh) + g(X(Yh))$.
3. **Application de Leibniz pour X :**
   De même, $Y(X(gh)) = Y(Xg)h + (Xg)(Yh) + (Yg)(Xh) + g(Y(Xh))$.
4. **Soustraction :**
   En faisant la différence, les termes croisés $(Yg)(Xh)$ et $(Xg)(Yh)$ s'annulent parfaitement !
   $X(Y(gh)) - Y(X(gh)) = (X(Yg) - Y(Xg))h + g(X(Yh) - Y(X(h)))$.
5. **Conclusion :**
   $[X, Y](gh) = ([X, Y]g)h + g([X, Y]h)$.
   C'est bien une dérivation, donc c'est bien un champ de vecteurs tangent.

## 4. Exercices d'Application

### Exercice 1 : Crochet sur le plan
**Énoncé :** Soient $X = \frac{\partial}{\partial x}$ (translation) and $Y = x \frac{\partial}{\partial y}$ (cisaillement). Calculer $[X, Y]$.
**Correction Détaillée :**
1. $[X, Y]f = X(Yf) - Y(Xf) = \frac{\partial}{\partial x}(x \frac{\partial f}{\partial y}) - x \frac{\partial}{\partial y}(\frac{\partial f}{\partial x})$.
2. $\frac{\partial}{\partial x}(x \frac{\partial f}{\partial y}) = \frac{\partial f}{\partial y} + x \frac{\partial^2 f}{\partial x \partial y}$.
3. Par le lemme de Schwarz (Jalon 47), $x \frac{\partial^2 f}{\partial x \partial y} = x \frac{\partial^2 f}{\partial y \partial x}$.
4. La différence donne $[X, Y]f = \frac{\partial f}{\partial y}$.
**Résultat :** $[X, Y] = \frac{\partial}{\partial y}$. En combinant translation et cisaillement, on peut générer une translation dans une nouvelle direction.

### Exercice 2 : Niveau Avancé (Théorème de Frobenius - Intuition)
**Énoncé :** Si $[X, Y]$ est une combinaison linéaire de $X$ et $Y$, que peut-on dire des flots ?
**Correction Détaillée :**
Cela signifie que les deux "vents" restent prisonniers d'une même surface (une sous-variété). On peut feuilleter l'espace en surfaces parallèles. C'est le théorème de Frobenius, crucial pour comprendre les contraintes dans les systèmes physiques.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** Le crochet de Lie définit la structure des **Groupes de Lie** (Jalon 119). En IA, on utilise ces structures pour créer des réseaux de neurones qui respectent les symétries des données.
- **Example Concret :**
    - **Neural ODEs (Ordinary Differential Equations) :** On définit le réseau comme un champ de vecteurs $f_\theta$. L'inférence est le calcul du flot $\Phi_1$. Si on a plusieurs champs, le crochet de Lie nous dit si l'ordre des couches du réseau est important ou non.
    - **Equivariant Neural Networks :** Pour qu'un réseau reconnaisse un objet dans n'importe quelle orientation, on utilise des couches dont les champs de vecteurs commutent avec les champs de vecteurs du groupe des rotations (leur crochet de Lie est nul).
    - **Contrôlabilité (Robotique/IA) :** Pour un agent qui doit apprendre à marcher, le crochet de Lie des forces qu'il peut appliquer nous dit s'il peut atteindre tous les états de son environnement ou s'il est restreint à une zone.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 111 (Applications différentiables et Fibré tangent).md]], [[Jalon 47 (Dérivées partielles d'ordre deux et Hessienne).md]]
- **Concepts Futurs dépendants :** [[Jalon 119 (Connexions avec les groupes de Lie).md]], [[Jalon 128 (Flots de gradient).md]]

---
uuid: "jalon-8-exo-10"
title: "Exercice 10 : Décomposition de Fitting et propriétés des puissances d'un endomorphisme"
tags:
  - math/algebre-lineaire
  - exercice
---
# Exercice 10 : Décomposition de Fitting et propriétés des puissances d'un endomorphisme (Difficulté : ★★★★★)

## Énoncé
Soit $E$ un $\mathbb{K}$-espace vectoriel de dimension finie $n \in \mathbb{N}^*$.
Soit $f \in \mathcal{L}(E)$ un endomorphisme de $E$.
Pour tout entier naturel $k \in \mathbb{N}$, on définit les sous-espaces vectoriels $K_k$ et $I_k$ de $E$ par :
$K_k = \ker(f^k)$ et $I_k = \text{Im}(f^k)$.
Par convention, $f^0 = \text{id}_E$ (l'application identité sur $E$), donc $K_0 = \ker(\text{id}_E) = \{0_E\}$ et $I_0 = \text{Im}(\text{id}_E) = E$.

1.  Démontrer que la suite $(K_k)_{k \in \mathbb{N}}$ est une suite croissante de sous-espaces vectoriels de $E$, c'est-à-dire que pour tout $k \in \mathbb{N}$, $K_k \subseteq K_{k+1}$.
2.  Démontrer que la suite $(I_k)_{k \in \mathbb{N}}$ est une suite décroissante de sous-espaces vectoriels de $E$, c'est-à-dire que pour tout $k \in \mathbb{N}$, $I_{k+1} \subseteq I_k$.
3.  Puisque $E$ est de dimension finie, en déduire qu'il existe un plus petit entier $p \in \mathbb{N}$ tel que $K_p = K_{p+1}$.
4.  Démontrer que si $K_p = K_{p+1}$, alors pour tout entier $j \ge 1$, on a $K_p = K_{p+j}$.
5.  Démontrer que si $K_p = K_{p+1}$, alors $I_p = I_{p+1}$.
6.  Démontrer que $E = K_p \oplus I_p$.

## Correction Détaillée

1.  **Démonstration de $K_k \subseteq K_{k+1}$ pour tout $k \in \mathbb{N}$ :**
    Soit $k \in \mathbb{N}$.
    Soit $x \in K_k$. Par définition de $K_k$, cela signifie que $f^k(x) = 0_E$.
    Nous voulons montrer que $x \in K_{k+1}$, c'est-à-dire que $f^{k+1}(x) = 0_E$.
    Calculons $f^{k+1}(x)$ :
    $$f^{k+1}(x) = (f \circ f^k)(x)$$
    $$f^{k+1}(x) = f(f^k(x))$$
    Puisque $f^k(x) = 0_E$, nous avons :
    $$f^{k+1}(x) = f(0_E)$$
    Comme $f$ est une application linéaire, elle envoie le vecteur nul de $E$ sur le vecteur nul de $E$.
    Donc, $f(0_E) = 0_E$.
    Par conséquent, $f^{k+1}(x) = 0_E$.
    Ceci implique que $x \in K_{k+1}$.
    Ainsi, tout élément de $K_k$ est aussi un élément de $K_{k+1}$.
    Par conséquent, $K_k \subseteq K_{k+1}$ pour tout $k \in \mathbb{N}$.

2.  **Démonstration de $I_{k+1} \subseteq I_k$ pour tout $k \in \mathbb{N}$ :**
    Soit $k \in \mathbb{N}$.
    Soit $y \in I_{k+1}$. Par définition de $I_{k+1}$, cela signifie qu'il existe un vecteur $x \in E$ tel que $y = f^{k+1}(x)$.
    Nous voulons montrer que $y \in I_k$, c'est-à-dire qu'il existe un vecteur $x' \in E$ tel que $y = f^k(x')$.
    Nous pouvons réécrire l'expression de $y$ comme suit :
    $$y = f^{k+1}(x) = f^k(f(x))$$
    Posons $x' = f(x)$. Puisque $x \in E$ et $f \in \mathcal{L}(E)$, l'image $f(x)$ est bien un vecteur de $E$. Donc $x' \in E$.
    Alors, l'expression de $y$ devient :
    $$y = f^k(x')$$
    Ceci implique que $y$ est l'image d'un vecteur de $E$ par $f^k$.
    Par conséquent, $y \in I_k$.
    Ainsi, tout élément de $I_{k+1}$ est aussi un élément de $I_k$.
    Par conséquent, $I_{k+1} \subseteq I_k$ pour tout $k \in \mathbb{N}$.

3.  **Existence de $p$ tel que $K_p = K_{p+1}$ :**
    D'après la question 1, nous avons une suite croissante de sous-espaces vectoriels de $E$:
    $$K_0 \subseteq K_1 \subseteq K_2 \subseteq \dots \subseteq K_k \subseteq K_{k+1} \subseteq \dots \subseteq E$$
    Puisque $E$ est un $\mathbb{K}$-espace vectoriel de dimension finie $n$, la dimension de chaque sous-espace $K_k$ est un entier naturel. De plus, la dimension d'un sous-espace ne peut pas excéder la dimension de l'espace ambiant.
    La suite des dimensions $(\dim(K_k))_{k \in \mathbb{N}}$ est donc une suite croissante d'entiers naturels :
    $$0 = \dim(K_0) \le \dim(K_1) \le \dim(K_2) \le \dots \le \dim(K_k) \le \dim(K_{k+1}) \le \dots \le n$$
    Une suite croissante d'entiers naturels qui est bornée (ici par $n$) est nécessairement stationnaire à partir d'un certain rang.
    Il existe donc un plus petit entier $p \in \mathbb{N}$ tel que $\dim(K_p) = \dim(K_{p+1})$.
    Or, nous savons que $K_p \subseteq K_{p+1}$. Si deux sous-espaces vectoriels sont inclus l'un dans l'autre et ont la même dimension, alors ils sont égaux.
    Par conséquent, $K_p = K_{p+1}$.

4.  **Démonstration de $K_p = K_{p+j}$ pour tout $j \ge 1$ si $K_p = K_{p+1}$ :**
    Nous allons démontrer cette propriété par récurrence sur l'entier $j \ge 1$.

    **Cas de base ($j=1$) :** L'énoncé stipule que $K_p = K_{p+1}$, donc la propriété est vraie pour $j=1$.

    **Hypothèse de récurrence :** Supposons que pour un certain entier $j \ge 1$, on ait $K_p = K_{p+j}$.

    **Étape de récurrence :** Montrons que $K_p = K_{p+j+1}$.
    D'après la question 1, nous savons que $K_{p+j} \subseteq K_{p+j+1}$.
    D'après l'hypothèse de récurrence, $K_p = K_{p+j}$, ce qui implique $K_p \subseteq K_{p+j+1}$.
    Il nous reste à montrer l'inclusion inverse, c'est-à-dire $K_{p+j+1} \subseteq K_p$.
    Soit $x \in K_{p+j+1}$. Par définition, $f^{p+j+1}(x) = 0_E$.
    Nous pouvons écrire $f^{p+j+1}(x)$ comme suit :
    $$f^{p+j+1}(x) = f^{p+1}(f^j(x))$$
    Puisque $f^{p+1}(f^j(x)) = 0_E$, cela signifie que le vecteur $f^j(x)$ appartient au noyau de $f^{p+1}$, c'est-à-dire $f^j(x) \in K_{p+1}$.
    Or, par l'hypothèse de l'énoncé, nous avons $K_p = K_{p+1}$.
    Donc, $f^j(x) \in K_p$.
    Par définition de $K_p$, cela signifie que $f^p(f^j(x)) = 0_E$.
    Ce qui est équivalent à $f^{p+j}(x) = 0_E$.
    Par définition, cela signifie que $x \in K_{p+j}$.
    D'après l'hypothèse de récurrence, $K_{p+j} = K_p$.
    Donc, $x \in K_p$.
    Ainsi, $K_{p+j+1} \subseteq K_p$.
    En combinant les deux inclusions $K_p \subseteq K_{p+j+1}$ et $K_{p+j+1} \subseteq K_p$, nous obtenons $K_p = K_{p+j+1}$.

    **Conclusion :** Par le principe de récurrence, pour tout entier $j \ge 1$, si $K_p = K_{p+1}$, alors $K_p = K_{p+j}$.

5.  **Démonstration de $I_p = I_{p+1}$ si $K_p = K_{p+1}$ :**
    D'après la question 2, nous savons que $I_{p+1} \subseteq I_p$.
    Pour montrer l'égalité, il suffit de montrer que $\dim(I_p) = \dim(I_{p+1})$.
    Nous utilisons le Théorème du Rang, qui s'applique car $E$ est de dimension finie.
    Pour tout $k \in \mathbb{N}$, le Théorème du Rang appliqué à l'endomorphisme $f^k \in \mathcal{L}(E)$ donne :
    $$\dim(E) = \dim(\ker(f^k)) + \dim(\text{Im}(f^k))$$
    En utilisant nos notations, cela s'écrit :
    $$\dim(E) = \dim(K_k) + \dim(I_k)$$

    Appliquons ce théorème pour $k=p$ et pour $k=p+1$ :
    1. Pour $k=p$ : $\dim(E) = \dim(K_p) + \dim(I_p)$ (Équation $\star$)
    2. Pour $k=p+1$ : $\dim(E) = \dim(K_{p+1}) + \dim(I_{p+1})$ (Équation $\star\star$)

    L'énoncé nous donne l'hypothèse $K_p = K_{p+1}$.
    Ceci implique que leurs dimensions sont égales : $\dim(K_p) = \dim(K_{p+1})$.
    En substituant $\dim(K_{p+1})$ par $\dim(K_p)$ dans l'Équation $\star\star$, nous obtenons :
    $$\dim(E) = \dim(K_p) + \dim(I_{p+1})$$
    Comparons cette nouvelle expression avec l'Équation $\star$ :
    $$\dim(K_p) + \dim(I_p) = \dim(K_p) + \dim(I_{p+1})$$
    En soustrayant $\dim(K_p)$ des deux côtés de l'égalité, nous obtenons :
    $$\dim(I_p) = \dim(I_{p+1})$$
    Puisque $I_{p+1} \subseteq I_p$ (démontré en question 2) et que ces deux sous-espaces ont la même dimension, ils sont égaux.
    Par conséquent, $I_p = I_{p+1}$.

6.  **Démonstration de $E = K_p \oplus I_p$ :**
    Pour démontrer que $E$ est la somme directe de $K_p$ et $I_p$, nous devons prouver deux conditions :
    a) L'intersection des deux sous-espaces est réduite au vecteur nul : $K_p \cap I_p = \{0_E\}$.
    b) La somme des dimensions de $K_p$ et $I_p$ est égale à la dimension de $E$ : $\dim(K_p) + \dim(I_p) = \dim(E)$. (Cette dernière condition est déjà établie par le Théorème du Rang, comme vu à la question 5).

    **Démonstration de $K_p \cap I_p = \{0_E\}$ :**
    Soit $x \in K_p \cap I_p$.
    Puisque $x \in K_p$, par définition, $f^p(x) = 0_E$.
    Puisque $x \in I_p$, par définition, il existe un vecteur $y \in E$ tel que $x = f^p(y)$.
    Substituons cette expression de $x$ dans la première égalité ($f^p(x) = 0_E$) :
    $$f^p(f^p(y)) = 0_E$$
    Ce qui est équivalent à :
    $$f^{2p}(y) = 0_E$$
    Par définition, cela signifie que $y \in \ker(f^{2p})$, c'est-à-dire $y \in K_{2p}$.
    D'après la question 4, puisque nous avons établi que $K_p = K_{p+1}$, nous avons $K_p = K_{p+j}$ pour tout entier $j \ge 1$.
    En particulier, pour $j=p$, nous avons $K_p = K_{p+p} = K_{2p}$.
    Donc, puisque $y \in K_{2p}$, il s'ensuit que $y \in K_p$.
    Par définition de $K_p$, cela signifie que $f^p(y) = 0_E$.
    Or, nous avions initialement $x = f^p(y)$.
    Par conséquent, $x = 0_E$.
    L'intersection $K_p \cap I_p$ est donc réduite au seul vecteur nul $\{0_E\}$.

    **Démonstration de $E = K_p + I_p$ :**
    Nous avons montré que $K_p$ et $I_p$ sont des sous-espaces vectoriels de $E$.
    Nous avons également démontré que leur intersection est triviale : $K_p \cap I_p = \{0_E\}$.
    Ces deux conditions impliquent que la somme $K_p + I_p$ est une somme directe, que l'on note $K_p \oplus I_p$.
    De plus, d'après le Théorème du Rang appliqué à l'endomorphisme $f^p$, nous avons :
    $$\dim(E) = \dim(K_p) + \dim(I_p)$$
    Puisque $K_p \oplus I_p$ est un sous-espace vectoriel de $E$ et que sa dimension est égale à la dimension de $E$, il en découle que $K_p \oplus I_p = E$.
    Par conséquent, $E = K_p \oplus I_p$.
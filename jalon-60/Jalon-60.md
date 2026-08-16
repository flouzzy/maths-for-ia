---
uuid: "jalon-60"
title: "Livrable IA T5 : Preuve du théorème d'approximation universelle"
year: 2
trimester: 5
tags:
  - math/analyse
  - ia/theorie
prev: "[[jalon-59/Jalon-59.md]]"
next: "[[jalon-61/Jalon-61.md]]"
---

# Jalon 60 : Livrable IA T5 : Preuve du théorème d'approximation universelle

## Genèse et Intuition Géométrique

Historiquement, l'intelligence artificielle a traversé plusieurs "hivers" causés par des limites théoriques. Dans les années 1960, Minsky et Papert ont démontré que le Perceptron simple (une seule couche sans couche cachée) était incapable de résoudre le problème non linéaire du XOR. Cela a plongé la recherche dans le doute : les réseaux de neurones étaient-ils fondamentalement limités à des séparations linéaires ?

La résurrection est venue en 1989 avec les travaux de George Cybenko (pour les activations sigmoïdales) et Kurt Hornik (pour les architectures multicouches générales). Ils ont prouvé un résultat extraordinairement puissant : **Le Théorème d'Approximation Universelle (UAT)**.

Le sens géométrique est frappant. Imaginez que vous deviez sculpter une statue complexe à partir d'un bloc d'argile. Si votre outil ne vous permet de faire que des coupes planes (fonctions linéaires), vous n'obtiendrez qu'un polyèdre. Mais si votre outil vous permet de faire des courbures douces (comme une sigmoïde $\sigma$) ou des pliures (comme une ReLU), et que vous pouvez combiner une infinité de ces petites déformations, vous pouvez approcher la surface complexe de la statue avec une précision arbitraire. Le théorème stipule précisément que la superposition de fonctions non-linéaires basiques, pondérées et décalées, permet de reconstruire n'importe quelle fonction continue sur un domaine compact.

## Définitions, Théorèmes et Exemples Numériques

### Énoncé formel du Théorème de Cybenko (1989)

Soit $I_n = [0, 1]^n$ le cube unité compact de $\mathbb{R}^n$. On note $\mathcal{C}(I_n, \mathbb{R})$ l'espace de Banach des fonctions continues de $I_n$ dans $\mathbb{R}$, muni de la norme de la convergence uniforme :
$$ \|f\|_\infty = \sup_{x \in I_n} |f(x)| $$

Soit $\sigma : \mathbb{R} \to \mathbb{R}$ une fonction continue, non constante et bornée (classiquement une fonction sigmoïdale telle que $\lim_{t \to +\infty} \sigma(t) = 1$ et $\lim_{t \to -\infty} \sigma(t) = 0$).

On définit l'ensemble $\mathcal{N}_\sigma$ des réseaux de neurones à une couche cachée de taille arbitraire :
$$ \mathcal{N}_\sigma = \left\{ x \mapsto \sum_{i=1}^{N} \alpha_i \sigma(w_i^T x + b_i) \;\middle|\; N \in \mathbb{N}^*, \alpha_i \in \mathbb{R}, w_i \in \mathbb{R}^n, b_i \in \mathbb{R} \right\} $$

**Théorème (Approximation Universelle) :**
L'ensemble $\mathcal{N}_\sigma$ est dense dans $\mathcal{C}(I_n, \mathbb{R})$ pour la topologie de la norme uniforme. Autrement dit, pour toute fonction $f \in \mathcal{C}(I_n, \mathbb{R})$ et pour tout $\epsilon > 0$, il existe $G \in \mathcal{N}_\sigma$ tel que :
$$ \|f - G\|_\infty < \epsilon $$

### Exemple Concret Immédiat : Approximation d'une fonction échelon

Considérons l'approximation de la fonction marche de Heaviside $H(x) = 1$ si $x \geq 0$ et $0$ sinon, sur le segment $[-1, 1]$. Bien que $H$ soit discontinue, nous pouvons approcher une version continue arbitrairement raide.

Prenons $\sigma(x) = \frac{1}{1 + e^{-x}}$.
Construisons le réseau simple $G_k(x) = \sigma(k x)$.
- Pour $x = 0.5$ et $k = 10$, $G_{10}(0.5) = \sigma(5) \approx 0.9933$.
- Pour $x = -0.5$ et $k = 10$, $G_{10}(-0.5) = \sigma(-5) \approx 0.0067$.
- Pour $x = 0.1$ et $k = 100$, $G_{100}(0.1) = \sigma(10) \approx 0.99995$.

En augmentant le poids scalaire $w = k$, l'activation sigmoïde s'étire et se rapproche uniformément de l'échelon sur tout compact évitant l'origine. En combinant deux échelons (par exemple $G_k(x) - G_k(x-1)$), on obtient une fonction "porte" (bump function) de largeur 1. Toute fonction continue pouvant être approximée par des fonctions en escalier, la combinaison linéaire de ces "portes" permet de reconstruire n'importe quelle forme continue.

### Généralisation aux activations non-polynomiales (Leshno et al., 1993)

Le théorème a été généralisé à des fonctions d'activation non bornées, comme la fonction ReLU très utilisée en Deep Learning moderne.

**Théorème de Leshno (1993) :**
Soit $\sigma : \mathbb{R} \to \mathbb{R}$ une fonction continue. L'espace $\mathcal{N}_\sigma$ est dense dans $\mathcal{C}(K, \mathbb{R})$ (pour tout compact $K \subset \mathbb{R}^n$) si et seulement si $\sigma$ n'est pas un polynôme algébrique.

**Exemple avec ReLU :** Pour $\sigma(x) = \max(0, x)$, $\sigma$ n'est pas polynomiale (à cause de la cassure en $0$). On peut créer une "fonction chapeau" triangulaire en combinant 3 neurones : $h(x) = \sigma(x) - 2\sigma(x-1) + \sigma(x-2)$. Ce chapeau vaut $0$ en dehors de $[0, 2]$ et forme une pointe en $x=1$. On peut alors paver l'espace avec ces chapeaux pour interpoler n'importe quelle fonction continue.

## Démonstrations Analytiques

### Preuve du Théorème de Cybenko via le Théorème de Hahn-Banach

La preuve repose sur un argument magistral d'analyse fonctionnelle : montrer qu'une forme linéaire s'annulant sur notre ensemble dense est nécessairement nulle.

**Étape 1 : Hypothèse par l'absurde et application de Hahn-Banach.**
Supposons que $\mathcal{N}_\sigma$ n'est pas dense dans $\mathcal{C}(I_n)$. Alors son adhérence $\overline{\mathcal{N}_\sigma}$ est un sous-espace vectoriel fermé strictement inclus dans $\mathcal{C}(I_n)$.
Par le Théorème de Hahn-Banach (forme géométrique / analytique), il existe une forme linéaire continue non nulle $L : \mathcal{C}(I_n) \to \mathbb{R}$ telle que $L(g) = 0$ pour tout $g \in \overline{\mathcal{N}_\sigma}$.

**Étape 2 : Représentation de Riesz-Markov.**
L'espace $\mathcal{C}(I_n)$ étant l'espace des fonctions continues sur un compact, le théorème de représentation de Riesz stipule que toute forme linéaire continue $L$ peut être représentée par une mesure de Radon finie et signée $\mu$ sur $I_n$ :
$$ \forall f \in \mathcal{C}(I_n), \quad L(f) = \int_{I_n} f(x) d\mu(x) $$
Ainsi, la condition $L(g) = 0$ pour tout $g \in \mathcal{N}_\sigma$ se traduit par :
$$ \forall \alpha, w, b, \quad \int_{I_n} \alpha \sigma(w^T x + b) d\mu(x) = 0 $$
Et comme on peut factoriser $\alpha \neq 0$, on obtient l'équation fondamentale :
$$ \forall w \in \mathbb{R}^n, \forall b \in \mathbb{R}, \quad \int_{I_n} \sigma(w^T x + b) d\mu(x) = 0 $$

**Étape 3 : Propriété Discriminatoire de la Sigmoïde.**
Cybenko introduit la notion de "fonction discriminatoire". Une fonction $\sigma$ est dite discriminatoire si la nullité de l'intégrale ci-dessus implique que la mesure $\mu$ est identiquement nulle.
Il démontre ensuite par la théorie de la mesure et l'analyse de Fourier que toute fonction sigmoïdale continue est discriminatoire.

Fixons un vecteur $w \in \mathbb{R}^n$. Définissons une forme linéaire bornée sur $L^\infty(\mathbb{R})$ par $F(h) = \int_{I_n} h(w^T x) d\mu(x)$.
Pour $h(t) = \sigma(k t + b)$, l'hypothèse donne $F(\sigma(k \cdot + b)) = 0$.
En faisant tendre $k \to +\infty$, comme $\sigma$ est une sigmoïde, $\sigma(k(w^T x) + b)$ converge ponctuellement vers une fonction indicatrice (l'échelon). Par le théorème de convergence dominée de Lebesgue, on déduit que l'intégrale s'annule pour les fonctions indicatrices de demi-espaces.
Par transformation de Fourier des mesures (fonctions caractéristiques), on montre que si $\mu$ annule tous les demi-espaces, alors $\mu$ est la mesure nulle.

**Étape 4 : Conclusion.**
Si $\mu = 0$, alors la forme linéaire $L$ est la forme linéaire nulle, ce qui contredit l'hypothèse initiale déduite de Hahn-Banach ($L \neq 0$).
L'hypothèse que $\mathcal{N}_\sigma$ n'est pas dense est donc fausse. La densité est prouvée. $\blacksquare$

## Applications dans les Architectures d'Intelligence Artificielle

L'UAT est la pierre angulaire justifiant théoriquement l'usage des réseaux de neurones.

### La Malédiction de la Dimensionnalité (Curse of Dimensionality)

Si le théorème prouve l'existence d'un réseau approximant $f$, il ne dit absolument rien sur l'efficacité de cette approximation. Pour approcher une fonction complexe en grande dimension $n$, le nombre de neurones $N$ requis sur une seule couche cachée croît de manière exponentielle : $N \sim \mathcal{O}(\epsilon^{-n})$. C'est la malédiction de la dimension.

### Séparation par la Profondeur (Depth Separation)

C'est ici qu'intervient le Deep Learning. Bien qu'une seule couche suffise théoriquement, les réseaux profonds (plusieurs couches) offrent une efficacité exponentiellement supérieure.
Il existe des familles de fonctions (comme les fonctions polynomiales de degré élevé, ou la parité) qui peuvent être approximées par un réseau profond avec un nombre de neurones polynomial $\mathcal{O}(n)$, mais qui exigeraient un nombre exponentiel $\mathcal{O}(2^n)$ de neurones pour un réseau superficiel.
Les couches successives composent l'espace et le "plient" (manifold folding), permettant d'exprimer des symétries et des hiérarchies (comme dans les Réseaux Convolutifs CNN) de manière incomparablement plus économique en termes de paramètres.

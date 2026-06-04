---
uuid: "jalon-71"
title: "Théorèmes de Fubini-Tonelli"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 70 (Espaces mesurés produits).md]]"
next: "[[Jalon 72 (Livrable IA).md]]"
---

# Jalon 71 : Théorèmes de Fubini-Tonelli

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous vouliez compter le nombre total d'élèves dans une école. Les élèves sont rangés en rangées et en colonnes dans la cour.
    - Vous avez deux méthodes :
        1. Compter le nombre d'élèves dans chaque **rangée**, puis additionner les totaux de toutes les rangées.
        2. Compter le nombre d'élèves dans chaque **colonne**, puis additionner les totaux de toutes les colonnes.
    - Le bon sens vous dit que vous trouverez le même résultat. Les **Théorèmes de Fubini et Tonelli** sont les règles mathématiques qui confirment ce bon sens pour des objets beaucoup plus complexes qu'une cour d'école (des fonctions continues ou sauvages sur des espaces infinis).
- **Le "Pourquoi on a inventé ça" :** Parfois, calculer une intégrale double est très difficile dans un sens, mais devient trivial si on change l'ordre d'intégration. Fubini est le "permis de changer d'ordre" qui simplifie la vie des mathématiciens et des ingénieurs.
- **Visualisation :** On scanne une surface 3D tranche par tranche. On peut scanner de gauche à droite ou de l'avant vers l'arrière. Si le volume est bien défini, le scan donne la même quantité totale.

## 2. Formalisation & Rigueur Académique

Soient $(X_1, \mathcal{F}_1, \mu_1)$ et $(X_2, \mathcal{F}_2, \mu_2)$ deux espaces mesurés **$\sigma$-finis**. Soit $\pi = \mu_1 \otimes \mu_2$ la mesure produit.

### A. Théorème de Tonelli (Fonctions Positives)

C'est la version "sans risque" pour les fonctions qui ne sont jamais négatives.

> **Théorème de Tonelli :**
> Soit $f : X_1 \times X_2 \to [0, +\infty]$ une fonction mesurable. Alors :
> 1. Les fonctions $x \mapsto \int_{X_2} f(x, y) d\mu_2(y)$ et $y \mapsto \int_{X_1} f(x, y) d\mu_1(x)$ sont mesurables.
> 2. On a l'égalité des intégrales (éventuellement égales à $+\infty$) :
>    $$\int_{X_1 \times X_2} f d\pi = \int_{X_1} \left( \int_{X_2} f(x, y) d\mu_2(y) \right) d\mu_1(x) = \int_{X_2} \left( \int_{X_1} f(x, y) d\mu_1(x) \right) d\mu_2(y)$$

### B. Théorème de Fubini (Fonctions Intégrables)

Si la fonction peut changer de signe, on doit s'assurer qu'elle n'explose pas.

> **Théorème de Fubini :**
> Soit $f : X_1 \times X_2 \to \mathbb{R}$ une fonction mesurable.
> **Si** l'une des intégrales itérées de $|f|$ est finie (par Tonelli) :
> $$\int_{X_1} \left( \int_{X_2} |f(x, y)| d\mu_2(y) \right) d\mu_1(x) < +\infty$$
> **Alors** $f$ est intégrable par rapport à $\pi$ et l'égalité des intégrales itérées est vraie.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Le danger de l'interversion : Un contre-exemple célèbre

Considérons $f(x, y) = \frac{x^2 - y^2}{(x^2 + y^2)^2}$ sur $]0, 1]^2$.

1. **Calcul dans un sens :**
   $\int_0^1 \frac{x^2 - y^2}{(x^2 + y^2)^2} dy = \left[ \frac{y}{x^2 + y^2} \right]_{y=0}^{y=1} = \frac{1}{x^2 + 1}$.
   Puis $\int_0^1 \frac{1}{x^2 + 1} dx = [\arctan x]_0^1 = \pi/4$.
2. **Calcul dans l'autre sens :**
   Par symétrie (en échangeant $x$ et $y$, on change le signe), on trouve $-\pi/4$.
3. **Conclusion :** $\pi/4 \neq -\pi/4$. L'ordre d'intégration change le résultat !
4. **Pourquoi Fubini ne s'applique pas ?** Si on calcule l'intégrale de la valeur absolue $|f|$, on trouvera $+\infty$. La fonction n'est pas intégrable sur le carré. Cela montre que l'hypothèse d'intégrabilité absolue dans Fubini est **indispensable**.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Intégrale de Gauss (Encore elle !)
**Énoncé :** Calculer $I = \int_0^{+\infty} e^{-x^2} dx$ en calculant $I^2$ à l'aide de Fubini.
**Correction Détaillée :**
1. $I^2 = (\int_0^\infty e^{-x^2} dx) (\int_0^\infty e^{-y^2} dy) = \int_0^\infty \int_0^\infty e^{-(x^2+y^2)} dx dy$ (par Tonelli).
2. On passe en coordonnées polaires (qui est une forme de Fubini avec changement de variable) :
   $I^2 = \int_0^{\pi/2} \int_0^\infty e^{-r^2} r dr d\theta$.
3. Intégrale en $r$ : $[- \frac{1}{2} e^{-r^2}]_0^\infty = 1/2$.
4. Intégrale en $\theta$ : $\int_0^{\pi/2} 1/2 d\theta = \pi/4$.
5. Résultat : $I = \sqrt{\pi}/2$.

### Exercice 2 : Niveau Avancé (Volume d'une boule)
**Énoncé :** Utiliser Fubini pour calculer le volume de la boule unité dans $\mathbb{R}^3$.
**Correction Détaillée :**
On écrit la boule comme l'ensemble des points $(x, y, z)$ tels que $x^2 + y^2 \le 1$ and $-\sqrt{1-x^2-y^2} \le z \le \sqrt{1-x^2-y^2}$. L'application successive de Fubini ramène le calcul à une intégrale simple sur un disque, puis sur un segment.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Fubini est le socle de tout le calcul des **Marginales** et des **Conditionnelles** en probabilités. $p(x) = \int p(x, y) dy$.
- **Example Concret :**
    - **Modèles de Langage (LLM) :** La probabilité d'une phrase $P(w_1, \dots, w_n)$ est une intégrale jointe sur toutes les significations possibles des mots. Pour calculer la probabilité d'un mot seul, on "intègre" tous les autres. Fubini garantit que l'ordre dans lequel on traite les variables n'influence pas la cohérence du modèle.
    - **Calcul du Gradient du Risque :** On veut $\nabla_\theta \mathbb{E}[L] = \nabla_\theta \int L(x, \theta) p(x) dx$. Pour passer le gradient sous l'intégrale (Jalon 69), on utilise souvent Fubini pour réorganiser les variables de manière à isoler le paramètre $\theta$.
    - **Convolution 2D :** En CNN, l'opération de convolution est une intégrale double. Fubini permet de décomposer une convolution 2D en deux convolutions 1D successives (Separable Convolutions), ce qui est beaucoup plus rapide pour un ordinateur.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 70 (Espaces mesurés produits).md]], [[Jalon 69 (Démonstration complète du théorème de convergence dominée de Lebesgue.).md]]
- **Concepts Futurs dépendants :** [[Jalon 88 (Indépendance d'événements).md]], [[Jalon 80 (Transformée de Fourier dans L1).md]]

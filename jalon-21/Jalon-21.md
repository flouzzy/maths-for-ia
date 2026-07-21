---
uuid: "jalon-21"
title: "Suites de fonctions : convergence simple et convergence uniforme"
author: "Professeur Émérite de Mathématiques"
keywords: ["suites de fonctions", "convergence simple", "convergence uniforme", "limite", "continuité", "intégrale", "analyse fonctionnelle", "théorème de Dini", "séries de fonctions", "convergence en norme sup"]
description: "Ce cours explore les concepts fondamentaux de convergence simple et de convergence uniforme pour les suites de fonctions. Il en déduit les implications majeures sur la préservation des propriétés analytiques comme la continuité et l'intégrabilité, et met en lumière leur pertinence dans des domaines avancés, notamment l'intelligence artificielle."
---

# Jalon 21 : Suites de fonctions, étude de la convergence simple et de la convergence uniforme

## 1. Présentation du concept clé : La danse des approximations

Imaginez que vous êtes un observateur attentif d'un phénomène complexe, par exemple l'évolution de la température le long d'une barre métallique chauffée. Chaque jour, vous effectuez des mesures, et ces mesures, prises à différents points de la barre, décrivent une certaine courbe de température. Appelons ces courbes $f_1(x)$, $f_2(x)$, $f_3(x)$, et ainsi de suite, où $x$ est la position le long de la barre et l'indice représente le jour. Vous obtenez ainsi une "suite" de fonctions.

L'objectif est de comprendre si cette suite de fonctions "tend" vers une situation finale stable, une sorte de profil de température d'équilibre. Mais qu'est-ce que cela signifie, pour une suite de fonctions, de tendre vers une autre fonction ?

Considérons une première approche : chaque jour, pour chaque point $x$ de la barre, la température $f_n(x)$ se rapproche de plus en plus de la température d'équilibre $f(x)$. C'est une convergence "point par point". Si je me fixe sur un point précis de la barre, disons son extrémité droite, et que je regarde la suite des températures à cet endroit ($f_1(x_0), f_2(x_0), \dots$), cette suite de nombres converge vers $f(x_0)$. Si cela est vrai pour *tous* les points de la barre, on parle de **convergence simple**. C'est une forme de rapprochement, certes, mais elle peut être trompeuse.

Imaginons une rangée de musiciens qui accordent leurs instruments. La convergence simple, c'est comme si chaque musicien réussissait à accorder parfaitement son instrument. L'un après l'autre, ils trouvent la note juste. Cependant, il n'y a aucune garantie qu'ils soient tous accordés *en même temps*. Il se pourrait que lorsque le premier a fini, le dernier est encore loin du compte, et inversement. Le temps nécessaire pour que chaque musicien atteigne l'accord parfait pourrait dépendre du musicien lui-même.

Maintenant, visualisez une seconde approche : non seulement chaque point de la barre voit sa température se stabiliser, mais l'écart maximum entre le profil de température du jour $n$ et le profil d'équilibre diminue globalement. Autrement dit, le "pire" désaccord sur l'ensemble de la barre devient de plus en plus petit à mesure que les jours passent. Ici, le rythme d'accordement n'est pas point par point, mais global. On exige qu'à partir d'un certain jour $N$, l'ensemble de la barre présente un écart de température partout inférieur à une petite marge $\epsilon$. C'est ce que l'on nomme la **convergence uniforme**.

Pour reprendre l'analogie des musiciens : la convergence uniforme, c'est lorsque, à partir d'un certain moment, l'ensemble de l'orchestre est globalement accordé avec une précision donnée. Il n'y a pas un musicien plus en retard qu'un autre dans le processus global d'accordement. L'écart maximal de justesse de l'ensemble de l'orchestre diminue de manière coordonnée.

La distinction est subtile mais capitale. La convergence simple nous assure que les choses s'améliorent localement, mais elle ne garantit rien sur la "qualité" globale de l'approximation à un instant donné. Elle peut entraîner des surprises désagréables, comme la perte de propriétés fondamentales : une suite de fonctions "lisses" (continues, par exemple) pourrait converger simplement vers une fonction qui ne l'est pas du tout. La convergence uniforme, en revanche, est le garde-fou qui préserve la "qualité" des fonctions dans le processus de passage à la limite. Elle est le prix à payer pour que les belles propriétés des fonctions initiales (continuité, intégrabilité) se transmettent à la fonction limite.

La nécessité de formaliser rigoureusement ces concepts est née d'une crise historique en analyse au XIXe siècle. Avant les travaux de figures éminentes telles qu'Augustin-Louis Cauchy et Karl Weierstrass, les mathématiciens manipulaient les séries de fonctions et les limites avec une intuition souvent géométrique ou physique, pensant qu'une limite infinie de fonctions continues conserverait naturellement la continuité. Cauchy lui-même, en 1821, affirmait à tort qu'une série de fonctions continues convergente produisait nécessairement une somme continue, ce qui fut démenti par des contre-exemples de Fourier et d'Abel. C'est Weierstrass et Gudermann qui introduiront la distinction cruciale de la "convergence uniforme" pour sauver l'édifice de l'analyse, prouvant que cette rigueur globale était la clé pour préserver la continuité, l'intégrabilité, et la dérivabilité lors d'un passage à la limite.

## 2. Formalisation : Le Protocole d'Exégèse Conceptuelle

Nous allons maintenant appliquer le protocole d'exégèse conceptuelle pour formaliser ces deux types de convergence.

### Notion 1 : La Convergence Simple

**A. Énoncé Symbolique Strict**

Soit un ensemble $I$ (généralement un sous-ensemble de $\mathbb{R}$ ou $\mathbb{C}$, tel qu'un intervalle). Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions définies sur $I$ à valeurs dans $\mathbb{R}$ ou $\mathbb{C}$. Soit $f$ une fonction définie sur $I$.
On dit que la suite de fonctions $(f_n)_{n \in \mathbb{N}}$ converge simplement vers $f$ sur $I$ si :
$$ \forall x \in I, \forall \epsilon > 0, \exists N \in \mathbb{N}, \text{ tel que } \forall n \ge N, |f_n(x) - f(x)| < \epsilon $$

**B. Anatomie et Typage Chirurgical**

*   **L'ensemble de départ $I$ :** C'est le domaine de définition commun à toutes les fonctions $f_n$ et à la fonction limite $f$. Il s'agit d'une donnée globale fixe du problème.
*   **Les fonctions $f_n : I \to \mathbb{K}$ :** Pour chaque entier $n \in \mathbb{N}$, $f_n$ associe à un point $x \in I$ un scalaire $f_n(x)$ (réel ou complexe).
*   **La fonction limite $f : I \to \mathbb{K}$ :** C'est la fonction "cible".
*   **L'ordre des quantificateurs (Crucial !) :** Observez attentivement le début de la proposition : $\forall x \in I, \forall \epsilon > 0, \exists N \in \mathbb{N}$. Le rang $N$ à partir duquel l'écart est inférieur à $\epsilon$ dépend *à la fois* de la précision $\epsilon$ voulue *et* du point $x$ choisi. On écrit formellement $N = N(\epsilon, x)$. C'est le marqueur absolu de la convergence simple : on étudie la convergence point par point de manière isolée.

**C. Exemples de Validation**

*Exemple Trivial :*
Soit $f_n(x) = \frac{x}{n}$ sur $I = \mathbb{R}$. Pour tout $x \in \mathbb{R}$ fixé, $\lim_{n \to \infty} \frac{x}{n} = 0$. Donc la suite $(f_n)$ converge simplement vers la fonction nulle $f(x) = 0$ sur $\mathbb{R}$.
Posons le cadre formel : Soit $x \in \mathbb{R}$ et $\epsilon > 0$. On cherche $N$ tel que pour $n \ge N$, $|\frac{x}{n} - 0| < \epsilon$.
$$ \frac{|x|}{n} < \epsilon \iff n > \frac{|x|}{\epsilon} $$
Il suffit de prendre l'entier $N = \lfloor \frac{|x|}{\epsilon} \rfloor + 1$. Ce $N$ dépend explicitement de $x$ et de $\epsilon$.

*Exemple Complexe :*
Considérons $f_n(x) = x^n e^{-nx}$ sur $I = [0, +\infty[$. Pour $x=0$, $f_n(0) = 0 \to 0$. Pour $x > 0$, l'exponentielle l'emporte sur la puissance, donc $\lim_{n \to \infty} x^n e^{-nx} = 0$. La suite converge simplement vers la fonction nulle sur $[0, +\infty[$.

**D. Cas Pathologiques et Contre-exemples**

*Contre-exemple aux limites (La bosse glissante) :*
Soit $f_n(x)$ définie sur $\mathbb{R}$ par $f_n(x) = 1$ si $x \in [n, n+1]$ et $0$ ailleurs.
Pour tout $x \in \mathbb{R}$ fixé, il existe un rang $N$ (tel que $N > x$) tel que pour tout $n \ge N$, $x \notin [n, n+1]$, et donc $f_n(x) = 0$.
Ainsi, $\lim_{n \to \infty} f_n(x) = 0$ pour tout $x$. La suite converge simplement vers la fonction nulle. Pourtant, la "bosse" de hauteur 1 existe toujours, elle glisse simplement vers l'infini, montrant que la convergence simple "perd de vue" l'allure globale de la fonction.

### Notion 2 : La Convergence Uniforme

**A. Énoncé Symbolique Strict**

On dit que la suite de fonctions $(f_n)_{n \in \mathbb{N}}$ converge uniformément vers $f$ sur $I$ si :
$$ \forall \epsilon > 0, \exists N \in \mathbb{N}, \text{ tel que } \forall n \ge N, \forall x \in I, |f_n(x) - f(x)| < \epsilon $$
Alternativement, en introduisant la norme infini $\|g\|_{\infty, I} = \sup_{x \in I} |g(x)|$, la convergence uniforme équivaut à :
$$ \lim_{n \to \infty} \|f_n - f\|_{\infty, I} = 0 $$

**B. Anatomie et Typage Chirurgical**

*   **Le basculement quantificatif (Le cœur de la différence) :** L'énoncé commence par $\forall \epsilon > 0, \exists N \in \mathbb{N}, \forall n \ge N, \forall x \in I$. Le quantificateur $\forall x \in I$ a été repoussé *après* l'existence de $N$. Cela signifie que le rang $N$ dépend de $\epsilon$, mais **ne dépend plus de $x$**. $N = N(\epsilon)$. C'est un rang global, universel pour tout l'intervalle $I$. Dès que $n \ge N$, l'écart $|f_n(x) - f(x)|$ est inférieur à $\epsilon$ *simultanément* pour absolument tous les points de $I$.
*   **La notion de bande de tolérance (Le "Tube") :** Dire que $\forall x \in I, |f_n(x) - f(x)| < \epsilon$ revient à affirmer que le graphe entier de la fonction $f_n$ est entièrement contenu dans un "tube" de largeur $2\epsilon$ centré sur le graphe de la fonction limite $f$ : $f(x) - \epsilon < f_n(x) < f(x) + \epsilon$.
*   **La norme sup $\| \cdot \|_{\infty, I}$ :** Cette norme (le supremum des valeurs absolues sur $I$) mesure précisément le pire écart entre $f_n$ et $f$ sur tout l'intervalle. La convergence uniforme stipule que ce pire écart absolu tend vers zéro lorsque $n$ tend vers l'infini.

**C. Exemples de Validation**

*Exemple Trivial :*
Soit $f_n(x) = \frac{\sin(nx)}{n}$ sur $I = \mathbb{R}$. La fonction limite simple est clairement $f(x) = 0$.
Pour la convergence uniforme, cherchons le supremum de l'écart :
$|f_n(x) - f(x)| = \left| \frac{\sin(nx)}{n} \right| \le \frac{1}{n}$ pour tout $x \in \mathbb{R}$.
Donc, $\|f_n - f\|_{\infty, \mathbb{R}} \le \frac{1}{n}$.
Puisque $\lim_{n \to \infty} \frac{1}{n} = 0$, on a $\lim_{n \to \infty} \|f_n - f\|_{\infty, \mathbb{R}} = 0$. La convergence est bien uniforme sur $\mathbb{R}$.

*Exemple de Non-Uniformité (La cassure de la continuité) :*
Soit $f_n(x) = x^n$ sur $I = [0, 1]$.
Convergence simple (déjà vue dans l'introduction) :
- Pour $x \in [0, 1[$, $x^n \to 0$.
- Pour $x = 1$, $1^n = 1 \to 1$.
La fonction limite $f$ vaut $0$ sur $[0, 1[$ et $1$ en $1$. $f$ est discontinue en $1$.
Étudions la convergence uniforme. Les fonctions $f_n$ sont continues sur $[0,1]$. La fonction limite $f$ ne l'est pas. Le théorème de continuité stipule que si une suite de fonctions continues converge uniformément, la limite DOIT être continue. Par contraposée, puisque la limite est discontinue, la convergence **ne peut pas être uniforme**.
Vérifions formellement par la norme sup :
Sur l'intervalle $[0, 1[$, l'écart est $|f_n(x) - f(x)| = |x^n - 0| = x^n$.
$\|f_n - f\|_{\infty, [0, 1[} = \sup_{x \in [0, 1[} x^n = 1$.
La limite de ce supremum lorsque $n \to \infty$ est $1$, et non $0$. La convergence n'est pas uniforme.

**D. Cas Pathologiques et Contre-exemples**

*Contre-exemple de la limite continue sans convergence uniforme :*
Soit $f_n(x) = nx(1-x)^n$ sur $I = [0, 1]$.
Pour $x=0$, $f_n(0) = 0 \to 0$.
Pour $x \in ]0, 1]$, on reconnait la forme $n q^n$ avec $|q| = 1-x < 1$. D'après les croissances comparées, $\lim_{n \to \infty} n(1-x)^n = 0$.
La suite converge donc simplement vers la fonction nulle $f(x) = 0$ sur $[0, 1]$. La fonction limite est continue. La continuité est préservée.
Cependant, la convergence est-elle uniforme ? Calculons le supremum.
La dérivée $f_n'(x) = n(1-x)^n - n^2x(1-x)^{n-1} = n(1-x)^{n-1}(1 - x - nx) = n(1-x)^{n-1}(1 - (n+1)x)$.
La dérivée s'annule en $x_n = \frac{1}{n+1}$, qui est le point de maximum sur $[0, 1]$.
La valeur maximale est $f_n\left(\frac{1}{n+1}\right) = n \left(\frac{1}{n+1}\right) \left(1 - \frac{1}{n+1}\right)^n = \frac{n}{n+1} \left(\frac{n}{n+1}\right)^n = \left(\frac{n}{n+1}\right)^{n+1}$.
$\|f_n - f\|_{\infty, [0,1]} = \left(1 - \frac{1}{n+1}\right)^{n+1}$.
Or, $\lim_{n \to \infty} \left(1 - \frac{1}{n+1}\right)^{n+1} = e^{-1} \approx 0.368 \neq 0$.
Le supremum de l'erreur ne tend pas vers zéro. Une "bosse" de hauteur $\frac{1}{e}$ se concentre de plus en plus près de 0 mais ne disparaît jamais. La convergence est simple, la limite est continue, **mais la convergence n'est pas uniforme**. C'est le cas pathologique par excellence qui montre que la convergence uniforme est une condition forte.

## 3. Démonstrations Pas-à-Pas

### Démonstration du Théorème Pivot : Le Théorème d'Interversion des Limites (Continuité de la Limite)

> **Théorème de Continuité de la Fonction Limite :**
> Soit $I$ un intervalle de $\mathbb{R}$. Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions définies sur $I$, convergeant uniformément vers une fonction $f$ sur $I$.
> Si, pour tout entier $n \in \mathbb{N}$, la fonction $f_n$ est continue en un point $a \in I$, alors la fonction limite $f$ est également continue en ce point $a$.

1. **Initialisation / Cadre :**
   L'objectif est de démontrer la continuité de la fonction limite $f$ au point $a \in I$.
   Rappel de l'objectif formel de continuité en $a$ :
   On doit prouver que : $\forall \epsilon > 0, \exists \delta > 0, \forall x \in I, |x - a| < \delta \implies |f(x) - f(a)| < \epsilon$.
   Nous disposons de deux hypothèses fondamentales :
   - Hypothèse 1 (Convergence Uniforme) : $\forall \epsilon' > 0, \exists N \in \mathbb{N}, \forall n \ge N, \forall x \in I, |f_n(x) - f(x)| < \epsilon'$.
   - Hypothèse 2 (Continuité des $f_n$) : Pour un $n$ fixé, $\forall \epsilon'' > 0, \exists \delta > 0, \forall x \in I, |x - a| < \delta \implies |f_n(x) - f_n(a)| < \epsilon''$.

   La stratégie consiste à majorer l'écart cible $|f(x) - f(a)|$ en introduisant astucieusement les fonctions $f_n$ par une "astuce des trois tiers" basée sur l'inégalité triangulaire.

2. **Étape 1 : Décomposition par l'Inégalité Triangulaire**
   Pour tout $x \in I$ et tout entier $n \in \mathbb{N}$, nous pouvons écrire l'identité tautologique suivante en ajoutant et soustrayant $f_n(x)$ et $f_n(a)$ à l'intérieur de la valeur absolue :
   $$ f(x) - f(a) = f(x) - f_n(x) + f_n(x) - f_n(a) + f_n(a) - f(a) $$
   En appliquant l'inégalité triangulaire ($|A + B + C| \le |A| + |B| + |C|$), nous obtenons la majoration fondamentale :
   $$ |f(x) - f(a)| \le |f(x) - f_n(x)| + |f_n(x) - f_n(a)| + |f_n(a) - f(a)| $$
   Cette ligne est la pierre angulaire de la preuve. Elle décompose l'erreur totale en trois composantes que nous allons contrôler séparément.

3. **Étape 2 (Transition micro-calculatoire) : Majoration des trois composantes**
   Soit un scalaire de précision arbitraire $\epsilon > 0$. Nous allons allouer un "budget d'erreur" de $\frac{\epsilon}{3}$ à chacune des trois composantes de la somme.

   **Contrôle du premier et du troisième terme (Convergence Uniforme) :**
   D'après l'Hypothèse 1 (Convergence Uniforme de $(f_n)$ vers $f$), appliquée avec le paramètre de tolérance $\epsilon' = \frac{\epsilon}{3}$ :
   Il existe un entier $N \in \mathbb{N}$ tel que, pour tout entier $n \ge N$ et pour *tout point* $t \in I$ (donc a fortiori pour $t=x$ et pour $t=a$) :
   $$ |f_n(t) - f(t)| < \frac{\epsilon}{3} $$
   Fixons définitivement un entier $n_0 \ge N$ (par exemple $n_0 = N$). L'inégalité précédente est vraie pour la fonction spécifique $f_{n_0}$ :
   - Pour le premier terme : $|f(x) - f_{n_0}(x)| = |f_{n_0}(x) - f(x)| < \frac{\epsilon}{3}$, et ce, quel que soit $x \in I$.
   - Pour le troisième terme : $|f_{n_0}(a) - f(a)| < \frac{\epsilon}{3}$.

   À ce stade de la preuve, l'entier $n_0$ est **fixé**.

   **Contrôle du deuxième terme (Continuité de $f_{n_0}$) :**
   Considérons la fonction $f_{n_0}$. D'après l'Hypothèse 2 (Continuité des $f_n$), la fonction $f_{n_0}$ est continue au point $a$.
   En appliquant la définition de la continuité avec le paramètre de tolérance $\epsilon'' = \frac{\epsilon}{3}$, nous savons qu'il existe un rayon $\delta > 0$ tel que :
   $$ \forall x \in I, \text{ si } |x - a| < \delta \text{ alors } |f_{n_0}(x) - f_{n_0}(a)| < \frac{\epsilon}{3} $$

4. **Conclusion : Assemblage final**
   Synthétisons les résultats des étapes précédentes.
   Soit $\epsilon > 0$. Nous avons construit un rayon $\delta > 0$ tel que, pour tout $x \in I$ vérifiant $|x - a| < \delta$, les trois majorations suivantes sont simultanément vraies :
   1. $|f(x) - f_{n_0}(x)| < \frac{\epsilon}{3}$
   2. $|f_{n_0}(x) - f_{n_0}(a)| < \frac{\epsilon}{3}$
   3. $|f_{n_0}(a) - f(a)| < \frac{\epsilon}{3}$

   En réinjectant ces bornes dans l'inégalité triangulaire de l'Étape 1 :
   $$ |f(x) - f(a)| \le |f(x) - f_{n_0}(x)| + |f_{n_0}(x) - f_{n_0}(a)| + |f_{n_0}(a) - f(a)| $$
   $$ |f(x) - f(a)| < \frac{\epsilon}{3} + \frac{\epsilon}{3} + \frac{\epsilon}{3} $$
   $$ |f(x) - f(a)| < \epsilon $$

   Nous avons rigoureusement établi que : $\forall \epsilon > 0, \exists \delta > 0, \forall x \in I, |x - a| < \delta \implies |f(x) - f(a)| < \epsilon$.
   Ceci est l'exacte définition de la continuité de la fonction $f$ au point $a$. Le théorème est prouvé.
   **C.Q.F.D.**

## 4. Exercices d'Application



## 5. Application en Intelligence Artificielle

Les concepts de convergence des suites de fonctions jouent un rôle discret mais fondamental dans le développement et l'analyse des algorithmes d'Intelligence Artificielle, en particulier dans l'apprentissage automatique.

1.  **Apprentissage des Réseaux de Neurones :** Un réseau de neurones est essentiellement une fonction paramétrée, $h_{\theta}(x)$, où $\theta$ représente l'ensemble des poids et biais. Le processus d'entraînement consiste à ajuster ces paramètres $\theta$ de manière itérative (par exemple, via la descente de gradient stochastique) pour minimiser une fonction de coût. Chaque itération de l'entraînement produit un nouvel ensemble de paramètres $\theta_k$, et donc une nouvelle fonction $h_{\theta_k}(x)$. La "convergence" d'un modèle d'IA peut être interprétée comme la convergence de cette suite de fonctions $(h_{\theta_k}(x))$ vers une fonction optimale $h_{\theta^*}(x)$.
    *   **Convergence simple (ou ponctuelle) :** Si, après un certain nombre d'époques, le réseau fournit des prédictions de plus en plus précises pour *chaque* exemple d'entraînement (ou de test) individuel, on peut parler de convergence simple. Cela garantit que l'erreur sur un point de donnée spécifique tend vers zéro.
    *   **Convergence uniforme :** Ce qui est souvent désiré en IA, c'est que l'erreur du réseau diminue *uniformément* sur l'ensemble du jeu de données (entraînement, validation ou test). Cela signifie que le réseau ne s'améliore pas seulement sur certains exemples au détriment d'autres, mais que sa performance globale s'améliore, et que l'écart maximal entre ses prédictions et les vraies valeurs sur l'ensemble du jeu de données tend vers zéro. Des techniques comme la régularisation, le "batch normalization" ou le "dropout" visent implicitement à favoriser une convergence plus uniforme et une meilleure généralisation en évitant l'hyper-spécialisation sur des sous-ensembles de données.

2.  **Théorèmes d'Approximation Universelle :** Ces théorèmes sont fondamentaux pour justifier la capacité des réseaux de neurones à modéliser des fonctions complexes. Le théorème d'approximation universelle de Cybenko ou de Hornik stipule qu'un réseau de neurones feedforward avec une seule couche cachée et un nombre suffisant de neurones peut approximer n'importe quelle fonction continue sur un compact avec une précision arbitraire. Cette "précision arbitraire" est une formulation directe de la convergence uniforme : pour toute marge d'erreur $\epsilon > 0$, il existe un réseau (une fonction) qui s'approche uniformément de la fonction cible à moins de $\epsilon$.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon-14.md|Jalon 14 (Suites réelles et complexes)]], [[Jalon-18.md|Jalon 18 (Continuité des fonctions d'une variable réelle)]]
- **Concepts Futurs dépendants :** [[Jalon-22.md|Jalon 22 (Séries de fonctions)]], [[Jalon-23.md|Jalon 23 (Séries entières)]]

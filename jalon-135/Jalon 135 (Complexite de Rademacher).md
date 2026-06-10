---
uuid: "jalon-135"
title: "Complexité de Rademacher"
year: 3
trimester: 12
tags:
  - math/statistiques_apprentissage
  - ia/theorie_apprentissage
prev: "[[Jalon 134 (Complexite des classes de fonctions).md]]"
next: "[[Jalon 136 (Theorie de Vapnik-Chervonenkis).md]]"
---

# Complexité de Rademacher

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Imagine qu'on donne à une classe d'élèves une série de questions sous forme de devinettes. Si les réponses correctes sont choisies totalement au hasard (pile ou face pour chaque question) par le professeur, il est impossible d'avoir systématiquement une bonne note en utilisant une vraie logique. Si un élève réussit quand même à avoir 100% de bonnes réponses même quand les réponses sont tirées à pile ou face, cela veut dire qu'il ne réfléchit pas : il triche en apprenant toutes les possibilités par cœur. La complexité de Rademacher mesure exactement cela pour un programme informatique : sa capacité à "apprendre par cœur" du bruit aléatoire. Plus un programme peut s'adapter à des résultats purement aléatoires, plus sa "complexité" est élevée, et plus on risque qu'il apprenne par cœur sans rien comprendre.
- **Le "Pourquoi on a inventé ça" :** En intelligence artificielle, on veut savoir si notre modèle a vraiment compris la règle sous-jacente ou s'il s'est contenté d'apprendre les exemples d'entraînement par cœur (ce qu'on appelle le surapprentissage ou *overfitting*). On avait besoin d'un outil mathématique précis pour évaluer la "richesse" ou la "puissance" d'une famille de modèles. Si cette famille est trop riche, elle pourra apprendre du bruit.
- **Visualisation :** Imagine un nuage de points où certains sont rouges et d'autres bleus, coloriés de façon totalement arbitraire (au lancer de pièce). Un modèle de faible complexité ne pourra tracer qu'une simple ligne droite et échouera à séparer parfaitement les points. Un modèle de très haute complexité (comme une courbe très sinueuse) réussira à séparer parfaitement les points rouges des points bleus. La complexité de Rademacher quantifie l'élasticité de cette courbe face à ce bruit aléatoire.

## 2. Formalisation
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soit $\mathcal{X}$ un espace d'entrée mesurable (par exemple un sous-ensemble compact de $\mathbb{R}^d$) et $S = (x_1, \dots, x_n)$ un échantillon d'exemples i.i.d. de taille $n$, tiré selon une distribution de probabilité inconnue $\mathcal{D}$ sur $\mathcal{X}$.
Soit $\mathcal{F}$ une classe de fonctions $f : \mathcal{X} \to \mathbb{R}$.

> **Définition (Variables de Rademacher) :**
> Une variable aléatoire de Rademacher $\sigma$ est une variable aléatoire réelle uniforme sur $\{-1, 1\}$, c'est-à-dire :
> $$\mathbb{P}(\sigma = 1) = \frac{1}{2} \quad \text{et} \quad \mathbb{P}(\sigma = -1) = \frac{1}{2}$$
> Une famille de Rademacher est une suite de variables de Rademacher $\boldsymbol{\sigma} = (\sigma_1, \dots, \sigma_n)$ mutuellement indépendantes.

> **Définition (Complexité de Rademacher Empirique) :**
> Soit $S = (x_1, \dots, x_n) \in \mathcal{X}^n$ un échantillon fixe. La complexité de Rademacher empirique de la classe de fonctions $\mathcal{F}$ par rapport à l'échantillon $S$, notée $\hat{\mathfrak{R}}_S(\mathcal{F})$, est définie par l'espérance par rapport au vecteur aléatoire de Rademacher $\boldsymbol{\sigma}$ :
> $$\hat{\mathfrak{R}}_S(\mathcal{F}) = \mathbb{E}_{\boldsymbol{\sigma}} \left[ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n \sigma_i f(x_i) \right]$$

> **Définition (Complexité de Rademacher) :**
> La complexité de Rademacher de la classe de fonctions $\mathcal{F}$, notée $\mathfrak{R}_n(\mathcal{F})$, est l'espérance de la complexité empirique de Rademacher par rapport à la distribution des échantillons de taille $n$ (tirés de la distribution $\mathcal{D}$) :
> $$\mathfrak{R}_n(\mathcal{F}) = \mathbb{E}_{S \sim \mathcal{D}^n} \left[ \hat{\mathfrak{R}}_S(\mathcal{F}) \right] = \mathbb{E}_{S, \boldsymbol{\sigma}} \left[ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n \sigma_i f(x_i) \right]$$

### B. Théorèmes, Propositions & Lemmes

> **Théorème de Généralisation basé sur la Complexité de Rademacher :**
> Soit $\mathcal{D}$ une distribution de probabilité sur $\mathcal{Z} = \mathcal{X} \times \mathcal{Y}$. Soit $\mathcal{F}$ une famille de fonctions de $\mathcal{Z}$ vers $[0, 1]$.
> Pour tout entier $n \ge 1$ et tout $\delta \in (0, 1)$, avec une probabilité au moins $1 - \delta$ sur le tirage de l'échantillon $S \sim \mathcal{D}^n$, la borne suivante est vérifiée simultanément pour toutes les fonctions $f \in \mathcal{F}$ :
> $$\mathbb{E}_{z \sim \mathcal{D}}[f(z)] \le \frac{1}{n} \sum_{i=1}^n f(z_i) + 2 \mathfrak{R}_n(\mathcal{F}) + \sqrt{\frac{\ln(1/\delta)}{2n}}$$
> Et on a aussi la forme utilisant la complexité empirique :
> $$\mathbb{E}_{z \sim \mathcal{D}}[f(z)] \le \frac{1}{n} \sum_{i=1}^n f(z_i) + 2 \hat{\mathfrak{R}}_S(\mathcal{F}) + 3 \sqrt{\frac{\ln(2/\delta)}{2n}}$$

## 3. Démonstrations
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : Théorème de Généralisation (Lemme de Symétrisation)

Nous allons démontrer la pierre angulaire de ce résultat : la majoration de l'espérance du supremum de la déviation empirique par la complexité de Rademacher.

Soit $\Phi(S) = \sup_{f \in \mathcal{F}} \left( \mathbb{E}[f] - \hat{\mathbb{E}}_S[f] \right)$, où $\mathbb{E}[f] = \mathbb{E}_{z \sim \mathcal{D}}[f(z)]$ et $\hat{\mathbb{E}}_S[f] = \frac{1}{n} \sum_{i=1}^n f(z_i)$.

1. **Initialisation / Cadre : Introduction d'un échantillon fantôme (ghost sample).**
   Soit $S' = (z'_1, \dots, z'_n)$ un deuxième échantillon i.i.d. de taille $n$ tiré selon $\mathcal{D}$, indépendant de $S$. Remarquons que $\mathbb{E}[f] = \mathbb{E}_{S' \sim \mathcal{D}^n} \left[ \frac{1}{n} \sum_{i=1}^n f(z'_i) \right]$.

2. **Étape 1 : Injection de l'échantillon fantôme.**
   On considère l'espérance par rapport à $S$ de la variable $\Phi(S)$.
   $$ \mathbb{E}_{S} \left[ \sup_{f \in \mathcal{F}} \left( \mathbb{E}[f] - \hat{\mathbb{E}}_S[f] \right) \right] = \mathbb{E}_{S} \left[ \sup_{f \in \mathcal{F}} \left( \mathbb{E}_{S'} \left[ \hat{\mathbb{E}}_{S'}[f] \right] - \hat{\mathbb{E}}_S[f] \right) \right] $$
   Comme $\hat{\mathbb{E}}_S[f]$ ne dépend pas de $S'$, on peut l'insérer dans l'espérance sur $S'$ :
   $$ \dots = \mathbb{E}_{S} \left[ \sup_{f \in \mathcal{F}} \left( \mathbb{E}_{S'} \left[ \hat{\mathbb{E}}_{S'}[f] - \hat{\mathbb{E}}_S[f] \right] \right) \right] $$

3. **Étape 2 : Application de l'inégalité de Jensen.**
   La fonction supremum $\sup$ est convexe. Par l'inégalité de Jensen, on a $\sup(\mathbb{E}[\cdot]) \le \mathbb{E}[\sup(\cdot)]$. Donc, en intervertissant le supremum et l'espérance sur $S'$, on obtient une majoration :
   $$ \mathbb{E}_{S} \left[ \sup_{f \in \mathcal{F}} \left( \mathbb{E}_{S'} \left[ \hat{\mathbb{E}}_{S'}[f] - \hat{\mathbb{E}}_S[f] \right] \right) \right] \le \mathbb{E}_{S} \left[ \mathbb{E}_{S'} \left[ \sup_{f \in \mathcal{F}} \left( \hat{\mathbb{E}}_{S'}[f] - \hat{\mathbb{E}}_S[f] \right) \right] \right] $$
   On regroupe les espérances :
   $$ \dots = \mathbb{E}_{S, S'} \left[ \sup_{f \in \mathcal{F}} \left( \frac{1}{n} \sum_{i=1}^n f(z'_i) - \frac{1}{n} \sum_{i=1}^n f(z_i) \right) \right] $$
   $$ \dots = \mathbb{E}_{S, S'} \left[ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n \left( f(z'_i) - f(z_i) \right) \right] $$

4. **Étape 3 : Symétrisation par l'introduction des variables de Rademacher.**
   Puisque $S$ et $S'$ sont identiquement distribués et indépendants, pour tout indice $i \in \{1, \dots, n\}$, échanger $z_i$ et $z'_i$ ne change pas la distribution conjointe de $(S, S')$. Par conséquent, on peut multiplier la différence $(f(z'_i) - f(z_i))$ par une variable de Rademacher $\sigma_i \in \{-1, 1\}$ sans modifier l'espérance. En introduisant le vecteur $\boldsymbol{\sigma} = (\sigma_1, \dots, \sigma_n)$, on écrit :
   $$ \mathbb{E}_{S, S'} \left[ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n \left( f(z'_i) - f(z_i) \right) \right] = \mathbb{E}_{S, S', \boldsymbol{\sigma}} \left[ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n \sigma_i \left( f(z'_i) - f(z_i) \right) \right] $$

5. **Étape 4 : Décomposition par sous-additivité du supremum.**
   On sépare les termes en $z'_i$ et $z_i$ par l'inégalité triangulaire (ou sous-additivité du sup, $\sup(A+B) \le \sup(A) + \sup(B)$) :
   $$ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n \sigma_i \left( f(z'_i) - f(z_i) \right) \le \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n \sigma_i f(z'_i) + \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n (-\sigma_i) f(z_i) $$
   En prenant l'espérance sur $(S, S', \boldsymbol{\sigma})$ de cette inégalité, et en remarquant que $\sigma_i$ et $-\sigma_i$ ont la même distribution (et de même pour $z'_i$ et $z_i$), les deux termes yield la même valeur de Rademacher.
   $$ \mathbb{E}_{S, S', \boldsymbol{\sigma}} \left[ \dots \right] \le \mathbb{E}_{S', \boldsymbol{\sigma}} \left[ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n \sigma_i f(z'_i) \right] + \mathbb{E}_{S, \boldsymbol{\sigma}} \left[ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n (-\sigma_i) f(z_i) \right] $$
   $$ \dots = \mathfrak{R}_n(\mathcal{F}) + \mathfrak{R}_n(\mathcal{F}) = 2 \mathfrak{R}_n(\mathcal{F}) $$

6. **Conclusion :**
   Nous venons de prouver rigoureusement le Lemme de Symétrisation :
   $$ \mathbb{E}_{S} \left[ \sup_{f \in \mathcal{F}} \left( \mathbb{E}[f] - \hat{\mathbb{E}}_S[f] \right) \right] \le 2 \mathfrak{R}_n(\mathcal{F}) $$
   La suite de la démonstration du Théorème de Généralisation (pour la borne avec probabilité au moins $1-\delta$) consiste à appliquer l'inégalité de concentration de McDiarmid (qui sera détaillée dans le [[Jalon 138 (Inegalites de concentration avancees)]]) à la variable aléatoire $\Phi(S)$, ce qui produit le terme en $\sqrt{\frac{\ln(1/\delta)}{2n}}$.

## 4. Exercices d'Application

### Exercice 1 : Application Directe (Complexité de Rademacher d'un singleton)
**Énoncé :** Soit une famille de fonctions $\mathcal{F} = \{f_0\}$ constituée d'une unique fonction $f_0 : \mathcal{X} \to \mathbb{R}$. Calculer la complexité de Rademacher $\mathfrak{R}_n(\mathcal{F})$.

**Correction Détaillée :**
* *Analyse de l'énoncé :* La famille $\mathcal{F}$ ne contient qu'une seule fonction. L'opérateur supremum $\sup_{f \in \mathcal{F}}$ devient donc une simple évaluation en $f_0$.
* *Résolution pas-à-pas :*
  Par définition de la complexité empirique :
  $$ \hat{\mathfrak{R}}_S(\mathcal{F}) = \mathbb{E}_{\boldsymbol{\sigma}} \left[ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n \sigma_i f(x_i) \right] $$
  Comme $\mathcal{F} = \{f_0\}$, le supremum est atteint trivialement pour $f_0$ :
  $$ \hat{\mathfrak{R}}_S(\{f_0\}) = \mathbb{E}_{\boldsymbol{\sigma}} \left[ \frac{1}{n} \sum_{i=1}^n \sigma_i f_0(x_i) \right] $$
  Par linéarité de l'espérance mathématique :
  $$ \dots = \frac{1}{n} \sum_{i=1}^n \mathbb{E}_{\boldsymbol{\sigma}} \left[ \sigma_i f_0(x_i) \right] $$
  Pour un échantillon fixe $S$, $f_0(x_i)$ est une constante déterministe. Ainsi :
  $$ \mathbb{E}_{\boldsymbol{\sigma}} \left[ \sigma_i f_0(x_i) \right] = f_0(x_i) \mathbb{E}_{\sigma_i}[\sigma_i] $$
  Or, par définition de la variable de Rademacher, $\mathbb{E}_{\sigma_i}[\sigma_i] = (+1)\frac{1}{2} + (-1)\frac{1}{2} = 0$.
  Par conséquent :
  $$ \hat{\mathfrak{R}}_S(\{f_0\}) = \frac{1}{n} \sum_{i=1}^n (f_0(x_i) \times 0) = 0 $$
  Enfin, en prenant l'espérance sur $S \sim \mathcal{D}^n$ :
  $$ \mathfrak{R}_n(\{f_0\}) = \mathbb{E}_S[0] = 0 $$
  Une famille ne contenant qu'une seule fonction n'a aucune capacité d'adaptation à du bruit aléatoire.

### Exercice 2 : Niveau Avancé (Inspiré Concours X / ENS / MIT - Borne de Massart)
**Énoncé :** Soit $A$ un ensemble fini de vecteurs dans $\mathbb{R}^n$. Soit $R = \max_{a \in A} \|a\|_2$.
Montrer que la complexité de Rademacher de l'ensemble $A$ (vue comme classe de fonctions linéaires évaluées sur la base canonique) vérifie la borne de Massart :
$$ \mathbb{E}_{\boldsymbol{\sigma}} \left[ \sup_{a \in A} \sum_{i=1}^n \sigma_i a_i \right] \le R \sqrt{2 \ln |A|} $$

**Correction Détaillée :**
* *Analyse de l'énoncé :* Il s'agit du célèbre lemme de Massart sur un ensemble fini (hypothèses de cardinalité finie). La technique standard pour isoler le supremum sur un ensemble discret est d'utiliser la fonction exponentielle (technique de type borne de Chernoff / borne de l'union continue).
* *Résolution pas-à-pas :*
  Soit $\lambda > 0$ un paramètre réel à optimiser ultérieurement. Par convexité et stricte croissance de la fonction exponentielle $x \mapsto \exp(\lambda x)$, on a pour tout sous-ensemble $A$ :
  $$ \exp \left( \lambda \mathbb{E}_{\boldsymbol{\sigma}} \left[ \sup_{a \in A} \sum_{i=1}^n \sigma_i a_i \right] \right) \le \mathbb{E}_{\boldsymbol{\sigma}} \left[ \exp \left( \lambda \sup_{a \in A} \sum_{i=1}^n \sigma_i a_i \right) \right] $$
  (Il s'agit de l'inégalité de Jensen appliquée à l'espérance).
  On peut intervertir le sup et l'exponentielle, et le supremum sur $A$ est trivialement majoré par la somme sur $A$ (puisque l'exponentielle est positive) :
  $$ \dots = \mathbb{E}_{\boldsymbol{\sigma}} \left[ \sup_{a \in A} \exp \left( \lambda \sum_{i=1}^n \sigma_i a_i \right) \right] \le \mathbb{E}_{\boldsymbol{\sigma}} \left[ \sum_{a \in A} \exp \left( \lambda \sum_{i=1}^n \sigma_i a_i \right) \right] $$
  Par linéarité de l'espérance et indépendance des $\sigma_i$ :
  $$ \mathbb{E}_{\boldsymbol{\sigma}} \left[ \sum_{a \in A} \exp \left( \sum_{i=1}^n \lambda \sigma_i a_i \right) \right] = \sum_{a \in A} \mathbb{E}_{\boldsymbol{\sigma}} \left[ \prod_{i=1}^n \exp(\lambda \sigma_i a_i) \right] = \sum_{a \in A} \prod_{i=1}^n \mathbb{E}_{\sigma_i} \left[ \exp(\lambda \sigma_i a_i) \right] $$
  Rappelons que $\sigma_i \in \{-1, 1\}$. Ainsi, $\mathbb{E}_{\sigma_i} [\exp(\lambda \sigma_i a_i)] = \frac{\exp(\lambda a_i) + \exp(-\lambda a_i)}{2} = \cosh(\lambda a_i)$.
  On utilise l'inégalité fondamentale $\cosh(x) \le \exp(x^2 / 2)$ (valide pour tout réel $x$) :
  $$ \mathbb{E}_{\sigma_i} \left[ \exp(\lambda \sigma_i a_i) \right] \le \exp\left( \frac{\lambda^2 a_i^2}{2} \right) $$
  On remplace dans le produit :
  $$ \prod_{i=1}^n \mathbb{E}_{\sigma_i} \left[ \exp(\lambda \sigma_i a_i) \right] \le \prod_{i=1}^n \exp\left( \frac{\lambda^2 a_i^2}{2} \right) = \exp\left( \sum_{i=1}^n \frac{\lambda^2 a_i^2}{2} \right) = \exp\left( \frac{\lambda^2 \|a\|_2^2}{2} \right) $$
  Puisque par définition $\|a\|_2 \le R$ pour tout $a \in A$, on a :
  $$ \dots \le \exp\left( \frac{\lambda^2 R^2}{2} \right) $$
  En sommant sur les éléments de $A$ :
  $$ \sum_{a \in A} \prod_{i=1}^n \mathbb{E}_{\sigma_i} \left[ \exp(\lambda \sigma_i a_i) \right] \le \sum_{a \in A} \exp\left( \frac{\lambda^2 R^2}{2} \right) = |A| \exp\left( \frac{\lambda^2 R^2}{2} \right) $$
  Ainsi, en revenant à la première inégalité :
  $$ \exp \left( \lambda \mathbb{E}_{\boldsymbol{\sigma}} \left[ \sup_{a \in A} \sum_{i=1}^n \sigma_i a_i \right] \right) \le |A| \exp\left( \frac{\lambda^2 R^2}{2} \right) $$
  On prend le logarithme népérien de chaque côté (qui respecte l'ordre car strictement croissante) et on divise par $\lambda$ (avec $\lambda > 0$) :
  $$ \lambda \mathbb{E}_{\boldsymbol{\sigma}} \left[ \sup_{a \in A} \sum_{i=1}^n \sigma_i a_i \right] \le \ln |A| + \frac{\lambda^2 R^2}{2} $$
  $$ \mathbb{E}_{\boldsymbol{\sigma}} \left[ \sup_{a \in A} \sum_{i=1}^n \sigma_i a_i \right] \le \frac{\ln |A|}{\lambda} + \frac{\lambda R^2}{2} $$
  Il reste à minimiser la borne droite par rapport au paramètre de Chernoff $\lambda > 0$. Soit $g(\lambda) = \frac{\ln |A|}{\lambda} + \frac{\lambda R^2}{2}$.
  La dérivée est $g'(\lambda) = - \frac{\ln |A|}{\lambda^2} + \frac{R^2}{2}$. En l'annulant :
  $$ \frac{R^2}{2} = \frac{\ln |A|}{\lambda^2} \implies \lambda^2 = \frac{2 \ln |A|}{R^2} \implies \lambda^* = \frac{\sqrt{2 \ln |A|}}{R} $$
  (On note que $|A| \ge 1$ et on suppose $|A| > 1$ pour avoir une borne non-triviale, garantissant $\lambda^* > 0$).
  En injectant ce minimum global $\lambda^*$ :
  $$ \frac{\ln |A|}{\lambda^*} + \frac{\lambda^* R^2}{2} = \frac{R \ln |A|}{\sqrt{2 \ln |A|}} + \frac{R \sqrt{2 \ln |A|}}{2} = \frac{R \sqrt{2 \ln |A|} \sqrt{2 \ln |A|}}{2 \sqrt{2 \ln |A|}} + \dots $$
  $$ = \frac{R}{\sqrt{2}} \sqrt{\ln |A|} + \frac{R}{\sqrt{2}} \sqrt{\ln |A|} = R \sqrt{2 \ln |A|} $$
  La borne de Massart est donc rigoureusement démontrée :
  $$ \mathbb{E}_{\boldsymbol{\sigma}} \left[ \sup_{a \in A} \sum_{i=1}^n \sigma_i a_i \right] \le R \sqrt{2 \ln |A|} $$

## 5. Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*

- **Le Pont Théorique :** Dans la construction formelle de l'apprentissage automatique, il est insuffisant de juste minimiser l'erreur d'un réseau de neurones sur un jeu de données (le risque empirique). Il faut des garanties solides affirmant que cette erreur est une bonne approximation de l'erreur réelle en production (le risque général). La complexité de Rademacher est l'outil mathématique moderne par excellence (préféré souvent à la dimension de Vapnik-Chervonenkis pour les réseaux récents car elle est dépendante des données et permet des bornes plus fines) pour prouver qu'une famille d'architectures (ex: "Tous les réseaux MLP à 3 couches avec activation ReLU et régularisation $L_2$ bornée") ne va pas sur-apprendre de manière catastrophique.
- **Exemple Concret :** Dans l'étude théorique moderne du Deep Learning (comme les réseaux de neurones profonds ou les SVM), les chercheurs utilisent des bornes de Rademacher pour prouver la convergence. Par exemple, grâce à la régularisation explicite du produit scalaire des matrices de poids (norme de Frobenius ou spectrale dans un mécanisme de Weight Decay), on peut encadrer la complexité de Rademacher de la famille des réseaux réalisables à la valeur $O(1/\sqrt{n})$. Ce résultat justifie théoriquement la descente de gradient stochastique : en pénalisant les poids avec un mécanisme Ridge ($L_2$), on limite artificiellement la complexité de Rademacher $\mathfrak{R}_n(\mathcal{F})$ de notre réseau, restreignant sa capacité d'adaptation au bruit, le forçant ainsi à converger vers une représentation généralisable de la structure intrinsèque des données.

## 6. Liens Sémantiques
- **Concepts Précédents requis :** [[Jalon 133 (Modele PAC)]], [[Jalon 134 (Complexite des classes de fonctions)]]
- **Concepts Futurs dépendants :** [[Jalon 136 (Theorie de Vapnik-Chervonenkis)]], [[Jalon 137 (Preuve des bornes de generalisation universelles de Vapnik via la dimension VC)]]

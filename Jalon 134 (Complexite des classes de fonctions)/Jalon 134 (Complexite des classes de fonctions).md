---
uuid: "jalon-134"
title: "Complexité des classes de fonctions"
year: 3
trimester: 12
tags:
  - math/probabilites
  - math/statistiques
  - ia/machine_learning
prev: "[[Jalon 133 (Modele PAC).md]]"
next: "[[Jalon 135 (Complexite de Rademacher).md]]"
---

# Complexité des classes de fonctions et Processus Empiriques

## 1. L'Intuition Première (Niveau 12 ans)
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Imagine que tu sois un détective cherchant à identifier un suspect parmi une foule immense, uniquement à l'aide d'un portrait-robot approximatif (tes données). Si tu as très peu de suspects possibles (comme dans un petit village), il est facile de trouver la bonne personne sans te tromper, même si le portrait est flou. En revanche, si tu cherches dans une métropole gigantesque et que ton "catalogue" de visages possibles est infini et extrêmement varié, il y a un risque énorme que tu arrêtes un innocent qui ressemble au portrait par pur hasard. En apprentissage automatique, la "foule de visages" correspond à notre "classe de fonctions" (les différents modèles possibles). La "complexité de la classe de fonctions" mesure à quel point ce catalogue est vaste et détaillé. Plus il est complexe, plus il est probable de trouver un modèle qui colle parfaitement aux données d'entraînement par accident, sans pour autant comprendre la vraie règle.
- **Le "Pourquoi on a inventé ça" :** Le Modèle PAC (que nous avons vu précédemment) nous dit qu'on peut apprendre si on a assez de données. Mais combien de données exactement ? Cela dépend de la puissance de notre modèle. Si notre modèle est trop puissant (par exemple, une courbe qui peut se tordre dans tous les sens pour relier tous les points), il fera du "sur-apprentissage" (overfitting). Les mathématiciens ont donc dû créer des outils de mesure pour quantifier exactement la "taille" ou la "richesse" d'un ensemble de modèles, afin de garantir qu'ils apprendront vraiment au lieu d'apprendre par cœur.
- **Visualisation :** Imagine un nuage de points sur une feuille. Si tu n'as le droit d'utiliser que des lignes droites (faible complexité), tu ne pourras séparer parfaitement les points que dans des cas simples. Si tu as le droit d'utiliser n'importe quelle courbe ondulée (haute complexité), tu pourras toujours séparer tous les points, même s'ils sont placés au hasard. La complexité mesure le degré de "souplesse" de la ligne que tu es autorisé à tracer.

## 2. Formalisation & Rigueur Académique
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soit $\mathcal{Z} = \mathcal{X} \times \mathcal{Y}$ l'espace des observations, où $\mathcal{X}$ est l'espace des caractéristiques (souvent un borélien de $\mathbb{R}^d$) et $\mathcal{Y}$ l'espace des étiquettes (par exemple $\{-1, 1\}$ pour la classification binaire). Soit $P$ une mesure de probabilité inconnue sur l'espace mesurable $(\mathcal{Z}, \mathcal{B}(\mathcal{Z}))$.
On dispose d'un $n$-échantillon $S_n = (Z_1, \dots, Z_n)$ composé de variables aléatoires indépendantes et identiquement distribuées selon $P$.

Soit $\mathcal{F}$ une classe de fonctions de perte $f : \mathcal{Z} \to \mathbb{R}$. Par exemple, $f(z) = \ell(h(x), y)$ où $h \in \mathcal{H}$ est une hypothèse et $\ell$ une fonction de coût.

> **Définition (Processus Empirique) :**
> L'espérance théorique (ou risque réel) d'une fonction $f \in \mathcal{F}$ est définie par $P f = \mathbb{E}_{Z \sim P}[f(Z)] = \int_{\mathcal{Z}} f(z) dP(z)$.
> La mesure empirique associée à l'échantillon $S_n$ est $P_n = \frac{1}{n} \sum_{i=1}^n \delta_{Z_i}$. L'espérance empirique (ou risque empirique) est donc $P_n f = \frac{1}{n} \sum_{i=1}^n f(Z_i)$.
> Le *processus empirique* indéxé par la classe $\mathcal{F}$ est la famille de variables aléatoires :
> $\left( \sqrt{n} (P_n f - P f) \right)_{f \in \mathcal{F}}$

Pour garantir la généralisation d'un algorithme d'apprentissage minimisant le risque empirique (ERM), nous devons contrôler le supremum du processus empirique :
$$ \sup_{f \in \mathcal{F}} (P f - P_n f) $$
ou de manière bilatérale :
$$ \sup_{f \in \mathcal{F}} |P_n f - P f| $$

> **Définition (Couverture et Nombres de Couverture / Covering Numbers) :**
> Soit $(M, d)$ un espace métrique. Pour un rayon $\epsilon > 0$, un sous-ensemble $C \subset M$ est un $\epsilon$-réseau de $M$ si pour tout $x \in M$, il existe $c \in C$ tel que $d(x, c) \leq \epsilon$.
> Le *nombre de couverture* $\mathcal{N}(\epsilon, M, d)$ est le cardinal minimal d'un $\epsilon$-réseau de $M$.

Appliquons cela à notre classe de fonctions $\mathcal{F}$. Pour une réalisation donnée $Z_1=z_1, \dots, Z_n=z_n$, nous munissons $\mathcal{F}$ de la pseudo-métrique empirique $\mathcal{L}_p$ :
$$ d_{L_p(P_n)}(f, g) = \left( \frac{1}{n} \sum_{i=1}^n |f(z_i) - g(z_i)|^p \right)^{1/p} $$
Le nombre de couverture empirique est noté $\mathcal{N}(\epsilon, \mathcal{F}, d_{L_1(P_n)})$.

### B. Théorèmes, Propositions & Lemmes

> **Théorème (Inégalité de symétrisation fondamentale) :**
> Soient $(Z_1, \dots, Z_n)$ des variables aléatoires i.i.d. selon $P$. Soient $(Z_1', \dots, Z_n')$ des copies indépendantes (échantillon fantôme). Soient $(\sigma_1, \dots, \sigma_n)$ des variables de Rademacher (i.e. $\mathbb{P}(\sigma_i = 1) = \mathbb{P}(\sigma_i = -1) = 1/2$), indépendantes des $Z_i$ et des $Z_i'$.
> Sous des hypothèses de mesurabilité sur la classe $\mathcal{F}$, nous avons :
> $$ \mathbb{E}\left[ \sup_{f \in \mathcal{F}} (P f - P_n f) \right] \leq 2 \mathbb{E}\left[ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n \sigma_i f(Z_i) \right] $$

> **Lemme (Lemme de Hoeffding étendu / Inégalité de Massart pour les ensembles finis) :**
> Soit $A \subset \mathbb{R}^n$ un ensemble fini de vecteurs $a = (a_1, \dots, a_n)$. Soit $R = \sup_{a \in A} \|a\|_2 = \sup_{a \in A} \left( \sum_{i=1}^n a_i^2 \right)^{1/2}$. Soit $\sigma = (\sigma_1, \dots, \sigma_n)$ un vecteur de variables de Rademacher indépendantes. Alors :
> $$ \mathbb{E} \left[ \sup_{a \in A} \sum_{i=1}^n \sigma_i a_i \right] \leq R \sqrt{2 \ln(|A|)} $$

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème : Inégalité de symétrisation fondamentale

1. **Initialisation / Cadre :**
L'objectif est de borner l'espérance de l'écart maximal entre le risque réel et le risque empirique. Le risque réel $P f$ peut s'écrire comme l'espérance du risque empirique évalué sur un échantillon indépendant $Z' = (Z_1', \dots, Z_n')$, appelé "échantillon fantôme".
Ainsi, pour toute fonction $f \in \mathcal{F}$ :
$$ P f = \mathbb{E}_{Z'} [P_n' f] = \mathbb{E}_{Z'} \left[ \frac{1}{n} \sum_{i=1}^n f(Z_i') \right] $$

2. **Étape 1 : Introduction de l'échantillon fantôme**
Considérons la quantité $\mathbb{E}_Z \left[ \sup_{f \in \mathcal{F}} (P f - P_n f) \right]$. En remplaçant $Pf$ par son expression intégrale :
$$ \mathbb{E}_Z \left[ \sup_{f \in \mathcal{F}} (P f - P_n f) \right] = \mathbb{E}_Z \left[ \sup_{f \in \mathcal{F}} \left( \mathbb{E}_{Z'} \left[ \frac{1}{n} \sum_{i=1}^n f(Z_i') \right] - \frac{1}{n} \sum_{i=1}^n f(Z_i) \right) \right] $$

Puisque le supremum d'une espérance est inférieur ou égal à l'espérance du supremum (conséquence de l'inégalité de Jensen pour la fonction convexe supremum), on peut rentrer l'espérance par rapport à $Z'$ à l'intérieur du supremum :
$$ \mathbb{E}_Z \left[ \sup_{f \in \mathcal{F}} \left( \mathbb{E}_{Z'} \left[ \frac{1}{n} \sum_{i=1}^n (f(Z_i') - f(Z_i)) \right] \right) \right] \leq \mathbb{E}_Z \left[ \mathbb{E}_{Z'} \left[ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n (f(Z_i') - f(Z_i)) \right] \right] $$

Grâce au théorème de Fubini-Tonelli, l'espérance emboîtée est équivalente à l'espérance jointe sur $(Z, Z')$ :
$$ \mathbb{E}_{Z, Z'} \left[ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n (f(Z_i') - f(Z_i)) \right] $$

3. **Étape 2 (Symétrisation par Rademacher) :**
Pour tout indice $i \in \{1, \dots, n\}$, les variables $Z_i$ et $Z_i'$ sont indépendantes et de même loi $P$. Par conséquent, la variable aléatoire symétrique $(f(Z_i') - f(Z_i))$ a la même distribution que $-(f(Z_i') - f(Z_i))$, c'est-à-dire $(f(Z_i) - f(Z_i'))$.
Introduisons des variables aléatoires $\sigma_i \in \{-1, 1\}$, de loi de Rademacher ($\mathbb{P}(\sigma_i=1)=1/2$, $\mathbb{P}(\sigma_i=-1)=1/2$), indépendantes de $Z$ et $Z'$ et indépendantes entre elles.
Multiplier $(f(Z_i') - f(Z_i))$ par $\sigma_i$ ne modifie en rien la distribution jointe du processus.
Ainsi :
$$ \mathbb{E}_{Z, Z'} \left[ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n (f(Z_i') - f(Z_i)) \right] = \mathbb{E}_{Z, Z', \sigma} \left[ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n \sigma_i (f(Z_i') - f(Z_i)) \right] $$

4. **Étape 3 (Séparation par inégalité triangulaire) :**
La fonction supremum vérifie la sous-additivité : $\sup(A+B) \leq \sup(A) + \sup(B)$.
En appliquant cette propriété :
$$ \sup_{f \in \mathcal{F}} \left( \frac{1}{n} \sum_{i=1}^n \sigma_i f(Z_i') - \frac{1}{n} \sum_{i=1}^n \sigma_i f(Z_i) \right) \leq \sup_{f \in \mathcal{F}} \left( \frac{1}{n} \sum_{i=1}^n \sigma_i f(Z_i') \right) + \sup_{f \in \mathcal{F}} \left( \frac{1}{n} \sum_{i=1}^n (-\sigma_i) f(Z_i) \right) $$

Prenons l'espérance de l'ensemble :
$$ \mathbb{E}_{Z, Z', \sigma} \left[ \dots \right] \leq \mathbb{E}_{Z', \sigma} \left[ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n \sigma_i f(Z_i') \right] + \mathbb{E}_{Z, \sigma} \left[ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n (-\sigma_i) f(Z_i) \right] $$

Or, les variables $\sigma_i$ et $-\sigma_i$ ont rigoureusement la même distribution de probabilité. De plus, $Z$ et $Z'$ sont i.i.d. de même loi $P$. Donc, les deux termes de droite sont identiques :
$$ \mathbb{E}_{Z', \sigma} \left[ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n \sigma_i f(Z_i') \right] = \mathbb{E}_{Z, \sigma} \left[ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n \sigma_i f(Z_i) \right] $$

5. **Conclusion :**
En sommant ces deux termes égaux, on aboutit à la majoration finale :
$$ \mathbb{E}_Z \left[ \sup_{f \in \mathcal{F}} (P f - P_n f) \right] \leq 2 \mathbb{E}_{Z, \sigma} \left[ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n \sigma_i f(Z_i) \right] $$
Ce qui clôture la démonstration. Le terme de droite est précisément proportionnel à la *Complexité de Rademacher* de la classe de fonctions $\mathcal{F}$, qui fera l'objet du jalon suivant.

## 4. Exercices d'Application & Pratique de Concours
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Application Directe de l'Inégalité de Massart
**Énoncé :**
Soit $A \subset \mathbb{R}^n$ un ensemble de cardinal fini $N = |A|$. On suppose que pour tout $a = (a_1, \dots, a_n) \in A$, on a la borne déterministe sur la norme euclidienne $\|a\|_2 = \sqrt{\sum_{i=1}^n a_i^2} \leq R$.
Soient $\sigma_1, \dots, \sigma_n$ des variables aléatoires indépendantes de Rademacher.
En utilisant le fait que pour tout $\lambda > 0$ et tout vecteur fixe $a$, la transformée de Laplace vérifie $\mathbb{E}[e^{\lambda \sum_{i=1}^n \sigma_i a_i}] \leq e^{\lambda^2 \|a\|_2^2 / 2}$, démontrez l'inégalité de Massart :
$$ \mathbb{E} \left[ \sup_{a \in A} \sum_{i=1}^n \sigma_i a_i \right] \leq R \sqrt{2 \ln(N)} $$

**Correction Détaillée :**
* *Analyse de l'énoncé :* La difficulté principale réside dans le passage du supremum à l'intérieur de l'espérance, qui n'est pas linéaire. L'astuce classique consiste à exponentier la quantité à borner, puis à utiliser l'inégalité de Jensen et la borne sur la transformée de Laplace des sommes de variables sous-gaussiennes.
* *Résolution pas-à-pas :*
Soit $\lambda > 0$ un paramètre réel à optimiser ultérieurement. Soit $Z = \sup_{a \in A} \sum_{i=1}^n \sigma_i a_i$.
Par monotonie de la fonction exponentielle $x \mapsto e^{\lambda x}$, on a :
$$ \exp(\lambda Z) = \exp\left( \lambda \sup_{a \in A} \sum_{i=1}^n \sigma_i a_i \right) = \sup_{a \in A} \exp\left( \lambda \sum_{i=1}^n \sigma_i a_i \right) $$

Puisque le supremum sur un ensemble fini est toujours inférieur ou égal à la somme de tous les éléments, on a :
$$ \sup_{a \in A} \exp\left( \lambda \sum_{i=1}^n \sigma_i a_i \right) \leq \sum_{a \in A} \exp\left( \lambda \sum_{i=1}^n \sigma_i a_i \right) $$

Prenons l'espérance de cette inégalité. Par linéarité de l'espérance :
$$ \mathbb{E} [\exp(\lambda Z)] \leq \mathbb{E} \left[ \sum_{a \in A} \exp\left( \lambda \sum_{i=1}^n \sigma_i a_i \right) \right] = \sum_{a \in A} \mathbb{E} \left[ \exp\left( \lambda \sum_{i=1}^n \sigma_i a_i \right) \right] $$

L'énoncé nous donne la borne de la transformée de Laplace (issue du lemme de Hoeffding) pour un vecteur $a$ fixe :
$$ \mathbb{E} \left[ \exp\left( \lambda \sum_{i=1}^n \sigma_i a_i \right) \right] \leq \exp\left( \frac{\lambda^2 \|a\|_2^2}{2} \right) $$

Puisque pour tout $a \in A$, on sait que $\|a\|_2 \leq R$, on obtient :
$$ \exp\left( \frac{\lambda^2 \|a\|_2^2}{2} \right) \leq \exp\left( \frac{\lambda^2 R^2}{2} \right) $$

En injectant cette borne uniforme dans la somme :
$$ \mathbb{E} [\exp(\lambda Z)] \leq \sum_{a \in A} \exp\left( \frac{\lambda^2 R^2}{2} \right) = |A| \exp\left( \frac{\lambda^2 R^2}{2} \right) = N \exp\left( \frac{\lambda^2 R^2}{2} \right) $$

Maintenant, appliquons l'inégalité de Jensen à la fonction convexe $x \mapsto \exp(\lambda x)$. Elle garantit que $\exp(\lambda \mathbb{E}[Z]) \leq \mathbb{E}[\exp(\lambda Z)]$.
Ainsi :
$$ \exp(\lambda \mathbb{E}[Z]) \leq N \exp\left( \frac{\lambda^2 R^2}{2} \right) $$

Prenons le logarithme népérien des deux côtés, ce qui préserve l'inégalité car $\ln$ est strictement croissante :
$$ \lambda \mathbb{E}[Z] \leq \ln(N) + \frac{\lambda^2 R^2}{2} $$

Divisons par $\lambda$ (rappel : $\lambda > 0$) :
$$ \mathbb{E}[Z] \leq \frac{\ln(N)}{\lambda} + \frac{\lambda R^2}{2} $$

Cette inégalité est vraie pour tout $\lambda > 0$. Pour obtenir la meilleure borne, nous minimisons le membre de droite par rapport à $\lambda$. Posons $g(\lambda) = \frac{\ln(N)}{\lambda} + \frac{\lambda R^2}{2}$.
Calculons la dérivée :
$$ g'(\lambda) = -\frac{\ln(N)}{\lambda^2} + \frac{R^2}{2} $$
La dérivée s'annule lorsque :
$$ \frac{R^2}{2} = \frac{\ln(N)}{\lambda^2} \iff \lambda^2 = \frac{2 \ln(N)}{R^2} \iff \lambda = \frac{\sqrt{2 \ln(N)}}{R} $$

Remplaçons cette valeur optimale de $\lambda$ dans notre majoration :
$$ \mathbb{E}[Z] \leq \frac{\ln(N)}{\frac{\sqrt{2 \ln(N)}}{R}} + \frac{\frac{\sqrt{2 \ln(N)}}{R} R^2}{2} $$
$$ \mathbb{E}[Z] \leq \frac{R \ln(N)}{\sqrt{2 \ln(N)}} + \frac{R \sqrt{2 \ln(N)}}{2} $$
$$ \mathbb{E}[Z] \leq R \sqrt{\frac{\ln(N)}{2}} + R \sqrt{\frac{\ln(N)}{2}} = 2 R \sqrt{\frac{\ln(N)}{2}} = R \sqrt{2 \ln(N)} $$

Ce qui donne exactement le résultat voulu.

### Exercice 2 : Niveau Avancé (Inspiré Concours ENS) - Borne sur une classe finie
**Énoncé :**
Soit $\mathcal{F}$ une classe finie de fonctions $f : \mathcal{X} \to [-M, M]$ avec $|\mathcal{F}| = K$. Soient $Z_1, \dots, Z_n$ des variables aléatoires i.i.d.
En combinant le théorème de symétrisation et l'inégalité de Massart, démontrez que :
$$ \mathbb{E} \left[ \sup_{f \in \mathcal{F}} (P f - P_n f) \right] \leq 2 M \sqrt{\frac{2 \ln(K)}{n}} $$

**Correction Détaillée :**
* *Analyse de l'énoncé :* On doit relier le problème continu d'évaluation de fonctions sur des variables aléatoires au problème discret résolu par Massart conditionnellement aux données.
* *Résolution pas-à-pas :*
1. **Application de la Symétrisation :**
D'après le théorème de symétrisation fondamentale démontré dans le cours, on a :
$$ \mathbb{E}_Z \left[ \sup_{f \in \mathcal{F}} (P f - P_n f) \right] \leq 2 \mathbb{E}_{Z, \sigma} \left[ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n \sigma_i f(Z_i) \right] $$

2. **Conditionnement par rapport à l'échantillon $Z$ :**
Écrivons l'espérance par rapport aux variables indépendantes sous forme itérée :
$$ \mathbb{E}_{Z, \sigma} \left[ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n \sigma_i f(Z_i) \right] = \mathbb{E}_Z \left[ \mathbb{E}_\sigma \left[ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n \sigma_i f(Z_i) \Bigg| Z \right] \right] $$

Fixons une réalisation de l'échantillon $Z = z = (z_1, \dots, z_n)$. Conditionnellement à $z$, les valeurs $f(z_i)$ sont des constantes déterministes.
Considérons l'ensemble des vecteurs dans $\mathbb{R}^n$ définis par l'évaluation des fonctions de $\mathcal{F}$ sur l'échantillon :
$$ A(z) = \left\{ \frac{1}{n} (f(z_1), \dots, f(z_n)) : f \in \mathcal{F} \right\} $$

3. **Application de l'Inégalité de Massart :**
Pour un vecteur $a \in A(z)$ correspondant à une fonction $f$, sa norme euclidienne est :
$$ \|a\|_2 = \sqrt{ \sum_{i=1}^n a_i^2 } = \sqrt{ \sum_{i=1}^n \left( \frac{f(z_i)}{n} \right)^2 } = \frac{1}{n} \sqrt{ \sum_{i=1}^n f(z_i)^2 } $$
Puisque chaque fonction $f$ prend ses valeurs dans l'intervalle $[-M, M]$, on a pour tout $i$, $f(z_i)^2 \leq M^2$.
Donc, la somme est majorée :
$$ \sum_{i=1}^n f(z_i)^2 \leq \sum_{i=1}^n M^2 = n M^2 $$
Et ainsi, la norme de tout vecteur $a \in A(z)$ est bornée par :
$$ \|a\|_2 \leq \frac{1}{n} \sqrt{n M^2} = \frac{M}{\sqrt{n}} = R $$

Le cardinal de $A(z)$ est au plus le cardinal de $\mathcal{F}$, soit $|A(z)| \leq K$.
Appliquons l'inégalité de Massart (démontrée dans l'Exercice 1) sur cet ensemble $A(z)$ conditionnellement à $z$ :
$$ \mathbb{E}_\sigma \left[ \sup_{a \in A(z)} \sum_{i=1}^n \sigma_i a_i \right] \leq R \sqrt{2 \ln(|A(z)|)} \leq \frac{M}{\sqrt{n}} \sqrt{2 \ln(K)} = M \sqrt{ \frac{2 \ln(K)}{n} } $$

4. **Conclusion :**
Cette majoration dépend de $M$, $K$ et $n$, mais elle est *indépendante* de la réalisation spécifique $z$ de l'échantillon $Z$.
Par conséquent, en réintégrant par rapport à $Z$ :
$$ \mathbb{E}_Z \left[ \mathbb{E}_\sigma \left[ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n \sigma_i f(Z_i) \Bigg| Z \right] \right] \leq \mathbb{E}_Z \left[ M \sqrt{ \frac{2 \ln(K)}{n} } \right] = M \sqrt{ \frac{2 \ln(K)}{n} } $$
Et en reprenant le facteur 2 issu de la symétrisation :
$$ \mathbb{E} \left[ \sup_{f \in \mathcal{F}} (P f - P_n f) \right] \leq 2 M \sqrt{ \frac{2 \ln(K)}{n} } $$
Ce résultat est un premier jalon crucial en théorie de l'apprentissage statistique pour prouver la consistance d'un classifieur sur une classe de complexité finie.

## 5. Ancrage & Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*

- **Le Pont Théorique :** En deep learning et en machine learning moderne, la "classe de fonctions" $\mathcal{F}$ représente l'architecture du réseau de neurones (par exemple, tous les réseaux ResNet-50 possibles selon les poids choisis). L'étude des processus empiriques et la borne via symétrisation sont les pierres angulaires pour garantir que si l'erreur d'entraînement (risque empirique) d'un modèle baisse, son erreur de test (risque réel) baissera également. Si la classe de fonctions est trop complexe (capacité démesurée), le terme de droite explose, indiquant une perte totale de garantie de généralisation.
- **Exemple Concret :** Lors de l'entraînement d'un classifieur SVM (Machine à Vecteurs de Support), ou lors de la définition d'un espace de recherche pour une forêt aléatoire, les data scientists emploient des méthodes de "régularisation" (comme la pénalité L1 ou L2). Mathématiquement, régulariser l'optimisation revient directement à contraindre l'espace des paramètres, et donc à diminuer artificiellement le nombre de couverture $\mathcal{N}(\epsilon, \mathcal{F}, d_{L_1(P_n)})$ de la classe. Moins de couverture équivaut à un supremum de processus empirique plus faible, empêchant ainsi l'overfitting.

## 6. Liens Sémantiques & Maillage Obsidian
- **Concepts Précédents requis :** [[Jalon 133 (Modele PAC)]], [[Jalon 91 (Inegalites de concentration)]]
- **Concepts Futurs dépendants :** [[Jalon 135 (Complexite de Rademacher)]], [[Jalon 136 (Theorie de Vapnik-Chervonenkis)]]

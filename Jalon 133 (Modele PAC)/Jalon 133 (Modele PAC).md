---
uuid: "jalon-133"
title: "Modèle PAC"
year: 3
trimester: 12
tags:
  - math/probabilites
  - ia/apprentissage_statistique
prev: "[[Jalon 132 (Livrable IA).md]]"
next: "[[Jalon 134 (Complexite des classes de fonctions).md]]"
---

# Modèle PAC (Probably Approximately Correct)

## 1. L'Intuition Première (Niveau 12 ans)
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Imagine que tu sois un goûteur dont le métier est de dire si une pomme est bonne (délicieuse) ou mauvaise (pourrie). Tu ne peux pas goûter toutes les pommes du monde. Tu dois te faire un avis ("apprendre" la règle) en ne goûtant qu'un petit panier (ton ensemble d'entraînement). Le modèle PAC, c'est comme une garantie sur un contrat : "Si tu goûtes assez de pommes, il est *très probable* (Probably) que ta règle pour trier les bonnes des mauvaises soit *presque parfaite* (Approximately Correct) sur toutes les pommes futures de ce verger."

- **Le "Pourquoi on a inventé ça" :** Les pionniers de l'Intelligence Artificielle (comme Leslie Valiant) se sont heurtés à un mur conceptuel : comment prouver qu'une machine "apprend" vraiment et ne fait pas juste du par cœur ? Si l'algorithme ne voit qu'une infime partie de la réalité, comment être sûr qu'il ne se trompera pas dramatiquement demain ? Il fallait un cadre mathématique rigoureux pour quantifier le volume de données nécessaire pour garantir la fiabilité d'un algorithme dans le futur.

- **Visualisation :** Imagine un grand sac rempli de millions de billes rouges et bleues. Tu tires une poignée de 100 billes. En fonction des billes de ta main, tu essaies de deviner la proportion de couleurs dans le sac tout entier. Tu peux faire une erreur (Approximately Correct), et il se peut même que par malchance incroyable tu aies tiré uniquement des billes bleues alors que le sac est rouge (c'est le risque d'échec : Probably). Le modèle PAC met en équation la taille de la poignée dont tu as besoin pour limiter ce double risque.

## 2. Formalisation & Rigueur Académique
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soit un espace d'entrée $\mathcal{X}$ (l'espace des instances) et un espace de sortie $\mathcal{Y}$ (l'espace des labels). Dans le cadre de la classification binaire, on fixe $\mathcal{Y} = \{0, 1\}$.
Soit $\mathcal{D}$ une distribution de probabilité inconnue mais fixe sur $\mathcal{X}$.
On suppose l'existence d'une **fonction cible** (target concept) déterministe $c : \mathcal{X} \to \mathcal{Y}$ telle que pour tout $x \in \mathcal{X}$, le label correct est $c(x)$.
Soit $\mathcal{H}$ un ensemble de fonctions $h : \mathcal{X} \to \mathcal{Y}$, appelé **espace d'hypothèses** (hypothesis class).

On dispose d'un **échantillon d'apprentissage** (training sample) de taille $m$, noté $S = (x_1, \dots, x_m)$, où chaque $x_i$ est tiré de manière indépendante et identiquement distribuée (i.i.d.) selon $\mathcal{D}$. L'algorithme d'apprentissage observe $S$ et les labels correspondants $(c(x_1), \dots, c(x_m))$ et retourne une hypothèse $h_S \in \mathcal{H}$.

> **Définition (Risque Réel / Erreur en Généralisation) :**
> Le risque réel (ou erreur de généralisation) d'une hypothèse $h \in \mathcal{H}$ par rapport à la distribution $\mathcal{D}$ et au concept cible $c$ est la probabilité que $h$ se trompe sur une instance tirée selon $\mathcal{D}$ :
> $$ L_{\mathcal{D}, c}(h) = \mathbb{P}_{x \sim \mathcal{D}}[h(x) \neq c(x)] $$

> **Définition (Risque Empirique / Erreur d'Entraînement) :**
> Le risque empirique d'une hypothèse $h$ sur l'échantillon $S$ de taille $m$ est la proportion d'erreurs commises par $h$ sur cet échantillon :
> $$ L_S(h) = \frac{1}{m} \sum_{i=1}^m \mathbb{1}_{\{h(x_i) \neq c(x_i)\}} $$
> où $\mathbb{1}$ est la fonction indicatrice.

> **Définition (PAC Apprenabilité) :**
> Une classe d'hypothèses $\mathcal{H}$ est **PAC-apprenable** (Probably Approximately Correct learnable) s'il existe une fonction $m_{\mathcal{H}} : (0,1)^2 \to \mathbb{N}$ et un algorithme d'apprentissage $\mathcal{A}$ tels que :
> Pour tout $\epsilon > 0$ (paramètre de précision),
> Pour tout $\delta > 0$ (paramètre de confiance),
> Pour toute distribution $\mathcal{D}$ sur $\mathcal{X}$,
> Pour tout concept cible $c \in \mathcal{H}$ (hypothèse du cas réalisable),
> Dès que la taille de l'échantillon $m \geq m_{\mathcal{H}}(\epsilon, \delta)$, l'algorithme $\mathcal{A}$ retourne une hypothèse $h_S$ vérifiant, avec une probabilité d'au moins $1 - \delta$ sur le tirage i.i.d. de l'échantillon $S \sim \mathcal{D}^m$ :
> $$ L_{\mathcal{D}, c}(h_S) \leq \epsilon $$
> La probabilité porte sur les tirages aléatoires de $S$. La fonction $m_{\mathcal{H}}$ est la **complexité échantillonnale** (sample complexity).

### B. Théorèmes, Propositions & Lemmes

> **Théorème de la Complexité Échantillonnale dans le Cas Réalisable (Ensemble d'Hypothèses Fini) :**
> Soit $\mathcal{H}$ un espace d'hypothèses fini ($|\mathcal{H}| < \infty$). Sous l'hypothèse de réalisabilité (il existe au moins un $h^* \in \mathcal{H}$ tel que $L_{\mathcal{D}, c}(h^*) = 0$), la classe $\mathcal{H}$ est PAC-apprenable par n'importe quel algorithme de Minimisation du Risque Empirique (ERM). La complexité échantillonnale est majorée par :
> $$ m_{\mathcal{H}}(\epsilon, \delta) \leq \left\lceil \frac{\ln(|\mathcal{H}|) + \ln(1/\delta)}{\epsilon} \right\rceil $$

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : PAC Bound pour $|\mathcal{H}| < \infty$ dans le cas réalisable

1. **Initialisation / Cadre :**
   Nous opérons sous l'hypothèse du "cas réalisable" : nous savons que le vrai concept $c$ appartient à $\mathcal{H}$ (ou qu'il existe un $h^*$ parfait dans $\mathcal{H}$). Par conséquent, il existe toujours au moins une hypothèse dans $\mathcal{H}$ qui a une erreur empirique nulle sur n'importe quel échantillon $S$.
   Soit $\mathcal{A}$ un algorithme ERM (Empirical Risk Minimization). Sur la base de l'échantillon $S$, $\mathcal{A}$ retourne une hypothèse $h_S \in \mathcal{H}$ telle que $L_S(h_S) = 0$.
   Nous voulons borner la probabilité que l'algorithme ERM retourne une "mauvaise" hypothèse. Une hypothèse $h$ est "mauvaise" si son risque réel est grand, c'est-à-dire $L_{\mathcal{D}, c}(h) > \epsilon$.
   Nous cherchons à majorer la probabilité de l'événement redouté (le risque de défaillance) :
   $$ \mathbb{P}_{S \sim \mathcal{D}^m} [L_{\mathcal{D}, c}(h_S) > \epsilon] $$

2. **Étape 1 : Isolation des "mauvaises" hypothèses et Borne de l'Union (Union Bound).**
   Définissons le sous-ensemble des mauvaises hypothèses dans $\mathcal{H}$ :
   $$ \mathcal{H}_B = \{ h \in \mathcal{H} \mid L_{\mathcal{D}, c}(h) > \epsilon \} $$
   Si l'algorithme ERM retourne une mauvaise hypothèse $h_S$, cela signifie que $h_S \in \mathcal{H}_B$. Mais parce que $h_S$ est le résultat d'un ERM dans le cas réalisable, nous savons que $L_S(h_S) = 0$.
   Donc, si l'événement redouté se produit, cela implique qu'il existe *au moins une* hypothèse mauvaise dans $\mathcal{H}_B$ qui a réussi à tromper l'échantillon d'entraînement en faisant 0 erreur.
   L'événement $\{L_{\mathcal{D}, c}(h_S) > \epsilon\}$ est inclus dans l'événement $\{\exists h \in \mathcal{H}_B \text{ tel que } L_S(h) = 0\}$.
   Nous pouvons donc écrire, par l'axiome de sous-additivité (Union Bound) :
   $$ \mathbb{P}_{S \sim \mathcal{D}^m} [L_{\mathcal{D}, c}(h_S) > \epsilon] \leq \mathbb{P}_{S \sim \mathcal{D}^m} [\exists h \in \mathcal{H}_B, L_S(h) = 0] $$
   $$ \mathbb{P}_{S \sim \mathcal{D}^m} [\exists h \in \mathcal{H}_B, L_S(h) = 0] \leq \sum_{h \in \mathcal{H}_B} \mathbb{P}_{S \sim \mathcal{D}^m} [L_S(h) = 0] $$

3. **Étape 2 : Majoration de la probabilité qu'une mauvaise hypothèse spécifique survive.**
   Fixons une hypothèse spécifique $h \in \mathcal{H}_B$. Quelle est la probabilité que cette hypothèse ne commette aucune erreur sur l'échantillon $S$ ?
   Par définition, $L_{\mathcal{D}, c}(h) > \epsilon$.
   Soit $x_i$ un point tiré selon $\mathcal{D}$. La probabilité que $h$ se trompe sur $x_i$ est $\mathbb{P}_{x_i \sim \mathcal{D}}[h(x_i) \neq c(x_i)] = L_{\mathcal{D}, c}(h)$.
   Donc la probabilité que $h$ donne la bonne réponse sur ce point est :
   $$ \mathbb{P}_{x_i \sim \mathcal{D}}[h(x_i) = c(x_i)] = 1 - L_{\mathcal{D}, c}(h) $$
   Puisque $L_{\mathcal{D}, c}(h) > \epsilon$, nous avons :
   $$ 1 - L_{\mathcal{D}, c}(h) < 1 - \epsilon $$
   L'échantillon $S$ est composé de $m$ tirages indépendants $(x_1, \dots, x_m)$. La probabilité que $h$ ait juste sur tous ces $m$ points simultanément est le produit des probabilités :
   $$ \mathbb{P}_{S \sim \mathcal{D}^m} [L_S(h) = 0] = \prod_{i=1}^m \mathbb{P}_{x_i \sim \mathcal{D}}[h(x_i) = c(x_i)] $$
   $$ \prod_{i=1}^m \mathbb{P}_{x_i \sim \mathcal{D}}[h(x_i) = c(x_i)] = (1 - L_{\mathcal{D}, c}(h))^m $$
   Par la stricte inégalité établie plus haut, nous obtenons :
   $$ \mathbb{P}_{S \sim \mathcal{D}^m} [L_S(h) = 0] < (1 - \epsilon)^m $$

4. **Étape 3 : Application de l'inégalité de convexité et synthèse.**
   Nous substituons cette borne dans notre somme de l'Union Bound (Étape 1) :
   $$ \sum_{h \in \mathcal{H}_B} \mathbb{P}_{S \sim \mathcal{D}^m} [L_S(h) = 0] < \sum_{h \in \mathcal{H}_B} (1 - \epsilon)^m $$
   Le nombre de mauvaises hypothèses $|\mathcal{H}_B|$ est au pire égal au nombre total d'hypothèses $|\mathcal{H}|$. Ainsi :
   $$ \sum_{h \in \mathcal{H}_B} (1 - \epsilon)^m \leq |\mathcal{H}| (1 - \epsilon)^m $$
   Nous utilisons maintenant l'inégalité fondamentale de l'analyse réelle : pour tout $z \in \mathbb{R}$, $1 - z \leq e^{-z}$. En posant $z = \epsilon > 0$, nous avons $1 - \epsilon \leq e^{-\epsilon}$.
   Élevé à la puissance $m$ (qui est positive), la croissance de la fonction exponentielle donne :
   $$ (1 - \epsilon)^m \leq (e^{-\epsilon})^m = e^{-\epsilon m} $$
   Nous obtenons la borne de probabilité de l'événement redouté :
   $$ \mathbb{P}_{S \sim \mathcal{D}^m} [L_{\mathcal{D}, c}(h_S) > \epsilon] \leq |\mathcal{H}| e^{-\epsilon m} $$

5. **Conclusion : Inversion de la borne pour trouver la complexité échantillonnale.**
   Pour satisfaire la condition PAC, nous exigeons que la probabilité de l'événement redouté soit au plus $\delta$ :
   $$ |\mathcal{H}| e^{-\epsilon m} \leq \delta $$
   Nous devons isoler $m$ :
   $$ e^{-\epsilon m} \leq \frac{\delta}{|\mathcal{H}|} $$
   Nous appliquons le logarithme népérien $\ln$ de chaque côté (le logarithme préserve l'ordre car strictement croissant) :
   $$ \ln(e^{-\epsilon m}) \leq \ln\left(\frac{\delta}{|\mathcal{H}|}\right) $$
   $$ -\epsilon m \leq \ln(\delta) - \ln(|\mathcal{H}|) $$
   Nous multiplions l'inéquation par $-1$ (ce qui inverse le sens de l'inégalité) :
   $$ \epsilon m \geq \ln(|\mathcal{H}|) - \ln(\delta) $$
   $$ \epsilon m \geq \ln(|\mathcal{H}|) + \ln\left(\frac{1}{\delta}\right) $$
   Nous divisons par $\epsilon$ (qui est strictement positif) :
   $$ m \geq \frac{\ln(|\mathcal{H}|) + \ln(1/\delta)}{\epsilon} $$
   Le théorème est rigoureusement démontré. $\blacksquare$

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Application Directe - PAC pour l'apprentissage de conjonctions booléennes
**Énoncé :**
Considérons l'espace des instances $\mathcal{X} = \{0, 1\}^n$ représentant des vecteurs de $n$ caractéristiques booléennes. L'espace d'hypothèses $\mathcal{H}$ est l'ensemble de toutes les conjonctions possibles de ces caractéristiques ou de leurs négations.
Une conjonction pourrait être par exemple $h(x) = x_1 \land \neg x_3 \land x_4$.
Calculez la taille de l'espace d'hypothèses $|\mathcal{H}|$ et déduisez-en le nombre d'exemples $m$ nécessaires pour garantir qu'un algorithme ERM retourne une hypothèse ayant une erreur inférieure à $\epsilon = 0.05$ avec une probabilité de confiance de $99\%$ ($\delta = 0.01$). L'algorithme opère dans le cas réalisable.

**Correction Détaillée :**
* *Analyse de l'énoncé :* Nous devons d'abord déterminer la cardinalité de $\mathcal{H}$. Pour chaque caractéristique $x_i$ (parmi les $n$ existantes), il y a 3 possibilités dans la construction d'une conjonction :
  1. $x_i$ apparaît sous forme positive.
  2. $x_i$ apparaît sous forme négative ($\neg x_i$).
  3. $x_i$ n'apparaît pas du tout dans la conjonction.
Il existe également une conjonction "vide" qui vaut toujours 1 (Vrai), et une conjonction contradictoire (ex: $x_1 \land \neg x_1$) qui vaut toujours 0 (Faux).
La combinatoire brute donne $3^n$ conjonctions syntaxiquement distinctes. En ajoutant la fonction constante 'Faux' (toutes les contradictions s'évaluant à 'Faux', elles forment une seule classe d'équivalence sémantique s'il on y est strict, mais on peut majorer $|\mathcal{H}| \leq 3^n + 1$).
Pour la borne PAC, nous utiliserons la majoration généreuse et correcte $|\mathcal{H}| = 3^n + 1$.

* *Résolution pas-à-pas :*
1. **Évaluation de $|\mathcal{H}|$ :** On retient $|\mathcal{H}| \leq 3^n + 1$.
2. **Paramètres PAC :** $\epsilon = 0.05$, $\delta = 0.01$.
3. **Application du théorème :**
   $$ m \geq \frac{\ln(|\mathcal{H}|) + \ln(1/\delta)}{\epsilon} $$
   Substituons les valeurs :
   $$ m \geq \frac{\ln(3^n + 1) + \ln(1/0.01)}{0.05} $$
   $$ m \geq \frac{\ln(3^n + 1) + \ln(100)}{0.05} $$
   On sait que $\ln(3^n + 1) \approx n \ln(3)$. Pour $n$ suffisamment grand, on peut approcher la borne par $\frac{n \ln(3) + 4.605}{0.05} = 20(n(1.098) + 4.605)$.
   Donc $m \geq 21.96 n + 92.1$.
   La complexité de l'apprentissage des conjonctions booléennes croît *linéairement* avec la dimension du problème $n$. L'algorithme est performant (polynomialement PAC apprenable).

### Exercice 2 : Niveau Avancé - Borne dans le cas non-réalisable (Agnostic PAC) (Inspiré X / ENS)
**Énoncé :**
Nous quittons le cas réalisable. Soit $\mathcal{H}$ un espace d'hypothèses fini. La distribution $\mathcal{D}$ définit maintenant non pas une fonction cible déterministe, mais un lien probabiliste entre $\mathcal{X}$ et $\mathcal{Y}$. Le risque réel est $L_{\mathcal{D}}(h) = \mathbb{P}_{(x,y)\sim \mathcal{D}}[h(x) \neq y]$. Le risque empirique est $L_S(h) = \frac{1}{m}\sum_{i=1}^m \mathbb{1}_{\{h(x_i) \neq y_i\}}$.
Sachant que par l'inégalité de Hoeffding, pour une hypothèse fixe $h$, la déviation entre les risques est bornée par $\mathbb{P}_{S \sim \mathcal{D}^m} [|L_S(h) - L_{\mathcal{D}}(h)| > \epsilon] \leq 2 e^{-2m\epsilon^2}$, démontrez rigoureusement la borne de complexité échantillonnale pour que, avec probabilité au moins $1 - \delta$, **pour toute** hypothèse $h \in \mathcal{H}$ simultanément, on ait $|L_S(h) - L_{\mathcal{D}}(h)| \leq \epsilon$ (Garantie de convergence uniforme).
Concluez sur la dépendance en $\epsilon$.

**Correction Détaillée :**
* *Analyse de l'énoncé :* C'est le cadre de l'apprentissage "Agnostique" (Agnostic PAC). L'erreur minimale dans $\mathcal{H}$ n'est plus forcément zéro. Nous cherchons la convergence uniforme empirique vers le risque réel, un prérequis pour prouver qu'un algorithme ERM sélectionne une hypothèse proche de la meilleure hypothèse possible dans $\mathcal{H}$.

* *Résolution pas-à-pas :*
1. **Borne de l'Union pour la convergence uniforme :**
   Nous voulons borner la probabilité de l'événement redouté : "il existe au moins une hypothèse $h \in \mathcal{H}$ dont la différence entre le risque empirique et le risque réel excède $\epsilon$".
   Soit l'événement $E = \{ \exists h \in \mathcal{H} \mid |L_S(h) - L_{\mathcal{D}}(h)| > \epsilon \}$.
   Par la sous-additivité des probabilités (Union Bound) :
   $$ \mathbb{P}(E) = \mathbb{P}\left(\bigcup_{h \in \mathcal{H}} \{ |L_S(h) - L_{\mathcal{D}}(h)| > \epsilon \} \right) \leq \sum_{h \in \mathcal{H}} \mathbb{P}(|L_S(h) - L_{\mathcal{D}}(h)| > \epsilon) $$
2. **Application de la borne de concentration :**
   On insère l'inégalité de Hoeffding donnée pour une seule hypothèse :
   $$ \sum_{h \in \mathcal{H}} \mathbb{P}(|L_S(h) - L_{\mathcal{D}}(h)| > \epsilon) \leq \sum_{h \in \mathcal{H}} 2 e^{-2m\epsilon^2} $$
   $$ \sum_{h \in \mathcal{H}} 2 e^{-2m\epsilon^2} = 2 |\mathcal{H}| e^{-2m\epsilon^2} $$
3. **Inversion de la borne :**
   Nous posons l'exigence que cette probabilité d'échec global soit au plus $\delta$ :
   $$ 2 |\mathcal{H}| e^{-2m\epsilon^2} \leq \delta $$
   On isole la taille de l'échantillon $m$ :
   $$ e^{-2m\epsilon^2} \leq \frac{\delta}{2|\mathcal{H}|} $$
   On applique le logarithme népérien :
   $$ -2m\epsilon^2 \leq \ln\left(\frac{\delta}{2|\mathcal{H}|}\right) $$
   $$ 2m\epsilon^2 \geq \ln\left(\frac{2|\mathcal{H}|}{\delta}\right) $$
   $$ m \geq \frac{\ln(2|\mathcal{H}|/\delta)}{2\epsilon^2} $$
   $$ m \geq \frac{\ln(|\mathcal{H}|) + \ln(2/\delta)}{2\epsilon^2} $$

* *Conclusion :*
Dans le cas agnostique (non-réalisable), la taille de l'échantillon $m$ requise évolue en $\frac{1}{\epsilon^2}$, contrairement au cas réalisable où elle évoluait en $\frac{1}{\epsilon}$. Pour atteindre une haute précision (un petit $\epsilon$), le cas non-réalisable est exponentiellement plus gourmand en données empiriques, reflétant la grande difficulté d'optimiser en présence de "bruit" fondamental incompressible de la distribution.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :**
Le cadre PAC est le socle fondateur de toute la "Statistical Learning Theory" (SLT). En Deep Learning, quand on observe un grand écart entre la précision sur l'ensemble d'entraînement ("Training Accuracy") et la précision sur l'ensemble de test ("Test Accuracy"), on est face à une perte de généralisation (Overfitting). Les bornes PAC quantifient théoriquement ce gap. Elles montrent que si un réseau de neurones possède un espace d'hypothèses $\mathcal{H}$ massivement grand (des millions de poids, ce qui implique une très grande "capacité"), le terme $\ln(|\mathcal{H}|)$ (qui deviendra la dimension VC ou la complexité de Rademacher) explose. Pour maintenir l'erreur $\epsilon$ basse, il faut augmenter $m$ (le nombre d'images, de textes) proportionnellement pour contrer cette capacité.

- **Exemple Concret :**
Si une équipe d'ingénieurs en IA chez OpenAI entraîne un modèle type GPT ou un classifieur d'images, et constate que le modèle mémorise le jeu de données mais s'effondre en production, la théorie PAC donne l'explication et la solution. Pour réduire l'écart de généralisation $\epsilon$, ils ont formellement deux choix :
1. Augmenter drastiquement $m$ (loi d'échelle ou "scaling law", récolter plus de données massives).
2. Restreindre mathématiquement la taille effective de $|\mathcal{H}|$ par des techniques de régularisation (Weight Decay, Dropout, ou architecture plus parcimonieuse, forçant un espace d'hypothèses effectif plus petit).

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 90 (Les modes de convergence)]], [[Jalon 91 (Inegalites de concentration)]]
- **Concepts Futurs dépendants :** [[Jalon 134 (Complexite des classes de fonctions)]], [[Jalon 136 (Theorie de Vapnik-Chervonenkis)]]

---
uuid: "jalon-129"
title: "Optimisation stochastique"
year: 3
trimester: 11
tags:
  - math/optimisation
  - math/probabilites
  - ia/machine_learning
prev: "[[Jalon 128 (Flots de gradient).md]]"
next: "[[Jalon 130 (Régularisation implicite de la descente de gradient dans les modèles sur-paramétrés.).md]]"
---

# Optimisation Stochastique

## 1. Présentation du concept clé

- **La Métaphore :** Imagine que tu sois un randonneur cherchant à atteindre le point le plus bas d'une immense vallée (le minimum d'une fonction). Le problème, c'est qu'il fait complètement nuit et qu'un vent très fort souffle. Ton seul outil est une boussole magique qui t'indique la pente, mais à cause du vent, l'aiguille tremble énormément. Parfois elle t'indique la bonne direction pour descendre, parfois elle se trompe complètement. L'optimisation stochastique, c'est la méthode qui t'explique comment, malgré cette boussole très imparfaite, tu peux quand même être sûr d'arriver tout au fond de la vallée : il suffit de faire des pas de plus en plus petits au fur et à mesure que tu avances, pour que les erreurs de la boussole se compensent et ne te fassent pas remonter.
- **Le "Pourquoi on a inventé ça" :** Dans la vraie vie (et surtout en Intelligence Artificielle), on a souvent des milliards de données. Calculer la pente exacte (le "vrai gradient") en utilisant *toutes* les données en même temps prendrait des mois pour un seul pas. L'idée géniale de l'optimisation stochastique est de n'utiliser qu'un tout petit peu de données au hasard à chaque pas. C'est beaucoup plus rapide, mais le calcul de la pente devient "bruité" (plein d'erreurs aléatoires). Il a fallu inventer des mathématiques pour prouver que cet algorithme avec des erreurs converge quand même.
- **Visualisation :** Dessine un grand bol. Si tu lâches une bille de tout en haut, elle descend en ligne droite jusqu'au fond : ça, c'est la descente de gradient normale. Maintenant, imagine une bille qui avance en zigzaguant, allant parfois un peu à gauche, parfois un peu à droite, voire même en remontant légèrement sur les bords de temps en temps, mais dont les zigzags deviennent de plus en plus minuscules, jusqu'à ce qu'elle s'arrête exactement et parfaitement au fond du bol. C'est la descente de gradient stochastique (SGD).

## 2. Formalisation & Rigueur Académique

### A. Définitions Formelles

**Espace ambiant :** Soit un espace euclidien $E = \mathbb{R}^d$, muni de son produit scalaire canonique $\langle \cdot, \cdot \rangle$ et de la norme euclidienne associée $\|\cdot\|$.
Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace de probabilité fondamental muni d'une filtration $(\mathcal{F}_t)_{t \in \mathbb{N}}$.

**Fonction objectif :** Soit $F : \mathbb{R}^d \to \mathbb{R}$ une fonction différentiable. On cherche à résoudre le problème d'optimisation non contraint :
$$ \min_{x \in \mathbb{R}^d} F(x) $$

**Contexte stochastique :** On suppose qu'on n'a pas accès directement à $\nabla F(x)$, mais seulement à un estimateur stochastique (ou "oracle" stochastique) de ce gradient. Pour tout $x \in \mathbb{R}^d$ et à l'instant $t \in \mathbb{N}$, on observe un vecteur aléatoire $g_t(x)$ qui est $\mathcal{F}_t$-mesurable.

**Définition 1 (Descente de Gradient Stochastique - SGD) :**
L'algorithme de descente de gradient stochastique génère une suite de variables aléatoires $(X_t)_{t \in \mathbb{N}}$ à valeurs dans $\mathbb{R}^d$ par la relation de récurrence :
$$ X_{t+1} = X_t - \gamma_t g_t(X_t) $$
où $X_0 \in \mathbb{R}^d$ est un point de départ (déterministe ou $\mathcal{F}_0$-mesurable), et $(\gamma_t)_{t \in \mathbb{N}}$ est une suite déterministe de réels strictement positifs appelée **pas d'apprentissage** (ou *learning rates*).

**Définition 2 (Conditions de Robbins-Monro) :**
La suite des pas $(\gamma_t)_{t \in \mathbb{N}}$ satisfait les conditions de Robbins-Monro si :
$$ \sum_{t=0}^{+\infty} \gamma_t = +\infty \quad \text{et} \quad \sum_{t=0}^{+\infty} \gamma_t^2 < +\infty $$
*(Exemple typique : $\gamma_t = \frac{c}{(t+1)^\alpha}$ avec $c > 0$ et $1/2 < \alpha \le 1$.)*

### B. Théorèmes, Propositions & Lemmes

**Lemme Fondamental de Robbins-Siegmund :**
Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace probabilisé muni d'une filtration $(\mathcal{F}_t)_{t \ge 0}$. Soient $(V_t)$, $(\alpha_t)$, $(\beta_t)$ et $(\eta_t)$ quatre suites de variables aléatoires positives intégrables et adaptées à $\mathcal{F}_t$. On suppose que presque sûrement (p.s.) :
$$ \mathbb{E}[V_{t+1} \mid \mathcal{F}_t] \le V_t (1 + \alpha_t) + \beta_t - \eta_t $$
Si de plus, $\sum_{t=0}^{+\infty} \alpha_t < +\infty$ p.s. et $\sum_{t=0}^{+\infty} \beta_t < +\infty$ p.s., alors :
1. La suite $(V_t)_{t \ge 0}$ converge presque sûrement vers une variable aléatoire $V_\infty \ge 0$.
2. La somme des pénalités converge : $\sum_{t=0}^{+\infty} \eta_t < +\infty$ p.s.

> **Théorème de Convergence Presque Sûre de la SGD (Cas fortement convexe) :**
> Soit $F : \mathbb{R}^d \to \mathbb{R}$ de classe $\mathcal{C}^1$. On suppose qu'il existe $L > 0$ et $\mu > 0$ tels que :
> 1. **(Gradient Lipschitz) :** $\forall x, y \in \mathbb{R}^d, \|\nabla F(x) - \nabla F(y)\| \le L \|x - y\|$
> 2. **(Forte convexité) :** $\forall x, y \in \mathbb{R}^d, F(y) \ge F(x) + \langle \nabla F(x), y - x \rangle + \frac{\mu}{2} \|x - y\|^2$
> Soit $x^* \in \mathbb{R}^d$ l'unique minimum global de $F$.
> On suppose que l'estimateur $g_t(X_t)$ satisfait presque sûrement :
> 3. **(Estimateur sans biais) :** $\mathbb{E}[g_t(X_t) \mid \mathcal{F}_t] = \nabla F(X_t)$
> 4. **(Variance bornée) :** $\mathbb{E}[\|g_t(X_t) - \nabla F(X_t)\|^2 \mid \mathcal{F}_t] \le \sigma^2$ (où $\sigma > 0$)
> Si la suite des pas $(\gamma_t)_{t \in \mathbb{N}}$ vérifie les conditions de Robbins-Monro (et $\gamma_t < \frac{2}{L}$), alors la suite $(X_t)_{t \in \mathbb{N}}$ générée par SGD converge presque sûrement vers l'optimum global $x^*$ :
> $$ \mathbb{P} \left( \lim_{t \to +\infty} X_t = x^* \right) = 1 $$

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration du Théorème Pivot : Convergence Presque Sûre de la SGD

1. **Initialisation / Cadre :**
Nous allons étudier la distance au carré entre l'itéré courant $X_t$ et la solution optimale $x^*$. On pose $V_t = \|X_t - x^*\|^2$.
Notre objectif est de trouver une relation de récurrence conditionnelle sur $V_{t+1}$ par rapport à $\mathcal{F}_t$ (la tribu engendrée par $X_0, g_0(X_0), \dots, g_{t-1}(X_{t-1})$) pour appliquer le lemme de Robbins-Siegmund.
Puisque $x^*$ est le minimum global de la fonction $F$ fortement convexe, alors par la condition d'optimalité du premier ordre, on a $\nabla F(x^*) = 0$.

2. **Étape 1 : Développement quadratique et espérance conditionnelle**
On développe la norme au carré de $X_{t+1} - x^*$ en utilisant la définition de l'algorithme :
$$ \|X_{t+1} - x^*\|^2 = \|X_t - \gamma_t g_t(X_t) - x^*\|^2 $$
$$ \|X_{t+1} - x^*\|^2 = \|X_t - x^*\|^2 - 2 \gamma_t \langle X_t - x^*, g_t(X_t) \rangle + \gamma_t^2 \|g_t(X_t)\|^2 $$
On passe à l'espérance conditionnelle par rapport à $\mathcal{F}_t$. Comme $X_t$ est $\mathcal{F}_t$-mesurable, on peut le sortir de l'espérance conditionnelle par linéarité :
$$ \mathbb{E}[\|X_{t+1} - x^*\|^2 \mid \mathcal{F}_t] = \|X_t - x^*\|^2 - 2 \gamma_t \langle X_t - x^*, \mathbb{E}[g_t(X_t) \mid \mathcal{F}_t] \rangle + \gamma_t^2 \mathbb{E}[\|g_t(X_t)\|^2 \mid \mathcal{F}_t] $$

3. **Étape 2 : Utilisation de l'hypothèse de l'estimateur sans biais**
Par l'hypothèse (3), nous savons que l'estimateur du gradient est sans biais : $\mathbb{E}[g_t(X_t) \mid \mathcal{F}_t] = \nabla F(X_t)$. On substitue cette valeur dans l'équation :
$$ \mathbb{E}[\|X_{t+1} - x^*\|^2 \mid \mathcal{F}_t] = \|X_t - x^*\|^2 - 2 \gamma_t \langle X_t - x^*, \nabla F(X_t) \rangle + \gamma_t^2 \mathbb{E}[\|g_t(X_t)\|^2 \mid \mathcal{F}_t] $$

4. **Étape 3 : Contrôle du terme de second ordre (la variance)**
Décomposons le terme carré $\mathbb{E}[\|g_t(X_t)\|^2 \mid \mathcal{F}_t]$. En ajoutant et retranchant $\nabla F(X_t)$, on obtient :
$$ \|g_t(X_t)\|^2 = \|g_t(X_t) - \nabla F(X_t) + \nabla F(X_t)\|^2 $$
$$ \|g_t(X_t)\|^2 = \|g_t(X_t) - \nabla F(X_t)\|^2 + 2 \langle g_t(X_t) - \nabla F(X_t), \nabla F(X_t) \rangle + \|\nabla F(X_t)\|^2 $$
En prenant l'espérance conditionnelle (le terme croisé s'annule par l'hypothèse sans biais), il reste la variance conditionnelle plus le carré du gradient exact :
$$ \mathbb{E}[\|g_t(X_t)\|^2 \mid \mathcal{F}_t] = \mathbb{E}[\|g_t(X_t) - \nabla F(X_t)\|^2 \mid \mathcal{F}_t] + \|\nabla F(X_t)\|^2 $$
Par l'hypothèse (4) sur la variance bornée, on peut majorer ce terme :
$$ \mathbb{E}[\|g_t(X_t)\|^2 \mid \mathcal{F}_t] \le \sigma^2 + \|\nabla F(X_t)\|^2 $$
On substitue cette borne dans l'inégalité de l'Étape 2 :
$$ \mathbb{E}[\|X_{t+1} - x^*\|^2 \mid \mathcal{F}_t] \le \|X_t - x^*\|^2 - 2 \gamma_t \langle X_t - x^*, \nabla F(X_t) \rangle + \gamma_t^2 (\sigma^2 + \|\nabla F(X_t)\|^2) $$

5. **Étape 4 : Utilisation de la forte convexité et du gradient Lipschitz**
La fonction $F$ est fortement convexe de paramètre $\mu$. Une propriété classique des fonctions $\mu$-fortement convexes s'écrit (en utilisant le point optimal $x^*$ où $\nabla F(x^*) = 0$) :
$$ \langle \nabla F(X_t) - \nabla F(x^*), X_t - x^* \rangle \ge \mu \|X_t - x^*\|^2 $$
Ce qui donne pour notre terme croisé (avec un signe moins) :
$$ - \langle X_t - x^*, \nabla F(X_t) \rangle \le - \mu \|X_t - x^*\|^2 $$
D'autre part, comme $F$ est $L$-lisse (gradient $L$-Lipschitz), on a l'inégalité de co-coercivité sur le gradient au carré :
$$ \|\nabla F(X_t)\|^2 = \|\nabla F(X_t) - \nabla F(x^*)\|^2 \le L \langle \nabla F(X_t) - \nabla F(x^*), X_t - x^* \rangle = L \langle \nabla F(X_t), X_t - x^* \rangle $$
Reprenons notre expression principale et injectons la borne sur le gradient au carré :
$$ \mathbb{E}[\|X_{t+1} - x^*\|^2 \mid \mathcal{F}_t] \le \|X_t - x^*\|^2 - 2 \gamma_t \langle X_t - x^*, \nabla F(X_t) \rangle + \gamma_t^2 \sigma^2 + \gamma_t^2 L \langle \nabla F(X_t), X_t - x^* \rangle $$
On regroupe les termes contenant le produit scalaire $\langle \nabla F(X_t), X_t - x^* \rangle$ :
$$ \mathbb{E}[\|X_{t+1} - x^*\|^2 \mid \mathcal{F}_t] \le \|X_t - x^*\|^2 - (2 \gamma_t - \gamma_t^2 L) \langle \nabla F(X_t), X_t - x^* \rangle + \gamma_t^2 \sigma^2 $$
Pour que l'algorithme converge, on suppose que le pas est suffisamment petit pour que $(2 \gamma_t - \gamma_t^2 L) \ge 0$ (c'est le cas dès que $\gamma_t \le 2/L$, et comme $\gamma_t \to 0$ c'est asymptotiquement vrai).
Nous pouvons maintenant utiliser notre inégalité issue de la forte convexité sur le terme produit scalaire :
$$ - \langle \nabla F(X_t), X_t - x^* \rangle \le - \mu \|X_t - x^*\|^2 $$
En substituant, nous obtenons :
$$ \mathbb{E}[\|X_{t+1} - x^*\|^2 \mid \mathcal{F}_t] \le \|X_t - x^*\|^2 - (2 \gamma_t - \gamma_t^2 L) \mu \|X_t - x^*\|^2 + \gamma_t^2 \sigma^2 $$
$$ \mathbb{E}[\|X_{t+1} - x^*\|^2 \mid \mathcal{F}_t] \le \|X_t - x^*\|^2 \left( 1 - \mu (2 \gamma_t - \gamma_t^2 L) \right) + \gamma_t^2 \sigma^2 $$
On peut affaiblir cette inégalité pour coller à la forme exacte de Robbins-Siegmund. Posons $\alpha_t = 0$. Soit $\eta_t = \mu (2 \gamma_t - \gamma_t^2 L) \|X_t - x^*\|^2$ et $\beta_t = \gamma_t^2 \sigma^2$.
$$ \mathbb{E}[\|X_{t+1} - x^*\|^2 \mid \mathcal{F}_t] \le \|X_t - x^*\|^2 + \beta_t - \eta_t $$

6. **Étape 5 : Application du lemme de Robbins-Siegmund**
Identifions les variables pour le lemme :
- $V_t = \|X_t - x^*\|^2 \ge 0$
- $\alpha_t = 0 \ge 0$ (et $\sum \alpha_t = 0 < +\infty$)
- $\beta_t = \gamma_t^2 \sigma^2$. Par l'hypothèse de Robbins-Monro (Définition 2), $\sum \gamma_t^2 < +\infty$, donc $\sum \beta_t = \sigma^2 \sum \gamma_t^2 < +\infty$.
- Pour $t$ assez grand ($\gamma_t \le 1/L$), on a $(2 \gamma_t - \gamma_t^2 L) \ge \gamma_t$. Ainsi, $\eta_t \ge \mu \gamma_t \|X_t - x^*\|^2 \ge 0$.
Les conditions du lemme de Robbins-Siegmund sont remplies. On en déduit deux conclusions presque sûrement :
1. $V_t = \|X_t - x^*\|^2$ converge p.s. vers une limite $V_\infty \ge 0$.
2. $\sum_{t=0}^{+\infty} \eta_t < +\infty$ p.s., ce qui implique $\sum_{t=0}^{+\infty} \mu (2 \gamma_t - \gamma_t^2 L) \|X_t - x^*\|^2 < +\infty$ p.s.

7. **Conclusion : Caractérisation de la limite**
La deuxième conclusion nous indique, puisque $(2 \gamma_t - \gamma_t^2 L) \sim 2\gamma_t$ pour $t$ grand, que :
$$ \sum_{t=0}^{+\infty} \gamma_t \|X_t - x^*\|^2 < +\infty \text{ p.s.} $$
Or, par la première condition de Robbins-Monro, nous savons que $\sum_{t=0}^{+\infty} \gamma_t = +\infty$.
La seule façon mathématique pour que la série des $\gamma_t \|X_t - x^*\|^2$ soit convergente alors que la série des $\gamma_t$ est divergente, c'est que la suite $(\|X_t - x^*\|^2)$ ne soit pas séparée de zéro. Mieux, comme la suite $\|X_t - x^*\|^2$ est convergente vers $V_\infty$ d'après la première conclusion, la seule limite possible est $V_\infty = 0$.
On a donc prouvé que :
$$ \lim_{t \to +\infty} \|X_t - x^*\|^2 = 0 \text{ presque sûrement.} $$
Ce qui clôt rigoureusement la démonstration.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Application Directe de SGD sur une fonction quadratique

**Énoncé :** Soit la fonction quadratique unidimensionnelle $F(x) = \frac{1}{2} x^2$. L'optimum évident est $x^* = 0$. On utilise SGD avec un estimateur de gradient bruité $g_t(x) = x + \xi_t$, où $\xi_t$ est un bruit centré ($\mathbb{E}[\xi_t] = 0$) de variance $\sigma^2$ indépendante de l'itération. Soit le pas constant $\gamma_t = \gamma > 0$. Exprimer $\mathbb{E}[X_{t+1}^2]$ en fonction de $\mathbb{E}[X_t^2]$, $\gamma$ et $\sigma^2$. L'algorithme converge-t-il vers $x^*=0$ avec un pas constant ?

**Correction Détaillée :**
* *Analyse de l'énoncé :* On est face au cas le plus simple d'optimisation stochastique : fonction fortement convexe, bruit additif de variance constante, mais on viole délibérément les conditions de Robbins-Monro en prenant un pas constant $\gamma$.
* *Résolution pas-à-pas :*
Écrivons la récurrence de SGD :
$$ X_{t+1} = X_t - \gamma g_t(X_t) = X_t - \gamma (X_t + \xi_t) = (1 - \gamma) X_t - \gamma \xi_t $$
Passons au carré :
$$ X_{t+1}^2 = (1 - \gamma)^2 X_t^2 - 2 \gamma (1 - \gamma) X_t \xi_t + \gamma^2 \xi_t^2 $$
Prenons l'espérance mathématique totale. Puisque le bruit $\xi_t$ est centré et indépendant de $X_t$, le terme croisé s'annule : $\mathbb{E}[X_t \xi_t] = \mathbb{E}[X_t] \mathbb{E}[\xi_t] = 0$.
On obtient la relation de récurrence sur les espérances des carrés :
$$ \mathbb{E}[X_{t+1}^2] = (1 - \gamma)^2 \mathbb{E}[X_t^2] + \gamma^2 \sigma^2 $$
Si on suppose que $\gamma \in ]0, 1[$, alors $(1-\gamma)^2 < 1$. Il s'agit d'une suite arithmético-géométrique sur $u_t = \mathbb{E}[X_t^2]$. Cherchons la limite asymptotique $u_\infty$ en résolvant $u_\infty = (1 - \gamma)^2 u_\infty + \gamma^2 \sigma^2$ :
$$ u_\infty - (1 - 2\gamma + \gamma^2) u_\infty = \gamma^2 \sigma^2 $$
$$ (2\gamma - \gamma^2) u_\infty = \gamma^2 \sigma^2 $$
$$ \gamma(2 - \gamma) u_\infty = \gamma^2 \sigma^2 $$
Comme $\gamma \neq 0$, on divise :
$$ u_\infty = \frac{\gamma \sigma^2}{2 - \gamma} $$
Pour des petits pas ($\gamma \ll 1$), la limite est environ $\frac{\gamma \sigma^2}{2}$.
*Conclusion :* Avec un pas constant, l'algorithme ne converge pas vers le minimum exact $x^* = 0$. L'espérance du carré (qui est la variance de l'estimateur autour du minimum) atteint un plancher asymptotique proportionnel au pas $\gamma$ et à la variance du bruit $\sigma^2$. C'est précisément pour écraser ce bruit résiduel qu'il faut décroître le pas (condition $\sum \gamma_t^2 < \infty$).

### Exercice 2 : Niveau Avancé (Inspiré Concours X / ENS / MIT)

**Énoncé :** Dans le cadre du Théorème de Convergence de la section 3 (fonction $L$-lisse et $\mu$-fortement convexe), supposons cette fois que la suite des pas est $\gamma_t = \frac{1}{\mu(t+1)}$.
Démontrer un taux de convergence en espérance (une borne sur $\mathbb{E}[\|X_t - x^*\|^2]$) de l'ordre de $\mathcal{O}(1/t)$.
*Indication : on pourra s'appuyer sur la majoration établie à l'étape 4 de la preuve : $\mathbb{E}[\|X_{t+1} - x^*\|^2 \mid \mathcal{F}_t] \le \|X_t - x^*\|^2 (1 - \mu \gamma_t) + \gamma_t^2 \sigma^2$, valable pour des pas assez petits.*

**Correction Détaillée :**
* *Analyse de l'énoncé :* On passe de la convergence presque sûre (étude asymptotique) à l'analyse de complexité (taux de convergence). Le choix de $\gamma_t = 1/(\mu t)$ est théoriquement optimal pour les fonctions fortement convexes.
* *Résolution pas-à-pas :*
Reprenons la majoration simplifiée pour un pas suffisamment petit $\gamma_t \le 1/L$. En espérance inconditionnelle totale, en notant $e_t = \mathbb{E}[\|X_t - x^*\|^2]$, l'inégalité devient :
$$ e_{t+1} \le e_t (1 - \mu \gamma_t) + \gamma_t^2 \sigma^2 $$
On substitue le choix de pas $\gamma_t = \frac{1}{\mu(t+1)}$ :
$$ e_{t+1} \le e_t \left( 1 - \frac{1}{t+1} \right) + \frac{\sigma^2}{\mu^2(t+1)^2} $$
$$ e_{t+1} \le e_t \left( \frac{t}{t+1} \right) + \frac{\sigma^2}{\mu^2(t+1)^2} $$
On cherche à borner $e_t$ par une fonction de type $C / t$. Montrons par récurrence sur $t \ge 1$ que $e_t \le \frac{Q}{t}$ pour une certaine constante $Q$.
Puisque pour tout paramètre c'est vrai à l'initialisation ($t=1$) en choisissant $Q = e_1 \ge 0$, examinons l'hérédité.
Supposons $e_t \le \frac{Q}{t}$ vrai pour un $t \ge 1$. Injectons cette hypothèse dans l'inégalité de récurrence :
$$ e_{t+1} \le \frac{Q}{t} \left( \frac{t}{t+1} \right) + \frac{\sigma^2}{\mu^2(t+1)^2} $$
$$ e_{t+1} \le \frac{Q}{t+1} + \frac{\sigma^2}{\mu^2(t+1)^2} $$
Ici, nous sommes bloqués si nous voulons strictement $e_{t+1} \le \frac{Q}{t+1}$, car le terme de bruit s'ajoute.
Pour pallier ce problème inhérent au pas $1/t$, l'astuce classique introduite par Nemirovski est d'utiliser un pas légèrement décalé, ou de procéder par induction sur une forme modifiée.
Reprenons depuis :
$$ e_{t+1} \le e_t \left( \frac{t}{t+1} \right) + \frac{\sigma^2}{\mu^2(t+1)^2} $$
Multiplions les deux côtés de l'inéquation par $(t+1)$ :
$$ (t+1) e_{t+1} \le t e_t + \frac{\sigma^2}{\mu^2(t+1)} $$
Cette forme télescopique est puissante. Sommons cette inéquation de $k=1$ à $t-1$ :
$$ \sum_{k=1}^{t-1} ((k+1) e_{k+1} - k e_k) \le \sum_{k=1}^{t-1} \frac{\sigma^2}{\mu^2(k+1)} $$
Le membre de gauche est une somme télescopique parfaite :
$$ t e_t - 1 e_1 \le \frac{\sigma^2}{\mu^2} \sum_{k=1}^{t-1} \frac{1}{k+1} $$
Or, on sait qu'une somme harmonique partielle est majorée par le logarithme : $\sum_{k=1}^{t-1} \frac{1}{k+1} \le \int_1^t \frac{1}{x} dx = \ln(t)$.
Ainsi, on obtient :
$$ t e_t \le e_1 + \frac{\sigma^2}{\mu^2} \ln(t) $$
En divisant par $t$, on obtient le taux rigoureux de convergence :
$$ \mathbb{E}[\|X_t - x^*\|^2] \le \frac{e_1}{t} + \frac{\sigma^2}{\mu^2} \frac{\ln(t)}{t} $$
Le taux global est donc en $\mathcal{O}\left( \frac{\ln(t)}{t} \right)$.
*Remarque de concours :* Pour obtenir le taux asymptotiquement optimal de $\mathcal{O}(1/t)$ sans le facteur logarithmique, la littérature démontre qu'il faut choisir un moyennage des itérés (moyennage de Polyak-Ruppert) couplé avec un pas qui décroît un peu plus lentement (typiquement $\gamma_t = \mathcal{O}(1/\sqrt{t})$).

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Le Machine Learning repose entièrement sur l'optimisation stochastique. L'apprentissage supervisé revient à trouver les paramètres (les poids $\theta$) d'un modèle qui minimisent l'espérance d'une fonction de perte sur une distribution de données inconnue. Comme on ne possède qu'un ensemble d'entraînement fini, on calcule l'estimateur du vrai gradient (le gradient de la perte) sur des "mini-batchs" (des petits échantillons tirés au hasard). L'estimateur de gradient ainsi formé est un estimateur sans biais (si les données sont i.i.d.) et de variance bornée. La SGD garantit ainsi la convergence des poids du réseau vers un minimum de la fonction de perte (bien que pour les réseaux de neurones, la fonction soit non-convexe et l'on converge vers un minimum local).
- **Exemple Concret :** Dans l'entraînement des réseaux profonds (par exemple un ResNet sur ImageNet), chaque étape de la SGD calcule le gradient de la perte de classification (Cross-Entropy) en n'utilisant que $B=256$ images sur les $1.2$ million disponibles. Le choix délicat du "Learning Rate Schedule" (la suite des pas $\gamma_t$) est justifié par la théorie de Robbins-Monro : on commence avec un pas grand pour avancer vite dans la vallée (phase d'exploration), puis on diminue le pas (Step Decay ou Cosine Annealing) pour s'assurer que $\sum \gamma_t^2 < \infty$ et ainsi écraser la variance due au petit échantillon, permettant aux poids $\theta$ de se stabiliser parfaitement au fond du minimum.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 128 (Flots de gradient)]], [[Jalon 121 (Ensembles convexes)]], [[Jalon 89 (Lemmes de Borel-Cantelli)]]
- **Concepts Futurs dépendants :** [[Jalon 130 (Régularisation implicite de la descente de gradient dans les modèles sur-paramétrés.)]], [[Jalon 131 (Algorithmes d'optimisation de second ordre en grande dimension)]]

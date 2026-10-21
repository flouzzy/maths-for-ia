---
uuid: "jalon-96"
title: "Livrable IA T8 : Convergence de la Cross-Entropy vers l'Entropie de Shannon"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/theorie-information
prev: "[[Jalon 95 (Vecteurs gaussiens).md]]"
next: "[[Jalon 97 (Espaces de Banach).md]]"
---
# Jalon 96 : Livrable IA T8 : Convergence de la Cross-Entropy vers l'Entropie de Shannon

## Contexte Historique et Physique de l'Information

L'étude de l'information trouve ses racines dans la physique statistique, notamment via les travaux de Ludwig Boltzmann. C'est Claude Shannon, en 1948, qui formalise mathématiquement la notion d'incertitude dans un processus aléatoire. En intelligence artificielle moderne, l'entraînement des modèles de langage massifs (LLM) repose sur la minimisation d'une fonction de perte appelée entropie croisée (ou Cross-Entropy).

Ce processus d'optimisation vise à rapprocher la distribution de probabilité prédite par le modèle de la distribution réelle du langage humain. Nous démontrerons que cette perte est bornée inférieurement par l'entropie intrinsèque du langage : l'incertitude irréductible inhérente à la communication humaine.

## Structures Mathématiques Fondamentales

Soit $(\mathcal{X}, \mathcal{B}(\mathcal{X}), \lambda)$ un espace mesuré, où $\mathcal{X}$ représente l'espace de nos données (par exemple, le vocabulaire d'une langue). Soit $P$ la distribution réelle et inconnue des données, absolument continue par rapport à $\lambda$, de densité $p$. Soit $Q_\theta$ la distribution de probabilité paramétrée par $\theta \in \Theta$, prédite par notre modèle, de densité $q_\theta$.

### Définitions, Théorèmes et Exemples Concrets Immédiats

> **Définition 1 (Entropie de Shannon) :**
> L'entropie de la source de données $P$ est définie par :
> $$H(P) = - \int_{\mathcal{X}} p(x) \ln p(x) d\lambda(x) = \mathbb{E}_{X \sim P}[-\ln p(X)]$$
> Cette grandeur mesure la quantité moyenne d'information (ou d'incertitude) intrinsèque aux données.

**Exemple 1 : Lancer de pièce biaisée**
Considérons une variable aléatoire binaire $X \in \{0, 1\}$ suivant une loi de Bernoulli de paramètre $p=0,2$.
La distribution est $P(X=1) = 0,2$ et $P(X=0) = 0,8$.
L'entropie de Shannon de cette source est :
$$H(P) = - (0,2 \ln(0,2) + 0,8 \ln(0,8))$$
Calculons pas-à-pas :
$$0,2 \ln(0,2) \approx 0,2 \times (-1,609) \approx -0,3218$$
$$0,8 \ln(0,8) \approx 0,8 \times (-0,223) \approx -0,1784$$
$$H(P) \approx 0,3218 + 0,1784 = 0,5002 \text{ nats}.$$

> **Définition 2 (Entropie Croisée ou Cross-Entropy) :**
> La cross-entropy entre la vraie distribution $P$ et la distribution approchée $Q_\theta$ est définie par :
> $$H(P, Q_\theta) = - \int_{\mathcal{X}} p(x) \ln q_\theta(x) d\lambda(x) = \mathbb{E}_{X \sim P}[-\ln q_\theta(X)]$$

**Exemple 2 : Entropie croisée pour un modèle imparfait**
Reprenons la pièce biaisée $P$ (Bernoulli $p=0,2$).
Supposons qu'un modèle naïf $Q_\theta$ estime que la pièce est équilibrée : $q(0)=0,5$ et $q(1)=0,5$.
La cross-entropy est :
$$H(P, Q_\theta) = - (P(X=1) \ln q(1) + P(X=0) \ln q(0))$$
$$H(P, Q_\theta) = - (0,2 \ln(0,5) + 0,8 \ln(0,5)) = - \ln(0,5) = \ln(2) \approx 0,693 \text{ nats}.$$
On remarque que $H(P, Q_\theta) > H(P)$. Le modèle équilibré est "surpris" par les résultats réels plus souvent qu'un modèle parfait ne le serait.



**Exemple 3 : Entropie d'un système déterministe**
Considérons une source $P$ qui émet toujours le même symbole $X=A$ avec certitude : $P(X=A) = 1$ et $P(X \neq A) = 0$.
L'entropie de cette source est :
$$H(P) = - (1 \ln(1)) = 0$$
L'incertitude est nulle. On ne peut extraire aucune information d'un tel système.

**Exemple 4 : Cross-Entropy infinie**
Soit un modèle $Q_\theta$ qui affirme avec certitude qu'une pièce tombera sur "Pile" : $q(Pile)=1, q(Face)=0$.
Si la vraie distribution $P$ est une pièce équilibrée $P(Pile)=0,5, P(Face)=0,5$.
La cross-entropy est :
$$H(P, Q_\theta) = - (0,5 \ln(1) + 0,5 \ln(0))$$
Or $\ln(0) \to -\infty$. La fonction de perte devient infinie. Le modèle est infiniment surpris et donc infiniment pénalisé pour avoir attribué une probabilité nulle à un événement réel.

**Exemple 5 : Divergence KL et compression**
Pour compresser des données issues d'une source $P$ (Entropie $H(P) = 2$ bits), on utilise un encodeur optimisé pour une loi $Q$.
La cross-entropy est mesurée à $H(P, Q) = 2,5$ bits.
La perte d'efficacité par symbole est exactement la divergence KL :
$$D_{KL}(P \| Q) = 2,5 - 2 = 0,5 \text{ bits/symbole}.$$
C'est le coût direct de modéliser $P$ par $Q$.

**Exemple 6 : Optimisation d'un modèle de langage**
Un LLM naïf prédit chaque lettre de l'alphabet latin (26 lettres) de manière uniforme : $q=1/26$.
La cross-entropy avec un texte français $P$ est :
$$H(P, Q) = - \sum_{x} p(x) \ln(1/26) = \ln(26) \approx 3,25 \text{ nats}.$$
Après entraînement sur un corpus, le modèle $Q^*$ apprend la vraie distribution $P$.
L'entropie de Shannon du français est estimée à environ $H(P) \approx 2,1 \text{ nats}$.
La perte du modèle va chuter de 3,25 à 2,1, atteignant le plancher théorique d'incertitude.

**Exemple 7 : Calcul sur une distribution continue (Entropie différentielle)**
Soit une variable aléatoire $X$ suivant une loi uniforme sur $[0, 2]$. La densité est $p(x) = 0,5$ sur ce segment.
Son entropie différentielle est :
$$H(X) = - \int_0^2 0,5 \ln(0,5) dx = - \ln(0,5) \int_0^2 0,5 dx = - \ln(0,5) \times 1 = \ln(2) \approx 0,69 \text{ nats}.$$

\begin{center}
\begin{tikzpicture}[scale=1]
  \draw[->,thick] (-0.5,0) -- (5,0) node[right] {Espace des modèles $\Theta$};
  \draw[->,thick] (0,-0.5) -- (0,4) node[above] {Perte / Information};

  % H(P)
  \draw[dashed, blue, thick] (0, 1.5) -- (4.5, 1.5) node[right] {$H(P)$ (Entropie)};

  % H(P, Q)
  \draw[red, thick] (0.5, 3.8) .. controls (1.5, 1.8) and (3, 1.5) .. (4.5, 1.6) node[above] {$H(P, Q_\theta)$};

  % D_KL
  \draw[<->, purple, thick] (3.5, 1.5) -- (3.5, 1.7) node[midway, right] {$D_{KL}$};
\end{tikzpicture}
\end{center}

> **Théorème 1 (Borne inférieure de l'entropie croisée) :**
> Pour toute distribution $Q_\theta$, l'entropie croisée est majorée inférieurement par l'entropie de Shannon :
> $$H(P, Q_\theta) \ge H(P)$$
> De plus, $H(P, Q_\theta) = H(P)$ si et seulement si $Q_\theta = P$ presque partout.

*Démonstration :*
On introduit la divergence de Kullback-Leibler $D_{KL}(P \| Q_\theta)$ :
$$D_{KL}(P \| Q_\theta) = \int_{\mathcal{X}} p(x) \ln \left( \frac{p(x)}{q_\theta(x)} \right) d\lambda(x)$$
Par l'inégalité de Jensen appliquée à la fonction convexe $-\ln(t)$ :
$$D_{KL}(P \| Q_\theta) = - \int_{\mathcal{X}} p(x) \ln \left( \frac{q_\theta(x)}{p(x)} \right) d\lambda(x) \ge - \ln \left( \int_{\mathcal{X}} p(x) \frac{q_\theta(x)}{p(x)} d\lambda(x) \right) = - \ln \left( \int_{\mathcal{X}} q_\theta(x) d\lambda(x) \right) = - \ln(1) = 0$$
En développant $D_{KL}(P \| Q_\theta)$ :
$$D_{KL}(P \| Q_\theta) = \int_{\mathcal{X}} p(x) \ln p(x) d\lambda(x) - \int_{\mathcal{X}} p(x) \ln q_\theta(x) d\lambda(x) = -H(P) + H(P, Q_\theta)$$
Par conséquent :
$$H(P, Q_\theta) = H(P) + D_{KL}(P \| Q_\theta)$$
Comme $D_{KL}(P \| Q_\theta) \ge 0$, nous obtenons $H(P, Q_\theta) \ge H(P)$. La stricte convexité de $-\ln$ assure l'égalité ssi $P=Q_\theta$ p.p.

## Démonstration Exhaustive de la Convergence Empirique

Dans un cadre d'apprentissage automatique, nous ne connaissons pas $P$, nous ne disposons que d'un ensemble de données d'entraînement $\{x_1, \dots, x_n\}$ tiré de manière indépendante et identiquement distribuée (i.i.d.) selon $P$. L'entraînement du modèle consiste à minimiser la **perte empirique** (Negative Log-Likelihood) :
$$\hat{H}_n(\theta) = - \frac{1}{n} \sum_{i=1}^n \ln q_\theta(x_i)$$

> **Théorème 2 (Convergence presque sûre de la perte empirique) :**
> Soit $\theta$ fixé. Sous la condition d'intégrabilité $\mathbb{E}_{X \sim P}[|\ln q_\theta(X)|] < \infty$, nous avons la convergence presque sûre :
> $$\hat{H}_n(\theta) \xrightarrow{p.s.} H(P, Q_\theta)$$
> lorsque $n \to \infty$.

*Démonstration pas-à-pas :*
1. Considérons les variables aléatoires $Y_i = - \ln q_\theta(x_i)$ pour $i \in \{1, \dots, n\}$.
2. Puisque les variables $x_i$ sont i.i.d. selon la loi $P$, les compositions $Y_i = -\ln q_\theta(x_i)$ sont également des variables aléatoires indépendantes et identiquement distribuées.
3. Calculons l'espérance mathématique de la variable $Y_1$ :
   $$\mathbb{E}[Y_1] = \mathbb{E}_{X \sim P}[-\ln q_\theta(X)]$$
4. Par définition de l'entropie croisée, nous avons exactement :
   $$\mathbb{E}[Y_1] = H(P, Q_\theta)$$
5. L'hypothèse $\mathbb{E}_{X \sim P}[|\ln q_\theta(X)|] < \infty$ implique que $\mathbb{E}[|Y_1|] < \infty$.
6. Nous pouvons alors invoquer la Loi Forte des Grands Nombres de Kolmogorov (LFGN, Jalon 92) sur la suite $(Y_i)_{i \ge 1}$ :
   $$\frac{1}{n} \sum_{i=1}^n Y_i \xrightarrow{p.s.} \mathbb{E}[Y_1]$$
7. En remplaçant par les définitions :
   $$- \frac{1}{n} \sum_{i=1}^n \ln q_\theta(x_i) \xrightarrow{p.s.} H(P, Q_\theta)$$
   Soit $\hat{H}_n(\theta) \xrightarrow{p.s.} H(P, Q_\theta)$.

Cette démonstration rigoureuse montre que, sur de grands jeux de données, la minimisation de la perte empirique équivaut à minimiser l'entropie croisée théorique, rapprochant ainsi le modèle de l'entropie asymptotique de Shannon.

## Applications à l'Intelligence Artificielle et à la Physique

- **Limite Fondamentale de l'Apprentissage :** Si la vraie distribution des données $P$ contient du bruit stochastique, $H(P) > 0$. Un modèle de langage massif ne pourra jamais atteindre une perte nulle. L'entraînement atteindra un plateau dicté par l'incertitude irréductible du langage.
- **Théorie du Codage :** D'après le théorème de codage source de Shannon, $H(P, Q_\theta)$ représente la longueur moyenne du code (en nats ou bits) pour compresser les données en utilisant le modèle $Q_\theta$, tandis que $H(P)$ est la limite théorique de compression. Optimiser un modèle de langage revient strictement à optimiser un compresseur de données.

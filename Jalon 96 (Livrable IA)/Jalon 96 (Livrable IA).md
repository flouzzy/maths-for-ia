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

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous essayiez de deviner quel sera le prochain mot d'une phrase.
    - La **Réalité ($P$)**, c'est la manière dont les gens parlent vraiment. Cette réalité a un niveau de "surprise" inévitable : on ne peut pas tout deviner (c'est l'**Entropie de Shannon**).
    - Votre **Modèle ($Q$)**, c'est votre cerveau artificiel qui essaie d'imiter les gens.
    - La **Cross-Entropy**, c'est votre score de mauvaise haleine : plus vous êtes surpris par les vrais mots, plus votre score est élevé.
    - Ce jalon prouve que si vous entraînez votre modèle sur des milliards de phrases, votre score de surprise va finir par se stabiliser et atteindre le niveau de surprise minimal de la langue elle-même. On ne peut pas faire mieux que la réalité.
- **Le "Pourquoi on a inventé ça" :** Pour savoir si l'entraînement d'un LLM (comme ChatGPT) a une fin. On veut savoir s'il existe une limite théorique à la précision d'un modèle de langage. Ce lien mathématique unit la probabilité pure et la science de l'information.
- **Visualisation :** Une courbe de perte qui descend au fil du temps. Elle ne descend pas jusqu'à zéro, elle s'écrase sur un "plancher" invisible. Ce plancher, c'est l'entropie de la source de données.

## 2. Formalisation

Soit $(\mathcal{X}, \mathcal{B}(\mathcal{X}))$ un espace de données. Soit $P$ la distribution réelle des données (inconnue) et $Q_\theta$ la distribution prédite par un modèle paramétré par $\theta$.

### A. Définitions Informationnelles

> **Définition 1 (Entropie de Shannon) :**
> L'entropie de la source de données $P$ est :
> $H(P) = - \int_{\mathcal{X}} p(x) \ln p(x) d\lambda(x) = \mathbb{E}_{X \sim P}[-\ln p(X)]$
> Elle mesure la quantité d'information (ou d'incertitude) intrinsèque aux données.

> **Définition 2 (Cross-Entropy) :**
> La cross-entropy entre $P$ et $Q_\theta$ est :
> $H(P, Q_\theta) = - \int_{\mathcal{X}} p(x) \ln q_\theta(x) d\lambda(x) = \mathbb{E}_{X \sim P}[-\ln q_\theta(X)]$

### B. Lien Fondamental

On a la relation directe avec la divergence KL (Jalon 72) :
$$H(P, Q_\theta) = H(P) + D_{KL}(P \| Q_\theta)$$
Comme $D_{KL} \ge 0$, on a toujours $H(P, Q_\theta) \ge H(P)$. L'entropie réelle est le plancher de la fonction de perte.

## 3. Démonstrations

### Démonstration de la convergence de la perte empirique

Lors de l'entraînement, on ne connaît pas $H(P, Q_\theta)$. On calcule la **perte empirique** sur un échantillon IID $x_1, \dots, x_n$ :
$$\hat{H}_n(\theta) = - \frac{1}{n} \sum_{i=1}^n \ln q_\theta(x_i)$$

1. **Variables Aléatoires :** Posons $Y_i = -\ln q_\theta(x_i)$. Comme les $x_i$ sont IID de loi $P$, les $Y_i$ sont des variables aléatoires IID.
2. **Espérance :** $\mathbb{E}[Y_1] = \mathbb{E}_{X \sim P}[-\ln q_\theta(X)] = H(P, Q_\theta)$.
3. **Application de la LFGN :** D'après la Loi Forte des Grands Nombres (Jalon 92), si l'espérance est finie :
   $$\frac{1}{n} \sum_{i=1}^n Y_i \xrightarrow{p.s.} \mathbb{E}[Y_1]$$
4. **Conclusion :**
   $$\hat{H}_n(\theta) \xrightarrow{p.s.} H(P, Q_\theta)$$
5. **Conséquence pour l'optimisation :** En minimisant $\hat{H}_n(\theta)$ sur un jeu de données de plus en plus grand, on tend vers la minimisation de $D_{KL}(P \| Q_\theta)$. Si le modèle est assez riche (Jalon 60), on peut espérer $Q_\theta \to P$, et donc $\hat{H}_n \to H(P)$.

## 4. Exercices d'Application

### Exercice 1 : Entropie d'un texte binaire
**Énoncé :** Un texte est composé uniquement de '0' (avec probabilité $p$) et de '1' (avec probabilité $1-p$). Quelle est la perte Cross-Entropy minimale d'un modèle de langage sur ce texte ?
**Correction Détaillée :**
1. La perte minimale est atteinte quand le modèle connaît parfaitement les probabilités : $q(0)=p$ and $q(1)=1-p$.
2. Elle est égale à l'entropie de la source : $H(P) = -p \ln p - (1-p) \ln (1-p)$.
3. Si $p=0.5$ (hasard total), $H(P) = \ln 2 \approx 0.69$ nats. C'est l'information maximale.
4. Si $p=1$ (texte prévisible), $H(P) = 0$. On ne peut pas être surpris.

### Exercice 2 : Niveau Avancé (Lien avec la Perplexité)
**Énoncé :** En NLP, on utilise souvent la Perplexité $PP = \exp(H(P, Q))$. Si un modèle a une perplexité de 10 sur un dictionnaire de 1000 mots, comment l'interpréter ?
**Correction Détaillée :**
Une perplexité de 10 signifie que le modèle est "aussi surpris" que s'il devait choisir uniformément entre 10 mots à chaque étape. Bien qu'il y ait 1000 mots possibles, la structure de la langue (apprise par le modèle) a réduit l'incertitude effective à seulement 10 choix probables.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** Ce jalon explique pourquoi nous utilisons la **Log-Likelihood** comme objectif d'entraînement. C'est la seule fonction de perte qui possède ce lien direct avec la limite fondamentale de l'information (Théorie de Shannon).
- **Example Concret :**
    - **Large Language Models (GPT-4, Llama) :** L'entraînement consiste à réduire la Cross-Entropy sur des téraoctets de texte. On observe que la perte suit une "Scaling Law" (loi de puissance) : elle diminue de manière prévisible en fonction de la taille du modèle et des données, tendant vers l'entropie du langage humain.
    - **Compression de données (Arithmetic Coding) :** Un modèle d'IA avec une faible Cross-Entropy peut être utilisé pour compresser des fichiers. La longueur du fichier compressé sera exactement $n \times H(P, Q)$. Plus le modèle est bon en IA, meilleur il est en compression.
    - **Détection d'anomalies :** Si un nouveau texte a une Cross-Entropy beaucoup plus élevée que la moyenne pour un modèle donné, c'est qu'il est "surprenant" (hors distribution).

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 92 (Loi forte des grands nombres (LFGN)).md]], [[Jalon 72 (Livrable IA).md]]
- **Concepts Futurs dépendants :** [[Jalon 135 (Complexité de Rademacher).md]], [[Jalon 144 (Le phénomène de double descente).md]]

---
uuid: "jalon-72"
title: "Livrable IA T6 : Formalisation de la divergence de Kullback-Leibler"
year: 2
trimester: 6
tags:
  - math/probabilites
  - ia/theorie-information
prev: "[[Jalon 71 (Théorèmes de Fubini-Tonelli).md]]"
next: "[[Jalon 73 (Définition des espaces Lp).md]]"
---

# Jalon 72 : Formalisation de la divergence de Kullback-Leibler

## 1. Genèse de la Théorie de l'Information et Divergence

En 1951, Solomon Kullback et Richard Leibler cherchaient à quantifier la différence d'information entre deux distributions de probabilités, dans la continuité des travaux de Claude Shannon sur l'entropie. En théorie de l'information, lorsqu'on encode des événements d'une distribution $P$ en utilisant un code optimisé pour une autre distribution $Q$, on observe une inefficacité, une perte d'information. La divergence de Kullback-Leibler (ou entropie relative) a été formulée pour mesurer exactement cette inefficacité, ce "surcoût" de bits ou de "nats".
Bien qu'elle ne soit pas une métrique géométrique classique en raison de son asymétrie, elle est devenue le pilier fondamental des statistiques, de la théorie des probabilités, et de l'optimisation en apprentissage automatique. C'est l'outil mathématique par excellence pour mesurer à quel point un modèle de croyance diffère de la réalité observée.

## 2. Définitions et Théorèmes Fondamentaux

Soit $(\mathcal{X}, \mathcal{F}, \lambda)$ un espace mesuré (généralement $\mathbb{R}^n$ avec la mesure de Lebesgue pour des variables continues, ou la mesure de comptage pour des variables discrètes). Soient $P$ et $Q$ deux mesures de probabilité sur cet espace. On suppose que $P$ et $Q$ admettent des densités $p$ et $q$ par rapport à $\lambda$.

### Définition de la Divergence KL

La divergence de Kullback-Leibler de $Q$ par rapport à $P$ est définie par l'intégrale de Lebesgue :
$$D_{KL}(P \| Q) = \int_{\mathcal{X}} p(x) \ln\left( \frac{p(x)}{q(x)} \right) d\lambda(x)$$
*Hypothèse cruciale (Continuité absolue) :* On suppose que $P \ll Q$, c'est-à-dire que pour tout $A \in \mathcal{F}$, $Q(A)=0 \implies P(A)=0$ (ou $q(x)=0 \implies p(x)=0$ presque partout). Si cette condition n'est pas remplie, on pose formellement $D_{KL}(P \| Q) = +\infty$.

Par convention, on pose $0 \ln(0/q) = 0$ et $p \ln(p/0) = +\infty$.

**Typage des variables :**
- $\mathcal{X}$ : Espace d'état (ex: $\mathbb{R}^d$).
- $\lambda$ : Mesure de référence (ex: mesure de Lebesgue).
- $P, Q$ : Mesures de probabilité.
- $p, q$ : Densités de probabilité respectives, i.e., des fonctions de $\mathcal{X} \to \mathbb{R}^+$ d'intégrale $1$.

### Inégalité de Gibbs (Positivité)

Pour toutes distributions de probabilité $P$ et $Q$ sur $\mathcal{X}$ :
$$D_{KL}(P \| Q) \ge 0$$
L'égalité $D_{KL}(P \| Q) = 0$ a lieu si et seulement si $P = Q$ presque partout (i.e. $p(x) = q(x)$ p.p.).

### Asymétrie et Non-métricité

En général, $D_{KL}(P \| Q) \neq D_{KL}(Q \| P)$. Par ailleurs, elle ne vérifie pas l'inégalité triangulaire. Ce n'est donc pas une distance au sens topologique.

### Exemple Concret 1 : Deux lois exponentielles

Soient deux lois exponentielles $P \sim \mathcal{E}(\lambda_1)$ et $Q \sim \mathcal{E}(\lambda_2)$ sur $\mathbb{R}^+$.
Densités : $p(x) = \lambda_1 e^{-\lambda_1 x}$ et $q(x) = \lambda_2 e^{-\lambda_2 x}$ pour $x \ge 0$.
Calculons $D_{KL}(P \| Q)$ :
$$\ln\left(\frac{p(x)}{q(x)}\right) = \ln\left(\frac{\lambda_1}{\lambda_2}\right) - \lambda_1 x + \lambda_2 x = \ln\left(\frac{\lambda_1}{\lambda_2}\right) + (\lambda_2 - \lambda_1)x$$
$$D_{KL}(P \| Q) = \int_0^\infty \lambda_1 e^{-\lambda_1 x} \left( \ln\left(\frac{\lambda_1}{\lambda_2}\right) + (\lambda_2 - \lambda_1)x \right) dx$$
Puisque $\int_0^\infty \lambda_1 e^{-\lambda_1 x} dx = 1$ et $\int_0^\infty x \lambda_1 e^{-\lambda_1 x} dx = \mathbb{E}_P[X] = \frac{1}{\lambda_1}$,
$$D_{KL}(P \| Q) = \ln\left(\frac{\lambda_1}{\lambda_2}\right) + \frac{\lambda_2 - \lambda_1}{\lambda_1} = \ln\left(\frac{\lambda_1}{\lambda_2}\right) + \frac{\lambda_2}{\lambda_1} - 1$$
**Vérification numérique :** Si $\lambda_1 = 2, \lambda_2 = 1$, $D_{KL} = \ln(2) + 1/2 - 1 = \ln(2) - 0.5 \approx 0.693 - 0.5 = 0.193 > 0$. L'asymétrie est claire si on échange les rôles.

### Exemple Concret 2 : Variables discrètes de Bernoulli

Soit $P \sim \mathcal{B}(p)$ et $Q \sim \mathcal{B}(q)$. (Mesure de référence = mesure de comptage sur $\{0, 1\}$).
$$D_{KL}(P \| Q) = p \ln\left(\frac{p}{q}\right) + (1-p) \ln\left(\frac{1-p}{1-q}\right)$$
Si $p = 0.5$ et $q = 0.1$ :
$$D_{KL} = 0.5 \ln\left(\frac{0.5}{0.1}\right) + 0.5 \ln\left(\frac{0.5}{0.9}\right) = 0.5 \ln(5) + 0.5 \ln(5/9) = 0.5 \ln(25/9) \approx 0.51 > 0.$$

### Cas limite / Pathologie

Si $p = 0.5$ et $q = 0$ ou $q = 1$. Par exemple, si le modèle $Q$ est absolument certain d'un événement (ex: $q=1$ pour 'pile'), mais que l'événement réel $P$ l'autorise (ex: $p=0.5$). Alors la divergence $D_{KL}$ "explose" vers $+\infty$. Un modèle qui assigne une probabilité $0$ à un événement qui se produit en réalité subit un coût infini.

## 3. Démonstrations Rigoureuses

### Preuve de l'Inégalité de Gibbs

Nous allons démontrer que $D_{KL}(P \| Q) \ge 0$ en utilisant l'inégalité de Jensen.

1. **Reformulation :**
Par définition :
$$D_{KL}(P \| Q) = \int_{\mathcal{X}} p(x) \left( - \ln\left( \frac{q(x)}{p(x)} \right) \right) d\lambda(x) = \mathbb{E}_{X \sim P}\left[ -\ln\left( \frac{q(X)}{p(X)} \right) \right]$$

2. **Propriétés de la fonction :**
Soit $\phi(t) = -\ln(t)$. La fonction $\phi$ est strictement convexe sur $\mathbb{R}^{+*}$, puisque $\phi''(t) = \frac{1}{t^2} > 0$.

3. **Application de l'Inégalité de Jensen :**
Pour toute variable aléatoire $Y$ (intégrable) et toute fonction strictement convexe $\phi$, on a :
$$\mathbb{E}[\phi(Y)] \ge \phi(\mathbb{E}[Y])$$
Soit la variable aléatoire $Y = \frac{q(X)}{p(X)}$ sous la probabilité $P$.
$$D_{KL}(P \| Q) = \mathbb{E}_P[\phi(Y)] \ge \phi(\mathbb{E}_P[Y])$$

4. **Calcul de l'espérance interne :**
$$\mathbb{E}_P[Y] = \int_{\mathcal{X}} \left( \frac{q(x)}{p(x)} \right) p(x) d\lambda(x) = \int_{\mathcal{X}} q(x) d\lambda(x)$$
Puisque $Q$ est une mesure de probabilité, l'intégrale de sa densité $q(x)$ sur tout l'espace vaut 1 (en supposant que le support de $p$ est inclus dans le support de $q$, sinon la divergence est $+\infty \ge 0$ trivialement).
$$\mathbb{E}_P[Y] = 1$$

5. **Conclusion :**
$$D_{KL}(P \| Q) \ge \phi(1) = -\ln(1) = 0$$
L'égalité est atteinte si et seulement si la variable aléatoire $Y$ est constante presque partout par rapport à $P$.
C'est-à-dire $\frac{q(X)}{p(X)} = 1$ p.p., donc $p(x) = q(x)$ presque partout pour $\lambda$.

## 4. Applications en Intelligence Artificielle

L'asymétrie de la divergence KL a des conséquences profondes en Intelligence Artificielle, notamment pour les algorithmes génératifs et l'inférence.

**1. Apprentissage de Modèle (Forward KL : $D_{KL}(P_{data} \| P_{\theta})$) :**
L'apprentissage supervisé standard (Cross-Entropy) minimise cette divergence.
$$D_{KL}(P_{data} \| P_{\theta}) = \mathbb{E}_{x \sim P_{data}}[\ln P_{data}(x)] - \mathbb{E}_{x \sim P_{data}}[\ln P_{\theta}(x)]$$
Minimiser la Forward KL revient exactement à maximiser la log-vraisemblance (Maximum Likelihood Estimation). Le modèle "couvre" la réalité. S'il met $P_{\theta}(x) \to 0$ là où $P_{data}(x) > 0$, la pénalité est infinie (mode covering, le modèle tend à être large et flou).

**2. Inférence Variationnelle (Reverse KL : $D_{KL}(P_{\theta} \| P_{data})$) :**
Utilisée dans les Variational Autoencoders (VAEs). Ici, l'espérance est prise sous la distribution du modèle $P_{\theta}$. Cette minimisation pousse le modèle à se concentrer uniquement sur les modes de la distribution de données (mode seeking). S'il met de la masse $P_{\theta}(x) > 0$ là où $P_{data}(x) = 0$, il est pénalisé.

**3. Apprentissage par Renforcement (PPO - Proximal Policy Optimization) :**
Dans les algorithmes de gradient de politique, on limite la taille de la mise à jour des poids en contraignant la divergence KL entre l'ancienne politique et la nouvelle politique :
$$D_{KL}(\pi_{old}(\cdot | s) \| \pi_{new}(\cdot | s)) \le \delta$$
Cela garantit une amélioration monotone sans détruire de manière catastrophique l'apprentissage précédent.

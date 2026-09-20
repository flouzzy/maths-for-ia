---
uuid: "jalon-74"
title: "Inégalités fondamentales : Hölder, Minkowski, Jensen"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/optimisation
prev: "[[Jalon 73 (Définition des espaces Lp).md]]"
next: "[[Jalon 75 (Preuve de la complétude des espaces Lp).md]]"
---

# Inégalités fondamentales : Hölder, Minkowski, Jensen

## 1. Introduction

L'analyse fonctionnelle et l'étude des espaces d'intégration (comme les espaces $L^p$) reposent sur la maîtrise des tailles et des distances entre les fonctions. En sciences physiques et mathématiques appliquées, on ne connaît presque jamais la solution exacte à un problème complexe. On se contente d'approximations dont il faut impérativement contrôler l'erreur.

C'est là qu'interviennent les trois grandes inégalités fondamentales :
- **L'inégalité de Jensen** relie l'image de la moyenne d'une variable par une fonction convexe à la moyenne de ses images. Elle quantifie le bénéfice ou la perte induite par la courbure lors d'une combinaison d'états.
- **L'inégalité de Hölder** généralise Cauchy-Schwarz. Elle permet de majorer l'intégrale d'un produit par le produit des normes (mesurées avec des puissances conjuguées).
- **L'inégalité de Minkowski** n'est autre que l'inégalité triangulaire généralisée aux espaces $L^p$. Elle garantit que le plus court chemin reste la ligne droite, même lorsque la notion de distance devient très abstraite.

Ces outils constituent le socle de la théorie de l'intégration moderne et des statistiques avancées.

## 2. Définitions, Théorèmes et Exemples

### A. L'Inégalité de Jensen

Soit $(X, \mathcal{M}, \mu)$ un espace de probabilité, ce qui signifie que $\mu(X) = 1$. Soit $f$ une fonction intégrable à valeurs réelles, et $\phi : \mathbb{R} \to \mathbb{R}$ une fonction **convexe**.

> **Théorème (Inégalité de Jensen) :**
> $$\phi \left( \int_X f \, d\mu \right) \le \int_X \phi(f) \, d\mu$$
> En termes probabilistes, pour une variable aléatoire $Y$ : $\phi(\mathbb{E}[Y]) \le \mathbb{E}[\phi(Y)]$.

**Exemples concrets pour Jensen :**

1. **La fonction exponentielle :** La fonction $\phi(x) = \exp(x)$ est convexe. Si l'on prend une variable aléatoire uniforme $Y$ sur $[0, 1]$, l'espérance est $\mathbb{E}[Y] = 0.5$. L'inégalité de Jensen donne $\exp(0.5) \approx 1.648 \le \int_0^1 \exp(x) \, dx = e - 1 \approx 1.718$.
2. **Le carré :** La fonction $\phi(x) = x^2$ est convexe. Pour toute variable aléatoire, $(\mathbb{E}[Y])^2 \le \mathbb{E}[Y^2]$. Cela prouve instantanément que la variance $\text{Var}(Y) = \mathbb{E}[Y^2] - (\mathbb{E}[Y])^2$ est toujours positive ou nulle.
3. **Le logarithme (concavité) :** La fonction $\phi(x) = \ln(x)$ est concave, donc l'inégalité est inversée : $\ln(\mathbb{E}[Y]) \ge \mathbb{E}[\ln(Y)]$. Si $Y$ prend les valeurs $a$ et $b$ avec probabilité $\frac{1}{2}$, on obtient $\ln\left(\frac{a+b}{2}\right) \ge \frac{1}{2}\ln(a) + \frac{1}{2}\ln(b) = \ln(\sqrt{ab})$, d'où l'inégalité entre moyenne arithmétique et géométrique : $\frac{a+b}{2} \ge \sqrt{ab}$.
4. **L'inverse :** La fonction $\phi(x) = 1/x$ est convexe sur $\mathbb{R}^{+*}$. Ainsi, pour $Y > 0$, on a $\frac{1}{\mathbb{E}[Y]} \le \mathbb{E}\left[\frac{1}{Y}\right]$. Par exemple, pour $Y \in \{2, 4\}$ équiprobable, $\frac{1}{3} \le \frac{1}{2}(\frac{1}{2} + \frac{1}{4}) = \frac{3}{8}$ (soit $0.33 \le 0.375$).
5. **Entropie :** La fonction $\phi(x) = x \ln x$ est convexe pour $x>0$. Cela permet de démontrer la positivité de la divergence de Kullback-Leibler entre deux distributions, fondamentale en théorie de l'information.

### B. L'Inégalité de Hölder

Soient $p, q \in [1, +\infty]$ tels que $\frac{1}{p} + \frac{1}{q} = 1$. On dit que $p$ et $q$ sont des **exposants conjugués**.

> **Théorème (Inégalité de Hölder) :**
> Pour toutes fonctions mesurables $f \in L^p(\mu)$ et $g \in L^q(\mu)$, le produit $fg$ appartient à $L^1(\mu)$ et :
> $$\|fg\|_1 \le \|f\|_p \cdot \|g\|_q$$
> Soit $\int_X |f(x)g(x)| \, d\mu \le \left(\int_X |f(x)|^p \, d\mu\right)^{1/p} \left(\int_X |g(x)|^q \, d\mu\right)^{1/q}$.

**Exemples concrets pour Hölder :**

1. **Cas de Cauchy-Schwarz ($p=2, q=2$) :** Pour $f(x) = x$ et $g(x) = x^2$ sur $[0,1]$. $\|fg\|_1 = \int_0^1 x^3 dx = \frac{1}{4} = 0.25$. Les normes 2 sont $\|f\|_2 = (\int_0^1 x^2 dx)^{1/2} = \sqrt{1/3} \approx 0.577$ et $\|g\|_2 = (\int_0^1 x^4 dx)^{1/2} = \sqrt{1/5} \approx 0.447$. Le produit est $\approx 0.258$. L'inégalité est vérifiée : $0.25 \le 0.258$.
2. **Couples (3, 3/2) sur espace discret :** Vecteurs dans $\mathbb{R}^2$ : $u = (1, 8)$, $v = (27, 0)$. Avec $p=3$ et $q=\frac{3}{2}$. Le produit scalaire est $|u \cdot v| = 1 \times 27 + 8 \times 0 = 27$. Normes : $\|u\|_3 = (1^3 + 8^3)^{1/3} = (1+512)^{1/3} \approx 8.005$. $\|v\|_{3/2} = (27^{3/2} + 0)^{2/3} = 27$. Le produit est $8.005 \times 27 \approx 216$. L'inégalité $27 \le 216$ est triviale mais vraie.
3. **Cas extrême $(p=1, q=\infty)$ :** Sur $[0, 2]$, $f(x) = x$, $g(x) = 3$. $\|f\|_1 = \int_0^2 x dx = 2$. $\|g\|_\infty = 3$. L'intégrale de $fg$ est $\int_0^2 3x dx = 6$. On a exactement l'égalité $6 \le 2 \times 3 = 6$.
4. **Vecteurs (4, 4/3) :** $x=(1, 2)$, $y=(1, 1)$. Produit : $1 \times 1 + 2 \times 1 = 3$. $\|x\|_4 = (1+16)^{1/4} = 17^{1/4} \approx 2.03$. $\|y\|_{4/3} = (1 + 1)^{3/4} = 2^{0.75} \approx 1.68$. Le produit donne $\approx 3.41$. $3 \le 3.41$.
5. **Inclusion des espaces $L^p$ :** Si la mesure de l'espace est finie $\mu(X) < \infty$, Hölder permet de prouver que si $p_1 < p_2$, alors $L^{p_2} \subset L^{p_1}$. En prenant $g(x)=1$, $\|f\|_{p_1}^{p_1} = \int |f|^{p_1} \cdot 1 \le \| |f|^{p_1} \|_{p_2/p_1} \|1\|_{q} = \|f\|_{p_2}^{p_1} \mu(X)^{1/q}$.

### C. L'Inégalité de Minkowski

> **Théorème (Inégalité de Minkowski) :**
> Pour tout $p \in [1, +\infty]$ et pour toutes fonctions mesurables $f, g \in L^p(\mu)$ :
> $$\|f+g\|_p \le \|f\|_p + \|g\|_p$$

**Exemples concrets pour Minkowski :**

1. **Norme euclidienne ($p=2$) dans $\mathbb{R}^2$ :** $u = (3, 0)$ et $v = (0, 4)$. $u+v = (3, 4)$. $\|u\|_2 = 3$, $\|v\|_2 = 4$. $\|u+v\|_2 = \sqrt{3^2 + 4^2} = 5$. L'inégalité $5 \le 3 + 4 = 7$ est bien vérifiée (c'est le triangle de Pythagore).
2. **Norme de Manhattan ($p=1$) :** Mêmes vecteurs. $\|u\|_1 = 3$, $\|v\|_1 = 4$. $\|u+v\|_1 = |3| + |4| = 7$. On obtient l'égalité $7 \le 3+4=7$.
3. **Norme du Sup ($p=\infty$) :** Mêmes vecteurs. $\|u\|_\infty = 3$, $\|v\|_\infty = 4$. $\|u+v\|_\infty = \max(3, 4) = 4$. $4 \le 3 + 4 = 7$.
4. **Sur des fonctions ($p=3$) :** Sur $[0, 1]$, $f(x) = x$, $g(x) = 1-x$. $f+g = 1$. $\|f+g\|_3 = (\int_0^1 1 dx)^{1/3} = 1$. $\|f\|_3 = (\int_0^1 x^3 dx)^{1/3} = (1/4)^{1/3} \approx 0.63$. $\|g\|_3 = (1/4)^{1/3} \approx 0.63$. On a bien $1 \le 0.63 + 0.63 = 1.26$.
5. **Cas pathologique d'annulation :** Si $f(x) = x$ et $g(x) = -x$. $f+g = 0 \implies \|f+g\|_p = 0$. Les normes de $f$ et $g$ sont positives, donc $0 \le \|f\|_p + \|g\|_p$ est toujours vrai de manière stricte sauf si $f$ est nulle presque partout.

## 3. Démonstrations

### Lemme préliminaire : L'Inégalité de Young
Pour tous $a, b \ge 0$ et $p, q > 1$ conjugués ($\frac{1}{p} + \frac{1}{q} = 1$) :
$$ab \le \frac{a^p}{p} + \frac{b^q}{q}$$
**Démonstration :** La fonction logarithme naturel est strictement concave sur $\mathbb{R}^{+*}$. Puisque $\frac{1}{p} + \frac{1}{q} = 1$, on peut utiliser l'inégalité de convexité (ou plutôt de concavité, ce qui correspond à une application de Jensen inversée sur une somme finie) :
$$\ln\left(\frac{1}{p} a^p + \frac{1}{q} b^q\right) \ge \frac{1}{p} \ln(a^p) + \frac{1}{q} \ln(b^q) = \frac{p}{p}\ln(a) + \frac{q}{q}\ln(b) = \ln(ab)$$
En passant à l'exponentielle (fonction strictement croissante), on obtient le résultat directement.

### Démonstration de l'inégalité de Hölder
1. Si $\|f\|_p = 0$ ou $\|g\|_q = 0$, alors $f=0$ p.p. ou $g=0$ p.p. Le produit $fg=0$ p.p., et l'inégalité $0 \le 0$ est évidente.
2. Écartons le cas trivial et posons les fonctions normalisées :
   $$u(x) = \frac{|f(x)|}{\|f\|_p} \quad \text{et} \quad v(x) = \frac{|g(x)|}{\|g\|_q}$$
3. Pour chaque point $x \in X$, on applique l'inégalité de Young :
   $$u(x)v(x) \le \frac{u(x)^p}{p} + \frac{v(x)^q}{q}$$
4. On intègre cette inégalité sur tout l'espace $X$ par rapport à la mesure $\mu$ (la monotonie de l'intégrale le permet car tout est positif) :
   $$\int_X u(x)v(x) \, d\mu \le \frac{1}{p} \int_X u(x)^p \, d\mu + \frac{1}{q} \int_X v(x)^q \, d\mu$$
5. Calculons les intégrales de droite :
   $$\int_X u^p \, d\mu = \int_X \frac{|f|^p}{\|f\|_p^p} \, d\mu = \frac{1}{\|f\|_p^p} \int_X |f|^p \, d\mu = 1$$
   De même, $\int_X v^q \, d\mu = 1$.
6. On substitue ces valeurs dans l'inégalité intégrée :
   $$\int_X \frac{|f(x)g(x)|}{\|f\|_p \|g\|_q} \, d\mu \le \frac{1}{p} \cdot 1 + \frac{1}{q} \cdot 1 = 1$$
7. En multipliant les deux membres par le dénominateur constant, on conclut :
   $$\|fg\|_1 = \int_X |fg| \, d\mu \le \|f\|_p \cdot \|g\|_q$$

### Démonstration de l'inégalité de Minkowski
1. Le cas $p=1$ est la conséquence directe de l'inégalité triangulaire pour les réels/complexes : $|f(x)+g(x)| \le |f(x)| + |g(x)|$. En intégrant, on a le résultat. Le cas $p=\infty$ est similaire par passage au supremum essentiel. Supposons donc $1 < p < \infty$.
2. Remarquons que $|f+g|^p = |f+g| \cdot |f+g|^{p-1} \le |f| \cdot |f+g|^{p-1} + |g| \cdot |f+g|^{p-1}$.
3. Intégrons cette inégalité sur $X$ :
   $$\int_X |f+g|^p \, d\mu \le \int_X |f| |f+g|^{p-1} \, d\mu + \int_X |g| |f+g|^{p-1} \, d\mu$$
4. Appliquons l'inégalité de Hölder à chaque terme du membre de droite, en conjuguant $p$ avec $q$ (où $q = \frac{p}{p-1}$, donc $(p-1)q = p$) :
   $$\int_X |f| |f+g|^{p-1} \, d\mu \le \|f\|_p \left( \int_X |f+g|^{(p-1)q} \, d\mu \right)^{1/q} = \|f\|_p \|f+g\|_p^{p/q}$$
   Et de même pour le terme avec $g$.
5. On a donc :
   $$\|f+g\|_p^p \le (\|f\|_p + \|g\|_p) \|f+g\|_p^{p/q}$$
6. Si $\|f+g\|_p = 0$, le théorème est trivial. Sinon, on divise par $\|f+g\|_p^{p/q}$. Sachant que $p - \frac{p}{q} = p(1 - \frac{1}{q}) = p \cdot \frac{1}{p} = 1$, on obtient finalement :
   $$\|f+g\|_p \le \|f\|_p + \|g\|_p$$

## 4. Applications en Physique, Logique et IA

L'inégalité de Jensen est la pierre angulaire de très nombreuses preuves dans les domaines de l'optimisation et des probabilités appliquées.

- **Divergence de Kullback-Leibler et Théorie de l'Information :**
  La divergence $D_{KL}(P || Q) = \int p(x) \ln \frac{p(x)}{q(x)} dx$ mesure la différence d'information entre deux distributions. L'inégalité de Jensen appliquée à la fonction strictement convexe $\phi(x) = -\ln(x)$ prouve de manière lumineuse que $D_{KL} \ge 0$. C'est cette positivité qui permet d'utiliser l'entropie croisée (Cross-Entropy) comme fonction de coût valide dans l'entraînement de tous les modèles d'apprentissage automatique modernes (LLMs, classification d'images).

- **Apprentissage Profond et Modèles Génératifs (VAE) :**
  Les Autoencodeurs Variationnels (VAE) cherchent à modéliser la distribution complexe des données d'un espace latent, nécessitant de maximiser la log-vraisemblance $\ln p(x)$. Le calcul exact de l'intégrale impliquée est intraitable. L'inégalité de Jensen est utilisée pour sortir l'intégrale du logarithme, donnant naissance à la limite inférieure nommée ELBO (Evidence Lower Bound) : $\ln \mathbb{E}[...] \ge \mathbb{E}[\ln(...) ]$. Optimiser l'ELBO est gérable par descente de gradient, ce qui rend l'entraînement possible.

- **Algorithme Expectation-Maximization (EM) :**
  Dans les problèmes statistiques contenant des variables latentes inobservées (par exemple, le clustering par mélanges de gaussiennes), l'algorithme EM itère en maximisant une borne inférieure de la vraisemblance à chaque étape. La garantie mathématique que cet algorithme converge vers un maximum local repose exclusivement sur des applications répétées de l'inégalité de Jensen.

- **Physique quantique et matrices de densité :**
  L'inégalité de Hölder est fondamentale pour analyser les opérateurs normés agissant sur les espaces de Hilbert, notamment dans la mesure des distances entre états quantiques (matrices de densité) sous l'action d'opérateurs bornés (Trace distance).

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

# Jalon 74 : Inégalités fondamentales : Hölder, Minkowski, Jensen

## 1. Genèse des Inégalités en Analyse Fonctionnelle

L'analyse fonctionnelle s'intéresse aux espaces de dimension infinie, en particulier les espaces de fonctions. Historiquement, l'étude des séries de Fourier par Dirichlet et Riemann a révélé la nécessité de quantifier la "taille" d'une fonction, non plus par son maximum (norme uniforme), mais par la somme ou l'intégrale de ses valeurs. Les espaces $L^p$, introduits par Henri Lebesgue et Frigyes Riesz au début du XXe siècle, formalisent cette idée.

Cependant, pour que ces ensembles de fonctions constituent de véritables espaces vectoriels normés, il fallait prouver des propriétés algébriques et topologiques fondamentales, notamment l'inégalité triangulaire. Hermann Minkowski, géomètre dans l'âme, a généralisé l'inégalité triangulaire euclidienne aux espaces $L^p$. Avant lui, Otto Hölder avait découvert une inégalité reliant les intégrales de produits de fonctions, indispensable pour majorer des termes croisés. Enfin, Johan Jensen, mathématicien danois, a formalisé les conséquences intégrales de la convexité géométrique, un concept qui trouve ses racines dans les travaux d'Archimède sur les barycentres.

Ces trois inégalités ne sont pas de simples astuces calculatoires ; elles sont les piliers de l'architecture des espaces fonctionnels, permettant de passer de la géométrie élémentaire à l'analyse moderne, et constituent aujourd'hui le socle théorique de l'optimisation convexe et de la théorie de l'apprentissage statistique.

## 2. Inégalité de Jensen : Convexité et Barycentres Intégraux

L'inégalité de Jensen est l'expression analytique du fait qu'une fonction convexe se situe toujours "en dessous" de ses cordes.

### A. Fonctions convexes

> **Définition (Fonction convexe) :**
> Soit $I \subset \mathbb{R}$ un intervalle. Une fonction $\phi : I \to \mathbb{R}$ est dite convexe si, pour tout $x, y \in I$ et pour tout $\lambda \in [0, 1]$ :
> $$\phi(\lambda x + (1 - \lambda)y) \le \lambda \phi(x) + (1 - \lambda)\phi(y)$$
> La fonction est dite strictement convexe si l'inégalité est stricte pour $x \neq y$ et $\lambda \in ]0, 1[$.

**Exemple concret immédiat :**
Soit $\phi(x) = x^2$ sur $\mathbb{R}$. Prenons $x=0, y=2, \lambda=0.5$.
$\lambda x + (1-\lambda)y = 0.5(0) + 0.5(2) = 1$.
$\phi(1) = 1^2 = 1$.
$\lambda \phi(x) + (1-\lambda)\phi(y) = 0.5(0^2) + 0.5(2^2) = 0.5(4) = 2$.
On a bien $1 \le 2$.

### B. Énoncé du Théorème de Jensen

> **Théorème (Inégalité de Jensen) :**
> Soit $(X, \mathcal{A}, \mu)$ un espace mesuré tel que $\mu(X) = 1$ (c'est-à-dire une mesure de probabilité). Soit $f \in L^1(\mu)$ une fonction à valeurs réelles telles que $f(x) \in I$ pour presque tout $x \in X$, où $I$ est un intervalle de $\mathbb{R}$.
> Si $\phi : I \to \mathbb{R}$ est une fonction convexe, et si $\phi \circ f$ est $\mu$-intégrable, alors :
> $$\phi\left(\int_X f(x) d\mu(x)\right) \le \int_X \phi(f(x)) d\mu(x)$$

*Remarque typologique :* $\int_X f d\mu$ est un réel (l'espérance $\mathbb{E}[f]$ en probabilités). L'inégalité s'écrit formellement : $\phi(\mathbb{E}[f]) \le \mathbb{E}[\phi(f)]$.

**Exemple concret immédiat :**
Considérons un espace fini $X = \{1, 2\}$, avec probabilités $\mu(\{1\}) = 0.5, \mu(\{2\}) = 0.5$. Soit $f(1) = a, f(2) = b$. L'intégrale est la moyenne arithmétique $\frac{a+b}{2}$.
Si $\phi(x) = e^x$ (fonction convexe), l'inégalité donne :
$$e^{\frac{a+b}{2}} \le \frac{1}{2} e^a + \frac{1}{2} e^b$$
Pour $a=0, b=2$, $e^1 \approx 2.718$. Et $\frac{1+e^2}{2} \approx \frac{1+7.389}{2} = 4.1945$. L'inégalité est largement vérifiée.

**Cas pathologique :**
Si $\mu(X) \neq 1$, l'inégalité est fausse. Par exemple, si $\mu$ est la mesure de Lebesgue sur $[0, 2]$, $\mu([0,2]) = 2$. Prenons $f(x) = x$ et $\phi(x) = x^2$.
$\int_0^2 x dx = [\frac{x^2}{2}]_0^2 = 2$. Donc $\phi(\int_0^2 x dx) = \phi(2) = 4$.
$\int_0^2 \phi(x) dx = \int_0^2 x^2 dx = [\frac{x^3}{3}]_0^2 = \frac{8}{3} \approx 2.66$.
Ici $4 \not\le 2.66$. La normalisation par la masse totale est cruciale.

## 3. Inégalité de Hölder : Majorations Produit

L'inégalité de Hölder est un outil fondamental pour majorer l'intégrale d'un produit. Elle repose sur la notion d'exposants conjugués.

### A. Exposants conjugués et Lemme de Young

> **Définition (Exposants conjugués) :**
> Deux réels $p, q \in [1, +\infty]$ sont dits conjugués si :
> $$\frac{1}{p} + \frac{1}{q} = 1$$
> avec la convention $\frac{1}{+\infty} = 0$. Ainsi, $1$ et $+\infty$ sont conjugués, et $2$ est son propre conjugué.

> **Lemme (Inégalité de Young) :**
> Soient $p, q \in ]1, +\infty[$ conjugués. Pour tous $a, b \ge 0$ :
> $$ab \le \frac{a^p}{p} + \frac{b^q}{q}$$
> L'égalité a lieu si et seulement si $a^p = b^q$.

### B. Énoncé du Théorème de Hölder

> **Théorème (Inégalité de Hölder) :**
> Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. Soient $p, q \in [1, +\infty]$ des exposants conjugués.
> Si $f \in L^p(\mu)$ et $g \in L^q(\mu)$, alors le produit $fg \in L^1(\mu)$ et :
> $$\|fg\|_1 = \int_X |f(x)g(x)| d\mu(x) \le \|f\|_p \|g\|_q$$

**Exemple concret immédiat :**
Soit $X = \{1, 2\}$ avec la mesure de comptage. Considérons les vecteurs $x = (x_1, x_2) = (1, 8)$ et $y = (y_1, y_2) = (4, 1)$. Prenons $p = \frac{4}{3}$ et $q = 4$ ($\frac{3}{4} + \frac{1}{4} = 1$).
$\|x\|_p = (|1|^{4/3} + |8|^{4/3})^{3/4} = (1 + 16)^{3/4} = 17^{3/4} \approx 8.35$
$\|y\|_q = (|4|^4 + |1|^4)^{1/4} = (256 + 1)^{1/4} = 257^{1/4} \approx 4.004$
Produit des normes : $8.35 \times 4.004 \approx 33.43$.
$\|xy\|_1 = |1\times 4| + |8\times 1| = 4 + 8 = 12$.
On a bien $12 \le 33.43$.

**Cas particulier (Cauchy-Schwarz) :**
Si $p = q = 2$, l'inégalité de Hölder devient l'inégalité de Cauchy-Schwarz : $\|fg\|_1 \le \|f\|_2 \|g\|_2$.

## 4. Inégalité de Minkowski : L'inégalité triangulaire dans $L^p$

L'inégalité de Minkowski garantit que la somme de deux fonctions $L^p$ reste dans $L^p$, et qu'elle satisfait la sous-additivité.

> **Théorème (Inégalité de Minkowski) :**
> Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. Soit $p \in [1, +\infty]$.
> Si $f, g \in L^p(\mu)$, alors $f+g \in L^p(\mu)$ et :
> $$\|f+g\|_p \le \|f\|_p + \|g\|_p$$

**Exemple concret immédiat :**
Dans $\mathbb{R}^2$ avec $p=2$, pour $x=(1,0)$ et $y=(0,1)$. $\|x\|_2 = 1$, $\|y\|_2 = 1$. $\|x+y\|_2 = \|(1,1)\|_2 = \sqrt{1^2+1^2} = \sqrt{2} \approx 1.414$.
$1.414 \le 1 + 1 = 2$.
Pour $p=1$ (norme Manhattan) : $\|(1,1)\|_1 = 1+1=2$, et $\|x\|_1 + \|y\|_1 = 1+1=2$. On a l'égalité.

**Cas limite :**
Pour $0 < p < 1$, l'inégalité s'inverse sur les termes strictement positifs : $\|f+g\|_p \ge \|f\|_p + \|g\|_p$. L'application $\|\cdot\|_p$ n'est donc pas une norme pour $p < 1$.

## 5. Démonstrations Complètes et Rigoureuses

### Preuve du Lemme de Young

Pour $a=0$ ou $b=0$, l'inégalité $0 \le 0$ est triviale. Supposons $a > 0$ et $b > 0$.
La fonction logarithme népérien $\ln : \mathbb{R}_{>0} \to \mathbb{R}$ est strictement concave (sa dérivée seconde est $-1/x^2 < 0$).
Par définition de la concavité (ou convexité de $-\ln$), pour $x, y > 0$ et $\lambda \in [0,1]$ :
$$\ln(\lambda x + (1-\lambda)y) \ge \lambda \ln(x) + (1-\lambda)\ln(y)$$
Posons $x = a^p$, $y = b^q$ et $\lambda = \frac{1}{p}$. Puisque $\frac{1}{p} + \frac{1}{q} = 1$, nous avons $(1-\lambda) = \frac{1}{q}$.
$$\ln\left( \frac{1}{p}a^p + \frac{1}{q}b^q \right) \ge \frac{1}{p}\ln(a^p) + \frac{1}{q}\ln(b^q)$$
$$\ln\left( \frac{1}{p}a^p + \frac{1}{q}b^q \right) \ge \ln(a) + \ln(b) = \ln(ab)$$
La fonction exponentielle étant strictement croissante sur $\mathbb{R}$, on applique $\exp$ aux deux membres :
$$\frac{a^p}{p} + \frac{b^q}{q} \ge ab$$
Ce qui clôt la preuve. L'égalité est stricte sauf si $x=y$, soit $a^p = b^q$.

### Preuve de l'Inégalité de Hölder

Soient $f \in L^p(\mu)$ et $g \in L^q(\mu)$.
**Cas 1 :** Si $\|f\|_p = 0$ ou $\|g\|_q = 0$. Alors $f=0$ presque partout ou $g=0$ presque partout. Donc $fg=0$ p.p. et $\|fg\|_1 = 0$. L'inégalité $0 \le 0$ est vérifiée.
**Cas 2 :** Supposons $\|f\|_p > 0$ et $\|g\|_q > 0$.
Définissons les fonctions normalisées :
$$u(x) = \frac{|f(x)|}{\|f\|_p} \quad \text{et} \quad v(x) = \frac{|g(x)|}{\|g\|_q}$$
Pour tout $x \in X$, appliquons l'inégalité de Young à $u(x)$ et $v(x)$ :
$$u(x)v(x) \le \frac{u(x)^p}{p} + \frac{v(x)^q}{q}$$
soit :
$$\frac{|f(x)g(x)|}{\|f\|_p \|g\|_q} \le \frac{1}{p}\frac{|f(x)|^p}{\|f\|_p^p} + \frac{1}{q}\frac{|g(x)|^q}{\|g\|_q^q}$$
Les fonctions à droite sont intégrables. En intégrant cette inégalité sur $X$ par rapport à la mesure $\mu$, par monotonie et linéarité de l'intégrale :
$$\int_X \frac{|f(x)g(x)|}{\|f\|_p \|g\|_q} d\mu \le \frac{1}{p} \int_X \frac{|f(x)|^p}{\|f\|_p^p} d\mu + \frac{1}{q} \int_X \frac{|g(x)|^q}{\|g\|_q^q} d\mu$$
Par définition de la norme, $\int_X |f|^p = \|f\|_p^p$ et $\int_X |g|^q = \|g\|_q^q$. Donc :
$$\frac{1}{\|f\|_p \|g\|_q} \int_X |f(x)g(x)| d\mu \le \frac{1}{p}(1) + \frac{1}{q}(1)$$
Comme $\frac{1}{p} + \frac{1}{q} = 1$ :
$$\frac{\|fg\|_1}{\|f\|_p \|g\|_q} \le 1$$
En multipliant par le dénominateur strictement positif :
$$\|fg\|_1 \le \|f\|_p \|g\|_q$$
Ce qui démontre le théorème.

### Preuve de l'Inégalité de Minkowski

Pour $p=1$, c'est une conséquence immédiate de l'inégalité triangulaire dans $\mathbb{R}$ : $|f(x)+g(x)| \le |f(x)| + |g(x)|$, que l'on intègre.
Pour $p=+\infty$, c'est également immédiat : $|f(x)+g(x)| \le \|f\|_\infty + \|g\|_\infty$ p.p., donc $\|f+g\|_\infty \le \|f\|_\infty + \|g\|_\infty$.
Considérons $1 < p < +\infty$.
On remarque d'abord que $f+g \in L^p$. En effet, $|f+g|^p \le (|f|+|g|)^p \le (2\max(|f|,|g|))^p \le 2^p(|f|^p + |g|^p)$, qui est intégrable.
Si $\|f+g\|_p = 0$, l'inégalité est évidente. Supposons $\|f+g\|_p > 0$.
Écrivons :
$$|f+g|^p = |f+g| \cdot |f+g|^{p-1} \le (|f| + |g|) |f+g|^{p-1} = |f||f+g|^{p-1} + |g||f+g|^{p-1}$$
Soit $q$ l'exposant conjugué de $p$, c'est-à-dire $q = \frac{p}{p-1}$.
La fonction $|f+g|^{p-1}$ appartient à $L^q(\mu)$ car :
$$\int (|f+g|^{p-1})^q = \int |f+g|^{(p-1)\frac{p}{p-1}} = \int |f+g|^p < +\infty$$
Nous appliquons l'inégalité de Hölder à chaque terme :
$$\int |f||f+g|^{p-1} \le \|f\|_p \| |f+g|^{p-1} \|_q$$
$$\int |g||f+g|^{p-1} \le \|g\|_p \| |f+g|^{p-1} \|_q$$
Or, $\| |f+g|^{p-1} \|_q = (\int |f+g|^p)^{1/q} = \|f+g\|_p^{p/q} = \|f+g\|_p^{p(1-1/p)} = \|f+g\|_p^{p-1}$.
En sommant et en intégrant l'inégalité initiale :
$$\int |f+g|^p \le \|f\|_p \|f+g\|_p^{p-1} + \|g\|_p \|f+g\|_p^{p-1}$$
$$\|f+g\|_p^p \le (\|f\|_p + \|g\|_p) \|f+g\|_p^{p-1}$$
En divisant par $\|f+g\|_p^{p-1}$ (qui est strictement positif par hypothèse), on obtient :
$$\|f+g\|_p \le \|f\|_p + \|g\|_p$$
La preuve est achevée.

## 6. Applications en Intelligence Artificielle et Théorie de l'Information

Les inégalités développées dans ce jalon ne sont pas confinées à l'analyse pure ; elles forment le socle algorithmique des modèles génératifs et de la théorie du transport.

- **Variational Auto-Encoders (VAE) et ELBO :** En apprentissage génératif, on cherche à maximiser la vraisemblance marginale $p(x) = \int p(x, z) dz$. Calculer cette intégrale est souvent intraitable en grande dimension. L'inégalité de Jensen permet de borner inférieurement la log-vraisemblance (la fonction logarithme étant concave). En introduisant une distribution variationnelle $q(z|x)$ :
  $$\ln p(x) = \ln \int q(z|x) \frac{p(x, z)}{q(z|x)} dz = \ln \mathbb{E}_{z \sim q}\left[\frac{p(x, z)}{q(z|x)}\right]$$
  Par l'inégalité de Jensen (pour la fonction concave $\ln$) :
  $$\ln p(x) \ge \mathbb{E}_{z \sim q}\left[\ln \frac{p(x, z)}{q(z|x)}\right]$$
  Le terme de droite est l'**ELBO** (Evidence Lower Bound), qui sert de fonction objectif dans l'entraînement des VAE.

- **Théorie de l'Information et Divergence KL :** L'inégalité de Jensen permet de prouver que la divergence de Kullback-Leibler entre deux distributions $P$ et $Q$ est toujours positive : $D_{KL}(P||Q) = \mathbb{E}_{P}\left[-\ln \frac{q(x)}{p(x)}\right] \ge -\ln(\mathbb{E}_{P}\left[\frac{q(x)}{p(x)}\right]) = -\ln(1) = 0$. C'est fondamental pour justifier l'utilisation de la Cross-Entropy comme fonction de perte en classification.

- **Inégalités de Concentration (Hoeffding/McDiarmid) :** Les démonstrations des bornes de généralisation en PAC-learning reposent sur l'inégalité de Hölder (souvent sous la forme Cauchy-Schwarz ou de bornes sur la transformée de Laplace via l'inégalité de Markov, qui découle elle-même de l'intégration positive formelle).

- **Optimisation et Gradient Proximal :** L'inégalité de Minkowski garantit la convexité des boules $L^p$ pour $p \ge 1$. Dans les algorithmes de régularisation (Lasso pour $L^1$, Ridge pour $L^2$), c'est la géométrie de ces boules induite par Minkowski qui dicte la parcimonie (sparsity) des poids appris par le modèle.

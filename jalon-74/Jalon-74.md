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

# Jalon 74 : Inégalités fondamentales de l'analyse fonctionnelle

## 1. Genèse des Inégalités de l'Analyse Fonctionnelle

La théorie des espaces $L^p$, introduite par Henri Lebesgue au début du XXe siècle, a nécessité le développement d'outils quantitatifs robustes pour mesurer la "taille" des fonctions et contrôler leur comportement asymptotique. Les inégalités de Hölder et de Minkowski, généralisant les travaux antérieurs d'Augustin-Louis Cauchy et d'Hermann Amandus Schwarz sur les sommes finies et les intégrales de carré sommable, fournissent l'armature métrique et topologique indispensable à l'étude des espaces fonctionnels modernes. L'inégalité de Jensen, formulée par Johan Jensen en 1906, offre quant à elle une caractérisation profonde de la convexité en liant la moyenne d'une fonction convexe à l'image de la moyenne. Ces résultats ne sont pas de simples astuces calculatoires : ils incarnent des principes géométriques fondamentaux – la dualité, l'inégalité triangulaire en dimension infinie, et la courbure – qui sous-tendent toute l'analyse fonctionnelle, la théorie des probabilités et l'optimisation convexe.

## 2. Théorèmes Fondamentaux, Inégalités et Exemples Concrets

### Inégalité de Jensen

Soit $(X, \mathcal{T}, \mu)$ un espace mesuré tel que $\mu(X) = 1$ (c'est-à-dire que $\mu$ est une mesure de probabilité). Soit $f \in L^1(\mu)$ une fonction à valeurs réelles, et $\varphi : \mathbb{R} \to \mathbb{R}$ une fonction convexe.

**Théorème (Inégalité de Jensen) :**
$$ \varphi\left( \int_X f(x) \, d\mu(x) \right) \le \int_X \varphi(f(x)) \, d\mu(x) $$

**Exemple Concret :**
Considérons la mesure de Lebesgue sur $X = [0, 1]$, donc $\mu(X) = 1$. Soit $f(x) = x$ et $\varphi(t) = t^2$ (qui est strictement convexe sur $\mathbb{R}$).
L'intégrale de $f$ est $\int_0^1 x \, dx = \frac{1}{2}$. L'image de cette intégrale par $\varphi$ est $\varphi(1/2) = 1/4$.
D'autre part, l'intégrale de $\varphi \circ f$ est $\int_0^1 x^2 \, dx = \frac{1}{3}$.
Puisque $1/4 \le 1/3$, l'inégalité de Jensen est strictement vérifiée. Ce résultat géométrique stipule que le barycentre d'une courbe convexe se situe "au-dessus" (ou sur) la courbe.

**Cas limite :** Si $\varphi(t) = at + b$ est une fonction affine (qui est à la fois convexe et concave), l'inégalité devient une égalité stricte, traduisant la linéarité de l'intégrale.

### Inégalité de Hölder

Soient $p, q \in [1, +\infty]$ deux exposants conjugués, c'est-à-dire tels que $\frac{1}{p} + \frac{1}{q} = 1$. Soit $(X, \mathcal{T}, \mu)$ un espace mesuré.

**Théorème (Inégalité de Hölder) :**
Pour toutes fonctions mesurables $f \in L^p(\mu)$ et $g \in L^q(\mu)$, le produit $fg$ appartient à $L^1(\mu)$, et l'on a la majoration :
$$ \int_X |f(x)g(x)| \, d\mu(x) \le \left( \int_X |f(x)|^p \, d\mu(x) \right)^{1/p} \left( \int_X |g(x)|^q \, d\mu(x) \right)^{1/q} $$
soit de manière plus compacte : $\|fg\|_1 \le \|f\|_p \|g\|_q$.

**Exemple Concret :**
Sur l'espace euclidien discret $X = \{1, 2\}$, munissons l'espace de la mesure de comptage. Soient les vecteurs $u = (1, 1)$ et $v = (1, 0)$. Posons $p = 1$ et $q = \infty$.
Ici, $\|u\|_1 = |1| + |1| = 2$ et $\|v\|_\infty = \max(|1|, |0|) = 1$.
Leur produit terme à terme est $uv = (1\cdot 1, 1\cdot 0) = (1, 0)$, dont la norme $L^1$ est $\|uv\|_1 = |1| + |0| = 1$.
On vérifie bien que $\|uv\|_1 = 1 \le \|u\|_1 \|v\|_\infty = 2 \times 1 = 2$.
Pour $p=q=2$, on retrouve la célèbre inégalité de Cauchy-Schwarz.

**Contre-exemple / Singularité :** Si $p$ et $q$ ne sont pas conjugués (par exemple $\frac{1}{p} + \frac{1}{q} \neq 1$), l'inégalité n'est plus dimensionnellement cohérente. Multiplier toutes les fonctions par une constante $\lambda > 0$ briserait l'inégalité, ce qui prouve son invalidité dans ces configurations.

### Inégalité de Minkowski

Soit $p \in [1, +\infty]$. Pour toutes fonctions $f, g \in L^p(\mu)$, la somme $f+g$ appartient à $L^p(\mu)$.

**Théorème (Inégalité de Minkowski) :**
$$ \left( \int_X |f(x) + g(x)|^p \, d\mu(x) \right)^{1/p} \le \left( \int_X |f(x)|^p \, d\mu(x) \right)^{1/p} + \left( \int_X |g(x)|^p \, d\mu(x) \right)^{1/p} $$
soit de manière plus compacte : $\|f+g\|_p \le \|f\|_p + \|g\|_p$.
Cette inégalité confère à la fonction $\|\cdot\|_p$ le statut rigoureux de norme vectorielle sur $L^p$ en établissant l'inégalité triangulaire.

**Exemple Concret :**
Sur $\mathbb{R}^2$ avec $p=2$, prenons les vecteurs $u = (3, 0)$ et $v = (0, 4)$.
La norme euclidienne $\|u\|_2$ vaut $3$, et $\|v\|_2$ vaut $4$.
La somme vectorielle $u+v = (3, 4)$ possède une norme euclidienne égale à $\sqrt{3^2 + 4^2} = 5$.
On vérifie l'inégalité de Minkowski : $5 \le 3 + 4 = 7$.

**Cas limite :** Si $0 < p < 1$, $\|\cdot\|_p$ ne satisfait plus l'inégalité triangulaire. La "boule unité" associée n'est plus un ensemble convexe, rendant ces espaces $L^p$ (pour $p < 1$) topologiquement pathologiques (ce ne sont pas des espaces de Banach).

## 3. Démonstrations

### Preuve de l'Inégalité de Hölder

Pour $p=1$ et $q=\infty$, la démonstration découle directement de la majoration d'une intégrale :
$|f(x)g(x)| \le |f(x)| \|g\|_\infty$ pour presque tout $x$. En intégrant, on obtient $\int |fg| \, d\mu \le \|g\|_\infty \int |f| \, d\mu = \|f\|_1 \|g\|_\infty$.

Concentrons-nous sur le cas non trivial où $1 < p, q < \infty$.
Si $\|f\|_p = 0$ ou $\|g\|_q = 0$, les fonctions sont nulles presque partout et l'inégalité est trivialement vérifiée ($0 \le 0$).
Supposons $\|f\|_p > 0$ et $\|g\|_q > 0$. Par homogénéité, définissons les fonctions normalisées :
$$ u(x) = \frac{|f(x)|}{\|f\|_p} \quad \text{et} \quad v(x) = \frac{|g(x)|}{\|g\|_q} $$
De sorte que $\|u\|_p = 1$ et $\|v\|_q = 1$.

Nous utilisons le Lemme de Young. Pour tout $a, b \ge 0$, la concavité de la fonction logarithme implique que :
$$ ab \le \frac{a^p}{p} + \frac{b^q}{q} $$
Appliquons ce lemme ponctuellement aux fonctions $u$ et $v$ :
$$ u(x)v(x) \le \frac{u(x)^p}{p} + \frac{v(x)^q}{q} $$
Intégrons cette inégalité sur l'espace mesuré $X$ par rapport à $\mu$ :
$$ \int_X u(x)v(x) \, d\mu(x) \le \int_X \left( \frac{u(x)^p}{p} + \frac{v(x)^q}{q} \right) \, d\mu(x) $$
Par linéarité de l'intégrale :
$$ \int_X u(x)v(x) \, d\mu(x) \le \frac{1}{p} \int_X u(x)^p \, d\mu(x) + \frac{1}{q} \int_X v(x)^q \, d\mu(x) $$
Puisque $u$ et $v$ sont normalisées en norme $L^p$ et $L^q$ respectivement :
$$ \int_X u^p \, d\mu = 1 \quad \text{et} \quad \int_X v^q \, d\mu = 1 $$
Ainsi :
$$ \int_X u(x)v(x) \, d\mu(x) \le \frac{1}{p}(1) + \frac{1}{q}(1) = 1 $$
Substituons les définitions originelles de $u$ et $v$ :
$$ \int_X \frac{|f(x)|}{\|f\|_p} \frac{|g(x)|}{\|g\|_q} \, d\mu(x) \le 1 $$
En sortant les constantes de l'intégrale et en multipliant par le dénominateur :
$$ \int_X |f(x)g(x)| \, d\mu(x) \le \|f\|_p \|g\|_q $$
Ce qui achève la démonstration rigoureuse de l'inégalité de Hölder.

### Preuve de l'Inégalité de Minkowski

Le cas $p=1$ est une conséquence directe de l'inégalité triangulaire dans $\mathbb{R}$ : $|f(x)+g(x)| \le |f(x)|+|g(x)|$, suivie de l'intégration.
Considérons $1 < p < \infty$.
Si $\|f+g\|_p = 0$, l'inégalité est triviale. Supposons $\|f+g\|_p > 0$.
L'inégalité triangulaire scalaire nous donne ponctuellement :
$$ |f(x) + g(x)|^p = |f(x) + g(x)| \cdot |f(x) + g(x)|^{p-1} \le (|f(x)| + |g(x)|) \cdot |f(x) + g(x)|^{p-1} $$
Soit :
$$ |f(x) + g(x)|^p \le |f(x)| \cdot |f(x) + g(x)|^{p-1} + |g(x)| \cdot |f(x) + g(x)|^{p-1} $$
Intégrons cette relation sur $X$ :
$$ \int_X |f+g|^p \, d\mu \le \int_X |f| \cdot |f+g|^{p-1} \, d\mu + \int_X |g| \cdot |f+g|^{p-1} \, d\mu $$
Appliquons l'inégalité de Hölder au premier terme du membre de droite. L'exposant conjugué de $p$ est $q = \frac{p}{p-1}$.
Posons $h_1(x) = |f(x)|$ et $h_2(x) = |f(x)+g(x)|^{p-1}$.
$$ \int_X |f| \cdot |f+g|^{p-1} \, d\mu \le \|f\|_p \left( \int_X (|f+g|^{p-1})^q \, d\mu \right)^{1/q} $$
Puisque $(p-1)q = p$, l'intégrale de droite devient $\left(\int_X |f+g|^p \, d\mu\right)^{1/q} = \|f+g\|_p^{p/q}$.
On procède de manière identique pour le terme en $g$ :
$$ \int_X |g| \cdot |f+g|^{p-1} \, d\mu \le \|g\|_p \|f+g\|_p^{p/q} $$
En sommant ces deux majorations, nous obtenons :
$$ \int_X |f+g|^p \, d\mu \le \left( \|f\|_p + \|g\|_p \right) \|f+g\|_p^{p/q} $$
Divisons les deux membres par $\|f+g\|_p^{p/q}$ (qui est strictement positif par hypothèse) :
$$ \|f+g\|_p^p \cdot \|f+g\|_p^{-p/q} \le \|f\|_p + \|g\|_p $$
L'exposant du membre de gauche se simplifie en $p - p/q = p(1 - 1/q) = p(1/p) = 1$.
Nous obtenons ainsi le résultat fondamental :
$$ \|f+g\|_p \le \|f\|_p + \|g\|_p $$

## 4. Applications en Physique, Logique et Intelligence Artificielle

Les inégalités d'analyse fonctionnelle sont les garantes de la stabilité et de la convergence algorithmique dans de multiples domaines scientifiques. En physique quantique, l'inégalité de Hölder (et sa spécialisation par Cauchy-Schwarz) est l'expression mathématique de la relation d'incertitude de Heisenberg, établissant des limites fondamentales sur la précision simultanée des mesures conjuguées.

En apprentissage automatique (IA), l'inégalité de Jensen est omniprésente. Elle constitue la clef de voûte de la dérivation de l'Evidence Lower Bound (ELBO) utilisée dans les Autoencodeurs Variationnels (VAE). Lors de l'entraînement de modèles probabilistes à variables latentes via l'algorithme d'Expectation-Maximization (EM), l'inégalité de Jensen garantit que la phase de maximisation augmente monotonement la log-vraisemblance des données. Plus fondamentalement, elle permet de prouver que la divergence de Kullback-Leibler, qui quantifie l'"écart" entre deux distributions de probabilités, est toujours positive ou nulle, validant ainsi son utilisation comme fonction de perte asymptotiquement consistante lors de la minimisation de l'entropie croisée dans l'entraînement des réseaux de neurones.

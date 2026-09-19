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

# Jalon 74 : Inégalités fondamentales (Hölder, Minkowski, Jensen)

## 1. Introduction

Les inégalités jouent un rôle fondamental en analyse mathématique, particulièrement dans la théorie de l'intégration et l'analyse fonctionnelle. Historiquement, l'étude des espaces de fonctions a nécessité de comprendre comment mesurer la "taille" d'une fonction et comment ces tailles interagissent lors d'opérations algébriques comme l'addition ou la multiplication.

L'inégalité de Hölder, généralisant celle de Cauchy-Schwarz, établit une limite absolue sur le produit de deux fonctions appartenant à des espaces $L^p$ différents mais complémentaires. Elle traduit l'idée physique qu'une certaine quantité d'énergie ou de ressource ne peut être amplifiée indéfiniment par combinaison.

L'inégalité de Minkowski, quant à elle, est la traduction analytique de l'inégalité triangulaire géométrique classique : le chemin le plus court entre deux points reste la ligne droite, même dans des espaces de dimension infinie mesurant des déviations à la puissance $p$.

Enfin, l'inégalité de Jensen formalise le comportement des fonctions convexes face à l'intégration, traduisant le fait que la moyenne des images par une fonction convexe est toujours supérieure ou égale à l'image de la moyenne. C'est un principe de minoration qui s'avère omniprésent en théorie des probabilités et en optimisation.

## 2. Définitions, Théorèmes et Exemples

### A. Exposants Conjugués et Inégalité de Hölder

**Définition (Exposants conjugués) :** Deux réels $p, q \in [1, +\infty]$ sont dits conjugués si et seulement si :
$$\frac{1}{p} + \frac{1}{q} = 1$$
Par convention, si $p=1$, alors $q=+\infty$, et inversement.

**Théorème (Inégalité de Hölder) :** Soit $(X, \mathcal{F}, \mu)$ un espace mesuré, et soient $p, q \in [1, +\infty]$ deux exposants conjugués. Pour toutes fonctions mesurables $f \in L^p(\mu)$ et $g \in L^q(\mu)$, le produit $fg$ appartient à $L^1(\mu)$ et on a :
$$\|fg\|_1 \le \|f\|_p \|g\|_q$$
Autrement dit, $\int_X |fg| d\mu \le \left( \int_X |f|^p d\mu \right)^{1/p} \left( \int_X |g|^q d\mu \right)^{1/q}$.

**Exemples concrets et cas limites :**
1. **Cas $p=2, q=2$ (Cauchy-Schwarz) :** Pour les vecteurs $(3, 4)$ et $(1, 2)$ dans $\mathbb{R}^2$, $|3(1) + 4(2)| = 11$. Les normes 2 sont $\sqrt{9+16}=5$ et $\sqrt{1+4}=\sqrt{5}$. On a bien $11 \le 5\sqrt{5} \approx 11.18$.
2. **Cas $p=1, q=+\infty$ :** Soit $f(x)=x$ sur $[0,1]$ et $g(x)=2$. $\|f\|_1 = 1/2$, $\|g\|_\infty = 2$. Le produit $fg(x)=2x$ a pour norme $\|fg\|_1 = 1$. On a exactement $\|fg\|_1 \le \|f\|_1 \|g\|_\infty \implies 1 \le (1/2) \times 2 = 1$.
3. **Cas $p=3, q=3/2$ sur $\mathbb{R}^2$ :** $u=(1, 2)$, $v=(2, 1)$. $\sum |u_i v_i| = 2 + 2 = 4$. $\|u\|_3 = (1+8)^{1/3} = 9^{1/3}$. $\|v\|_{3/2} = (2^{3/2} + 1)^{2/3}$. $4 \le 9^{1/3} \times (2\sqrt{2}+1)^{2/3}$.
4. **Matrices :** L'inégalité s'applique aux normes de Schatten pour les matrices. $\|AB\|_1 \le \|A\|_p \|B\|_q$.
5. **Edge case (Fonction nulle) :** Si $f=0$ presque partout, $\|fg\|_1 = 0$, et $\|f\|_p \|g\|_q = 0 \times \|g\|_q = 0$. L'inégalité est triviale.
6. **Edge case (Non intégrabilité) :** Si $p, q$ ne sont pas conjugués (ex: $p=2, q=3$), l'inégalité de Hölder standard ne s'applique pas directement pour borner $L^1$, il faut utiliser une version généralisée.

### B. Inégalité de Minkowski

**Théorème (Inégalité de Minkowski) :** Soit $(X, \mathcal{F}, \mu)$ un espace mesuré et $p \in [1, +\infty]$. Pour toutes fonctions $f, g \in L^p(\mu)$, la somme $f+g \in L^p(\mu)$ et :
$$\|f+g\|_p \le \|f\|_p + \|g\|_p$$

**Exemples concrets et cas limites :**
1. **Dimension 1, $p=2$ :** $|a+b|^2 \le (|a|+|b|)^2$. Pour $a=3, b=-1$, $|2|^2 = 4$, et $(|3|+|-1|)^2 = 16$. $2 \le 4$.
2. **Vecteurs de $\mathbb{R}^2$, $p=1$ :** $u = (1, -2), v = (3, 4)$. $u+v = (4, 2)$. $\|u+v\|_1 = 4+2=6$. $\|u\|_1 = 1+2=3$. $\|v\|_1 = 3+4=7$. $6 \le 3+7 = 10$.
3. **Vecteurs de $\mathbb{R}^2$, $p=2$ :** $\|u+v\|_2 = \sqrt{16+4} = \sqrt{20} \approx 4.47$. $\|u\|_2 = \sqrt{5} \approx 2.23$. $\|v\|_2 = 5$. $4.47 \le 2.23 + 5 = 7.23$.
4. **Vecteurs de $\mathbb{R}^2$, $p=\infty$ :** $\|u+v\|_\infty = \max(4, 2) = 4$. $\|u\|_\infty = 2$, $\|v\|_\infty = 4$. $4 \le 2+4=6$.
5. **Espaces de fonctions continues :** $f(x)=x, g(x)=1-x$ sur $[0,1]$ avec $p=2$. $\|f+g\|_2 = \|1\|_2 = 1$. $\|f\|_2 = \sqrt{1/3} \approx 0.57$. $\|g\|_2 = \sqrt{1/3} \approx 0.57$. $1 \le 1.15$.
6. **Cas d'égalité :** L'égalité se produit si et seulement si les fonctions sont colinéaires et de même signe (presque partout).
7. **Échec pour $p < 1$ :** Si $p=1/2$, $u=(1,0), v=(0,1)$. $\|u+v\|_{1/2} = (1^{1/2} + 1^{1/2})^2 = 4$. Mais $\|u\|_{1/2} + \|v\|_{1/2} = 1 + 1 = 2$. $4 \not\le 2$. Minkowski n'est vraie que pour $p \ge 1$.

### C. Inégalité de Jensen

**Théorème (Inégalité de Jensen) :** Soit $(X, \mathcal{F}, \mu)$ un espace de probabilité (c'est-à-dire $\mu(X)=1$). Soit $f \in L^1(\mu)$ une fonction à valeurs dans un intervalle $I \subset \mathbb{R}$, et $\phi : I \to \mathbb{R}$ une fonction convexe. Alors $\phi(f)$ est mesurable et :
$$\phi \left( \int_X f d\mu \right) \le \int_X \phi(f) d\mu$$

**Exemples concrets et cas limites :**
1. **Fonction carré ($x \mapsto x^2$) :** Pour un dé équilibré, $X \in \{1,2,3,4,5,6\}$. $\mathbb{E}[X] = 3.5$. $\phi(\mathbb{E}[X]) = 12.25$. $\mathbb{E}[X^2] = (1+4+9+16+25+36)/6 = 91/6 \approx 15.16$. On a bien $12.25 \le 15.16$.
2. **Fonction inverse ($x \mapsto 1/x$) sur $\mathbb{R}_+^*$ :** Soit $X$ valant $2$ ou $4$ avec probabilité $1/2$. $\mathbb{E}[X] = 3$, $1/\mathbb{E}[X] = 1/3 \approx 0.33$. $\mathbb{E}[1/X] = (1/2+1/4)/2 = 3/8 = 0.375$. On a $0.33 \le 0.375$.
3. **Fonction exponentielle ($x \mapsto e^x$) :** $X$ uniforme sur $[0,1]$. $\mathbb{E}[X] = 1/2$. $e^{1/2} \approx 1.648$. $\mathbb{E}[e^X] = \int_0^1 e^x dx = e - 1 \approx 1.718$. $1.648 \le 1.718$.
4. **Moyenne arithmético-géométrique :** Avec $\phi(x) = -\ln(x)$ (convexe), on prouve que la moyenne géométrique est bornée par la moyenne arithmétique.
5. **Cas discret pondéré :** Pour $x_1=1, x_2=4$, poids $\lambda_1=1/4, \lambda_2=3/4$. $\phi(x)=x^2$. $\phi(1/4 \times 1 + 3/4 \times 4) = \phi(13/4) = 169/16 = 10.56$. Et $1/4 \phi(1) + 3/4 \phi(4) = 1/4 + 48/4 = 49/4 = 12.25$. $10.56 \le 12.25$.
6. **Échec si non convexe :** Si $\phi(x) = \sin(x)$ sur $[0, \pi]$ (concave). $X \in \{0, \pi\}$ avec proba $1/2$. $\mathbb{E}[X] = \pi/2$. $\sin(\pi/2) = 1$. $\mathbb{E}[\sin(X)] = 0$. $1 \not\le 0$. L'inégalité est inversée pour les fonctions concaves.

## 3. Démonstrations

### A. Preuve du Lemme de Young

**Lemme :** Pour tous $a, b \ge 0$ et $p, q \in ]1, +\infty[$ conjugués, $ab \le \frac{a^p}{p} + \frac{b^q}{q}$.

**Démonstration :**
1. Si $a=0$ ou $b=0$, l'inégalité est immédiate ($0 \le 0$). Supposons $a > 0$ et $b > 0$.
2. La fonction logarithme népérien $\ln$ est strictement concave sur $\mathbb{R}_+^*$.
3. On écrit $ab = \exp(\ln(a) + \ln(b)) = \exp \left( \frac{1}{p} \ln(a^p) + \frac{1}{q} \ln(b^q) \right)$.
4. Puisque $\frac{1}{p} + \frac{1}{q} = 1$, la concavité de $\ln$ (ou convexité de $\exp$) donne :
   $$\exp \left( \frac{1}{p} \ln(a^p) + \frac{1}{q} \ln(b^q) \right) \le \frac{1}{p} \exp(\ln(a^p)) + \frac{1}{q} \exp(\ln(b^q))$$
5. Ce qui se simplifie en :
   $$ab \le \frac{a^p}{p} + \frac{b^q}{q}$$

### B. Preuve de l'inégalité de Hölder

**Démonstration :**
1. Si $\|f\|_p = 0$ ou $\|g\|_q = 0$, alors $f=0$ p.p. ou $g=0$ p.p., donc $fg=0$ p.p., et l'inégalité $0 \le 0$ est triviale.
2. Si $\|f\|_p = +\infty$ ou $\|g\|_q = +\infty$, le membre de droite est $+\infty$, l'inégalité est évidente.
3. Supposons $0 < \|f\|_p < +\infty$ et $0 < \|g\|_q < +\infty$. Définissons les fonctions normalisées :
   $$u(x) = \frac{|f(x)|}{\|f\|_p}, \quad v(x) = \frac{|g(x)|}{\|g\|_q}$$
4. Par construction, $\|u\|_p = 1$ et $\|v\|_q = 1$ car $\int |u|^p d\mu = \frac{1}{\|f\|_p^p} \int |f|^p d\mu = 1$.
5. On applique le lemme de Young ponctuellement pour presque tout $x \in X$ :
   $$u(x)v(x) \le \frac{u(x)^p}{p} + \frac{v(x)^q}{q}$$
6. On intègre cette inégalité sur $X$ :
   $$\int_X u(x)v(x) d\mu \le \frac{1}{p} \int_X u(x)^p d\mu + \frac{1}{q} \int_X v(x)^q d\mu$$
7. En remplaçant les intégrales par $1$ :
   $$\int_X \frac{|f(x)g(x)|}{\|f\|_p \|g\|_q} d\mu \le \frac{1}{p}(1) + \frac{1}{q}(1) = 1$$
8. En multipliant par $\|f\|_p \|g\|_q$, on obtient :
   $$\int_X |fg| d\mu \le \|f\|_p \|g\|_q$$

### C. Preuve de l'inégalité de Minkowski

**Démonstration :**
1. Pour $p=1$, l'inégalité triangulaire classique $|f(x)+g(x)| \le |f(x)| + |g(x)|$ s'intègre directement. Supposons $p > 1$. Soit $q$ le conjugué de $p$ tel que $(p-1)q = p$.
2. On remarque que $|f+g|^p = |f+g| \cdot |f+g|^{p-1} \le (|f| + |g|) |f+g|^{p-1} = |f||f+g|^{p-1} + |g||f+g|^{p-1}$.
3. On intègre sur $X$ :
   $$\int |f+g|^p d\mu \le \int |f| |f+g|^{p-1} d\mu + \int |g| |f+g|^{p-1} d\mu$$
4. Appliquons l'inégalité de Hölder au premier terme avec $p$ et $q$ :
   $$\int |f| |f+g|^{p-1} d\mu \le \|f\|_p \left( \int (|f+g|^{p-1})^q d\mu \right)^{1/q}$$
5. Comme $(p-1)q = p$, cela donne :
   $$\int |f| |f+g|^{p-1} d\mu \le \|f\|_p \left( \int |f+g|^p d\mu \right)^{1/q} = \|f\|_p \|f+g\|_p^{p/q}$$
6. De même pour le second terme :
   $$\int |g| |f+g|^{p-1} d\mu \le \|g\|_p \|f+g\|_p^{p/q}$$
7. En sommant, on obtient :
   $$\|f+g\|_p^p \le (\|f\|_p + \|g\|_p) \|f+g\|_p^{p/q}$$
8. Si $\|f+g\|_p = 0$, l'inégalité est vraie. Sinon, on divise par $\|f+g\|_p^{p/q}$. Comme $p - p/q = p(1 - 1/q) = p(1/p) = 1$, il reste :
   $$\|f+g\|_p \le \|f\|_p + \|g\|_p$$

### D. Preuve de l'inégalité de Jensen

**Démonstration :**
1. Soit $t_0 = \int_X f d\mu$. Comme $f \in L^1$ et $\mu(X)=1$, $t_0 \in I$.
2. La fonction $\phi$ étant convexe sur $I$, elle possède en tout point intérieur de $I$ une droite d'appui (sous-gradient). Il existe une constante $c \in \mathbb{R}$ (pente) telle que pour tout $t \in I$ :
   $$\phi(t) \ge \phi(t_0) + c(t - t_0)$$
3. On applique cette inégalité ponctuellement à la fonction $f(x)$ pour tout $x \in X$ :
   $$\phi(f(x)) \ge \phi(t_0) + c(f(x) - t_0)$$
4. On intègre cette relation par rapport à la mesure de probabilité $\mu$ :
   $$\int_X \phi(f(x)) d\mu \ge \int_X \phi(t_0) d\mu + \int_X c(f(x) - t_0) d\mu$$
5. Par linéarité de l'intégrale et comme $\mu(X)=1$, on a $\int_X \phi(t_0) d\mu = \phi(t_0)$. De plus :
   $$\int_X c(f(x) - t_0) d\mu = c \left( \int_X f(x) d\mu - t_0 \int_X 1 d\mu \right) = c (t_0 - t_0) = 0$$
6. On obtient donc l'inégalité voulue :
   $$\int_X \phi(f) d\mu \ge \phi(t_0) = \phi \left( \int_X f d\mu \right)$$

## 4. Applications en Intelligence Artificielle et Physique

L'inégalité de Jensen est la clé de voûte des méthodes variationnelles en apprentissage profond. Dans les Auto-encodeurs Variationnels (VAE), on cherche à maximiser la vraisemblance marginale des données $\ln(p(x))$. Le logarithme étant une fonction concave, on applique l'inégalité de Jensen dans le sens inverse pour obtenir une borne inférieure (ELBO - Evidence Lower Bound) calculable.

En théorie de l'information, Jensen garantit que la divergence de Kullback-Leibler, qui mesure la différence entre deux distributions de probabilité, est toujours positive ou nulle. C'est l'essence même de la notion de distance d'information en machine learning, justifiant l'usage de la Cross-Entropy comme fonction de perte fiable.

Les inégalités de Hölder et Minkowski sont fondamentales pour la théorie de la régularisation en machine learning. Lors de l'apprentissage de réseaux de neurones, imposer des contraintes sur la norme $L^p$ des poids du réseau modifie la nature de l'espace de recherche. Hölder permet de borner les produits scalaires (qui représentent les activations des neurones) en séparant l'entrée et les poids dans des normes conjuguées optimales, garantissant la robustesse des modèles face aux perturbations de l'entrée.

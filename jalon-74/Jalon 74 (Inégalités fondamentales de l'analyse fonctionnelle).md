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

## 1. Présentation du concept clé

- **La Métaphore :**
    - **Jensen (Les moyennes) :** Imaginez que vous fassiez cuire une omelette. Est-il préférable de faire cuire chaque œuf séparément puis de les mélanger, ou de mélanger tous les œufs puis de les faire cuire d'un coup ? Si la poêle est "convexe" (elle répartit bien la chaleur), le mélange global sera toujours "meilleur" (ou égal) à la somme des parties.
    - **Hölder (Les produits) :** Imaginez que vous ayez deux ressources (énergie et temps). L'inégalité de Hölder vous donne la limite maximale de ce que vous pouvez produire en combinant ces deux ressources. C'est une généralisation de l'idée qu'on ne peut pas faire plus que ce que nos capacités permettent.
    - **Minkowski (Le chemin le plus court) :** C'est simplement l'inégalité triangulaire que vous connaissez depuis l'école (le détour est plus long que la ligne droite), mais appliquée à des mondes très étranges où les distances se mesurent avec des puissances $p$.
- **Le "Pourquoi on a inventé ça" :** Pour pouvoir majorer des erreurs. En sciences, on ne connaît jamais la valeur exacte d'une fonction, on connaît seulement sa "taille" (sa norme). Ces inégalités sont les outils de base qui permettent de dire : "si l'erreur sur A est petite et l'erreur sur B est petite, alors l'erreur sur leur combinaison reste sous contrôle".
- **Visualisation :** La courbure d'une fonction convexe ( Jensen). La superposition de deux ondes (Minkowski).

## 2. Formalisation & Rigueur Académique

### A. L'Inégalité de Hölder

Soient $p, q \in [1, +\infty]$ tels que $\frac{1}{p} + \frac{1}{q} = 1$ (on dit que $p$ et $q$ sont **conjugués**).

> **Théorème (Inégalité de Hölder) :**
> Pour toutes fonctions $f \in L^p(\mu)$ et $g \in L^q(\mu)$, le produit $fg$ appartient à $L^1(\mu)$ et :
> $$\|fg\|_1 \le \|f\|_p \cdot \|g\|_q$$
> *Cas particulier :* Pour $p=q=2$, on retrouve l'inégalité de **Cauchy-Schwarz**.

### B. L'Inégalité de Minkowski

> **Théorème (Inégalité de Minkowski) :**
> Pour tout $p \in [1, +\infty]$ et pour toutes fonctions $f, g \in L^p(\mu)$ :
> $$\|f+g\|_p \le \|f\|_p + \|g\|_p$$
> C'est l'inégalité triangulaire qui fait de $L^p$ un espace vectoriel normé.

### C. L'Inégalité de Jensen

> **Théorème (Inégalité de Jensen) :**
> Soit $\mu$ une mesure de **probabilité** ($\mu(X)=1$). Soit $f$ une fonction intégrable et $\phi : I \to \mathbb{R}$ une fonction **convexe** sur un intervalle $I$ contenant les valeurs de $f$. Alors :
> $$\phi \left( \int_X f d\mu \right) \le \int_X \phi(f) d\mu$$
> En termes probabilistes : $\phi(\mathbb{E}[X]) \le \mathbb{E}[\phi(X)]$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration de l'inégalité de Hölder

1. **Lemme de Young :** Pour tous $a, b \ge 0$ et $p, q$ conjugués : $ab \le \frac{a^p}{p} + \frac{b^q}{q}$.
   *(Preuve par concavité du logarithme)*.
2. **Normalisation :** Supposons $\|f\|_p > 0$ et $\|g\|_q > 0$. Posons $u = \frac{|f|}{\|f\|_p}$ and $v = \frac{|g|}{\|g\|_q}$.
3. **Application du lemme point par point :**
   $$u(x)v(x) \le \frac{u(x)^p}{p} + \frac{v(x)^q}{q}$$
4. **Intégration :**
   $$\int_X uv d\mu \le \frac{1}{p} \int_X u^p d\mu + \frac{1}{q} \int_X v^q d\mu$$
5. **Calcul des intégrales de u et v :**
   $\int u^p = \int \frac{|f|^p}{\|f\|_p^p} = \frac{\|f\|_p^p}{\|f\|_p^p} = 1$. De même $\int v^q = 1$.
6. **Substitution :**
   $\int \frac{|fg|}{\|f\|_p \|g\|_q} d\mu \le \frac{1}{p}(1) + \frac{1}{q}(1) = 1$.
7. **Conclusion :** $\|fg\|_1 \le \|f\|_p \|g\|_q$.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Application de Jensen (Moyennes)
**Énoncé :** Prouver que la moyenne géométrique est inférieure à la moyenne arithmétique : $(x_1 x_2 \dots x_n)^{1/n} \le \frac{x_1 + \dots + x_n}{n}$.
**Correction Détaillée :**
Considérons la fonction $\phi(u) = -\ln(u)$, qui est convexe sur $]0, +\infty[$. Soit une variable aléatoire $X$ prenant les valeurs $x_i$ avec probabilité $1/n$.
Par Jensen : $-\ln(\mathbb{E}[X]) \le \mathbb{E}[-\ln(X)]$.
$-\ln(\frac{\sum x_i}{n}) \le \frac{1}{n} \sum -\ln(x_i) = -\ln( (\prod x_i)^{1/n} )$.
En multipliant par $-1$ et en appliquant l'exponentielle (croissante), on a le résultat.

### Exercice 2 : Niveau Avancé (Inégalité de Minkowski pour $p=2$)
**Énoncé :** Retrouver Minkowski pour $p=2$ en utilisant Cauchy-Schwarz.
**Correction Détaillée :**
$\|f+g\|_2^2 = \int (f+g)^2 = \int f^2 + 2\int fg + \int g^2$.
Par Cauchy-Schwarz : $\int fg \le \|f\|_2 \|g\|_2$.
Donc $\|f+g\|_2^2 \le \|f\|_2^2 + 2\|f\|_2 \|g\|_2 + \|g\|_2^2 = (\|f\|_2 + \|g\|_2)^2$.
En prenant la racine, on obtient Minkowski.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** L'inégalité de Jensen est la "reine" de l'apprentissage automatique moderne. Elle permet de transformer des problèmes de minimisation impossibles (car l'intégrale est à l'intérieur d'une fonction complexe) en problèmes gérables.
- **Example Concret :**
    - **Variational Auto-Encoders (VAE) :** On veut maximiser la log-vraisemblance $\ln p(x) = \ln \int p(x, z) dz$. L'intégrale est *dans* le logarithme (qui est concave). Jensen permet de dire que $\ln \mathbb{E} \ge \mathbb{E} \ln$. On obtient ainsi l'**ELBO** (Evidence Lower Bound), que l'on peut maximiser par descente de gradient.
    - **Divergence KL :** La preuve que $D_{KL} \ge 0$ (Jalon 72) repose entièrement sur Jensen. C'est ce qui justifie que minimiser la Cross-Entropy a un sens.
    - **EM Algorithm :** L'algorithme Expectation-Maximization utilise Jensen à chaque étape pour garantir que l'on augmente bien la vraisemblance du modèle.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 73 (Espaces Lp et passage au quotient).md]], [[Jalon 18 (Continuité des fonctions d'une variable réelle).md]]
- **Concepts Futurs dépendants :** [[Jalon 75 (Preuve de la complétude des espaces Lp).md]], [[Jalon 91 (Inégalités de concentration).md]]

---
uuid: "jalon-82"
title: "Introduction aux distributions de Schwartz"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 81 (Transformée de Fourier dans L2).md]]"
next: "[[Jalon 83 (Dérivation au sens des distributions).md]]"
---
# Jalon 82 : Introduction à la théorie des distributions de Schwartz

## 1. Introduction historique et physique

La notion de fonction mathématique classique s'est trouvée mise en défaut au cours du $XX^\text{ème}$ siècle face à des besoins physiques concrets. Comment décrire la densité d'une masse ponctuelle ? Comment modéliser mathématiquement une impulsion électrique de durée nulle mais d'intensité infinie, telle qu'une charge ponctuelle ou un choc mécanique instantané ? Les fonctions habituelles, pour lesquelles une valeur non nulle en un seul point n'a aucune influence sur l'intégrale (qui vaut 0), sont incapables de capter ce phénomène.

L'idée fondatrice, théorisée notamment par le mathématicien français Laurent Schwartz (médaille Fields 1950) et pressentie par le physicien Paul Dirac, est de cesser d'évaluer une fonction point par point. Au lieu de s'intéresser à la valeur ponctuelle $f(x)$, on va "tester" l'objet par le biais de fonctions très régulières, dites fonctions tests. Un objet mathématique (une distribution) ne sera plus défini par ses valeurs, mais par son action, via une intégrale, sur toutes les fonctions tests possibles. Cette approche constructiviste et globale étend drastiquement la notion de fonction, permettant de donner un sens rigoureux à la "masse de Dirac" et ouvrant la voie à la dérivation de fonctions discontinues.

## 2. Définitions, Théorèmes et Exemples

### 2.1 L'espace des fonctions tests $\mathcal{D}(\mathbb{R})$

Avant de définir les distributions, il faut construire l'espace des fonctions "sondes", qui vont venir tester notre objet.

**Définition (Espace des fonctions tests) :**
L'espace $\mathcal{D}(\mathbb{R})$ (ou $C^\infty_c(\mathbb{R})$) est l'espace vectoriel des fonctions $\varphi : \mathbb{R} \to \mathbb{C}$ qui satisfont simultanément deux conditions :
1. Elles sont indéfiniment dérivables, c'est-à-dire $\varphi \in C^\infty(\mathbb{R})$.
2. Elles sont à support compact. Le support, noté $\text{supp}(\varphi) = \overline{\{ x \in \mathbb{R} \mid \varphi(x) \neq 0 \}}$, doit être un sous-ensemble borné de $\mathbb{R}$.

**Exemple 1 (Fonction test bulle) :**
Construisons explicitement une fonction test non triviale. Soit $\rho : \mathbb{R} \to \mathbb{R}$ définie par :
$$ \rho(x) = \begin{cases} \exp\left(-\frac{1}{1-x^2}\right) & \text{si } |x| < 1 \\ 0 & \text{si } |x| \ge 1 \end{cases} $$
- **Support :** Par définition, $\rho(x) = 0$ pour $|x| \ge 1$. Donc, $\text{supp}(\rho) \subset [-1, 1]$, qui est compact.
- **Régularité :** Sur $]-1, 1[$, la fonction est une composée de fonctions $C^\infty$. En $x=1$ (et $x=-1$), on peut vérifier que toutes les dérivées à gauche de $x \mapsto \exp\left(-\frac{1}{1-x^2}\right)$ tendent vers $0$. Par conséquent, toutes les dérivées se recollent continûment à $0$, ce qui prouve que $\rho \in C^\infty(\mathbb{R})$.
Ainsi, $\rho \in \mathcal{D}(\mathbb{R})$.

### 2.2 Notion de Topologie sur $\mathcal{D}(\mathbb{R})$ (Convergence)

Pour parler de la continuité d'une forme linéaire sur $\mathcal{D}(\mathbb{R})$, il nous faut définir ce que signifie la convergence d'une suite de fonctions tests vers zéro.

**Définition (Convergence dans $\mathcal{D}(\mathbb{R})$) :**
Une suite $(\varphi_n)_{n \in \mathbb{N}}$ de fonctions de $\mathcal{D}(\mathbb{R})$ converge vers $0$ dans $\mathcal{D}(\mathbb{R})$ si les deux conditions suivantes sont réunies :
1. Il existe un compact fixe $K \subset \mathbb{R}$ tel que pour tout $n \in \mathbb{N}$, $\text{supp}(\varphi_n) \subset K$. (Leurs supports ne s'échappent pas à l'infini).
2. Pour tout entier $k \ge 0$, la suite des dérivées $k$-ièmes $(\varphi_n^{(k)})_{n \in \mathbb{N}}$ converge uniformément vers $0$ sur $K$.

**Exemple 2 (Suite de fonctions tests tendant vers $0$) :**
Posons $\varphi_n(x) = \frac{1}{n} \rho(x)$, où $\rho$ est la fonction définie dans l'Exemple 1.
- Pour tout $n$, $\text{supp}(\varphi_n) \subset [-1, 1]$. On pose donc $K = [-1, 1]$.
- Pour un entier $k$ fixé, $\varphi_n^{(k)}(x) = \frac{1}{n} \rho^{(k)}(x)$. Comme $\rho^{(k)}$ est continue sur le compact $K$, elle est bornée par une constante $M_k$.
- Ainsi, $\| \varphi_n^{(k)} \|_\infty \le \frac{M_k}{n}$, qui tend vers $0$ quand $n \to +\infty$.
La suite $(\varphi_n)$ converge donc vers $0$ dans $\mathcal{D}(\mathbb{R})$.

### 2.3 Définition des Distributions $\mathcal{D}'(\mathbb{R})$

Nous pouvons maintenant définir rigoureusement ce qu'est une distribution.

**Définition (Distribution) :**
Une distribution $T$ sur $\mathbb{R}$ est une forme linéaire continue sur l'espace $\mathcal{D}(\mathbb{R})$. L'ensemble des distributions est noté $\mathcal{D}'(\mathbb{R})$ (le dual topologique de $\mathcal{D}(\mathbb{R})$).
Plus précisément, $T : \mathcal{D}(\mathbb{R}) \to \mathbb{C}$ vérifie :
1. **Linéarité :** Pour tout $\lambda, \mu \in \mathbb{C}$ et $\varphi, \psi \in \mathcal{D}(\mathbb{R})$,
   $$ \langle T, \lambda\varphi + \mu\psi \rangle = \lambda\langle T, \varphi \rangle + \mu\langle T, \psi \rangle $$
2. **Continuité séquentielle :** Pour toute suite $(\varphi_n)$ tendant vers $0$ dans $\mathcal{D}(\mathbb{R})$, la suite complexe $\langle T, \varphi_n \rangle$ tend vers $0$ dans $\mathbb{C}$.

*Remarque typographique :* On note souvent l'action de la distribution $T$ sur la fonction test $\varphi$ par le crochet de dualité $\langle T, \varphi \rangle$ au lieu de $T(\varphi)$.

### 2.4 Distributions régulières associées aux fonctions $L^1_{loc}$

Toute fonction "classique" raisonnable peut être vue comme une distribution.

**Définition (Fonction localement intégrable) :**
Une fonction $f : \mathbb{R} \to \mathbb{C}$ est dite localement intégrable, notée $f \in L^1_{loc}(\mathbb{R})$, si pour tout compact $K \subset \mathbb{R}$, l'intégrale de Lebesgue $\int_K |f(x)| \,dx$ est finie.

**Théorème et Définition (Distribution régulière) :**
Soit $f \in L^1_{loc}(\mathbb{R})$. L'application $T_f : \mathcal{D}(\mathbb{R}) \to \mathbb{C}$ définie par
$$ \langle T_f, \varphi \rangle = \int_{\mathbb{R}} f(x)\varphi(x) \,dx $$
est une distribution sur $\mathbb{R}$, appelée distribution régulière.

**Exemple 3 (La fonction constante 1) :**
Soit $f(x) = 1$ pour tout $x \in \mathbb{R}$. Bien que $f$ ne soit pas globalement intégrable (elle n'est pas dans $L^1(\mathbb{R})$), elle est localement intégrable car l'intégrale sur un compact $[a,b]$ donne $b-a < +\infty$.
La distribution associée est :
$$ \langle T_1, \varphi \rangle = \int_{\mathbb{R}} 1 \cdot \varphi(x) \,dx = \int_{-\infty}^{+\infty} \varphi(x) \,dx $$
Cette intégrale est bien définie car $\varphi$ est continue et à support compact.

**Exemple 4 (La fonction échelon de Heaviside) :**
Considérons la fonction $H(x) = 1$ si $x > 0$, et $0$ sinon. Elle est dans $L^1_{loc}(\mathbb{R})$. Sa distribution associée opère ainsi :
$$ \langle T_H, \varphi \rangle = \int_{\mathbb{R}} H(x)\varphi(x) \,dx = \int_{0}^{+\infty} \varphi(x) \,dx $$
Encore une fois, l'intégrale converge car le support de $\varphi$ borne l'intervalle d'intégration.

### 2.5 Distributions singulières : La masse de Dirac

Les distributions singulières sont celles qui ne peuvent pas être représentées par l'intégration d'une fonction $L^1_{loc}$.

**Définition (Distribution de Dirac) :**
Soit $a \in \mathbb{R}$. La distribution de Dirac au point $a$, notée $\delta_a$, est définie par son action sur une fonction test $\varphi \in \mathcal{D}(\mathbb{R})$ :
$$ \langle \delta_a, \varphi \rangle = \varphi(a) $$
En particulier, l'impulsion à l'origine est $\delta_0$, définie par $\langle \delta_0, \varphi \rangle = \varphi(0)$.

**Exemple 5 (Action d'une somme de Diracs) :**
Soit $T = 3\delta_1 - 2\delta_{-1}$. Pour $\varphi \in \mathcal{D}(\mathbb{R})$ :
$$ \langle T, \varphi \rangle = 3\langle \delta_1, \varphi \rangle - 2\langle \delta_{-1}, \varphi \rangle = 3\varphi(1) - 2\varphi(-1) $$
C'est une évaluation ponctuelle pondérée.

**Contre-exemple (Distribution non définie) :**
L'expression $\langle T, \varphi \rangle = \sum_{n=1}^\infty \varphi^{(n)}(0)$ ne définit pas une distribution. Bien que chaque terme soit bien défini (puisque $\varphi \in C^\infty$), la somme n'a aucune raison de converger pour une fonction test arbitraire. La continuité d'une distribution impose qu'elle ne fasse intervenir localement qu'un nombre fini de dérivées.

## 3. Démonstrations Fondamentales

### 3.1 Démonstration de la continuité de la distribution régulière $T_f$

**Théorème :** Si $f \in L^1_{loc}(\mathbb{R})$, la forme linéaire $T_f : \varphi \mapsto \int_{\mathbb{R}} f(x)\varphi(x) \,dx$ est continue sur $\mathcal{D}(\mathbb{R})$, et est donc bien une distribution.

*Preuve détaillée ligne par ligne :*
1. La linéarité découle immédiatement de la linéarité de l'intégrale.
2. Pour la continuité, soit $(\varphi_n)$ une suite de fonctions de $\mathcal{D}(\mathbb{R})$ convergeant vers $0$ dans $\mathcal{D}(\mathbb{R})$.
3. Par définition de cette convergence, il existe un compact $K$ tel que pour tout $n$, $\text{supp}(\varphi_n) \subset K$.
4. De plus, la suite $(\varphi_n)$ converge uniformément vers $0$ sur $K$. C'est-à-dire que $\| \varphi_n \|_{\infty, K} = \sup_{x \in K} |\varphi_n(x)| \xrightarrow[n \to \infty]{} 0$.
5. Majorons la valeur absolue de l'action de $T_f$ sur $\varphi_n$ :
   $$ |\langle T_f, \varphi_n \rangle| = \left| \int_{\mathbb{R}} f(x)\varphi_n(x) \,dx \right| $$
6. Puisque $\text{supp}(\varphi_n) \subset K$, l'intégrale se réduit à $K$ :
   $$ |\langle T_f, \varphi_n \rangle| = \left| \int_K f(x)\varphi_n(x) \,dx \right| \le \int_K |f(x)| |\varphi_n(x)| \,dx $$
7. On extrait le terme constant de la fonction borne sur $K$ :
   $$ \int_K |f(x)| |\varphi_n(x)| \,dx \le \| \varphi_n \|_{\infty, K} \int_K |f(x)| \,dx $$
8. Comme $f \in L^1_{loc}(\mathbb{R})$ et $K$ est compact, l'intégrale $C_K = \int_K |f(x)| \,dx$ est une constante finie fixée indépendante de $n$.
9. On a donc : $|\langle T_f, \varphi_n \rangle| \le C_K \| \varphi_n \|_{\infty, K}$.
10. Comme $\| \varphi_n \|_{\infty, K} \to 0$, le théorème des gendarmes impose que $|\langle T_f, \varphi_n \rangle| \to 0$.
11. $T_f$ est donc une forme linéaire continue, d'où $T_f \in \mathcal{D}'(\mathbb{R})$. $\blacksquare$

### 3.2 Démonstration : La masse de Dirac $\delta_0$ n'est pas une distribution régulière

**Théorème :** Il n'existe aucune fonction $f \in L^1_{loc}(\mathbb{R})$ telle que pour tout $\varphi \in \mathcal{D}(\mathbb{R})$, on ait $\int_{\mathbb{R}} f(x)\varphi(x) \,dx = \varphi(0)$.

*Preuve détaillée par l'absurde :*
1. Supposons qu'il existe $f \in L^1_{loc}(\mathbb{R})$ telle que $T_f = \delta_0$.
2. Considérons une fonction plateau $\rho \in \mathcal{D}(\mathbb{R})$ telle que $0 \le \rho \le 1$, $\rho(0) = 1$ et $\text{supp}(\rho) \subset [-1, 1]$.
3. Pour tout entier $n \ge 1$, définissons la suite de fonctions tests "rétrécies" : $\varphi_n(x) = \rho(nx)$.
4. Vérifions les propriétés de $\varphi_n$ : $\varphi_n(0) = \rho(0) = 1$, et $\text{supp}(\varphi_n) \subset [-1/n, 1/n]$. De plus, $0 \le \varphi_n(x) \le 1$ partout.
5. Évaluons $\delta_0$ sur $\varphi_n$ :
   $$ \langle \delta_0, \varphi_n \rangle = \varphi_n(0) = 1 $$
6. Évaluons $T_f$ sur $\varphi_n$ :
   $$ \langle T_f, \varphi_n \rangle = \int_{\mathbb{R}} f(x)\varphi_n(x) \,dx = \int_{-1/n}^{1/n} f(x)\varphi_n(x) \,dx $$
7. Majorons cette intégrale :
   $$ |\langle T_f, \varphi_n \rangle| \le \int_{-1/n}^{1/n} |f(x)| |\varphi_n(x)| \,dx $$
8. Comme $|\varphi_n(x)| \le 1$, on obtient l'inégalité :
   $$ |\langle T_f, \varphi_n \rangle| \le \int_{-1/n}^{1/n} |f(x)| \,dx $$
9. Puisque $f \in L^1_{loc}(\mathbb{R})$, $|f|$ est localement intégrable (donc intégrable sur un compact contenant $[-1,1]$).
10. L'ensemble d'intégration $A_n = [-1/n, 1/n]$ a pour mesure de Lebesgue $\mu(A_n) = \frac{2}{n}$.
11. Lorsque $n \to +\infty$, $\mu(A_n) \to 0$. Le théorème de la convergence dominée (ou la continuité absolue de l'intégrale de Lebesgue) stipule que si l'on intègre une fonction $L^1$ sur un ensemble dont la mesure tend vers $0$, l'intégrale tend vers $0$.
12. Donc, $\lim_{n \to \infty} \int_{-1/n}^{1/n} |f(x)| \,dx = 0$.
13. On aboutit à la conclusion que $\lim_{n \to \infty} |\langle T_f, \varphi_n \rangle| = 0$.
14. Or, par notre hypothèse d'égalité $T_f = \delta_0$, nous avions $\langle T_f, \varphi_n \rangle = 1$ pour tout $n$, ce qui force $1 = 0$.
15. Cette contradiction démontre que la masse de Dirac ne peut en aucun cas être identifiée à une fonction usuelle. C'est une authentique distribution singulière. $\blacksquare$

## 4. Applications en Physique, Logique et IA

**Physique et Traitement du Signal**
En traitement du signal, la masse de Dirac (aussi appelée impulsion unité) est cruciale. Elle permet de définir la réponse impulsionnelle d'un système. Lorsqu'un système physique linéaire (comme un filtre électrique ou un amortisseur mécanique) est frappé par un choc instantané (modélisé par $\delta_0$), la fonction de sortie qui en résulte caractérise intégralement le système. Par le formalisme des convolutions de distributions, la réponse du système à toute entrée arbitraire $e(t)$ sera donnée par $s(t) = (e * h)(t)$, où $h$ est la réponse impulsionnelle.

**Intelligence Artificielle et Statistiques**
Dans le domaine du Machine Learning, nous manipulons constamment des distributions de Dirac sans toujours le dire.
- **Probabilités empiriques :** Lorsque nous disposons d'un jeu de données d'apprentissage fini $\{x_1, x_2, \dots, x_N\}$, la "vraie" distribution des données est inconnue. L'algorithme se base sur la distribution empirique des données, qui s'écrit formelusement comme une somme de Diracs :
  $$ \hat{\mathbb{P}}(x) = \frac{1}{N} \sum_{i=1}^N \delta_{x_i}(x) $$
- **Espérance et Loss :** L'espérance mathématique d'une fonction (par exemple, la fonction de perte $L(x)$) sous cette distribution empirique se traduit par l'action de la distribution sur la fonction :
  $$ \mathbb{E}_{x \sim \hat{\mathbb{P}}}[L(x)] = \langle \hat{\mathbb{P}}, L \rangle = \frac{1}{N} \sum_{i=1}^N L(x_i) $$
Cela donne un cadre analytique rigoureux justifiant pourquoi l'optimisation stochastique (SGD) travaille au sens des distributions sur la surface d'erreur définie par un ensemble fini de points singuliers. L'extension continue de ces Dirac (par ajout de bruit gaussien) s'appelle le lissage de la distribution, une technique utilisée pour rendre les surfaces de perte différentiables.

---
uuid: "jalon-79"
title: "Convergence L2 et Identité de Parseval"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/traitement-du-signal
prev: "[[Jalon-78.md]]"
next: "[[Jalon 80 (Transformée de Fourier dans L1).md]]"
---

# Jalon 79 : Convergence $L^2$ et Identité de Parseval

## 1. Introduction

L'étude des séries de Fourier nous permet de décomposer une fonction périodique en une somme infinie de sinus et cosinus, ou de façon équivalente, d'exponentielles complexes. Mais en quel sens cette série converge-t-elle vers la fonction initiale ? Le théorème de convergence de Dirichlet (vu au Jalon précédent) donne des conditions suffisantes pour une convergence ponctuelle. Cependant, dans de nombreux problèmes physiques et d'ingénierie, il est plus pertinent de s'intéresser à l'énergie globale du signal plutôt qu'à sa valeur exacte en chaque point isolé.

Imaginez que vous démontiez une voiture pour la vendre en pièces détachées. La voiture entière a un certain poids total, représentant sa "masse". Vous la démontez en sous-composants : le moteur, les roues, les boulons. L'Identité de Parseval stipule que le poids total de la voiture assemblée est rigoureusement égal à la somme des poids de toutes les pièces détachées. Aucune masse n'est perdue ni créée lors du démontage.

En traitement du signal, le "poids" correspond à l'énergie du signal, définie par l'intégrale de son carré (la norme $L^2$). Les "pièces détachées" sont les composantes fréquentielles pures, dont le "poids" est donné par le carré des coefficients de Fourier. L'Identité de Parseval affirme que l'énergie totale calculée dans le domaine temporel (l'onde continue) est égale à la somme des énergies de ses harmoniques calculées dans le domaine fréquentiel.

Historiquement, cette égalité profonde a permis de résoudre des problèmes autrement insolubles. Parfois, calculer l'intégrale du carré d'une fonction complexe est ardu, mais si ses coefficients de Fourier sont simples, on peut trouver la réponse par une somme infinie de termes. Inversement, l'identité de Parseval offre une méthode spectaculaire pour calculer la valeur exacte de séries numériques complexes en les identifiant à l'énergie d'un signal connu (comme la somme des inverses des carrés d'entiers $\sum \frac{1}{n^2}$).

## 2. Formalisation et Rigueur Mathématique

### A. Cadre Hilbertien des fonctions de carré intégrable

Nous considérons l'espace $H = L^2([0, 2\pi], \mathbb{C})$, l'espace des fonctions mesurables $2\pi$-périodiques, de carré intégrable sur une période, à valeurs complexes, quotienté par la relation d'égalité presque partout.

Cet espace est muni du produit scalaire hermitien canonique :
$$\forall f, g \in L^2, \quad \langle f, g \rangle = \frac{1}{2\pi} \int_0^{2\pi} f(t) \overline{g(t)} \, dt$$
et de la norme associée (la norme quadratique) :
$$\|f\|_2 = \sqrt{\langle f, f \rangle} = \left( \frac{1}{2\pi} \int_0^{2\pi} |f(t)|^2 \, dt \right)^{1/2}$$

La famille des fonctions exponentielles complexes $(e_n)_{n \in \mathbb{Z}}$ définies par $e_n(t) = e^{int}$ forme une famille orthonormée dans $H$ car :
$$\langle e_n, e_m \rangle = \frac{1}{2\pi} \int_0^{2\pi} e^{int} e^{-imt} \, dt = \delta_{n,m}$$

Pour tout $f \in L^2$, les coefficients de Fourier exponentiels sont définis par les produits scalaires :
$$c_n(f) = \langle f, e_n \rangle = \frac{1}{2\pi} \int_0^{2\pi} f(t) e^{-int} \, dt$$

La $N$-ième somme partielle de la série de Fourier de $f$ est la fonction :
$$S_N(f)(t) = \sum_{n=-N}^{N} c_n(f) e^{int}$$
Géométriquement, $S_N(f)$ est la projection orthogonale de la fonction $f$ sur le sous-espace de dimension finie $H_N = \text{Vect}(e_{-N}, e_{-N+1}, \dots, e_0, \dots, e_N)$.


### B. Théorème de Convergence en Moyenne Quadratique

> **Théorème (Convergence $L^2$) :**
> Soit $f \in L^2([0, 2\pi])$. La série de Fourier de $f$ converge vers $f$ au sens de la norme quadratique $L^2$, c'est-à-dire :
> $$\lim_{N \to \infty} \| f - S_N(f) \|_2 = 0$$
> Ce qui s'écrit explicitement :
> $$\lim_{N \to \infty} \frac{1}{2\pi} \int_0^{2\pi} \left| f(t) - \sum_{n=-N}^N c_n(f) e^{int} \right|^2 dt = 0$$

Ce théorème énonce que la famille $(e_n)_{n \in \mathbb{Z}}$ est "totale" dans $L^2$, elle constitue donc une base hilbertienne de l'espace $L^2([0, 2\pi])$.

### C. L'Identité de Parseval

> **Théorème (Identité de Parseval) :**
> Pour toute fonction $f \in L^2([0, 2\pi])$, l'énergie totale (norme au carré) est égale à la somme de la série des carrés des modules de ses coefficients de Fourier :
> $$\frac{1}{2\pi} \int_0^{2\pi} |f(t)|^2 \, dt = \sum_{n=-\infty}^{+\infty} |c_n(f)|^2$$
>
> En utilisant la convention des coefficients trigonométriques réels ($a_n, b_n$) définis pour une fonction réelle par :
> $$a_n(f) = \frac{1}{\pi} \int_0^{2\pi} f(t) \cos(nt) \, dt \quad (n \ge 0)$$
> $$b_n(f) = \frac{1}{\pi} \int_0^{2\pi} f(t) \sin(nt) \, dt \quad (n \ge 1)$$
> L'identité de Parseval s'écrit de manière équivalente :
> $$\frac{1}{2\pi} \int_0^{2\pi} |f(t)|^2 \, dt = \frac{a_0(f)^2}{4} + \frac{1}{2} \sum_{n=1}^\infty \left( a_n(f)^2 + b_n(f)^2 \right)$$

**Exemple 1 : Signal constant**
Soit $f(t) = 5$.
Calculons son énergie temporelle :
$$\frac{1}{2\pi} \int_0^{2\pi} 5^2 dt = \frac{1}{2\pi} [25t]_0^{2\pi} = 25$$
Ses coefficients de Fourier : $c_0 = \frac{1}{2\pi} \int_0^{2\pi} 5 e^0 dt = 5$. Pour $n \neq 0$, $c_n = 0$.
Somme des carrés fréquentiels : $\sum |c_n|^2 = |c_0|^2 = 5^2 = 25$.
Les deux membres sont égaux.

**Exemple 2 : Fonction sinusoïdale simple**
Soit $f(t) = 3 \cos(t)$.
Énergie temporelle :
$$\frac{1}{2\pi} \int_0^{2\pi} 9 \cos^2(t) dt = \frac{9}{2\pi} \int_0^{2\pi} \frac{1 + \cos(2t)}{2} dt = \frac{9}{2\pi} \left[ \frac{t}{2} + \frac{\sin(2t)}{4} \right]_0^{2\pi} = \frac{9}{2\pi} \times \pi = 4.5$$
Coefficients de Fourier : $f(t) = 3 \left(\frac{e^{it} + e^{-it}}{2}\right) = 1.5 e^{it} + 1.5 e^{-it}$.
Donc $c_1 = 1.5$, $c_{-1} = 1.5$, et tous les autres $c_n = 0$.
Somme des carrés : $|c_{-1}|^2 + |c_1|^2 = 1.5^2 + 1.5^2 = 2.25 + 2.25 = 4.5$.
L'égalité est bien vérifiée.

**Exemple 3 : Onde carrée modifiée**
Soit $f(t)$ qui vaut $1$ sur $[0, \pi[$ et $-1$ sur $[\pi, 2\pi[$.
Énergie temporelle :
$$\frac{1}{2\pi} \int_0^{2\pi} |f(t)|^2 dt = \frac{1}{2\pi} \left( \int_0^{\pi} 1 dt + \int_{\pi}^{2\pi} (-1)^2 dt \right) = \frac{1}{2\pi} (\pi + \pi) = 1$$
Coefficients de Fourier :
$c_0 = 0$. Pour $n \neq 0$ :
$$c_n = \frac{1}{2\pi} \left( \int_0^{\pi} e^{-int} dt - \int_{\pi}^{2\pi} e^{-int} dt \right) = \frac{1}{2\pi} \left( \left[ \frac{e^{-int}}{-in} \right]_0^\pi - \left[ \frac{e^{-int}}{-in} \right]_\pi^{2\pi} \right)$$
$$c_n = \frac{i}{2\pi n} \left( (e^{-in\pi} - 1) - (1 - e^{-in\pi}) \right) = \frac{i}{2\pi n} (2(-1)^n - 2) = \frac{i( (-1)^n - 1 )}{\pi n}$$
Si $n$ est pair ($n=2p$), $c_{2p} = 0$.
Si $n$ est impair ($n=2p+1$), $c_{2p+1} = \frac{-2i}{\pi(2p+1)}$.
L'énergie fréquentielle est la somme sur tous les $n$ impairs (positifs et négatifs) :
$$\sum_{k=-\infty}^\infty \left| \frac{-2i}{\pi(2k+1)} \right|^2 = \sum_{k=-\infty}^\infty \frac{4}{\pi^2 (2k+1)^2} = \frac{8}{\pi^2} \sum_{k=0}^\infty \frac{1}{(2k+1)^2}$$
Puisque la somme de l'énergie vaut $1$, on en déduit la relation remarquable :
$$\sum_{k=0}^\infty \frac{1}{(2k+1)^2} = \frac{\pi^2}{8}$$
Une illustration élégante de l'utilité du théorème de Parseval.

**Exemple 4 : La fonction "triangle"**
Soit $f(t) = |t|$ sur $[-\pi, \pi]$. C'est une fonction paire. L'intégrale sur $[-\pi, \pi]$ est égale à celle sur $[0, 2\pi]$ pour le carré.
Énergie temporelle :
$$\frac{1}{2\pi} \int_{-\pi}^\pi t^2 dt = \frac{1}{2\pi} \left[ \frac{t^3}{3} \right]_{-\pi}^\pi = \frac{1}{2\pi} \frac{2\pi^3}{3} = \frac{\pi^2}{3}$$
Le coefficient $a_0 = \frac{1}{\pi} \int_{-\pi}^\pi |t| dt = \pi$.
Les coefficients $a_n = \frac{1}{\pi} \int_{-\pi}^\pi |t| \cos(nt) dt = \frac{2}{\pi} \int_0^\pi t \cos(nt) dt$. Par intégration par parties ($u=t, v'=\cos(nt), u'=1, v=\frac{\sin(nt)}{n}$) :
$$a_n = \frac{2}{\pi} \left[ t \frac{\sin(nt)}{n} \right]_0^\pi - \frac{2}{\pi} \int_0^\pi \frac{\sin(nt)}{n} dt = 0 - \frac{2}{\pi} \left[ \frac{-\cos(nt)}{n^2} \right]_0^\pi = \frac{2}{\pi n^2} ((-1)^n - 1)$$
Ainsi $a_{2p} = 0$ et $a_{2p+1} = \frac{-4}{\pi(2p+1)^2}$.
Par Parseval avec la convention réelle : $\frac{a_0^2}{4} + \frac{1}{2} \sum_{n=1}^\infty a_n^2 = \frac{\pi^2}{3}$
$$\frac{\pi^2}{4} + \frac{1}{2} \sum_{p=0}^\infty \frac{16}{\pi^2(2p+1)^4} = \frac{\pi^2}{3}$$
$$\frac{8}{\pi^2} \sum_{p=0}^\infty \frac{1}{(2p+1)^4} = \frac{\pi^2}{3} - \frac{\pi^2}{4} = \frac{\pi^2}{12}$$
On trouve ainsi la somme $\sum_{p=0}^\infty \frac{1}{(2p+1)^4} = \frac{\pi^4}{96}$.

**Exemple 5 : Signal impulsion de Dirac lissée**
Prenons la suite de fonctions $D_N(t) = \sum_{n=-N}^N e^{int} = \frac{\sin((N+1/2)t)}{\sin(t/2)}$ (Noyau de Dirichlet).
C'est un polynôme trigonométrique, il est égal à sa propre somme de Fourier.
$c_n(D_N) = 1$ pour $-N \le n \le N$, et $0$ sinon.
Énergie fréquentielle : $\sum_{n=-N}^N |1|^2 = 2N + 1$.
Par Parseval, cela signifie immédiatement que l'intégrale de son carré (très fastidieuse à calculer directement) est :
$$\frac{1}{2\pi} \int_0^{2\pi} \left( \frac{\sin((N+1/2)t)}{\sin(t/2)} \right)^2 dt = 2N + 1$$


## 3. Démonstrations Pas-à-Pas

### Démonstration de l'Identité de Parseval

Cette preuve repose sur la géométrie hilbertienne, en exploitant l'orthonormalité de la base exponentielle et le Théorème de Pythagore généralisé, combinés à la densité des polynômes trigonométriques.

1. **Calcul de l'énergie de la projection orthogonale (somme partielle $S_N(f)$) :**
   Considérons la somme partielle de Fourier $S_N(f)(t) = \sum_{n=-N}^N c_n e_n(t)$.
   Calculons sa norme $L^2$ au carré :
   $$\|S_N(f)\|_2^2 = \langle S_N(f), S_N(f) \rangle = \langle \sum_{n=-N}^N c_n e_n, \sum_{m=-N}^N c_m e_m \rangle$$
   Par la bilinéarité (linéarité à gauche et antilinéarité à droite) du produit scalaire hermitien :
   $$\|S_N(f)\|_2^2 = \sum_{n=-N}^N \sum_{m=-N}^N c_n \overline{c_m} \langle e_n, e_m \rangle$$

2. **Exploitation de l'orthonormalité :**
   Or, le système exponentiel est orthonormé : $\langle e_n, e_m \rangle = \delta_{n,m}$. L'expression double ne garde donc que les termes "diagonaux" où $n = m$, réduisant la double somme à une simple somme :
   $$\|S_N(f)\|_2^2 = \sum_{n=-N}^N c_n \overline{c_n} \cdot 1 = \sum_{n=-N}^N |c_n|^2$$
   Ceci est le théorème de Pythagore classique en dimension finie.

3. **Inégalité de Bessel (Étape intermédiaire) :**
   Le signal $f$ se décompose orthogonalement en $f = S_N(f) + (f - S_N(f))$.
   La somme $S_N(f)$ appartient au sous-espace engendré par $\{e_{-N}, \dots, e_N\}$, et le "reste" $f - S_N(f)$ est orthogonal à ce sous-espace par propriété de la projection orthogonale, donc $\langle S_N(f), f - S_N(f) \rangle = 0$.
   En appliquant le théorème de Pythagore dans $L^2$ :
   $$\|f\|_2^2 = \|S_N(f) + (f - S_N(f))\|_2^2 = \|S_N(f)\|_2^2 + \|f - S_N(f)\|_2^2$$
   Puisque $\|f - S_N(f)\|_2^2 \ge 0$, on en déduit immédiatement :
   $$\|S_N(f)\|_2^2 \le \|f\|_2^2 \implies \sum_{n=-N}^N |c_n|^2 \le \frac{1}{2\pi} \int_0^{2\pi} |f(t)|^2 dt$$
   C'est l'**Inégalité de Bessel**, valable pour tout $N$. La série des carrés est croissante et majorée, elle converge donc formellement vers une valeur finie $\le \|f\|_2^2$.

4. **Passage à la limite via la convergence $L^2$ :**
   Le théorème de convergence en moyenne quadratique (basé sur la densité des fonctions continues et le théorème de Fejér) stipule que la limite de l'erreur est nulle :
   $$\lim_{N \to \infty} \|f - S_N(f)\|_2^2 = 0$$
   Reprenons l'égalité du théorème de Pythagore :
   $$\|f\|_2^2 = \sum_{n=-N}^N |c_n|^2 + \|f - S_N(f)\|_2^2$$
   En passant à la limite lorsque $N \to \infty$, le terme de l'erreur s'annule, et il reste :
   $$\|f\|_2^2 = \lim_{N \to \infty} \sum_{n=-N}^N |c_n|^2 = \sum_{n=-\infty}^\infty |c_n|^2$$
   C'est exactement l'Identité de Parseval.


## 4. Exercices d'Application

### Exercice 1 : Calcul de la somme de Bâle $\sum \frac{1}{n^2}$
**Énoncé :** En étudiant la fonction $f(t) = t$ sur $]-\pi, \pi]$ étendue par périodicité, démontrer que $\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$.

**Correction Détaillée :**
* *Calcul de l'énergie temporelle :*
  La fonction $f(t)$ est définie sur $]-\pi, \pi]$ et $2\pi$-périodique.
  $$\frac{1}{2\pi} \int_{-\pi}^\pi (t)^2 dt = \frac{1}{2\pi} \left[ \frac{t^3}{3} \right]_{-\pi}^\pi = \frac{1}{2\pi} \left( \frac{\pi^3}{3} - \frac{-\pi^3}{3} \right) = \frac{1}{2\pi} \frac{2\pi^3}{3} = \frac{\pi^2}{3}$$
* *Calcul des coefficients de Fourier complexes :*
  La fonction est impaire, $c_0 = \frac{1}{2\pi}\int_{-\pi}^\pi t dt = 0$.
  Pour $n \neq 0$ :
  $$c_n = \frac{1}{2\pi} \int_{-\pi}^\pi t e^{-int} dt$$
  On réalise une intégration par parties, avec $u=t \implies u'=1$ et $v'=e^{-int} \implies v = \frac{e^{-int}}{-in}$ :
  $$c_n = \frac{1}{2\pi} \left( \left[ t \frac{e^{-int}}{-in} \right]_{-\pi}^\pi - \int_{-\pi}^\pi \frac{e^{-int}}{-in} dt \right)$$
  $$c_n = \frac{1}{2\pi} \left( \frac{\pi e^{-in\pi}}{-in} - \frac{(-\pi) e^{in\pi}}{-in} - \left[ \frac{e^{-int}}{-(in)^2} \right]_{-\pi}^\pi \right)$$
  Sachant que $e^{-in\pi} = e^{in\pi} = (-1)^n$. Et l'intégrale résiduelle s'annule car $e^{-int}$ a une intégrale nulle sur une période.
  $$c_n = \frac{1}{2\pi} \left( \frac{\pi (-1)^n}{-in} + \frac{\pi (-1)^n}{-in} \right) = \frac{1}{2\pi} \frac{2\pi (-1)^n}{-in} = \frac{i (-1)^n}{n}$$
* *Identité de Parseval :*
  On applique $\frac{1}{2\pi} \int_{-\pi}^\pi |f(t)|^2 dt = \sum_{n=-\infty}^\infty |c_n|^2$.
  On calcule le carré du module des coefficients : $|c_n|^2 = \left|\frac{i (-1)^n}{n}\right|^2 = \frac{1}{n^2}$.
  La somme bilatérale (pour $n \in \mathbb{Z}^*$ car $c_0=0$) est :
  $$\sum_{n \neq 0} \frac{1}{n^2} = \sum_{n=1}^\infty \frac{1}{n^2} + \sum_{n=1}^\infty \frac{1}{(-n)^2} = 2 \sum_{n=1}^\infty \frac{1}{n^2}$$
  En injectant dans l'équation de Parseval :
  $$\frac{\pi^2}{3} = 2 \sum_{n=1}^\infty \frac{1}{n^2}$$
  D'où le résultat exceptionnel d'Euler : $\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$.


### Exercice 2 : Inégalité de Wirtinger (Poincaré en dimension 1)
**Énoncé :** Soit $f \in \mathcal{C}^1([0, 2\pi])$ telle que $f(0)=f(2\pi)$ (fonction $2\pi$-périodique de classe $C^1$) et de moyenne nulle : $\int_0^{2\pi} f(t) dt = 0$.
Montrer rigoureusement l'inégalité optimale : $\int_0^{2\pi} |f(t)|^2 dt \le \int_0^{2\pi} |f'(t)|^2 dt$.
Dans quels cas y a-t-il égalité ?

**Correction Détaillée :**
* *Utilisation des séries de Fourier de la dérivée :*
  On exprime les coefficients de $f'$ en fonction de ceux de $f$.
  $$c_n(f') = \frac{1}{2\pi} \int_0^{2\pi} f'(t) e^{-int} dt$$
  Intégration par parties ($u = e^{-int}, u' = -in e^{-int}$ et $v' = f', v = f$) :
  $$c_n(f') = \frac{1}{2\pi} \left[ f(t) e^{-int} \right]_0^{2\pi} - \frac{1}{2\pi} \int_0^{2\pi} f(t) (-in e^{-int}) dt$$
  Comme $f(2\pi) = f(0)$ et $e^{-i n 2\pi} = 1 = e^0$, le terme de bord s'annule strictement.
  Il reste $c_n(f') = in c_n(f)$.
* *Application de Parseval aux deux fonctions :*
  Pour $f'$ : $\frac{1}{2\pi} \int_0^{2\pi} |f'(t)|^2 dt = \sum_{n \in \mathbb{Z}} |c_n(f')|^2 = \sum_{n \in \mathbb{Z}} |in c_n(f)|^2 = \sum_{n \in \mathbb{Z}} n^2 |c_n(f)|^2$
  Pour $f$ : $\frac{1}{2\pi} \int_0^{2\pi} |f(t)|^2 dt = \sum_{n \in \mathbb{Z}} |c_n(f)|^2$
* *Comparaison des spectres :*
  Par hypothèse de moyenne nulle, le terme constant de Fourier est nul :
  $$c_0(f) = \frac{1}{2\pi} \int_0^{2\pi} f(t) dt = 0$$
  On compare les sommes terme à terme. Pour tout $n \in \mathbb{Z} \setminus \{0\}$, on a clairement $n^2 \ge 1$.
  Donc $\forall n \neq 0, |c_n(f)|^2 \le n^2 |c_n(f)|^2$.
  En sommant ces inégalités sur tous les $n \neq 0$ :
  $$\sum_{n \neq 0} |c_n(f)|^2 \le \sum_{n \neq 0} n^2 |c_n(f)|^2$$
  On réécrit avec les intégrales via Parseval :
  $$\frac{1}{2\pi} \int_0^{2\pi} |f(t)|^2 dt \le \frac{1}{2\pi} \int_0^{2\pi} |f'(t)|^2 dt$$
  Ce qui prouve $\int_0^{2\pi} |f(t)|^2 dt \le \int_0^{2\pi} |f'(t)|^2 dt$.
* *Cas d'égalité :*
  Il y a égalité ssi la somme des différences est nulle : $\sum_{n \neq 0} (n^2 - 1) |c_n(f)|^2 = 0$.
  Comme $n^2 - 1 > 0$ pour $|n| \ge 2$, l'égalité impose impérativement $c_n(f) = 0$ pour tout $n \notin \{-1, 0, 1\}$.
  Comme $c_0 = 0$, la fonction $f$ doit s'écrire uniquement avec les harmoniques de fréquence 1 : $f(t) = c_1 e^{it} + c_{-1} e^{-it}$.
  Donc $f(t) = a \cos(t) + b \sin(t)$, c'est-à-dire une combinaison linéaire des ondes fondamentales.


## 5. Application en Intelligence Artificielle

L'Identité de Parseval est la clé de voûte de l'optimisation dans l'espace des fréquences en Machine Learning. Elle stipule que la distance quadratique (l'erreur MSE - Mean Squared Error) entre deux fonctions est exactement identique dans le domaine d'origine (temporel/spatial) et dans le domaine spectral (Fourier). Si on minimise l'erreur entre les coefficients de Fourier de deux signaux, on garantit mathématiquement que la différence physique temporelle est minimisée de la même quantité. L'espace $L^2$ et son espace spectral dual isomorphe sont indiscernables du point de vue de la norme.

Dans le développement de modèles génératifs audio basés sur la diffusion (comme WaveGrad ou DiffWave), l'objectif est d'apprendre à débruiter une onde sonore en générant $\hat{y}(t)$ pour approcher le son réel $y(t)$.
La fonction de coût naïve est $\mathcal{L}_{time} = \int_0^T (y(t) - \hat{y}(t))^2 dt$.
Cependant, les erreurs sur les hautes et basses fréquences ne sont pas perceptibles de la même manière par l'oreille humaine. Grâce à l'identité de Parseval, les ingénieurs remplacent $\mathcal{L}_{time}$ par sa formulation spectrale équivalente :
$$\mathcal{L}_{freq} = \sum_{n} (c_n(y) - c_n(\hat{y}))^2$$
L'avantage majeur de ce changement de point de vue est qu'ils peuvent attribuer des *poids* $\lambda_n$ à chaque bande de fréquence pour orienter l'IA à accorder plus d'importance aux fréquences de la voix humaine (0.3 à 3 kHz), définissant ainsi une Loss modifiée : $\mathcal{L}_{weighted} = \sum_{n} \lambda_n (c_n(y) - c_n(\hat{y}))^2$. Le modèle converge plus vite et produit un son infiniment plus naturel, car la géométrie euclidienne canonique a été déformée pour imiter la psycho-acoustique.

## 6. Liens Sémantiques
- **Concepts Précédents requis :** [[Jalon-78.md]], [[Jalon 76 (Propriétés géométriques de l'espace de Hilbert L2).md]]
- **Concepts Futurs dépendants :** [[Jalon 81 (Transformée de Fourier dans L2).md]], [[Jalon 116 (Variétés riemanniennes).md]]

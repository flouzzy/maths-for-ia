---
uuid: "jalon-67"
title: "Théorème de convergence monotone (Beppo Levi)"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 66 (Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives.).md]]"
next: "[[Jalon 68 (Lemme de Fatou et définition de l'intégrale pour les fonctions de signe quelconque).md]]"
---

# Jalon 67 : Théorème de convergence monotone (Beppo-Levi)

## 1. Introduction historique et conceptuelle

Au début du XXe siècle, l'intégrale de Riemann, bien qu'efficace pour les fonctions continues par morceaux, se heurte à une limite structurelle majeure lors des passages à la limite. Si une suite de fonctions intégrables $(f_n)_{n \in \mathbb{N}}$ converge simplement vers une fonction $f$, rien ne garantit que $f$ soit Riemann-intégrable, et encore moins que la limite des intégrales soit l'intégrale de la limite. L'absence de théorèmes robustes de convergence rendait l'analyse fonctionnelle et la théorie des probabilités extrêmement ardues à formaliser.

C'est dans ce contexte que la théorie de l'intégration développée par Henri Lebesgue (1902) prend toute sa puissance. En déplaçant la mesure de l'axe des abscisses vers l'axe des ordonnées (intégrer par rapport à la mesure des ensembles de niveau), Lebesgue construit une intégrale fondamentalement adaptée aux processus de passage à la limite. Le mathématicien italien Beppo Levi (1906) prouve alors le premier grand pilier de cette théorie : le théorème de convergence monotone.

Ce théorème affirme que pour une suite croissante de fonctions positives, l'opération d'intégration commute avec le passage à la limite supérieure. Géométriquement, si une suite de "profils" (fonctions) croît inexorablement vers un "plafond" (fonction limite), le volume sous ces profils convergera exactement vers le volume sous le plafond, même si ce plafond possède une structure fractale ou discontinue, tant qu'il est mesurable. Ce résultat libère les analystes et forme la base de toutes les démonstrations modernes en théorie de la mesure.

## 2. Définitions, Théorèmes et Exemples Concrets Immédiats

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. Toutes les fonctions considérées dans cette section sont mesurables de $X$ dans $\overline{\mathbb{R}}_+ = [0, +\infty]$.

> **Théorème de Convergence Monotone (Beppo-Levi)**
>
> Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables positives définies sur $X$.
> Si pour tout $x \in X$ et pour tout $n \in \mathbb{N}$, la suite est croissante :
> $$\forall n \in \mathbb{N}, \quad 0 \leq f_n(x) \leq f_{n+1}(x)$$
> Alors, la fonction limite simple $f(x) = \lim_{n \to +\infty} f_n(x) = \sup_{n \in \mathbb{N}} f_n(x)$ est mesurable, et on a l'égalité :
> $$\int_X f \, d\mu = \lim_{n \to +\infty} \int_X f_n \, d\mu$$

**Remarque de typage :** Les variables $f_n$ sont des éléments de $\mathcal{M}^+(X, \mathcal{A})$, l'espace des fonctions mesurables positives. L'intégrale $\int_X f \, d\mu$ est une valeur dans $\overline{\mathbb{R}}_+$, le théorème est donc valable même si la limite est $+\infty$.

**Exemple concret immédiat :**
Soit $X = ]0, 1[$ muni de la mesure de Lebesgue $\lambda$. Considérons la suite de fonctions $f_n(x) = \frac{1}{x^{1/2}} \mathbf{1}_{]1/n, 1[}(x)$.
- Chaque $f_n$ est mesurable et positive.
- La suite est croissante : l'intervalle $]1/n, 1[$ grandit avec $n$, donc $\mathbf{1}_{]1/n, 1[}(x) \leq \mathbf{1}_{]1/(n+1), 1[}(x)$.
- La limite simple est $f(x) = \frac{1}{x^{1/2}}$ sur $]0, 1[$.
Calculons les intégrales des $f_n$ :
$$I_n = \int_0^1 f_n(x) dx = \int_{1/n}^1 x^{-1/2} dx = \left[ 2x^{1/2} \right]_{1/n}^1 = 2 - 2\frac{1}{\sqrt{n}}$$
En appliquant le théorème de Beppo-Levi :
$$\lim_{n \to +\infty} I_n = \lim_{n \to +\infty} \left( 2 - \frac{2}{\sqrt{n}} \right) = 2$$
Ce qui correspond exactement à l'intégrale généralisée de Lebesgue : $\int_0^1 \frac{1}{\sqrt{x}} dx = 2$.

**Cas limite et défaut des hypothèses :**
Si la suite n'est pas positive, le théorème s'effondre. Prenons $X = \mathbb{R}$ et $f_n(x) = -\frac{1}{n} \mathbf{1}_{[0, n]}(x)$.
La suite $(f_n)$ est bien croissante (elle tend vers 0 par valeurs négatives). La limite $f(x) = 0$.
Cependant :
$\int_\mathbb{R} f_n(x) dx = -\frac{1}{n} \times n = -1$.
La limite des intégrales est $-1$, alors que l'intégrale de la limite $f$ est $\int_\mathbb{R} 0 \, dx = 0$.
La condition de positivité est un rempart contre la "fuite de masse" infinie négative.

> **Corollaire (Théorème d'intégration terme à terme pour les séries positives)**
>
> Soit $(u_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables positives sur $X$. Alors :
> $$\int_X \left( \sum_{n=0}^{+\infty} u_n \right) d\mu = \sum_{n=0}^{+\infty} \int_X u_n \, d\mu$$

**Exemple concret immédiat (Série géométrique fonctionnelle) :**
Sur $X = [0, 1[$ avec la mesure de Lebesgue, posons $u_n(x) = x^n$.
La somme partielle est $S_N(x) = \sum_{n=0}^N x^n$, qui croît vers $f(x) = \frac{1}{1-x}$.
D'après le corollaire :
$$\int_0^1 \frac{1}{1-x} dx = \sum_{n=0}^{+\infty} \int_0^1 x^n dx = \sum_{n=0}^{+\infty} \frac{1}{n+1} = +\infty$$
Ce qui confirme rigoureusement la divergence de l'intégrale en $x=1$ par le biais de la divergence de la série harmonique, sans nécessiter d'étude asymptotique locale.

## 3. Démonstrations

### Démonstration du Théorème de Convergence Monotone

La démonstration s'établit en deux phases, par double inégalité.

**Étape 1 : Majoration immédiate (L'inégalité facile)**
Puisque la suite $(f_n)$ est croissante, on a pour tout $n \in \mathbb{N}$ et pour tout $x \in X$, $f_n(x) \leq f(x)$.
L'intégrale de Lebesgue respecte la monotonie (croissance de l'intégrale), donc :
$$\int_X f_n \, d\mu \leq \int_X f \, d\mu$$
La suite de réels positifs $\left( \int_X f_n \, d\mu \right)_{n \in \mathbb{N}}$ est croissante et majorée par $\int_X f \, d\mu$, elle admet donc une limite dans $\overline{\mathbb{R}}_+$. En passant à la limite, on obtient la première borne :
$$\lim_{n \to +\infty} \int_X f_n \, d\mu \leq \int_X f \, d\mu$$

**Étape 2 : Minoration par les fonctions simples (Le cœur de la preuve de Lebesgue)**
Il s'agit de prouver l'inégalité inverse. Par définition de l'intégrale de Lebesgue pour une fonction positive $f$, on a :
$$\int_X f \, d\mu = \sup \left\{ \int_X \varphi \, d\mu \ \mid \ \varphi \text{ est étagée, } 0 \leq \varphi \leq f \right\}$$
Soit donc $\varphi$ une fonction étagée positive minorant $f$ : $0 \leq \varphi \leq f$.
Soit $\alpha \in ]0, 1[$. Nous définissons les ensembles mesurables suivants pour tout $n \in \mathbb{N}$ :
$$E_n = \{ x \in X \mid f_n(x) \geq \alpha \varphi(x) \}$$
1. *Propriétés des $E_n$ :* Puisque $(f_n)$ est croissante, la condition $f_n(x) \geq \alpha \varphi(x)$ implique $f_{n+1}(x) \geq \alpha \varphi(x)$. Donc la suite d'ensembles $(E_n)$ est une suite croissante : $E_n \subset E_{n+1}$.
2. *Limite des $E_n$ :* Soit $x \in X$. Si $f(x) = 0$, alors $\varphi(x) = 0$, donc $x \in E_1$. Si $f(x) > 0$, comme $\alpha < 1$, on a $\alpha \varphi(x) < f(x)$. Comme $f_n(x) \to f(x)$, il existe un rang $N$ à partir duquel $f_N(x) > \alpha \varphi(x)$, donc $x \in E_N$. Dans tous les cas, $\bigcup_{n \in \mathbb{N}} E_n = X$.
3. *Minoration sur $E_n$ :* Sur $X$, on peut minorer brutalement $f_n$ par sa restriction à $E_n$ :
$$\int_X f_n \, d\mu \geq \int_{E_n} f_n \, d\mu \geq \int_{E_n} \alpha \varphi \, d\mu = \alpha \int_{E_n} \varphi \, d\mu$$
4. *Continuité monotone de la mesure :* La fonction $\varphi$ s'écrit $\sum_{i=1}^k c_i \mathbf{1}_{A_i}$. L'intégrale sur $E_n$ vaut $\sum_{i=1}^k c_i \mu(A_i \cap E_n)$. Puisque $E_n \uparrow X$, $A_i \cap E_n \uparrow A_i$. Par le théorème de continuité séquentielle croissante d'une mesure, $\mu(A_i \cap E_n) \to \mu(A_i)$. Ainsi :
$$\lim_{n \to +\infty} \int_{E_n} \varphi \, d\mu = \int_X \varphi \, d\mu$$
5. *Passage à la limite finale :* En prenant la limite quand $n \to +\infty$ dans l'inégalité de l'étape 3 :
$$\lim_{n \to +\infty} \int_X f_n \, d\mu \geq \alpha \int_X \varphi \, d\mu$$
Cette inégalité est vraie pour tout $\alpha < 1$. En faisant tendre $\alpha$ vers 1, on obtient :
$$\lim_{n \to +\infty} \int_X f_n \, d\mu \geq \int_X \varphi \, d\mu$$
Ceci est vrai pour toute fonction étagée $\varphi \leq f$. En prenant le supremum sur l'ensemble de ces fonctions $\varphi$, on conclut la démonstration :
$$\lim_{n \to +\infty} \int_X f_n \, d\mu \geq \int_X f \, d\mu$$
Les deux inégalités établissent le théorème. $\blacksquare$

### Démonstration du Corollaire (Séries)

Soit $S_N(x) = \sum_{n=0}^N u_n(x)$. Comme les $u_n$ sont positives, la suite de fonctions $(S_N)_{N \in \mathbb{N}}$ est une suite de fonctions mesurables positives, et elle est croissante par rapport à $N$.
La limite simple est la série $S(x) = \sum_{n=0}^{+\infty} u_n(x)$.
Par linéarité de l'intégrale pour des sommes finies :
$$\int_X S_N \, d\mu = \sum_{n=0}^N \int_X u_n \, d\mu$$
On applique le Théorème de Beppo-Levi à la suite $(S_N)$ :
$$\int_X \left( \sum_{n=0}^{+\infty} u_n \right) d\mu = \int_X S \, d\mu = \lim_{N \to +\infty} \int_X S_N \, d\mu = \lim_{N \to +\infty} \sum_{n=0}^N \int_X u_n \, d\mu = \sum_{n=0}^{+\infty} \int_X u_n \, d\mu$$
Le résultat est formellement démontré. $\blacksquare$

## 4. Applications en Physique, Logique et Intelligence Artificielle

### Probabilités et Mesure de l'Information
En théorie de l'information, l'entropie différentielle d'une variable aléatoire continue $X$ de densité $p$ est $H(X) = - \int p(x) \log(p(x)) dx$. Lors de processus de diffusion ou de lissage, la distribution $p_n$ converge vers une distribution cible. Beppo-Levi est l'outil central pour s'assurer que l'information (mesurée par ces intégrales) ne disparaît pas dans les limites, garantissant la validité asymptotique du théorème H de Boltzmann en mécanique statistique, modélisant l'accroissement monotone de l'entropie.

### Intelligence Artificielle : Processus stochastiques et Divergence KL
Dans les modèles génératifs modernes (comme les Diffusion Models ou les VAE), on modélise un processus en une infinité d'étapes d'ajout de bruit. Les preuves de convergence de l'ELBO (Evidence Lower Bound) qui approximent la log-vraisemblance d'une image générée exigent de manipuler des séries infinies d'intégrales d'espérance. Le corollaire de Beppo-Levi justifie formellement le fait que minimiser le risque empirique cumulé à chaque étape discrète de temps garantit la minimisation de la borne de l'intégrale totale en temps continu.

### Espaces de Hilbert en Mécanique Quantique (Fonctions de carré intégrable)
Le théorème permet de construire rigoureusement l'espace de Hilbert $L^2$. Lorsqu'un système quantique est décomposé sur une base orthonormée infinie (les états propres d'un hamiltonien), la norme de la fonction d'onde s'exprime comme l'intégrale du module carré : $\int |\psi(x)|^2 dx = \int \sum |c_n \phi_n(x)|^2 dx$. Intervertir la somme et l'intégrale via le corollaire est le fondement axiomatique pour prouver que les probabilités de transition somment exactement à 1 (conservation de l'unitarité quantique).

\begin{center}
\begin{tikzpicture}[scale=1.5]
    % Axes
    \draw[->,thick] (-0.5,0) -- (4,0) node[right] {$x$};
    \draw[->,thick] (0,-0.5) -- (0,3) node[above] {$f_n(x)$};

    % Fonctions f_n
    \draw[domain=0.2:3.5, smooth, variable=\x, blue!30, thick] plot ({\x}, {2 - 1.5*exp(-0.5*\x)});
    \node[blue!40] at (3.7, 1.2) {$f_1$};

    \draw[domain=0.2:3.5, smooth, variable=\x, blue!50, thick] plot ({\x}, {2 - 1.0*exp(-1*\x)});
    \node[blue!60] at (3.7, 1.6) {$f_2$};

    \draw[domain=0.2:3.5, smooth, variable=\x, blue!70, thick] plot ({\x}, {2 - 0.5*exp(-2*\x)});
    \node[blue!80] at (3.7, 1.85) {$f_3$};

    % Fonction limite f
    \draw[domain=0.2:3.5, smooth, variable=\x, red, ultra thick] plot ({\x}, {2});
    \node[red] at (3.7, 2.2) {$f = \lim f_n$};

    % Area under f_3
    \fill[blue!20, opacity=0.5] (0.2,0) -- plot[domain=0.2:3.5, smooth] ({\x}, {2 - 0.5*exp(-2*\x)}) -- (3.5,0) -- cycle;

    \node[below] at (2,-0.5) {La surface sous les courbes approche la surface du rectangle limite};
\end{tikzpicture}
\end{center}

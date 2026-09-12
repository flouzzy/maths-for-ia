# Jalon 67 : Théorème de convergence monotone (Beppo-Levi)

## 1. Introduction

La théorie de l'intégration de Riemann souffre d'une faiblesse rédhibitoire : ses théorèmes de passage à la limite sous l'intégrale sont extrêmement restrictifs, requérant généralement la convergence uniforme de la suite de fonctions. Dans de nombreuses situations physiques (par exemple, la résolution de l'équation de la chaleur où des phénomènes locaux se propagent, ou l'étude des séries de Fourier), la convergence uniforme n'est pas garantie, voire fondamentalement absente. Il fallait un nouvel outil d'intégration, plus flexible face aux processus limites.

C'est dans ce contexte que la théorie de l'intégration de Lebesgue révèle toute sa puissance. Le mathématicien italien Beppo Levi (1875-1961) a formulé en 1906 un théorème d'une élégance et d'une force remarquables. Ce résultat, le Théorème de convergence monotone, stipule que pour une suite croissante de fonctions positives, l'intégrale de la limite est toujours égale à la limite des intégrales, sans aucune condition supplémentaire sur le type de convergence (autre que la convergence simple). Géométriquement, si vous accumulez des strates de matière (fonctions croissantes), le volume total limite est exactement la limite des volumes approchés. C'est la pierre angulaire qui permet l'interversion série/intégrale pour les séries à termes positifs et, plus tard, la démonstration du théorème de convergence dominée.

## 2. Définitions et Théorème Fondamental

### A. Le cadre formel

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré. Rappelons que l'intégrale de Lebesgue pour les fonctions mesurables positives est construite à partir des fonctions étagées.

**Théorème (Convergence Monotone de Beppo-Levi) :**
Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables de $X$ dans $\overline{\mathbb{R}}_+$ (c'est-à-dire à valeurs dans $[0, +\infty]$).
On suppose que la suite $(f_n)$ est croissante presque partout par rapport à $\mu$ :
$$ \forall n \in \mathbb{N}, \quad f_n \le f_{n+1} \quad \mu\text{-p.p.} $$
Soit $f : X \to \overline{\mathbb{R}}_+$ définie presque partout par la limite ponctuelle :
$$ f(x) = \lim_{n \to +\infty} f_n(x) = \sup_{n \in \mathbb{N}} f_n(x) $$
Alors $f$ est une fonction mesurable, et on a l'égalité des intégrales :
$$ \int_X f \, d\mu = \lim_{n \to +\infty} \int_X f_n \, d\mu $$

**Exemple concret immédiat :**
Plaçons-nous sur $X = [0, 1)$ avec la mesure de Lebesgue $\lambda$.
Considérons la suite de fonctions $f_n(x) = \sum_{k=1}^n x^k$.
Pour tout $x \in [0, 1)$, chaque terme $x^k$ est positif, donc $f_n(x) \le f_{n+1}(x)$. La suite est croissante.
La limite ponctuelle est $f(x) = \sum_{k=1}^\infty x^k = \frac{x}{1 - x}$.
L'intégrale de $f_n$ est $\int_{[0, 1)} f_n d\lambda = \sum_{k=1}^n \frac{1}{k+1}$.
D'après le théorème de Beppo-Levi, on peut affirmer sans calcul supplémentaire complexe que :
$\int_{[0, 1)} \frac{x}{1-x} d\lambda = \lim_{n \to \infty} \sum_{k=1}^n \frac{1}{k+1} = +\infty$.

### B. Conséquence cruciale : Intégration terme à terme des séries

**Corollaire :**
Soit $(u_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables de $X$ dans $\overline{\mathbb{R}}_+$.
Alors, la série $\sum_{n=0}^\infty u_n$ est mesurable et :
$$ \int_X \left( \sum_{n=0}^\infty u_n \right) d\mu = \sum_{n=0}^\infty \left( \int_X u_n \, d\mu \right) $$

Ceci se déduit immédiatement de Beppo-Levi en posant $f_n = \sum_{k=0}^n u_k$, qui est bien une suite croissante de fonctions mesurables positives.

**Cas limite :** L'hypothèse de positivité (ou au moins de croissance) est indispensable. Considérons $f_n(x) = \frac{1}{n} \mathbf{1}_{[0, n]}(x)$. La suite $(f_n)$ converge ponctuellement vers $f(x) = 0$. On a $\int f_n = \frac{1}{n} \times n = 1$, mais $\int f = 0$. La limite des intégrales (1) n'est pas l'intégrale de la limite (0). Ici, $f_n$ n'est pas croissante, ce qui montre que le théorème ne s'applique pas (c'est le rôle du Lemme de Fatou de traiter ce genre de cas par une inégalité).

## 3. Démonstrations

**Démonstration du Théorème de Convergence Monotone :**

*Étape 1 : Mesurabilité et Inégalité Triviale*
Comme $f_n$ est une suite de fonctions mesurables, $f = \sup_n f_n$ est mesurable (propriété fondamentale des limites de fonctions mesurables).
Par hypothèse, pour tout $n$, on a $f_n \le f$.
Par croissance de l'intégrale, on obtient :
$$ \int_X f_n \, d\mu \le \int_X f \, d\mu $$
Puisque la suite numérique $\left( \int_X f_n \, d\mu \right)_{n \in \mathbb{N}}$ est croissante (car $f_n \le f_{n+1}$), elle admet une limite (éventuellement $+\infty$). Le passage à la limite dans l'inégalité précédente donne :
$$ \lim_{n \to +\infty} \int_X f_n \, d\mu \le \int_X f \, d\mu $$

*Étape 2 : L'Inégalité Fondamentale*
Pour montrer l'inégalité inverse, nous devons revenir à la définition de l'intégrale de $f$ via les fonctions étagées.
Soit $\phi$ une fonction étagée mesurable positive telle que $0 \le \phi \le f$.
Fixons une constante $c \in ]0, 1[$.
Définissons les ensembles mesurables :
$$ E_n = \{ x \in X \mid f_n(x) \ge c \phi(x) \} $$
Puisque la suite $(f_n)$ est croissante, la suite d'ensembles $(E_n)$ est une suite croissante pour l'inclusion ($E_n \subset E_{n+1}$).
Montrons que $\bigcup_{n \in \mathbb{N}} E_n = X$.
Pour tout $x \in X$, si $f(x) = 0$, alors $\phi(x) = 0$, et $f_n(x) \ge 0 = c \phi(x)$, donc $x \in E_0$.
Si $f(x) > 0$, on a $c \phi(x) < \phi(x) \le f(x)$. Comme $f_n(x) \to f(x)$, il existe un rang $N$ tel que pour tout $n \ge N$, $f_n(x) > c \phi(x)$, ce qui implique $x \in E_N$.
Ainsi, l'union est bien $X$.

*Étape 3 : Utilisation de la continuité de la mesure*
Pour tout $n$, on peut minorer l'intégrale de $f_n$ :
$$ \int_X f_n \, d\mu \ge \int_{E_n} f_n \, d\mu \ge \int_{E_n} c \phi \, d\mu = c \int_{E_n} \phi \, d\mu $$
Comme $\phi$ est une fonction étagée, on l'écrit $\phi = \sum_{i=1}^k a_i \mathbf{1}_{A_i}$.
L'intégrale sur $E_n$ est :
$$ \int_{E_n} \phi \, d\mu = \sum_{i=1}^k a_i \mu(A_i \cap E_n) $$
Puisque $(E_n)$ croît vers $X$, $(A_i \cap E_n)$ croît vers $A_i \cap X = A_i$. Par continuité croissante de la mesure $\mu$, $\lim_{n \to \infty} \mu(A_i \cap E_n) = \mu(A_i)$.
En passant à la limite quand $n \to +\infty$ dans notre minoration :
$$ \lim_{n \to +\infty} \int_X f_n \, d\mu \ge c \sum_{i=1}^k a_i \mu(A_i) = c \int_X \phi \, d\mu $$

*Étape 4 : Conclusion*
Cette inégalité est vraie pour tout $c \in ]0, 1[$. En faisant tendre $c$ vers $1$, on obtient :
$$ \lim_{n \to +\infty} \int_X f_n \, d\mu \ge \int_X \phi \, d\mu $$
Cette borne inférieure est valable pour *toute* fonction étagée $\phi \le f$. Par définition de l'intégrale de $f$ (qui est le supremum sur toutes ces fonctions étagées), il s'ensuit que :
$$ \lim_{n \to +\infty} \int_X f_n \, d\mu \ge \int_X f \, d\mu $$
Les deux inégalités établissent l'égalité cherchée.

## 4. Applications en Mathématiques et Intelligence Artificielle

En Intelligence Artificielle et en Machine Learning, le théorème de Beppo-Levi (ainsi que la convergence dominée qui s'appuie dessus) est utilisé de manière récurrente dans les formalismes probabilistes pour justifier les interversions entre les signes sommes (Espérance, intégration des pertes) et les limites d'apprentissage.

- **Processus de décision markoviens (MDP) et Reinforcement Learning :** Lors de l'évaluation de la fonction de valeur d'état $V^\pi(s) = \mathbb{E}_\pi[\sum_{t=0}^\infty \gamma^t R_{t+1} | S_0 = s]$, le fait de pouvoir intégrer cette somme infinie de récompenses (lorsqu'elles sont positives, ou bornées par translation) terme à terme requiert le théorème de convergence monotone, garantissant que l'espérance de la somme est la somme des espérances.
- **Formulation de la divergence KL et modèles génératifs :** Lors du calcul d'entropies différentielles ou de divergences de Kullback-Leibler qui impliquent des intégrales sur des densités de probabilités (limites de suites de fonctions approchées, comme dans les Normalizing Flows), les théorèmes de passage à la limite de Lebesgue garantissent la robustesse théorique de la minimisation de ces fonctions d'objectif.
- **Réseaux de neurones infinis et théorèmes de limite universelle :** L'analyse des architectures à la limite de la sur-paramétrisation (réseaux de largeur infinie convergeant vers des Processus Gaussiens) nécessite de passer à la limite sous les intégrales d'espérance de la fonction de perte empirique, une justification rendue possible par les outils de l'analyse fonctionnelle basés sur la théorie de la mesure et Beppo-Levi.

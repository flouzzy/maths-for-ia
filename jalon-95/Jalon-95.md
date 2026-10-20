---
uuid: "jalon-95"
title: "Vecteurs gaussiens"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/fondations
prev: "[[Jalon 94 (Démonstration du théorème central limite).md]]"
next: "[[Jalon 96 (Livrable IA).md]]"
---

Mes chers étudiants,

Asseyez-vous, s'il vous plaît. Aujourd'hui, nous allons nous aventurer dans un domaine de la théorie des probabilités qui, bien qu'abstrait en apparence, est d'une puissance et d'une ubiquité étonnantes. Nous allons parler des *vecteurs gaussiens*, ou, comme on les appelle parfois, de la *loi normale multidimensionnelle*. C'est un sujet que mes maîtres, Arnold, Kolmogorov, Gelfand, auraient abordé avec une intuition physique profonde, une rigueur implacable et un déluge d'exemples concrets. C'est dans cet esprit que je vous propose cette leçon.

### I. Genèse d'une Idée Puissante : Le Bruit, La Forme et l'Incertitude

D'où vient cette idée de distribution "normale" ? L'histoire est fascinante, elle est tissée de la quête humaine de la compréhension du monde, de la mesure des étoiles aux erreurs de tir d'artillerie.

Imaginez un instant que vous effectuez une série de mesures. Que ce soit la position d'une planète, le poids d'un échantillon chimique, ou la tension aux bornes d'un circuit. Chaque mesure est entachée d'une petite erreur. Ces erreurs sont souvent le résultat d'une multitude de petites perturbations aléatoires, indépendantes les unes des autres. Le *Théorème Central Limite* nous enseigne que la somme de ces nombreuses petites perturbations, quelle que soit leur distribution individuelle, tend vers une distribution très particulière : la loi normale, ou gaussienne.

C'est là le génie de Carl Friedrich Gauss et de Pierre-Simon Laplace. Au début du XIXe siècle, ils ont formalisé cette distribution en 1D. Mais le monde n'est pas unidimensionnel ! Nos mesures sont souvent multiples, corrélées. La position d'une balle de fusil n'est pas juste une coordonnée $x$, mais $(x, y, z)$. La taille et le poids d'une personne sont deux variables liées. Comment modéliser ces phénomènes conjoints lorsque chaque composante est, individuellement, gaussienne, et qu'elles sont de surcroît liées entre elles ? C'est là que le concept de *vecteur gaussien* prend tout son sens.

Pensez à une cible de tir. Les impacts ne sont jamais parfaitement au centre. Ils forment un nuage de points. Ce nuage est plus dense au centre et s'éclaircit à mesure que l'on s'éloigne. Si les tirs sont aléatoires mais concentrés, les contours d'égale densité de ce nuage ne sont pas des carrés, ni des étoiles, mais des *ellipses* (ou des sphères en 3D, des hyper-ellipsoïdes en nD). Ces ellipses décrivent la "forme" de l'incertitude.

*   En 1D, c'est la fameuse "courbe en cloche".
*   En 2D, imaginez une montagne dont le sommet est au point moyen, et dont les pentes s'étendent de manière elliptique. La projection de cette montagne sur le plan forme des "isocontours" elliptiques.
*   En dimensions supérieures, c'est la même idée : une "hyper-montagne" dont les isocontours sont des hyper-ellipsoïdes.

Cette forme elliptique, cette "orientation" et cet "étirement" du nuage de points, c'est précisément ce que la *matrice de covariance* va capturer. C'est le cœur de la géométrie des vecteurs gaussiens. C'est une distribution qui, pour une moyenne et une variance données, maximise l'entropie, c'est-à-dire qu'elle est "la plus aléatoire possible" sous ces contraintes. C'est pourquoi elle apparaît si souvent dans la nature et en ingénierie : c'est la forme naturelle du bruit, de l'erreur, de l'incertitude agrégée.

### II. Les Fondations : Vecteurs Aléatoires et Structure Gaussiene

Commençons par les définitions fondamentales, en construisant pas à pas notre compréhension.

#### 1. Vecteurs Aléatoires : Le Point de Départ

Un vecteur aléatoire est simplement un ensemble de variables aléatoires regroupées en un vecteur.

**Définition 1.1 : Vecteur Aléatoire**
Un vecteur aléatoire $X$ de dimension $d$ est une fonction mesurable $X: \Omega \to \mathbb{R}^d$ définie sur un espace de probabilité $(\Omega, \mathcal{F}, P)$, tel que $X = (X_1, X_2, \dots, X_d)^T$, où chaque $X_i$ est une variable aléatoire réelle.

```latex
\begin{definition}[Vecteur Aléatoire]
Un vecteur aléatoire $X$ de dimension $d$ est une fonction mesurable $X: \Omega \to \mathbb{R}^d$ définie sur un espace de probabilité $(\Omega, \mathcal{F}, P)$, tel que $X = (X_1, X_2, \dots, X_d)^T$, où chaque $X_i$ est une variable aléatoire réelle.
\end{definition}
```

**Exemple 1.1 : Mesures Biologiques**
Considérons un échantillon de personnes. Pour chaque personne, nous mesurons sa taille (en cm) et son poids (en kg).
Soit $X_1$ la variable aléatoire représentant la taille et $X_2$ la variable aléatoire représentant le poids.
Le vecteur aléatoire $X = \begin{pmatrix} X_1 \\ X_2 \end{pmatrix}$ est un vecteur aléatoire de dimension $d=2$.
Si nous tirons une personne au hasard et mesurons sa taille $175$ cm et son poids $70$ kg, alors une réalisation de $X$ est $\begin{pmatrix} 175 \\ 70 \end{pmatrix}$.

#### 2. Vecteurs Gaussiens : La Définition Essentielle

La définition la plus robuste et la plus générale d'un vecteur gaussien ne passe pas par sa densité de probabilité (qui n'existe pas toujours, notamment si la matrice de covariance est singulière), mais par la propriété de ses combinaisons linéaires.

**Définition 2.1 : Vecteur Gaussien**
Un vecteur aléatoire $X = (X_1, \dots, X_d)^T$ est appelé un vecteur gaussien si, pour tout vecteur constant $a = (a_1, \dots, a_d)^T \in \mathbb{R}^d$, la variable aléatoire unidimensionnelle $Y = a^T X = \sum_{i=1}^d a_i X_i$ est une variable aléatoire gaussienne (ou une constante dégénérée, c'est-à-dire une gaussienne de variance nulle).

```latex
\begin{definition}[Vecteur Gaussien]
Un vecteur aléatoire $X = (X_1, \dots, X_d)^T$ est appelé un vecteur gaussien si, pour tout vecteur constant $a = (a_1, \dots, a_d)^T \in \mathbb{R}^d$, la variable aléatoire unidimensionnelle $Y = a^T X = \sum_{i=1}^d a_i X_i$ est une variable aléatoire gaussienne (ou une constante dégénérée).
\end{definition}
```

**Exemple 2.1 : Variables Gaussiens Indépendantes**
Soient $Z_1 \sim \mathcal{N}(0, 1)$ et $Z_2 \sim \mathcal{N}(0, 1)$ deux variables aléatoires indépendantes.
Considérons le vecteur aléatoire $X = \begin{pmatrix} Z_1 \\ Z_2 \end{pmatrix}$.
Prenons un vecteur $a = \begin{pmatrix} a_1 \\ a_2 \end{pmatrix} \in \mathbb{R}^2$.
La combinaison linéaire $Y = a^T X = a_1 Z_1 + a_2 Z_2$.
Puisque $Z_1$ et $Z_2$ sont des gaussiennes indépendantes, leur somme pondérée $Y$ est également une variable gaussienne.
Son espérance est $\mathbb{E}[Y] = a_1 \mathbb{E}[Z_1] + a_2 \mathbb{E}[Z_2] = a_1 \cdot 0 + a_2 \cdot 0 = 0$.
Sa variance est $\text{Var}(Y) = a_1^2 \text{Var}(Z_1) + a_2^2 \text{Var}(Z_2) = a_1^2 \cdot 1 + a_2^2 \cdot 1 = a_1^2 + a_2^2$.
Donc $Y \sim \mathcal{N}(0, a_1^2 + a_2^2)$. Par conséquent, $X$ est un vecteur gaussien.

#### 3. La Fonction Caractéristique d'un Vecteur Gaussien

La fonction caractéristique est un outil puissant en théorie des probabilités. Elle existe toujours, même si la densité n'existe pas, et elle caractérise de manière unique la distribution de probabilité.

**Définition 3.1 : Fonction Caractéristique d'un Vecteur Aléatoire**
La fonction caractéristique d'un vecteur aléatoire $X \in \mathbb{R}^d$ est la fonction $\phi_X: \mathbb{R}^d \to \mathbb{C}$ définie par :
$$ \phi_X(t) = \mathbb{E}[e^{i t^T X}] $$
pour tout $t \in \mathbb{R}^d$.

```latex
\begin{definition}[Fonction Caractéristique d'un Vecteur Aléatoire]
La fonction caractéristique d'un vecteur aléatoire $X \in \mathbb{R}^d$ est la fonction $\phi_X: \mathbb{R}^d \to \mathbb{C}$ définie par :
$$ \phi_X(t) = \mathbb{E}[e^{i t^T X}] $$
pour tout $t \in \mathbb{R}^d$.
\end{definition}
```

**Théorème 3.1 : Fonction Caractéristique d'un Vecteur Gaussien**
Si $X$ est un vecteur gaussien de vecteur espérance $\mu \in \mathbb{R}^d$ et de matrice de covariance $\Sigma \in \mathbb{R}^{d \times d}$, alors sa fonction caractéristique est donnée par :
$$ \phi_X(t) = e^{i t^T \mu - \frac{1}{2} t^T \Sigma t} $$
pour tout $t \in \mathbb{R}^d$.

```latex
\begin{theorem}[Fonction Caractéristique d'un Vecteur Gaussien]
Si $X$ est un vecteur gaussien de vecteur espérance $\mu \in \mathbb{R}^d$ et de matrice de covariance $\Sigma \in \mathbb{R}^{d \times d}$, alors sa fonction caractéristique est donnée par :
$$ \phi_X(t) = e^{i t^T \mu - \frac{1}{2} t^T \Sigma t} $$
pour tout $t \in \mathbb{R}^d$.
\end{theorem}
```

**Exemple 3.1 : Fonction Caractéristique 2D**
Soit $X = \begin{pmatrix} X_1 \\ X_2 \end{pmatrix}$ un vecteur gaussien avec $\mu = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$ et $\Sigma = \begin{pmatrix} 1 & 0.5 \\ 0.5 & 2 \end{pmatrix}$.
Pour un vecteur $t = \begin{pmatrix} t_1 \\ t_2 \end{pmatrix}$, nous avons :
$t^T \mu = t_1 \cdot 1 + t_2 \cdot 2 = t_1 + 2t_2$.
$t^T \Sigma t = \begin{pmatrix} t_1 & t_2 \end{pmatrix} \begin{pmatrix} 1 & 0.5 \\ 0.5 & 2 \end{pmatrix} \begin{pmatrix} t_1 \\ t_2 \end{pmatrix} = \begin{pmatrix} t_1 + 0.5t_2 & 0.5t_1 + 2t_2 \end{pmatrix} \begin{pmatrix} t_1 \\ t_2 \end{pmatrix}$
$= t_1(t_1 + 0.5t_2) + t_2(0.5t_1 + 2t_2) = t_1^2 + 0.5t_1t_2 + 0.5t_1t_2 + 2t_2^2 = t_1^2 + t_1t_2 + 2t_2^2$.
Donc, la fonction caractéristique est :
$$ \phi_X(t_1, t_2) = e^{i(t_1 + 2t_2) - \frac{1}{2}(t_1^2 + t_1t_2 + 2t_2^2)} $$

#### 4. Moments du Premier et Deuxième Ordre : Centre et Forme

Ces moments sont essentiels pour caractériser un vecteur gaussien. Ils sont suffisants pour définir entièrement la distribution.

**Définition 4.1 : Vecteur Espérance (Moyenne)**
Le vecteur espérance (ou vecteur moyenne) d'un vecteur aléatoire $X = (X_1, \dots, X_d)^T$ est défini par :
$$ \mu = \mathbb{E}[X] = \begin{pmatrix} \mathbb{E}[X_1] \\ \mathbb{E}[X_2] \\ \vdots \\ \mathbb{E}[X_d] \end{pmatrix} $$

```latex
\begin{definition}[Vecteur Espérance]
Le vecteur espérance d'un vecteur aléatoire $X = (X_1, \dots, X_d)^T$ est défini par :
$$ \mu = \mathbb{E}[X] = \begin{pmatrix} \mathbb{E}[X_1] \\ \mathbb{E}[X_2] \\ \vdots \\ \mathbb{E}[X_d] \end{pmatrix} $$
\end{definition}
```

**Exemple 4.1 : Calcul de la Moyenne**
Soit $X = \begin{pmatrix} X_1 \\ X_2 \end{pmatrix}$ où $X_1 \sim \mathcal{N}(5, 1)$ et $X_2 \sim \mathcal{N}(-2, 4)$.
Le vecteur espérance est $\mu = \begin{pmatrix} \mathbb{E}[X_1] \\ \mathbb{E}[X_2] \end{pmatrix} = \begin{pmatrix} 5 \\ -2 \end{pmatrix}$.

**Définition 4.2 : Matrice de Covariance**
La matrice de covariance d'un vecteur aléatoire $X = (X_1, \dots, X_d)^T$ est la matrice $d \times d$ définie par :
$$ \Sigma = \text{Cov}(X) = \mathbb{E}[(X - \mu)(X - \mu)^T] $$
Ses éléments sont $\Sigma_{ij} = \text{Cov}(X_i, X_j) = \mathbb{E}[(X_i - \mu_i)(X_j - \mu_j)]$.
Les éléments diagonaux $\Sigma_{ii} = \text{Var}(X_i)$ sont les variances de chaque composante.
Les éléments hors-diagonaux $\Sigma_{ij}$ (pour $i \neq j$) sont les covariances entre les composantes.

```latex
\begin{definition}[Matrice de Covariance]
La matrice de covariance d'un vecteur aléatoire $X = (X_1, \dots, X_d)^T$ est la matrice $d \times d$ définie par :
$$ \Sigma = \text{Cov}(X) = \mathbb{E}[(X - \mu)(X - \mu)^T] $$
Ses éléments sont $\Sigma_{ij} = \text{Cov}(X_i, X_j) = \mathbb{E}[(X_i - \mu_i)(X_j - \mu_j)]$.
\end{definition}
```

**Exemple 4.2 : Calcul de la Matrice de Covariance**
Reprenons $X = \begin{pmatrix} X_1 \\ X_2 \end{pmatrix}$ avec $\mu = \begin{pmatrix} 5 \\ -2 \end{pmatrix}$.
Supposons que $\text{Var}(X_1) = 1$, $\text{Var}(X_2) = 4$, et $\text{Cov}(X_1, X_2) = 0.8$.
Alors, la matrice de covariance est :
$$ \Sigma = \begin{pmatrix} \text{Cov}(X_1, X_1) & \text{Cov}(X_1, X_2) \\ \text{Cov}(X_2, X_1) & \text{Cov}(X_2, X_2) \end{pmatrix} = \begin{pmatrix} \text{Var}(X_1) & \text{Cov}(X_1, X_2) \\ \text{Cov}(X_1, X_2) & \text{Var}(X_2) \end{pmatrix} = \begin{pmatrix} 1 & 0.8 \\ 0.8 & 4 \end{pmatrix} $$
Notez que $\text{Cov}(X_2, X_1) = \text{Cov}(X_1, X_2)$, ce qui rend la matrice symétrique.

**Propriétés de la Matrice de Covariance : Symétrie et Positive Semi-Définie**

**Théorème 4.1 : Propriétés de $\Sigma$**
La matrice de covariance $\Sigma$ d'un vecteur aléatoire est toujours :
1.  **Symétrique** : $\Sigma = \Sigma^T$.
2.  **Positive semi-définie** : Pour tout vecteur non-nul $a \in \mathbb{R}^d$, on a $a^T \Sigma a \ge 0$.
    Si de plus $X$ n'est pas dégénéré (c'est-à-dire qu'aucune composante n'est une combinaison linéaire des autres), alors $\Sigma$ est positive définie, c'est-à-dire $a^T \Sigma a > 0$ pour tout $a \neq 0$.

```latex
\begin{theorem}[Propriétés de la Matrice de Covariance]
La matrice de covariance $\Sigma$ d'un vecteur aléatoire est toujours :
\begin{enumerate}
    \item \textbf{Symétrique} : $\Sigma = \Sigma^T$.
    \item \textbf{Positive semi-définie} : Pour tout vecteur non-nul $a \in \mathbb{R}^d$, on a $a^T \Sigma a \ge 0$.
    Si de plus $X$ n'est pas dégénéré, alors $\Sigma$ est positive définie, c'est-à-dire $a^T \Sigma a > 0$ pour tout $a \neq 0$.
\end{enumerate}
\end{theorem}
```

**Exemple 4.3 : Vérification des Propriétés**
Reprenons $\Sigma = \begin{pmatrix} 1 & 0.8 \\ 0.8 & 4 \end{pmatrix}$.
1.  **Symétrie** : $\Sigma^T = \begin{pmatrix} 1 & 0.8 \\ 0.8 & 4 \end{pmatrix} = \Sigma$. C'est vérifié.
2.  **Positive semi-définie** : Prenons un vecteur $a = \begin{pmatrix} a_1 \\ a_2 \end{pmatrix}$.
    $a^T \Sigma a = \begin{pmatrix} a_1 & a_2 \end{pmatrix} \begin{pmatrix} 1 & 0.8 \\ 0.8 & 4 \end{pmatrix} \begin{pmatrix} a_1 \\ a_2 \end{pmatrix} = \begin{pmatrix} a_1 + 0.8a_2 & 0.8a_1 + 4a_2 \end{pmatrix} \begin{pmatrix} a_1 \\ a_2 \end{pmatrix}$
    $= a_1(a_1 + 0.8a_2) + a_2(0.8a_1 + 4a_2) = a_1^2 + 0.8a_1a_2 + 0.8a_1a_2 + 4a_2^2 = a_1^2 + 1.6a_1a_2 + 4a_2^2$.
    Pour vérifier si cette forme quadratique est toujours non-négative, on peut utiliser le critère de Sylvester (les mineurs principaux doivent être positifs).
    Mineur principal d'ordre 1 : $\det(1) = 1 > 0$.
    Mineur principal d'ordre 2 : $\det \begin{pmatrix} 1 & 0.8 \\ 0.8 & 4 \end{pmatrix} = 1 \cdot 4 - 0.8 \cdot 0.8 = 4 - 0.64 = 3.36 > 0$.
    Puisque tous les mineurs principaux sont positifs, la matrice est positive définie. Donc $a^T \Sigma a > 0$ pour $a \neq 0$.
    L'intuition physique est que $a^T \Sigma a = \text{Var}(a^T X)$, qui est la variance de la combinaison linéaire $a^T X$. Une variance ne peut jamais être négative. Si elle est nulle pour un $a \ne 0$, cela signifie que $a^T X$ est une constante, et donc que les composantes de $X$ sont linéairement dépendantes.

**Théorème 4.2 : Théorème Spectral pour la Matrice de Covariance**
Puisque $\Sigma$ est une matrice symétrique, le théorème spectral garantit qu'elle peut être diagonalisée par une matrice orthogonale. C'est-à-dire, il existe une matrice orthogonale $U$ (dont les colonnes sont les vecteurs propres normalisés de $\Sigma$, et $U^T U = I$) et une matrice diagonale $\Lambda$ (dont les éléments diagonaux sont les valeurs propres de $\Sigma$) telles que :
$$ \Sigma = U \Lambda U^T $$
Les valeurs propres $\lambda_i$ sont les variances le long des directions définies par les vecteurs propres $u_i$. Géométriquement, les vecteurs propres $u_i$ définissent les axes principaux de l'hyper-ellipsoïde d'isodensité, et les racines carrées des valeurs propres $\sqrt{\lambda_i}$ sont proportionnelles aux longueurs des demi-axes de cet ellipsoïde.

```latex
\begin{theorem}[Théorème Spectral pour la Matrice de Covariance]
Puisque $\Sigma$ est une matrice symétrique, il existe une matrice orthogonale $U$ et une matrice diagonale $\Lambda$ telles que :
$$ \Sigma = U \Lambda U^T $$
Les valeurs propres $\lambda_i$ (éléments diagonaux de $\Lambda$) sont les variances le long des directions définies par les vecteurs propres $u_i$ (colonnes de $U$).
\end{theorem}
```

**Exemple 4.4 : Diagonalisation et Interprétation Géométrique**
Considérons $\Sigma = \begin{pmatrix} 5 & 1 \\ 1 & 5 \end{pmatrix}$.
Calculons les valeurs propres : $\det(\Sigma - \lambda I) = (5-\lambda)^2 - 1 = 0 \implies (5-\lambda)^2 = 1 \implies 5-\lambda = \pm 1$.
$\lambda_1 = 4$, $\lambda_2 = 6$.
Calculons les vecteurs propres :
Pour $\lambda_1 = 4$: $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies v_1 + v_2 = 0$. Un vecteur propre est $\begin{pmatrix} 1 \\ -1 \end{pmatrix}$. Normalisé : $u_1 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}$.
Pour $\lambda_2 = 6$: $\begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies -v_1 + v_2 = 0$. Un vecteur propre est $\begin{pmatrix} 1 \\ 1 \end{pmatrix}$. Normalisé : $u_2 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}$.
Donc, $U = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}$ et $\Lambda = \begin{pmatrix} 4 & 0 \\ 0 & 6 \end{pmatrix}$.
Géométriquement, les isocontours de la densité gaussienne sont des ellipses. Les axes principaux de ces ellipses sont dirigés selon les vecteurs $u_1 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}$ et $u_2 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}$. Les "étirements" de l'ellipse le long de ces axes sont proportionnels à $\sqrt{\lambda_1} = 2$ et $\sqrt{\lambda_2} = \sqrt{6}$. L'ellipse est plus étirée le long de la direction $\begin{pmatrix} 1 \\ 1 \end{pmatrix}$ que le long de $\begin{pmatrix} 1 \\ -1 \end{pmatrix}$.

#### 5. Changements de Base et Transformations Affines de Vecteurs Gaussiens

Les vecteurs gaussiens ont une propriété remarquable : ils conservent leur "gaussienneté" sous les transformations affines.

**Théorème 5.1 : Transformation Affine d'un Vecteur Gaussien**
Soit $X$ un vecteur gaussien de dimension $d$ avec vecteur espérance $\mu$ et matrice de covariance $\Sigma$. Soit $A$ une matrice $k \times d$ et $b$ un vecteur constant $k \times 1$. Alors le vecteur aléatoire $Y = AX + b$ est un vecteur gaussien de dimension $k$, avec :
$$ \mathbb{E}[Y] = A\mu + b $$
$$ \text{Cov}(Y) = A\Sigma A^T $$

```latex
\begin{theorem}[Transformation Affine d'un Vecteur Gaussien]
Soit $X$ un vecteur gaussien de dimension $d$ avec vecteur espérance $\mu$ et matrice de covariance $\Sigma$. Soit $A$ une matrice $k \times d$ et $b$ un vecteur constant $k \times 1$. Alors le vecteur aléatoire $Y = AX + b$ est un vecteur gaussien de dimension $k$, avec :
$$ \mathbb{E}[Y] = A\mu + b $$
$$ \text{Cov}(Y) = A\Sigma A^T $$
\end{theorem}
```

**Exemple 5.1 : Transformation Linéaire 2D**
Soit $X \sim \mathcal{N}\left(\begin{pmatrix} 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}\right)$, c'est-à-dire $X_1, X_2$ sont des gaussiennes centrées réduites indépendantes.
Considérons la transformation $Y = AX + b$ avec $A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}$ et $b = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$.
Alors $Y$ est gaussien.
Son vecteur espérance est $\mathbb{E}[Y] = A\mu + b = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 0 \\ 0 \end{pmatrix} + \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} + \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$.
Sa matrice de covariance est $\text{Cov}(Y) = A\Sigma A^T = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 1 & 3 \end{pmatrix}$
$= \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 1 & 3 \end{pmatrix} = \begin{pmatrix} 2 \cdot 2 + 1 \cdot 1 & 2 \cdot 0 + 1 \cdot 3 \\ 0 \cdot 2 + 3 \cdot 1 & 0 \cdot 0 + 3 \cdot 3 \end{pmatrix} = \begin{pmatrix} 5 & 3 \\ 3 & 9 \end{pmatrix}$.
Donc, $Y \sim \mathcal{N}\left(\begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 5 & 3 \\ 3 & 9 \end{pmatrix}\right)$.

#### 6. La Fonction de Densité de Probabilité (PDF)

La fonction de densité existe pour les vecteurs gaussiens seulement si la matrice de covariance est non-singulière (c'est-à-dire inversible, $\det(\Sigma) > 0$). C'est la forme explicite de notre "hyper-montagne".

**Théorème 6.1 : Fonction de Densité de Probabilité d'un Vecteur Gaussien Non-Singulier**
Si $X$ est un vecteur gaussien de dimension $d$ avec vecteur espérance $\mu$ et matrice de covariance $\Sigma$ non-singulière, alors sa fonction de densité de probabilité (PDF) est donnée par :
$$ f_X(x) = \frac{1}{\sqrt{(2\pi)^d \det(\Sigma)}} \exp\left(-\frac{1}{2}(x - \mu)^T \Sigma^{-1} (x - \mu)\right) $$
pour tout $x \in \mathbb{R}^d$.

```latex
\begin{theorem}[Fonction de Densité de Probabilité d'un Vecteur Gaussien Non-Singulier]
Si $X$ est un vecteur gaussien de dimension $d$ avec vecteur espérance $\mu$ et matrice de covariance $\Sigma$ non-singulière, alors sa fonction de densité de probabilité (PDF) est donnée par :
$$ f_X(x) = \frac{1}{\sqrt{(2\pi)^d \det(\Sigma)}} \exp\left(-\frac{1}{2}(x - \mu)^T \Sigma^{-1} (x - \mu)\right) $$
pour tout $x \in \mathbb{R}^d$.
\end{theorem}
```

**Exemple 6.1 : Densité 2D**
Soit $X \sim \mathcal{N}\left(\begin{pmatrix} 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 & 0.5 \\ 0.5 & 1 \end{pmatrix}\right)$.
Ici, $\mu = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$.
Calculons $\det(\Sigma) = 1 \cdot 1 - 0.5 \cdot 0.5 = 1 - 0.25 = 0.75$.
Calculons $\Sigma^{-1} = \frac{1}{0.75} \begin{pmatrix} 1 & -0.5 \\ -0.5 & 1 \end{pmatrix} = \frac{4}{3} \begin{pmatrix} 1 & -0.5 \\ -0.5 & 1 \end{pmatrix} = \begin{pmatrix} 4/3 & -2/3 \\ -2/3 & 4/3 \end{pmatrix}$.
Alors la densité est :
$$ f_X(x_1, x_2) = \frac{1}{\sqrt{(2\pi)^2 \cdot 0.75}} \exp\left(-\frac{1}{2} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}^T \begin{pmatrix} 4/3 & -2/3 \\ -2/3 & 4/3 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}\right) $$
$$ = \frac{1}{\sqrt{3\pi^2}} \exp\left(-\frac{1}{2} \left(\frac{4}{3}x_1^2 - \frac{4}{3}x_1x_2 + \frac{4}{3}x_2^2\right)\right) $$
$$ = \frac{1}{\sqrt{3}\pi} \exp\left(-\frac{2}{3}(x_1^2 - x_1x_2 + x_2^2)\right) $$
Les termes $(x - \mu)^T \Sigma^{-1} (x - \mu)$ définissent les ellipses d'isodensité. Lorsque cette quantité est constante, $f_X(x)$ est constante.

#### 7. Le Conditionnement Gaussien : Observer et Prédire

C'est l'un des aspects les plus puissants et pratiques des vecteurs gaussiens. Si nous connaissons une partie d'un vecteur gaussien, comment cela affecte-t-il la distribution des autres parties ? C'est le principe de la régression linéaire et de la prédiction.

**Théorème 7.1 : Conditionnement de Vecteurs Gaussiens**
Soit $X = \begin{pmatrix} X_1 \\ X_2 \end{pmatrix}$ un vecteur gaussien de dimension $d$, où $X_1 \in \mathbb{R}^{d_1}$ et $X_2 \in \mathbb{R}^{d_2}$ ($d_1 + d_2 = d$).
Son vecteur espérance et sa matrice de covariance sont partitionnés en blocs :
$$ \mu = \mathbb{E}[X] = \begin{pmatrix} \mu_1 \\ \mu_2 \end{pmatrix} \quad \text{et} \quad \Sigma = \text{Cov}(X) = \begin{pmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{pmatrix} $$
où $\mu_1 = \mathbb{E}[X_1]$, $\mu_2 = \mathbb{E}[X_2]$, $\Sigma_{11} = \text{Cov}(X_1)$, $\Sigma_{22} = \text{Cov}(X_2)$, et $\Sigma_{12} = \text{Cov}(X_1, X_2)$, $\Sigma_{21} = \text{Cov}(X_2, X_1) = \Sigma_{12}^T$.
Si $\Sigma_{22}$ est inversible, alors la distribution conditionnelle de $X_1$ étant donné $X_2 = x_2$ est également gaussienne :
$$ (X_1 | X_2 = x_2) \sim \mathcal{N}(\mu_{1|2}, \Sigma_{1|2}) $$
avec :
$$ \mu_{1|2} = \mathbb{E}[X_1 | X_2 = x_2] = \mu_1 + \Sigma_{12} \Sigma_{22}^{-1} (x_2 - \mu_2) $$
$$ \Sigma_{1|2} = \text{Cov}[X_1 | X_2 = x_2] = \Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21} $$
La matrice $\Sigma_{1|2}$ est appelée le complément de Schur de $\Sigma_{22}$ dans $\Sigma$.

```latex
\begin{theorem}[Conditionnement de Vecteurs Gaussiens]
Soit $X = \begin{pmatrix} X_1 \\ X_2 \end{pmatrix}$ un vecteur gaussien de dimension $d$, où $X_1 \in \mathbb{R}^{d_1}$ et $X_2 \in \mathbb{R}^{d_2}$ ($d_1 + d_2 = d$).
Son vecteur espérance et sa matrice de covariance sont partitionnés en blocs :
$$ \mu = \mathbb{E}[X] = \begin{pmatrix} \mu_1 \\ \mu_2 \end{pmatrix} \quad \text{et} \quad \Sigma = \text{Cov}(X) = \begin{pmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{pmatrix} $$
Si $\Sigma_{22}$ est inversible, alors la distribution conditionnelle de $X_1$ étant donné $X_2 = x_2$ est également gaussienne :
$$ (X_1 | X_2 = x_2) \sim \mathcal{N}(\mu_{1|2}, \Sigma_{1|2}) $$
avec :
$$ \mu_{1|2} = \mathbb{E}[X_1 | X_2 = x_2] = \mu_1 + \Sigma_{12} \Sigma_{22}^{-1} (x_2 - \mu_2) $$
$$ \Sigma_{1|2} = \text{Cov}[X_1 | X_2 = x_2] = \Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21} $$
\end{theorem}
```

**Exemple 7.1 : Prédiction Simple 2D**
Soit $X = \begin{pmatrix} X_1 \\ X_2 \end{pmatrix}$ un vecteur gaussien avec $\mu = \begin{pmatrix} 10 \\ 5 \end{pmatrix}$ et $\Sigma = \begin{pmatrix} 4 & 2 \\ 2 & 9 \end{pmatrix}$.
Nous voulons connaître la distribution de $X_1$ sachant $X_2 = x_2$.
Ici, $d_1 = 1$, $d_2 = 1$.
$\mu_1 = 10$, $\mu_2 = 5$.
$\Sigma_{11} = 4$, $\Sigma_{12} = 2$, $\Sigma_{21} = 2$, $\Sigma_{22} = 9$.
$\Sigma_{22}^{-1} = 1/9$.

L'espérance conditionnelle de $X_1$ sachant $X_2 = x_2$ est :
$$ \mu_{1|2} = \mu_1 + \Sigma_{12} \Sigma_{22}^{-1} (x_2 - \mu_2) = 10 + 2 \cdot (1/9) \cdot (x_2 - 5) $$
$$ = 10 + \frac{2}{9}(x_2 - 5) = 10 + \frac{2}{9}x_2 - \frac{10}{9} = \frac{80}{9} + \frac{2}{9}x_2 $$
Si $x_2 = 8$, alors $\mu_{1|2} = \frac{80}{9} + \frac{16}{9} = \frac{96}{9} = \frac{32}{3} \approx 10.67$.
La variance conditionnelle de $X_1$ sachant $X_2 = x_2$ est :
$$ \Sigma_{1|2} = \Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21} = 4 - 2 \cdot (1/9) \cdot 2 = 4 - \frac{4}{9} = \frac{36-4}{9} = \frac{32}{9} $$
Ainsi, $(X_1 | X_2 = x_2) \sim \mathcal{N}\left(\frac{80}{9} + \frac{2}{9}x_2, \frac{32}{9}\right)$.
Remarquez que la variance conditionnelle ne dépend pas de la valeur observée $x_2$. C'est une propriété unique aux distributions gaussiennes.

### III. Preuves Fondamentales et Construction Algébrique

Une bonne théorie n'est rien sans des preuves solides. Nous allons maintenant nous atteler à la démonstration des théorèmes clés, sans aucune omission.

#### 1. Preuve de la Fonction Caractéristique d'un Vecteur Gaussien

Nous voulons montrer que si $X \sim \mathcal{N}(\mu, \Sigma)$, alors $\phi_X(t) = e^{i t^T \mu - \frac{1}{2} t^T \Sigma t}$.

**Preuve :**
Par définition, $X$ est un vecteur gaussien si pour tout $t \in \mathbb{R}^d$, la variable aléatoire $Y_t = t^T X$ est une variable aléatoire gaussienne unidimensionnelle (ou dégénérée).
Calculons l'espérance de $Y_t$:
$$ \mathbb{E}[Y_t] = \mathbb{E}[t^T X] = t^T \mathbb{E}[X] = t^T \mu $$
Calculons la variance de $Y_t$:
$$ \text{Var}(Y_t) = \text{Var}(t^T X) = \mathbb{E}[(t^T X - t^T \mu)^2] = \mathbb{E}[(t^T (X - \mu))^2] $$
Puisque $t^T (X - \mu)$ est un scalaire, $(t^T (X - \mu))^2 = (t^T (X - \mu))(t^T (X - \mu))^T = t^T (X - \mu) (X - \mu)^T t$.
$$ \text{Var}(Y_t) = \mathbb{E}[t^T (X - \mu) (X - \mu)^T t] $$
Puisque $t$ est un vecteur constant, nous pouvons le sortir de l'espérance :
$$ \text{Var}(Y_t) = t^T \mathbb{E}[(X - \mu) (X - \mu)^T] t = t^T \Sigma t $$
Donc, $Y_t \sim \mathcal{N}(t^T \mu, t^T \Sigma t)$.

Maintenant, rappelons la fonction caractéristique d'une variable aléatoire gaussienne unidimensionnelle $Y \sim \mathcal{N}(\mu_Y, \sigma_Y^2)$, qui est $\phi_Y(\tau) = e^{i \tau \mu_Y - \frac{1}{2} \tau^2 \sigma_Y^2}$.
La fonction caractéristique du vecteur $X$ est $\phi_X(t) = \mathbb{E}[e^{i t^T X}]$.
Nous pouvons réécrire $t^T X$ comme $Y_t$ avec $\tau = 1$.
Donc, $\phi_X(t) = \mathbb{E}[e^{i Y_t}]$. C'est la fonction caractéristique de $Y_t$ évaluée en $\tau=1$.
En utilisant la formule de la fonction caractéristique 1D avec $\mu_Y = t^T \mu$ et $\sigma_Y^2 = t^T \Sigma t$ :
$$ \phi_X(t) = e^{i (1) (t^T \mu) - \frac{1}{2} (1)^2 (t^T \Sigma t)} = e^{i t^T \mu - \frac{1}{2} t^T \Sigma t} $$
Ceci conclut la preuve.

#### 2. Preuve du Théorème de Conditionnement Gaussien

Nous allons démontrer les formules pour l'espérance et la covariance conditionnelles de $X_1$ étant donné $X_2 = x_2$.
Soit $X = \begin{pmatrix} X_1 \\ X_2 \end{pmatrix}$ un vecteur gaussien avec moyenne $\mu = \begin{pmatrix} \mu_1 \\ \mu_2 \end{pmatrix}$ et covariance $\Sigma = \begin{pmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{pmatrix}$.
L'idée est de construire une nouvelle variable aléatoire $Z$ qui est une combinaison linéaire de $X_1$ et $X_2$, telle que $Z$ et $X_2$ soient indépendantes. Puisque $X$ est gaussien, toute transformation affine de $X$ est aussi gaussienne. Si $Z$ et $X_2$ sont conjointement gaussiens et non corrélés, ils sont indépendants.

Considérons la variable aléatoire $Z = X_1 - A X_2$ pour une matrice $A$ que nous allons déterminer.
Nous voulons que $Z$ soit non corrélé avec $X_2$. C'est-à-dire $\text{Cov}(Z, X_2) = 0$.
$$ \text{Cov}(Z, X_2) = \mathbb{E}[(Z - \mathbb{E}[Z])(X_2 - \mathbb{E}[X_2])^T] $$
$$ \mathbb{E}[Z] = \mathbb{E}[X_1 - A X_2] = \mu_1 - A \mu_2 $$
Donc, $Z - \mathbb{E}[Z] = (X_1 - \mu_1) - A (X_2 - \mu_2)$.
$$ \text{Cov}(Z, X_2) = \mathbb{E}[((X_1 - \mu_1) - A (X_2 - \mu_2))(X_2 - \mu_2)^T] $$
$$ = \mathbb{E}[(X_1 - \mu_1)(X_2 - \mu_2)^T] - A \mathbb{E}[(X_2 - \mu_2)(X_2 - \mu_2)^T] $$
$$ = \Sigma_{12} - A \Sigma_{22} $$
Pour que $\text{Cov}(Z, X_2) = 0$, nous devons avoir $\Sigma_{12} - A \Sigma_{22} = 0$.
Si $\Sigma_{22}$ est inversible, nous pouvons choisir $A = \Sigma_{12} \Sigma_{22}^{-1}$.
Avec ce choix de $A$, nous avons construit $Z = X_1 - \Sigma_{12} \Sigma_{22}^{-1} X_2$.
Comme $Z$ et $X_2$ sont non corrélés et conjointement gaussiens (car $X$ est gaussien et $Z$ est une transformation linéaire de $X$), ils sont indépendants.

Maintenant, nous pouvons écrire $X_1$ en fonction de $Z$ et $X_2$:
$$ X_1 = Z + \Sigma_{12} \Sigma_{22}^{-1} X_2 $$
Conditionnons sur $X_2 = x_2$:
$$ (X_1 | X_2 = x_2) = Z + \Sigma_{12} \Sigma_{22}^{-1} x_2 $$
Puisque $Z$ et $X_2$ sont indépendants, la distribution de $Z$ n'est pas affectée par la connaissance de $X_2 = x_2$.
Donc, $(X_1 | X_2 = x_2)$ est gaussien parce que $Z$ est gaussien et que $\Sigma_{12} \Sigma_{22}^{-1} x_2$ est une constante.

**Calcul de l'Espérance Conditionnelle $\mu_{1|2}$ :**
$$ \mathbb{E}[X_1 | X_2 = x_2] = \mathbb{E}[Z + \Sigma_{12} \Sigma_{22}^{-1} x_2 | X_2 = x_2] $$
$$ = \mathbb{E}[Z | X_2 = x_2] + \Sigma_{12} \Sigma_{22}^{-1} x_2 $$
Puisque $Z$ et $X_2$ sont indépendants, $\mathbb{E}[Z | X_2 = x_2] = \mathbb{E}[Z]$.
Calculons $\mathbb{E}[Z]$ :
$$ \mathbb{E}[Z] = \mathbb{E}[X_1 - \Sigma_{12} \Sigma_{22}^{-1} X_2] = \mathbb{E}[X_1] - \Sigma_{12} \Sigma_{22}^{-1} \mathbb{E}[X_2] $$
$$ = \mu_1 - \Sigma_{12} \Sigma_{22}^{-1} \mu_2 $$
En substituant ceci dans l'expression de l'espérance conditionnelle :
$$ \mu_{1|2} = \mu_1 - \Sigma_{12} \Sigma_{22}^{-1} \mu_2 + \Sigma_{12} \Sigma_{22}^{-1} x_2 $$
$$ \mu_{1|2} = \mu_1 + \Sigma_{12} \Sigma_{22}^{-1} (x_2 - \mu_2) $$
Ceci correspond à la formule de l'espérance conditionnelle.

**Calcul de la Covariance Conditionnelle $\Sigma_{1|2}$ :**
$$ \text{Cov}[X_1 | X_2 = x_2] = \text{Cov}[Z + \Sigma_{12} \Sigma_{22}^{-1} x_2 | X_2 = x_2] $$
Puisque $\Sigma_{12} \Sigma_{22}^{-1} x_2$ est une constante par rapport à $Z$ (une fois $x_2$ est fixé), elle n'affecte pas la covariance.
$$ \text{Cov}[X_1 | X_2 = x_2] = \text{Cov}[Z | X_2 = x_2] $$
Puisque $Z$ et $X_2$ sont indépendants, $\text{Cov}[Z | X_2 = x_2] = \text{Cov}[Z]$.
Calculons $\text{Cov}[Z]$ :
$$ \text{Cov}[Z] = \text{Cov}[X_1 - A X_2] \quad \text{où} \quad A = \Sigma_{12} \Sigma_{22}^{-1} $$
$$ \text{Cov}[Z] = \text{Cov}[X_1 - A X_2, X_1 - A X_2] $$
En utilisant la bilinéarité de la covariance :
$$ \text{Cov}[Z] = \text{Cov}[X_1, X_1] - \text{Cov}[X_1, A X_2] - \text{Cov}[A X_2, X_1] + \text{Cov}[A X_2, A X_2] $$
$$ = \Sigma_{11} - \Sigma_{12} A^T - A \Sigma_{21} + A \Sigma_{22} A^T $$
Substituons $A = \Sigma_{12} \Sigma_{22}^{-1}$ et $A^T = (\Sigma_{12} \Sigma_{22}^{-1})^T = (\Sigma_{22}^{-1})^T \Sigma_{12}^T = \Sigma_{22}^{-1} \Sigma_{21}$ (car $\Sigma_{22}$ est symétrique et donc $\Sigma_{22}^{-1}$ l'est aussi, et $\Sigma_{12}^T = \Sigma_{21}$).
$$ \Sigma_{1|2} = \Sigma_{11} - \Sigma_{12} (\Sigma_{22}^{-1} \Sigma_{21}) - (\Sigma_{12} \Sigma_{22}^{-1}) \Sigma_{21} + (\Sigma_{12} \Sigma_{22}^{-1}) \Sigma_{22} (\Sigma_{22}^{-1} \Sigma_{21}) $$
$$ = \Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21} + \Sigma_{12} (\Sigma_{22}^{-1} \Sigma_{22}) (\Sigma_{22}^{-1} \Sigma_{21}) $$
$$ = \Sigma_{11} - 2 \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21} + \Sigma_{12} I (\Sigma_{22}^{-1} \Sigma_{21}) $$
$$ = \Sigma_{11} - 2 \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21} + \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21} $$
$$ = \Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21} $$
Ceci correspond à la formule de la covariance conditionnelle.

La preuve est complète. On voit bien que la construction de la variable $Z$ qui est indépendante de $X_2$ est la clé de voûte de cette démonstration.

### IV. Applications : L'Impact Pratique des Vecteurs Gaussiens

Maintenant que nous avons une compréhension solide des vecteurs gaussiens, voyons quelques-unes de leurs applications les plus importantes.

#### 1. Analyse en Composantes Principales (PCA)

La PCA est une technique de réduction de dimensionnalité très utilisée, et elle est intrinsèquement liée à la structure gaussienne des données.

**Le Concept :**
Imaginez un nuage de points de données multidimensionnelles. La PCA vise à trouver les directions (composantes principales) le long desquelles la variance des données est maximale. Ces directions sont orthogonales entre elles. En projetant les données sur les quelques premières composantes principales, on peut réduire la dimensionnalité tout en conservant le maximum d'information (au sens de la variance).

**Lien avec les Vecteurs Gaussiens :**
Si nos données sont distribuées selon un vecteur gaussien, alors les axes de l'ellipsoïde d'isodensité (définis par les vecteurs propres de la matrice de covariance) sont précisément les directions de plus grande variance. Les longueurs des axes de cet ellipsoïde sont proportionnelles aux racines carrées des valeurs propres.
La PCA revient à diagonaliser la matrice de covariance (ou la matrice de corrélation) des données.
Les vecteurs propres $u_i$ de $\Sigma$ sont les composantes principales.
Les valeurs propres $\lambda_i$ de $\Sigma$ mesurent la variance le long de ces composantes principales.
En retenant les $k$ vecteurs propres associés aux $k$ plus grandes valeurs propres, on obtient une projection optimale des données dans un sous-espace de dimension $k$.

**Exemple 8.1 : Réduction de Dimension 2D vers 1D**
Reprenons la matrice de covariance de l'exemple 4.4 : $\Sigma = \begin{pmatrix} 5 & 1 \\ 1 & 5 \end{pmatrix}$.
Ses valeurs propres étaient $\lambda_1 = 4$ et $\lambda_2 = 6$.
Ses vecteurs propres normalisés étaient $u_1 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}$ et $u_2 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}$.
Puisque $\lambda_2 = 6 > \lambda_1 = 4$, la direction de plus grande variance est $u_2 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}$.
Si nous avons un ensemble de données $X_1, \dots, X_N$ tirées de cette distribution gaussienne, la PCA nous dirait que la "meilleure" direction pour projeter ces données en 1D (celle qui conserve le plus de variance) est le long de $u_2$.
Chaque point de données $x_j = \begin{pmatrix} x_{j1} \\ x_{j2} \end{pmatrix}$ serait projeté sur $u_2$ pour obtenir une nouvelle coordonnée $y_j = u_2^T x_j$.
Par exemple, si un point est $x = \begin{pmatrix} 2 \\ 3 \end{pmatrix}$, sa projection sur la première composante principale est $y = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \end{pmatrix} \begin{pmatrix} 2 \\ 3 \end{pmatrix} = \frac{5}{\sqrt{2}}$.

#### 2. Modèles de Mélange Gaussiens (GMM)

Les GMM sont des modèles probabilistes qui représentent la densité de probabilité d'un ensemble de données comme une somme pondérée de plusieurs densités gaussiennes.

**Le Concept :**
Souvent, nos données ne proviennent pas d'une seule distribution gaussienne, mais de plusieurs groupes distincts, chacun pouvant être modélisé par sa propre gaussienne. Par exemple, les hauteurs d'une population peuvent être modélisées par un mélange de deux gaussiennes, une pour les hommes et une pour les femmes.
Un GMM est défini par :
$$ f(x) = \sum_{k=1}^K \pi_k \mathcal{N}(x | \mu_k, \Sigma_k) $$
où $K$ est le nombre de composantes gaussiennes, $\pi_k$ sont les poids de mélange ($\sum \pi_k = 1, \pi_k \ge 0$), et $\mathcal{N}(x | \mu_k, \Sigma_k)$ est la PDF d'une gaussienne multidimensionnelle avec moyenne $\mu_k$ et covariance $\Sigma_k$.

**Application : Clustering**
Les GMM sont largement utilisés pour le clustering, où l'objectif est de regrouper des points de données similaires. Contrairement à des algorithmes comme k-means qui assignent un point à un seul cluster, les GMM fournissent une probabilité qu'un point appartienne à chaque cluster. L'algorithme d'Espérance-Maximisation (EM) est couramment utilisé pour estimer les paramètres $(\pi_k, \mu_k, \Sigma_k)$ à partir des données.

**Exemple 9.1 : Clustering de Données 2D**
Imaginez un ensemble de points de données en 2D qui semblent former deux groupes distincts, l'un centré autour de $\begin{pmatrix} 0 \\ 0 \end{pmatrix}$ et l'autre autour de $\begin{pmatrix} 5 \\ 5 \end{pmatrix}$.
Un GMM avec $K=2$ pourrait modéliser cela.
La première composante gaussienne pourrait avoir $\mu_1 = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$ et $\Sigma_1 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$.
La deuxième composante gaussienne pourrait avoir $\mu_2 = \begin{pmatrix} 5 \\ 5 \end{pmatrix}$ et $\Sigma_2 = \begin{pmatrix} 2 & 0.5 \\ 0.5 & 1 \end{pmatrix}$.
Les poids $\pi_1$ et $\pi_2$ indiqueraient la proportion de points dans chaque groupe.
Si un nouveau point $x_{new} = \begin{pmatrix} 0.2 \\ 0.1 \end{pmatrix}$ arrive, le GMM calculerait $P(x_{new} | \text{cluster 1})$ et $P(x_{new} | \text{cluster 2})$ et fournirait une probabilité pondérée pour chaque cluster.

#### 3. Processus Gaussiens (GP)

Les processus gaussiens sont une généralisation des distributions gaussiennes à des espaces fonctionnels. Plutôt que de modéliser des vecteurs aléatoires, ils modélisent des *fonctions* aléatoires.

**Le Concept :**
Un processus gaussien est une collection de variables aléatoires, toute collection finie d'entre elles ayant une distribution gaussienne jointe. C'est une distribution sur des fonctions.
Pour définir un GP, nous avons besoin de deux fonctions :
1.  Une fonction moyenne $m(x) = \mathbb{E}[f(x)]$ qui spécifie la moyenne à chaque point $x$.
2.  Une fonction de covariance (ou noyau) $k(x, x') = \mathbb{E}[(f(x) - m(x))(f(x') - m(x'))]$ qui spécifie la covariance entre les valeurs de la fonction à deux points $x$ et $x'$.

**Application : Régression et Interpolation**
Les GPs sont excellents pour la régression non-paramétrique. Étant donné un ensemble de points de données observés $(x_i, y_i)$, un GP peut prédire la valeur de la fonction $y^*$ à un nouveau point $x^*$ tout en fournissant une mesure d'incertitude sur cette prédiction.
L'idée est que si nous observons $N$ points de données, $(y_1, \dots, y_N)$, et que nous voulons prédire $y^*$ à $x^*$, le vecteur $(y_1, \dots, y_N, y^*)$ est conjointement gaussien. Nous pouvons alors utiliser le théorème de conditionnement gaussien pour trouver la distribution conditionnelle de $y^*$ étant donné $(y_1, \dots, y_N)$.

**Exemple 10.1 : Prédiction de Température avec Incertitude**
Imaginons que nous mesurons la température à différents moments de la journée. Nous avons des observations $y_1, \dots, y_N$ aux temps $x_1, \dots, x_N$. Nous voulons prédire la température $y^*$ à un nouveau temps $x^*$.
Un processus gaussien peut modéliser la fonction de température sous-jacente.
Si nous utilisons un noyau de covariance exponentielle-quadratique (souvent appelé RBF ou noyau gaussien) : $k(x, x') = \sigma^2 \exp\left(-\frac{(x-x')^2}{2l^2}\right)$, où $\sigma^2$ est la variance du signal et $l$ est la longueur caractéristique.
En utilisant le conditionnement gaussien, la prédiction $y^*$ à $x^*$ sera une gaussienne avec une moyenne et une variance qui dépendent des observations.
Si les observations sont $y = (y_1, \dots, y_N)^T$ et que nous voulons prédire $y^*$, le vecteur conjoint est $Y_{joint} = \begin{pmatrix} y \\ y^* \end{pmatrix}$.
Sa moyenne est $\begin{pmatrix} m(x_1) \\ \vdots \\ m(x_N) \\ m(x^*) \end{pmatrix}$.
Sa matrice de covariance est $\begin{pmatrix} K(X,X) & K(X,x^*) \\ K(x^*,X) & K(x^*,x^*) \end{pmatrix}$, où $K(X,X)$ est la matrice de covariance des observations, $K(X,x^*)$ est le vecteur de covariance entre les observations et le point de prédiction, etc.
La moyenne conditionnelle $\mathbb{E}[y^* | y]$ sera la meilleure estimation de la température à $x^*$, et la variance conditionnelle $\text{Var}[y^* | y]$ nous donnera une mesure de l'incertitude de cette prédiction. Plus le point $x^*$ est éloigné des observations, plus la variance conditionnelle sera grande, reflétant une incertitude accrue.

---

Voilà, mes chers étudiants. Nous avons parcouru un chemin considérable. Des origines historiques du concept aux définitions rigoureuses, en passant par des démonstrations exhaustives et des applications concrètes qui montrent la puissance de cette théorie. Les vecteurs gaussiens ne sont pas juste une curiosité mathématique ; ils sont un pilier fondamental de la modélisation statistique, de l'apprentissage automatique et de l'ingénierie. Ils nous permettent de quantifier et de raisonner sur l'incertitude, une tâche essentielle dans un monde intrinsèquement stochastique.

Je vous encourage à méditer sur la beauté de ces concepts et à chercher leurs manifestations dans le monde qui vous entoure. La théorie des probabilités, comme la physique, est avant tout une science de l'intuition affûtée par la rigueur.
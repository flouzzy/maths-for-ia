---
uuid: "jalon-64"
title: "Construction de la mesure de Lebesgue"
year: 2
trimester: 6
tags:
  - math/mesure
  - ia/abstraction
prev: "[[Jalon 63 (Définition axiomatique d'une mesure).md]]"
next: "[[Jalon 65 (Fonctions mesurables).md]]"
---

# Jalon 64 : Construction de la mesure de Lebesgue

## Introduction

L'objectif de la théorie de la mesure est de généraliser les notions élémentaires de longueur, d'aire et de volume à des sous-ensembles arbitrairement complexes de $\mathbb{R}^n$. Historiquement, l'intégrale de Riemann, bien qu'efficace pour les fonctions continues par morceaux, montre ses limites face à des fonctions fortement discontinues ou lors de passages à la limite (comme avec des suites de fonctions). Émile Borel, puis Henri Lebesgue, ont introduit au début du XXe siècle une approche fondamentalement différente. Au lieu de découper l'axe des abscisses en intervalles pour approcher l'aire sous une courbe, Lebesgue propose de mesurer la taille des ensembles de valeurs de la fonction sur l'axe des ordonnées, ce qui requiert d'être capable de "mesurer" des ensembles très fractionnés, tels que l'image réciproque d'un petit intervalle.

La construction de la mesure de Lebesgue sur $\mathbb{R}$ commence par l'idée intuitive que l'on peut "recouvrir" n'importe quel ensemble par une réunion dénombrable de petits intervalles ouverts, pour lesquels la notion de longueur est triviale. L'infimum des sommes des longueurs de ces intervalles de recouvrement fournit une première estimation, appelée *mesure extérieure*. Cependant, pour préserver la propriété fondamentale d'additivité (la mesure de la réunion disjointe de deux ensembles doit être la somme de leurs mesures), la mesure extérieure ne peut pas être appliquée à toutes les parties de $\mathbb{R}$ sans créer de paradoxes géométriques (comme le paradoxe de Banach-Tarski, ou l'ensemble de Vitali). Constantin Carathéodory a formulé un critère élégant permettant de sélectionner les "bons" ensembles : les ensembles mesurables. Sur cette classe restreinte d'ensembles, qui forme une tribu (ou $\sigma$-algèbre), la mesure extérieure devient une véritable mesure, complète et invariante par translation, appelée la mesure de Lebesgue.

## Mesure Extérieure et Théorèmes Fondamentaux

Soit $\mathcal{P}(\mathbb{R})$ l'ensemble des parties de $\mathbb{R}$. Pour tout intervalle $I$ de bornes $a$ et $b$ (avec $a \le b$), on définit sa longueur $\ell(I) = b - a$.

**Définition 1 (Mesure extérieure de Lebesgue) :**
Pour toute partie $A \subset \mathbb{R}$, on définit la mesure extérieure de Lebesgue $\lambda^*(A)$ par :
$$\lambda^*(A) = \inf \left\lbrace \sum_{n=1}^\infty \ell(I_n) \mid A \subset \bigcup_{n=1}^\infty I_n, \quad I_n \text{ ouverts} \right\rbrace$$

La figure suivante illustre le principe de recouvrement pour la mesure extérieure d'un ensemble de points isolés.

\begin{tikzpicture}[scale=1.5]
  % Axe réel
  \draw[->, thick] (0,0) -- (6,0) node[right] {$\mathbb{R}$};

  % Points de l'ensemble A
  \fill[blue] (1,0) circle (1.5pt) node[below=2pt] {$x_1$};
  \fill[blue] (2.5,0) circle (1.5pt) node[below=2pt] {$x_2$};
  \fill[blue] (4.2,0) circle (1.5pt) node[below=2pt] {$x_3$};
  \fill[blue] (4.8,0) circle (1.5pt) node[below=2pt] {$x_4$};

  % Intervalles ouverts I_n
  \draw[red, thick, |-|] (0.7,0.2) -- (1.3,0.2) node[midway, above] {$I_1$};
  \draw[red, thick, |-|] (2.1,0.2) -- (2.9,0.2) node[midway, above] {$I_2$};
  \draw[red, thick, |-|] (3.8,0.2) -- (5.1,0.2) node[midway, above] {$I_3$};

  % Lignes pointillées
  \draw[dotted, gray] (0.7,0) -- (0.7,0.2);
  \draw[dotted, gray] (1.3,0) -- (1.3,0.2);
  \draw[dotted, gray] (2.1,0) -- (2.1,0.2);
  \draw[dotted, gray] (2.9,0) -- (2.9,0.2);
  \draw[dotted, gray] (3.8,0) -- (3.8,0.2);
  \draw[dotted, gray] (5.1,0) -- (5.1,0.2);

  % Titre
  \node at (3,-0.7) {Recouvrement d'un ensemble discret $A$ par des intervalles ouverts $I_n$.};
\end{tikzpicture}


**Exemple Concret 1 : Mesure extérieure d'un point**
Considérons l'ensemble $A = \{x\}$ avec $x \in \mathbb{R}$.
Pour tout $\epsilon > 0$, l'intervalle ouvert $I_\epsilon = \left]x - \frac{\epsilon}{2}, x + \frac{\epsilon}{2}\right[$ contient $A$.
La longueur de cet intervalle est $\ell(I_\epsilon) = \epsilon$.
Ainsi, $\lambda^*(A) \le \epsilon$ pour tout $\epsilon > 0$, ce qui implique rigoureusement que $\lambda^*(A) = 0$.

**Exemple Concret 2 : Mesure extérieure d'un segment fermé**
Considérons le segment $A = [0, 1]$.
Pour tout $\epsilon > 0$, on peut recouvrir $A$ par l'intervalle $I = ]-\epsilon, 1+\epsilon[$, de longueur $1+2\epsilon$.
Donc $\lambda^*(A) \le 1+2\epsilon$ pour tout $\epsilon > 0$, ce qui implique $\lambda^*(A) \le 1$.
D'autre part, si $\bigcup_{n=1}^\infty I_n$ recouvre $[0, 1]$, on peut, par compacité (Théorème de Heine-Borel), extraire un sous-recouvrement fini. On peut montrer, par récurrence sur le nombre d'intervalles finis, que la somme de leurs longueurs est au moins la longueur de l'intervalle recouvert. Ainsi, $\sum_{n=1}^\infty \ell(I_n) \ge 1$.
Par définition de l'infimum, $\lambda^*([0, 1]) = 1$.

**Exemple Concret 3 : Mesure extérieure de l'ensemble de Cantor**
L'ensemble de Cantor $\mathcal{C}$ est construit en retirant itérativement le tiers central ouvert des segments restants, à partir de $[0, 1]$.
À l'étape $n$, l'ensemble $C_n$ est composé de $2^n$ intervalles fermés de longueur $\frac{1}{3^n}$.
La longueur totale (mesure extérieure) à l'étape $n$ est $2^n \times \frac{1}{3^n} = \left(\frac{2}{3}\right)^n$.
Puisque $\mathcal{C} \subset C_n$ pour tout $n$, nous avons $\lambda^*(\mathcal{C}) \le \left(\frac{2}{3}\right)^n$.
En faisant tendre $n \to \infty$, on obtient $\lambda^*(\mathcal{C}) = 0$. L'ensemble de Cantor est donc de mesure extérieure nulle, bien qu'il ait la puissance du continu (non dénombrable).

La mesure extérieure possède les propriétés de monotonie ($A \subset B \implies \lambda^*(A) \le \lambda^*(B)$) et de sous-additivité dénombrable ($\lambda^*\left(\bigcup_{n=1}^\infty A_n\right) \le \sum_{n=1}^\infty \lambda^*(A_n)$). Toutefois, elle n'est pas additive.

**Définition 2 (Ensemble Lebesgue-mesurable, Critère de Carathéodory) :**
Une partie $E \subset \mathbb{R}$ est dite mesurable au sens de Lebesgue si, pour tout sous-ensemble $A \subset \mathbb{R}$ (que nous appellerons sous-ensemble de test), on a :
$$\lambda^*(A) = \lambda^*(A \cap E) + \lambda^*(A \cap (\mathbb{R} \setminus E))$$
On note $\mathcal{L}(\mathbb{R})$ l'ensemble des parties mesurables de $\mathbb{R}$.

\begin{tikzpicture}[scale=1.5]
  % Espace total R
  \draw[thick] (0,0) rectangle (6,3);
  \node at (0.3, 2.7) {$\mathbb{R}$};

  % Ensemble de test A
  \fill[gray!20, draw=black, thick] (3,1.5) ellipse (1.5 and 1);
  \node at (3, 2) {$A$};

  % Ligne séparatrice représentant l'ensemble mesurable E (partie gauche) et E^c (partie droite)
  \draw[dashed, very thick, blue] (2.5,0) -- (3.5,3);
  \node[blue] at (1.5, 0.3) {Ensemble Mesurable $E$};
  \node[red] at (4.5, 0.3) {$E^c = \mathbb{R} \setminus E$};

  % Mettre en évidence les intersections
  \node at (2.2, 1.2) {$A \cap E$};
  \node at (4.0, 1.2) {$A \cap E^c$};
\end{tikzpicture}

Le critère de Carathéodory exprime que $E$ "coupe" proprement (au sens de la mesure extérieure) tout ensemble de test $A$. Si $E$ est très "irrégulier" ou "chiffonné" (comme l'ensemble non mesurable de Vitali), sa frontière est tellement pathologique qu'elle crée un excédent de mesure : la somme des mesures des parties excède la mesure extérieure de l'ensemble de départ.

**Définition 3 (Mesure de Lebesgue) :**
On appelle mesure de Lebesgue, notée $\lambda$, la restriction de la mesure extérieure $\lambda^*$ à la tribu $\mathcal{L}(\mathbb{R})$ des ensembles Lebesgue-mesurables.

**Exemple Concret 4 : Mesurabilité d'un ensemble de mesure nulle**
Soit $E \subset \mathbb{R}$ tel que $\lambda^*(E) = 0$.
Soit $A \subset \mathbb{R}$ un ensemble de test quelconque.
On a $A \cap E \subset E$, donc par monotonie, $\lambda^*(A \cap E) \le \lambda^*(E) = 0$, ce qui implique $\lambda^*(A \cap E) = 0$.
D'autre part, $A \cap (\mathbb{R} \setminus E) \subset A$, donc $\lambda^*(A \cap (\mathbb{R} \setminus E)) \le \lambda^*(A)$.
Ainsi, $\lambda^*(A \cap E) + \lambda^*(A \cap (\mathbb{R} \setminus E)) = 0 + \lambda^*(A \cap (\mathbb{R} \setminus E)) \le \lambda^*(A)$.
Comme l'inégalité inverse (sous-additivité) $\lambda^*(A) \le \lambda^*(A \cap E) + \lambda^*(A \cap (\mathbb{R} \setminus E))$ est toujours vraie, nous avons bien l'égalité.
Conclusion : tout ensemble de mesure extérieure nulle est Lebesgue-mesurable, et sa mesure de Lebesgue est nulle.

**Exemple Concret 5 : Mesure d'une réunion dénombrable disjointe**
Par définition des tribus et des mesures, la mesure de Lebesgue est $\sigma$-additive.
Considérons l'ensemble des rationnels $\mathbb{Q} \cap [0, 1]$. Cet ensemble est dénombrable. Soit $\{q_1, q_2, \dots \}$ une énumération.
$\mathbb{Q} \cap [0, 1] = \bigcup_{n=1}^\infty \{q_n\}$, qui est une union disjointe d'ensembles mesurables de mesure nulle (Exemple 1 et 4).
Ainsi, $\lambda(\mathbb{Q} \cap [0, 1]) = \sum_{n=1}^\infty \lambda(\{q_n\}) = \sum_{n=1}^\infty 0 = 0$.
Les irrationnels dans $[0, 1]$, notés $\mathbb{I} \cap [0, 1]$, satisfont $\lambda([0, 1]) = \lambda(\mathbb{Q} \cap [0, 1]) + \lambda(\mathbb{I} \cap [0, 1])$, donc $1 = 0 + \lambda(\mathbb{I} \cap [0, 1])$.
La mesure des irrationnels dans $[0, 1]$ est exactement 1.

**Exemple Concret 6 : L'ensemble de Vitali (cas pathologique non mesurable)**
On définit une relation d'équivalence sur $[0, 1]$ par $x \sim y \iff x - y \in \mathbb{Q}$.
Par l'axiome du choix, on construit un ensemble $V \subset [0, 1]$ contenant exactement un représentant de chaque classe d'équivalence.
On peut translater cet ensemble $V$ par tous les rationnels $q \in \mathbb{Q} \cap [-1, 1]$. On obtient une famille dénombrable disjointe de translations $V_q = V + q$.
Leur réunion couvre $[0, 1]$ et est contenue dans $[-1, 2]$.
Si $V$ était mesurable, on aurait par invariance par translation $\lambda(V_q) = \lambda(V)$.
La $\sigma$-additivité donnerait : $\lambda\left(\bigcup_q V_q\right) = \sum_q \lambda(V)$.
Si $\lambda(V) = 0$, la somme fait $0$, contredisant le fait que la réunion recouvre $[0, 1]$ (de mesure 1).
Si $\lambda(V) > 0$, la somme vaut $+\infty$, contredisant le fait que la réunion est incluse dans $[-1, 2]$ (de mesure 3).
Conclusion : on ne peut pas attribuer de mesure à $V$. L'ensemble de Vitali n'est pas Lebesgue-mesurable.

**Exemple Concret 7 : Invariance par translation des intervalles**
Soit $I = [a, b]$ un intervalle fermé.
Soit $x \in \mathbb{R}$. Le translaté de $I$ est $I + x = [a+x, b+x]$.
La mesure extérieure de $I$ est $\lambda^*(I) = b - a$.
La mesure extérieure de $I+x$ est $\lambda^*(I+x) = (b+x) - (a+x) = b - a$.
Nous vérifions directement que $\lambda^*(I+x) = \lambda^*(I)$, un fait fondamental de la mesure de Lebesgue qui assure son unicité mathématique en tant que mesure régulière invariante par translation sur les boréliens de $\mathbb{R}$.

## Démonstrations

**Démonstration 1 : Un ensemble dénombrable est de mesure nulle**

Soit $A = \{a_1, a_2, \dots, a_n, \dots \}$ un sous-ensemble dénombrable de $\mathbb{R}$.
Soit $\epsilon > 0$ un réel strictement positif fixé arbitrairement.
Pour chaque élément $a_n \in A$ (indexé par $n \in \mathbb{N}^*$), construisons un intervalle ouvert $I_n$ centré en $a_n$ et de longueur $\frac{\epsilon}{2^n}$.
Plus précisément, on pose $I_n = \left] a_n - \frac{\epsilon}{2^{n+1}}, a_n + \frac{\epsilon}{2^{n+1}} \right[$.
La longueur de chaque intervalle $I_n$ est strictement $\ell(I_n) = \frac{\epsilon}{2^n}$.
Par construction, chaque $a_n$ appartient à l'intervalle $I_n$, et par conséquent, la collection $\{I_n\}_{n \ge 1}$ forme un recouvrement ouvert dénombrable de l'ensemble $A$ :
$A \subset \bigcup_{n=1}^\infty I_n$
La définition de la mesure extérieure nous garantit que :
$\lambda^*(A) \le \sum_{n=1}^\infty \ell(I_n)$
Substituons les longueurs et calculons la série géométrique :
$\lambda^*(A) \le \sum_{n=1}^\infty \frac{\epsilon}{2^n} = \epsilon \sum_{n=1}^\infty \left(\frac{1}{2}\right)^n$
La somme géométrique convergente vaut exactement $1$ : $\sum_{n=1}^\infty \left(\frac{1}{2}\right)^n = \frac{1/2}{1 - 1/2} = 1$.
Ainsi, $\lambda^*(A) \le \epsilon$.
Cette inégalité est vérifiée pour tout réel $\epsilon > 0$. La mesure extérieure $\lambda^*(A)$ étant par définition positive ou nulle, nous en déduisons rigoureusement que :
$\lambda^*(A) = 0$
Puisque tout sous-ensemble de mesure extérieure nulle est mesurable (Exemple 4), $A \in \mathcal{L}(\mathbb{R})$ et $\lambda(A) = 0$.

**Démonstration 2 : La sous-additivité dénombrable de la mesure extérieure**

Soit $(A_k)_{k \in \mathbb{N}^*}$ une suite d'ensembles quelconques de $\mathbb{R}$. Nous souhaitons montrer que $\lambda^*\left( \bigcup_{k=1}^\infty A_k \right) \le \sum_{k=1}^\infty \lambda^*(A_k)$.
Si la série du membre de droite diverge (somme infinie), l'inégalité est trivialement vérifiée. Supposons donc que pour tout $k \in \mathbb{N}^*$, $\lambda^*(A_k) < +\infty$.
Soit $\epsilon > 0$. Par la définition de l'infimum pour la mesure extérieure, pour chaque entier $k$, il existe une suite d'intervalles ouverts $(I_{k, n})_{n \in \mathbb{N}^*}$ telle que :
$A_k \subset \bigcup_{n=1}^\infty I_{k, n}$ et $\sum_{n=1}^\infty \ell(I_{k, n}) < \lambda^*(A_k) + \frac{\epsilon}{2^k}$.
La réunion de tous ces ensembles donne :
$\bigcup_{k=1}^\infty A_k \subset \bigcup_{k=1}^\infty \bigcup_{n=1}^\infty I_{k, n}$
La famille de tous les intervalles $\{I_{k, n}\}_{(k, n) \in (\mathbb{N}^*)^2}$ est dénombrable et forme un recouvrement ouvert de $\bigcup_{k=1}^\infty A_k$.
Par conséquent, la définition de la mesure extérieure de la réunion implique :
$\lambda^*\left( \bigcup_{k=1}^\infty A_k \right) \le \sum_{k=1}^\infty \sum_{n=1}^\infty \ell(I_{k, n})$
En utilisant la borne supérieure sur les sommes des longueurs pour chaque $k$, on a :
$\lambda^*\left( \bigcup_{k=1}^\infty A_k \right) \le \sum_{k=1}^\infty \left( \lambda^*(A_k) + \frac{\epsilon}{2^k} \right) = \sum_{k=1}^\infty \lambda^*(A_k) + \epsilon \sum_{k=1}^\infty \frac{1}{2^k} = \sum_{k=1}^\infty \lambda^*(A_k) + \epsilon$
Étant donné que cette inégalité est vraie pour tout $\epsilon > 0$, le passage à la limite $\epsilon \to 0$ conclut la preuve rigoureusement.

## Applications en Physique, Logique et IA

En probabilités et apprentissage automatique (IA), l'espace mesuré $(\mathbb{R}, \mathcal{L}(\mathbb{R}), \lambda)$ constitue la fondation de la notion de variable aléatoire à densité. Une densité de probabilité $f : \mathbb{R} \to \mathbb{R}^+$ n'est intégrable rigoureusement que par l'intégrale de Lebesgue (Jalons suivants) qui repose sur cette mesure.

Dans les architectures de génération de données (GANs, Normalizing Flows), un problème théorique profond découle de la mesure de Lebesgue. Supposons que les données réelles (images de visages par exemple) résident sur une variété différentielle de faible dimension au sein d'un espace de très grande dimension $\mathbb{R}^D$ (ex: $D = 1000 \times 1000 = 10^6$ pixels). La mesure de Lebesgue d'une variété de dimension $d < D$ dans $\mathbb{R}^D$ est stricement nulle. Par conséquent, toute distribution de probabilité absolue continue par rapport à la mesure de Lebesgue (qui assigne une masse non nulle à tout volume ouvert) aura un support disjoint de la variété des données réelles. Cela cause des divergences infinies lors du calcul de la divergence de Kullback-Leibler, expliquant fondamentalement pourquoi l'entraînement des GANs est si instable mathématiquement et a justifié l'introduction de la distance de Wasserstein (qui s'appuie sur la théorie du transport optimal) pour mesurer la distance entre des distributions supportées sur des ensembles de mesure de Lebesgue nulle.

De plus, en théorie de la mesure, la non-mesurabilité de certains ensembles (comme les ensembles de Vitali) prévient l'apparition de paradoxes lors de l'apprentissage statistique. Tous les ouverts, fermés, intersections dénombrables et réunions dénombrables (les ensembles boréliens) sont inclus dans la tribu de Lebesgue, ce qui assure que l'image réciproque d'intervalles par des réseaux de neurones (fonctions continues, donc mesurables) sera toujours un ensemble pour lequel la probabilité (la taille) est mathématiquement bien définie, évitant ainsi toute ambiguïté théorique dans la formulation empirique du risque.

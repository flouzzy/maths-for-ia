---
uuid: "jalon-43"
title: "Systèmes différentiels linéaires et exponentielle de matrice"
year: 1
trimester: 4
tags:
  - math/algebre-lineaire
  - ia/systemes-dynamiques
prev: "[[Jalon 42 (Équations différentielles linéaires du second ordre à coefficients constants.).md]]"
next: "[[Jalon 44 (Fonctions de plusieurs variables).md]]"
---

# Jalon 43 : Systèmes différentiels linéaires et exponentielle de matrice

## 1. Genèse du concept
Au tournant du XIXe siècle, les physiciens et mathématiciens sont confrontés à un problème d'une complexité vertigineuse : comment modéliser l'évolution temporelle d'un système où chaque composante influence continuellement toutes les autres ? Prenons le mouvement de plusieurs corps en interaction gravitationnelle, ou la diffusion de chaleur dans un matériau composite. Si l'on écrit les équations différentielles qui régissent chaque composante, on obtient un système d'équations couplées. Résoudre une équation différentielle d'ordre 1 isolée $x'(t) = a x(t)$ est immédiat : la solution est de la forme $x(t) = C e^{at}$. L'idée fulgurante, développée notamment par Peano et systématisée par la théorie spectrale naissante, fut d'audacieusement généraliser la fonction exponentielle, d'une variable scalaire, aux matrices, traitant le système couplé non plus composante par composante, mais comme un unique objet vectoriel évoluant dans l'espace d'état. L'exponentielle de matrice devient alors le flux de propagation de la dynamique, offrant une vue unifiée et globale du mouvement.

## 2. Définition et algèbre de l'exponentielle de matrice

Considérons l'espace des matrices carrées d'ordre $n$ à coefficients réels ou complexes, noté $\mathcal{M}_n(\mathbb{K})$ (où $\mathbb{K} = \mathbb{R}$ ou $\mathbb{C}$). Cet espace, muni d'une norme d'algèbre matricielle usuelle $\|\cdot\|$, est un espace de Banach (un espace vectoriel normé complet).

**Théorème et Définition 1 (Exponentielle de Matrice)**
Pour toute matrice $A \in \mathcal{M}_n(\mathbb{K})$, la série matricielle $\sum_{k=0}^{+\infty} \frac{A^k}{k!}$ est absolument convergente. On définit l'exponentielle de $A$, notée $\exp(A)$ ou $e^A$, par sa somme :
$$ e^A = \sum_{k=0}^{+\infty} \frac{A^k}{k!} = I_n + A + \frac{A^2}{2} + \frac{A^3}{6} + \dots $$

**Exemple concret immédiat : Matrice Diagonale**
Soit $D = \begin{pmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{pmatrix}$. Alors $D^k = \begin{pmatrix} \lambda_1^k & 0 \\ 0 & \lambda_2^k \end{pmatrix}$.
Le calcul de la série donne trivialement :
$$ e^D = \sum_{k=0}^{+\infty} \frac{1}{k!} \begin{pmatrix} \lambda_1^k & 0 \\ 0 & \lambda_2^k \end{pmatrix} = \begin{pmatrix} \sum_{k=0}^{+\infty} \frac{\lambda_1^k}{k!} & 0 \\ 0 & \sum_{k=0}^{+\infty} \frac{\lambda_2^k}{k!} \end{pmatrix} = \begin{pmatrix} e^{\lambda_1} & 0 \\ 0 & e^{\lambda_2} \end{pmatrix} $$

**Cas limites et contre-exemples**
Contrairement aux scalaires, pour deux matrices quelconques $A$ et $B$, l'égalité $e^{A+B} = e^A e^B$ est **fausse** en général. Elle n'est vraie que si $A$ et $B$ commutent (c'est-à-dire si $AB = BA$). Si l'on ignore cette hypothèse cruciale, on commet une erreur d'algèbre non-commutative fondamentale (que corrige la complexe formule de Baker-Campbell-Hausdorff).

## 3. Démonstrations et propriétés spectrales

**Théorème 2 (Invariance par similitude)**
Soit $A \in \mathcal{M}_n(\mathbb{K})$. Si $A = P B P^{-1}$ avec $P$ inversible, alors $e^A = P e^B P^{-1}$.

**Démonstration détaillée ligne par ligne**
Soit l'entier $k \geq 0$. Calculons la puissance $k$-ième de $A$ :
$$ A^k = (P B P^{-1})^k $$
$$ A^k = (P B P^{-1})(P B P^{-1}) \dots (P B P^{-1}) \quad \text{(k termes)} $$
Les termes $P^{-1}P$ adjacents s'annulent pour donner l'identité $I_n$.
$$ A^k = P B (P^{-1}P) B (P^{-1}P) \dots B P^{-1} $$
$$ A^k = P B^k P^{-1} $$
L'application $M \mapsto P M P^{-1}$ est linéaire et continue sur $\mathcal{M}_n(\mathbb{K})$ (endomorphisme d'un espace de dimension finie).
Donc, en l'appliquant aux sommes partielles puis en passant à la limite :
$$ \sum_{k=0}^{N} \frac{A^k}{k!} = \sum_{k=0}^{N} \frac{P B^k P^{-1}}{k!} = P \left( \sum_{k=0}^{N} \frac{B^k}{k!} \right) P^{-1} $$
En prenant la limite quand $N \to +\infty$ :
$$ e^A = P e^B P^{-1} $$
La démonstration est ainsi achevée.

## 4. Systèmes différentiels linéaires et théorème de Cauchy-Lipschitz

**Définition 2 (Système Différentiel Linéaire d'ordre 1 à coefficients constants)**
Un tel système s'écrit sous forme vectorielle :
$$ Y'(t) = A Y(t) $$
Où $Y(t) \in \mathbb{R}^n$ est le vecteur d'état à l'instant $t$, et $A \in \mathcal{M}_n(\mathbb{R})$ est la matrice du système.

**Théorème 3 (Solution fondamentale)**
La fonction matricielle $t \mapsto e^{tA}$ est dérivable sur $\mathbb{R}$ et sa dérivée est :
$$ \frac{d}{dt}(e^{tA}) = A e^{tA} = e^{tA} A $$
Par conséquent, l'unique solution du problème de Cauchy $Y'(t) = A Y(t)$ avec condition initiale $Y(0) = Y_0$ est donnée par :
$$ Y(t) = e^{tA} Y_0 $$

**Exemple concret immédiat : Matrice Nilpotente**
Soit le système $Y'(t) = A Y(t)$ avec $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.
Calculons $A^2 = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$. La matrice est nilpotente d'indice 2.
Donc pour l'exponentielle, la série est tronquée :
$$ e^{tA} = I_2 + tA + \frac{t^2 A^2}{2} + \dots = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + t \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix} $$
Si $Y_0 = \begin{pmatrix} y_1(0) \\ y_2(0) \end{pmatrix}$, la solution au temps $t$ est $Y(t) = \begin{pmatrix} y_1(0) + t y_2(0) \\ y_2(0) \end{pmatrix}$.

## 5. Applications en Intelligence Artificielle

### Dynamiques temporelles et RNN
En modélisation de séquences, un Réseau de Neurones Récurrent (RNN) en temps continu (modèle ODE-Net ou Neural ODE) définit l'état caché par l'équation $\frac{dh(t)}{dt} = f(h(t), x(t))$. Lorsque la dynamique interne est linéarisée, on se retrouve avec $\frac{dh}{dt} = A h(t)$. Le calcul de l'exponentielle de $A$ détermine comment l'information se propage dans le temps. Si les valeurs propres de $A$ ont une partie réelle strictement positive, l'exponentielle diverge exponentiellement, provoquant l'explosion du gradient (Exploding Gradient). Si la partie réelle est trop négative, l'exponentielle s'effondre à 0 (Vanishing Gradient), détruisant la mémoire longue du réseau. Le contrôle du spectre de la matrice du système est donc la clé de voûte de la stabilité des algorithmes d'apprentissage sur des séries temporelles longues.

### State Space Models (Mamba, S4)
Les architectures modernes de State Space Models modélisent les séries temporelles très longues via des systèmes linéaires $x'(t) = A x(t) + B u(t)$. Pour le traiter numériquement sur des ordinateurs discrets, on utilise la transformée bilinéaire ou directement l'exponentielle de matrice $e^{\Delta \cdot A}$ pour discrétiser le modèle exact, sans approximation de pas d'intégration, ce qui permet à ces modèles de battre les Transformers sur l'analyse de séquences gigantesques sans être bridés par la limite quadratique de l'Attention.

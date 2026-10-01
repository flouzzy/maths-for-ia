---
uuid: "jalon-81"
title: "Transformée de Fourier dans L2 et Plancherel"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/traitement-du-signal
prev: "[[Jalon 80 (Transformée de Fourier dans L1).md]]"
next: "[[Jalon 82 (Introduction à la théorie des distributions de Schwartz).md]]"
---
# Jalon 81 : Transformée de Fourier dans $L^2$ et Plancherel

## 1. Introduction à la transformée de Fourier sur l'espace $L^2$

La théorie de l'intégrale de Lebesgue développée pour l'espace $L^1(\mathbb{R})$ a permis de définir la transformée de Fourier $\mathcal{F}(f)$ pour des fonctions dont l'intégrale de la valeur absolue converge. Cependant, en physique et en traitement du signal, l'espace naturel de travail est $L^2(\mathbb{R})$, l'espace des fonctions de carré intégrable, qui modélise les signaux d'énergie finie. Or, une fonction de $L^2(\mathbb{R})$ n'est pas nécessairement dans $L^1(\mathbb{R})$ (par exemple, la fonction $x \mapsto \frac{\sin(x)}{x}$ n'est pas intégrable au sens de Lebesgue sur $\mathbb{R}$).

Le défi fondamental est donc d'étendre la transformée de Fourier à tout l'espace $L^2(\mathbb{R})$. Cette extension repose sur la densité de $L^1(\mathbb{R}) \cap L^2(\mathbb{R})$ dans $L^2(\mathbb{R})$ et sur le théorème de Plancherel, qui affirme que la transformée de Fourier conserve l'énergie du signal, agissant comme une isométrie (à un facteur multiplicatif près) sur l'espace de Hilbert $L^2(\mathbb{R})$.

## 2. Définitions, Théorèmes et Exemples

### A. L'opérateur de Fourier sur $L^1 \cap L^2$

\begin{tikzpicture}[scale=1]
  \draw[->] (-3,0) -- (3,0) node[right] {Temps $t$};
  \draw[->] (0,-1) -- (0,2) node[above] {$f(t)$};
  \draw[domain=-2.5:2.5,smooth,variable=\x,blue,thick] plot ({\x},{exp(-\x*\x)});
  \node[blue] at (1.5,1.5) {$f \in L^1 \cap L^2$};

  \draw[thick, ->] (3.5, 0.5) -- (4.5, 0.5) node[midway, above] {$\mathcal{F}$};

  \begin{scope}[shift={(8,0)}]
  \draw[->] (-3,0) -- (3,0) node[right] {Fréquence $\xi$};
  \draw[->] (0,-1) -- (0,2) node[above] {$\hat{f}(\xi)$};
  \draw[domain=-2.5:2.5,smooth,variable=\x,red,thick] plot ({\x},{sqrt(pi)*exp(-\x*\x/4)/1.5});
  \node[red] at (1.5,1.5) {$\hat{f} \in L^2$};
  \end{scope}
\end{tikzpicture}

**Définition 1.** Soit $f \in L^1(\mathbb{R}) \cap L^2(\mathbb{R})$. La transformée de Fourier de $f$ est définie par l'intégrale convergente :
$$ \hat{f}(\xi) = \int_{-\infty}^{+\infty} f(t) e^{-i\xi t} dt $$

**Exemple 1 : La fonction porte.**
Considérons la fonction $f(t) = \mathbf{1}_{[-1, 1]}(t)$. Elle appartient à $L^1(\mathbb{R}) \cap L^2(\mathbb{R})$.
Calculons sa transformée de Fourier :
$$ \hat{f}(\xi) = \int_{-1}^{1} e^{-i\xi t} dt = \left[ \frac{e^{-i\xi t}}{-i\xi} \right]_{-1}^{1} = \frac{e^{-i\xi} - e^{i\xi}}{-i\xi} = \frac{2\sin(\xi)}{\xi} = 2\text{sinc}(\xi) $$
La fonction $\xi \mapsto 2\text{sinc}(\xi)$ appartient à $L^2(\mathbb{R})$ mais n'appartient pas à $L^1(\mathbb{R})$.

**Exemple 2 : Fonction exponentielle décroissante unilatérale.**
Considérons $f(t) = e^{-at} \mathbf{1}_{[0, +\infty[}(t)$ avec $a > 0$.
$f \in L^1(\mathbb{R}) \cap L^2(\mathbb{R})$.
$$ \hat{f}(\xi) = \int_{0}^{+\infty} e^{-at} e^{-i\xi t} dt = \int_{0}^{+\infty} e^{-(a+i\xi)t} dt $$
$$ \hat{f}(\xi) = \left[ \frac{e^{-(a+i\xi)t}}{-(a+i\xi)} \right]_{0}^{+\infty} = \frac{1}{a+i\xi} = \frac{a - i\xi}{a^2 + \xi^2} $$
On vérifie que $\hat{f} \in L^2(\mathbb{R})$. En effet, $|\hat{f}(\xi)|^2 = \frac{1}{a^2 + \xi^2}$ dont l'intégrale sur $\mathbb{R}$ est finie (elle vaut $\frac{\pi}{a}$).

### B. Le Théorème de Plancherel

**Théorème 1 (Plancherel).**
Pour toute fonction $f \in L^1(\mathbb{R}) \cap L^2(\mathbb{R})$, on a :
$$ \|\hat{f}\|_2^2 = 2\pi \|f\|_2^2 $$
C'est-à-dire :
$$ \int_{-\infty}^{+\infty} |\hat{f}(\xi)|^2 d\xi = 2\pi \int_{-\infty}^{+\infty} |f(t)|^2 dt $$

**Exemple 3 : Vérification du théorème de Plancherel sur la fonction porte.**
Reprenons $f(t) = \mathbf{1}_{[-1, 1]}(t)$ et $\hat{f}(\xi) = 2\frac{\sin(\xi)}{\xi}$.
Calculons $\|f\|_2^2$ :
$$ \|f\|_2^2 = \int_{-1}^{1} 1^2 dt = 2 $$
Calculons $\|\hat{f}\|_2^2$ :
$$ \|\hat{f}\|_2^2 = \int_{-\infty}^{+\infty} 4\frac{\sin^2(\xi)}{\xi^2} d\xi $$
Or, on sait par l'intégrale de Dirichlet que $\int_{-\infty}^{+\infty} \frac{\sin^2(\xi)}{\xi^2} d\xi = \pi$.
Donc $\|\hat{f}\|_2^2 = 4\pi$.
On a bien $4\pi = 2\pi \times 2$, soit $\|\hat{f}\|_2^2 = 2\pi \|f\|_2^2$. L'isométrie est vérifiée.

**Exemple 4 : Vérification du théorème de Plancherel sur l'exponentielle décroissante unilatérale.**
Reprenons $f(t) = e^{-at} \mathbf{1}_{[0, +\infty[}(t)$ avec $a > 0$ et $\hat{f}(\xi) = \frac{1}{a+i\xi}$.
Calcul de $\|f\|_2^2$ :
$$ \|f\|_2^2 = \int_{0}^{+\infty} e^{-2at} dt = \left[ \frac{e^{-2at}}{-2a} \right]_0^{+\infty} = \frac{1}{2a} $$
Calcul de $\|\hat{f}\|_2^2$ :
$$ \|\hat{f}\|_2^2 = \int_{-\infty}^{+\infty} \frac{1}{a^2 + \xi^2} d\xi $$
Effectuons le changement de variable $\xi = a u$, $d\xi = a du$ :
$$ \|\hat{f}\|_2^2 = \int_{-\infty}^{+\infty} \frac{1}{a^2(1+u^2)} a du = \frac{1}{a} \int_{-\infty}^{+\infty} \frac{du}{1+u^2} = \frac{1}{a} \left[ \arctan(u) \right]_{-\infty}^{+\infty} = \frac{\pi}{a} $$
On a bien $\|\hat{f}\|_2^2 = \frac{\pi}{a} = 2\pi \times \frac{1}{2a} = 2\pi \|f\|_2^2$.

### C. Le prolongement à $L^2$ tout entier

L'application $\mathcal{F} : f \mapsto \hat{f}$, définie sur $L^1(\mathbb{R}) \cap L^2(\mathbb{R})$, à valeurs dans $L^2(\mathbb{R})$, est linéaire et vérifie $\|\mathcal{F}(f)\|_2 = \sqrt{2\pi}\|f\|_2$. Elle est donc continue pour la norme $\|\cdot\|_2$.
Comme l'espace $L^1(\mathbb{R}) \cap L^2(\mathbb{R})$ est un sous-espace vectoriel dense dans l'espace de Banach $L^2(\mathbb{R})$, le théorème de prolongement des applications linéaires continues permet d'affirmer l'existence d'un unique prolongement continu de $\mathcal{F}$ à $L^2(\mathbb{R})$.

**Théorème 2 (Prolongement de la transformée de Fourier).**
Il existe un unique opérateur linéaire continu $\widetilde{\mathcal{F}} : L^2(\mathbb{R}) \to L^2(\mathbb{R})$ tel que pour tout $f \in L^1(\mathbb{R}) \cap L^2(\mathbb{R})$, $\widetilde{\mathcal{F}}(f) = \mathcal{F}(f)$.
De plus, pour tout $f \in L^2(\mathbb{R})$, on a :
$$ \|\widetilde{\mathcal{F}}(f)\|_2^2 = 2\pi \|f\|_2^2 $$
Cet opérateur est défini, pour tout $f \in L^2(\mathbb{R})$, par la limite dans $L^2(\mathbb{R})$ :
$$ \widetilde{\mathcal{F}}(f)(\xi) = \lim_{R \to +\infty} \int_{-R}^{R} f(t) e^{-i\xi t} dt $$
(Par abus de notation, on note toujours cet opérateur $\mathcal{F}$ et on écrit $\hat{f}$).

**Exemple 5 : Fonction sinc (Sinus cardinal).**
La fonction $f(t) = \frac{\sin(t)}{t}$ appartient à $L^2(\mathbb{R})$ mais pas à $L^1(\mathbb{R})$. On ne peut donc pas écrire $\int_{-\infty}^{+\infty} \frac{\sin(t)}{t} e^{-i\xi t} dt$ au sens de Lebesgue.
Cependant, la transformée de Fourier $\hat{f}$ existe dans $L^2(\mathbb{R})$. Elle correspond à $\hat{f}(\xi) = \pi \mathbf{1}_{[-1, 1]}(\xi)$, presque partout.
Vérifions Plancherel :
$\|f\|_2^2 = \int_{-\infty}^{+\infty} \frac{\sin^2(t)}{t^2} dt = \pi$.
$\|\hat{f}\|_2^2 = \int_{-1}^1 \pi^2 d\xi = 2\pi^2$.
On a bien $2\pi^2 = 2\pi \times \pi$.

### D. La Formule d'Inversion dans $L^2$

**Théorème 3 (Inversion dans $L^2$).**
L'opérateur de transformée de Fourier $\mathcal{F}$ est un isomorphisme de $L^2(\mathbb{R})$ dans lui-même. Son application inverse $\mathcal{F}^{-1}$ est donnée, pour tout $g \in L^2(\mathbb{R})$, par :
$$ \mathcal{F}^{-1}(g)(t) = \frac{1}{2\pi} \lim_{R \to +\infty} \int_{-R}^{R} g(\xi) e^{i\xi t} d\xi $$
limite au sens de la norme de $L^2(\mathbb{R})$.

**Exemple 6 : Récupération de l'exponentielle décroissante.**
Soit $\hat{f}(\xi) = \frac{1}{a+i\xi}$ pour $a>0$. $\hat{f} \in L^2(\mathbb{R})$.
Appliquons la formule d'inversion :
$$ f(t) = \frac{1}{2\pi} \int_{-\infty}^{+\infty} \frac{1}{a+i\xi} e^{i\xi t} d\xi $$
Pour $t < 0$, en fermant un contour d'intégration dans le demi-plan inférieur du plan complexe, on n'entoure aucun pôle (le seul pôle de $\frac{1}{a+i\xi} = \frac{-i}{\xi-ia}$ est en $\xi = ia$, situé dans le demi-plan supérieur). L'intégrale vaut 0.
Pour $t > 0$, en fermant le contour dans le demi-plan supérieur, on entoure le pôle $\xi = ia$. Par le théorème des résidus :
$$ \int_{-\infty}^{+\infty} \frac{-i}{\xi-ia} e^{i\xi t} d\xi = 2i\pi \text{Res}\left( \frac{-i e^{i\xi t}}{\xi-ia}, ia \right) = 2i\pi (-i) e^{i(ia)t} = 2\pi e^{-at} $$
Ainsi, $f(t) = e^{-at}$ pour $t>0$, et 0 pour $t<0$. On retrouve bien $f(t) = e^{-at} \mathbf{1}_{]0, +\infty[}(t)$, confirmant la formule d'inversion.

## 3. Démonstrations

**Démonstration du Théorème de Plancherel pour $f \in \mathcal{S}(\mathbb{R})$ (Espace de Schwartz).**
On considère l'espace de Schwartz $\mathcal{S}(\mathbb{R})$ des fonctions infiniment dérivables à décroissance rapide, qui est inclus dans $L^1(\mathbb{R}) \cap L^2(\mathbb{R})$.
Soit $f \in \mathcal{S}(\mathbb{R})$. Définissons la fonction $g(t) = \overline{f(-t)}$.
La transformée de Fourier de $g$ est :
$$ \hat{g}(\xi) = \int_{-\infty}^{+\infty} \overline{f(-t)} e^{-i\xi t} dt $$
Changement de variable $u = -t$, $du = -dt$ :
$$ \hat{g}(\xi) = \int_{+\infty}^{-\infty} \overline{f(u)} e^{i\xi u} (-du) = \int_{-\infty}^{+\infty} \overline{f(u) e^{-i\xi u}} du = \overline{\hat{f}(\xi)} $$
Considérons le produit de convolution $h = f * g$. Par les propriétés de la transformée de Fourier, on a :
$$ \hat{h}(\xi) = \hat{f}(\xi) \hat{g}(\xi) = \hat{f}(\xi) \overline{\hat{f}(\xi)} = |\hat{f}(\xi)|^2 $$
La fonction $f$ et la fonction $g$ sont dans $\mathcal{S}(\mathbb{R})$, donc $h \in \mathcal{S}(\mathbb{R})$ et $\hat{h} \in \mathcal{S}(\mathbb{R}) \subset L^1(\mathbb{R})$.
On peut donc appliquer la formule d'inversion de Fourier à $h$ évaluée en $t=0$ :
$$ h(0) = \frac{1}{2\pi} \int_{-\infty}^{+\infty} \hat{h}(\xi) e^{i\xi \times 0} d\xi $$
$$ h(0) = \frac{1}{2\pi} \int_{-\infty}^{+\infty} |\hat{f}(\xi)|^2 d\xi $$
Par ailleurs, exprimons $h(0)$ à partir de la définition du produit de convolution $h = f * g$ :
$$ h(t) = (f * g)(t) = \int_{-\infty}^{+\infty} f(\tau) g(t - \tau) d\tau $$
Pour $t = 0$ :
$$ h(0) = \int_{-\infty}^{+\infty} f(\tau) g(-\tau) d\tau = \int_{-\infty}^{+\infty} f(\tau) \overline{f(-(-\tau))} d\tau = \int_{-\infty}^{+\infty} f(\tau) \overline{f(\tau)} d\tau $$
$$ h(0) = \int_{-\infty}^{+\infty} |f(\tau)|^2 d\tau = \|f\|_2^2 $$
En égalant les deux expressions de $h(0)$, on obtient :
$$ \|f\|_2^2 = \frac{1}{2\pi} \int_{-\infty}^{+\infty} |\hat{f}(\xi)|^2 d\xi $$
Soit :
$$ \int_{-\infty}^{+\infty} |\hat{f}(\xi)|^2 d\xi = 2\pi \int_{-\infty}^{+\infty} |f(t)|^2 dt $$
Ce qui est exactement l'égalité de Plancherel pour $f \in \mathcal{S}(\mathbb{R})$.

**Démonstration du Théorème de Prolongement (Densité).**
Soit $f \in L^2(\mathbb{R})$.
Comme $\mathcal{S}(\mathbb{R})$ est dense dans $L^2(\mathbb{R})$, il existe une suite $(f_n)_{n \in \mathbb{N}}$ d'éléments de $\mathcal{S}(\mathbb{R})$ telle que $\lim_{n \to +\infty} \|f_n - f\|_2 = 0$.
La suite $(f_n)_{n \in \mathbb{N}}$ est une suite convergente dans $L^2(\mathbb{R})$, donc c'est une suite de Cauchy.
Pour tout $\epsilon > 0$, il existe $N \in \mathbb{N}$ tel que pour tout $n, m \ge N$, $\|f_n - f_m\|_2 \le \frac{\epsilon}{\sqrt{2\pi}}$.
Considérons la suite des transformées de Fourier $(\hat{f}_n)_{n \in \mathbb{N}}$.
Par la linéarité de la transformée de Fourier sur $\mathcal{S}(\mathbb{R})$, on a $\mathcal{F}(f_n - f_m) = \hat{f}_n - \hat{f}_m$.
Appliquons l'égalité de Plancherel (déjà démontrée sur $\mathcal{S}(\mathbb{R})$) à la fonction $f_n - f_m \in \mathcal{S}(\mathbb{R})$ :
$$ \|\hat{f}_n - \hat{f}_m\|_2 = \sqrt{2\pi} \|f_n - f_m\|_2 $$
Ainsi, pour tout $n, m \ge N$, on a :
$$ \|\hat{f}_n - \hat{f}_m\|_2 \le \sqrt{2\pi} \frac{\epsilon}{\sqrt{2\pi}} = \epsilon $$
La suite $(\hat{f}_n)_{n \in \mathbb{N}}$ est donc une suite de Cauchy dans l'espace $L^2(\mathbb{R})$.
Or, d'après le théorème de Riesz-Fischer, l'espace $L^2(\mathbb{R})$ est un espace de Banach (il est complet).
Par conséquent, la suite $(\hat{f}_n)_{n \in \mathbb{N}}$ admet une limite dans $L^2(\mathbb{R})$. On définit la transformée de Fourier de $f$, notée $\widetilde{\mathcal{F}}(f)$, comme cette limite :
$$ \widetilde{\mathcal{F}}(f) = \lim_{n \to +\infty} \hat{f}_n $$
Il reste à vérifier que cette limite ne dépend pas du choix de la suite approximante. Si $(g_n)_{n \in \mathbb{N}}$ est une autre suite de $\mathcal{S}(\mathbb{R})$ convergeant vers $f$, alors la suite mélangée $f_1, g_1, f_2, g_2, \dots$ converge vers $f$ et est de Cauchy, donc la suite de ses transformées converge, imposant $\lim \hat{f}_n = \lim \hat{g}_n$.
Enfin, la norme passant à la limite, $\|\widetilde{\mathcal{F}}(f)\|_2 = \lim \|\hat{f}_n\|_2 = \lim \sqrt{2\pi}\|f_n\|_2 = \sqrt{2\pi}\|f\|_2$. L'isométrie est ainsi étendue à $L^2(\mathbb{R})$ tout entier.

## 4. Applications en Physique, Logique et Intelligence Artificielle

L'opérateur de transformée de Fourier sur $L^2(\mathbb{R})$ est l'outil fondateur du traitement du signal et, par extension, d'une grande partie des réseaux de neurones modernes traitant l'audio ou les séries temporelles.

Le théorème de Plancherel y joue un rôle conceptuel fondamental car il établit que l'énergie totale d'un signal dans le domaine temporel est strictement conservée lors du passage dans le domaine fréquentiel (Densité Spectrale de Puissance). L'apprentissage des caractéristiques (features) peut donc se faire sans perte d'information énergétique.
Dans les réseaux de neurones, la contrainte de norme spectrale (Spectral Normalization), utilisée notamment pour stabiliser la fonction d'apprentissage des réseaux génératifs adverses (GANs), s'appuie directement sur cette isométrie. En bornant la norme $L^2$ de la transformée de Fourier de l'opérateur de convolution du réseau, on garantit que celui-ci est lipschitzien globalement sur $L^2(\mathbb{R})$, empêchant la divergence de l'optimisation par rétropropagation du gradient.

L'isométrie de Plancherel garantit également que le produit scalaire (et donc la notion d'angle entre deux signaux, ou la similarité cosinus) est préservé, ce qui est crucial lors du calcul des couches d'attention (Self-Attention) appliquées sur des embeddings fréquentiels.

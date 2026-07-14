---
uuid: "jalon-17"
title: "Séries absolument convergentes, semi-convergentes et produit de Cauchy de deux séries"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/calcul-series
prev: "[[Jalon-16.md]]"
next: "[[Jalon 18 (Continuité des fonctions d'une variable réelle).md]]"
---

# Jalon 17 : Séries absolument convergentes, semi-convergentes et produit de Cauchy de deux séries


## 1. Intuition et genèse du concept

Au commencement, les mathématiciens manipulaient l'infini avec la hardiesse de l'innocence. Ils additionnaient des termes positifs et négatifs, permutant les signes comme s'il s'agissait de sommes finies, portés par l'intuition que l'algèbre de l'infini ne devait être que le prolongement naturel de l'algèbre du fini. Mais cette insouciance allait se heurter à un mur conceptuel.

La genèse historique de la convergence absolue et de la semi-convergence trouve ses racines dans les paradoxes vertigineux rencontrés par les mathématiciens du XVIIIe siècle, notamment Euler et plus tard Cauchy et Riemann. À cette époque, on manipulait les séries infinies (des sommes ne s'arrêtant jamais) avec l'intuition naïve qu'elles se comportaient exactement comme des sommes finies. Or, lorsque les termes d'une série alternent entre des valeurs positives et négatives, l'édifice intuitif s'effondre.

L'étude des séries a révélé une vérité mathématique d'une profondeur insoupçonnée : l'ordre dans lequel on additionne une infinité de termes n'est pas toujours invariant. C'est le choc de la semi-convergence. Une série peut converger vers une valeur, mais en réarrangeant simplement l'ordre de ses termes, elle peut diverger, ou converger vers n'importe quel autre réel, comme l'a magistralement démontré Bernhard Riemann.

La convergence absolue est alors née non pas comme une contrainte artificielle, mais comme la condition de survie de la commutativité et de l'associativité à l'infini. Dire qu'une série converge absolument, c'est affirmer que l'accumulation de son "énergie" globale (la somme des valeurs absolues) est finie. Cette propriété garantit que la série est intrinsèquement stable. Ainsi, la distinction entre convergence simple et convergence absolue est la frontière entre ce qui est algébriquement robuste (les sommes inconditionnelles) et ce qui est infiniment fragile (les compensations miracles entre termes de signes opposés).

Pour retrouver la sécurité des opérations algébriques classiques (réarranger les termes, multiplier deux séries entre elles), Cauchy a introduit le concept salvateur de convergence absolue. Une série est absolument convergente si elle continue de converger même lorsqu'on remplace tous ses termes négatifs par des termes positifs. Si elle passe ce test de robustesse extrême, alors elle se comporte comme une somme finie ordinaire.


## 2. Formalisation et structures algébriques


\begin{center}
\begin{tikzpicture}[scale=1.5]
  % Axe des réels
  \draw[->,thick] (-1,0) -- (5,0) node[right] {$\mathbb{R}$};
  \draw (0,-0.1) -- (0,0.1) node[above] {$0$};

  % Trajet d'une série absolument convergente
  \draw[->, blue, thick] (0,-0.2) to[out=-45,in=-135] (1.5,-0.2);
  \draw[->, blue, thick] (1.5,-0.2) to[out=-45,in=-135] (2.2,-0.2);
  \draw[->, blue, thick] (2.2,-0.2) to[out=-45,in=-135] (2.6,-0.2);
  \node[blue] at (2.6,-0.4) {$S_{abs}$};
  \node[blue] at (1.5, -0.6) {Mouvements amortis garantis};

  % Trajet d'une série semi-convergente (allers-retours compensatoires)
  \draw[->, red, thick] (0,0.2) to[out=45,in=135] (4,0.2);
  \draw[->, red, thick] (4,0.2) to[out=135,in=45] (1,0.2);
  \draw[->, red, thick] (1,0.2) to[out=45,in=135] (3,0.2);
  \draw[->, red, thick] (3,0.2) to[out=135,in=45] (1.5,0.2);
  \draw[->, red, thick] (1.5,0.2) to[out=45,in=135] (2.5,0.2);
  \node[red] at (2.5,0.6) {Compensations précaires $S_{semi}$};
\end{tikzpicture}
\end{center}



### A. Énoncé Symbolique Strict

Soit $(u_n)_{n \in \mathbb{N}}$ une suite d'éléments à valeurs dans le corps $\mathbb{K}$ (où $\mathbb{K}$ désigne $\mathbb{R}$ ou $\mathbb{C}$).

**Définition 1 : Convergence absolue**
On dit que la série $\sum u_n$ est absolument convergente si la série des valeurs absolues (ou des modules) $\sum |u_n|$ est convergente dans $\mathbb{R}^+$.
Symboliquement :
$\sum_{n=0}^\infty |u_n| < +\infty \implies \sum u_n$ est absolument convergente.

**Définition 2 : Semi-convergence**
On dit que la série $\sum u_n$ est semi-convergente si :
1. $\sum u_n$ est convergente dans $\mathbb{K}$.
2. $\sum |u_n|$ est divergente dans $\mathbb{R}^+$.

**Définition 3 : Produit de Cauchy de deux séries**
Soient $\sum a_n$ et $\sum b_n$ deux séries à termes dans $\mathbb{K}$. On définit la série produit de Cauchy, notée $\sum c_n$, par la suite de terme général $c_n$ définie pour tout $n \in \mathbb{N}$ par :
$$c_n = \sum_{k=0}^n a_k b_{n-k}$$

### B. Anatomie et Typage Chirurgical

- $\mathbb{K}$ : Le corps de base. Il s'agit d'un espace de Banach complet. La notion de valeur absolue $| \cdot |$ correspond à la valeur absolue standard sur $\mathbb{R}$ ou au module usuel sur $\mathbb{C}$.
- $(u_n)$ : Suite indexée par $n \in \mathbb{N}$. Chaque terme $u_n$ possède un signe (ou une phase en complexe) qui peut fluctuer arbitrairement.
- $\sum |u_n|$ : Étant une série à termes réels positifs ou nuls, l'étude de la convergence absolue se ramène aux théorèmes du Jalon 16 (comparaison, équivalents, d'Alembert, Cauchy). Sa suite des sommes partielles est obligatoirement croissante.
- $c_n = \sum_{k=0}^n a_k b_{n-k}$ : Cette formule correspond exactement à la convolution discrète $(a \ast b)[n]$. L'indice $k$ parcourt l'ensemble des entiers de $0$ à $n$, assurant que la somme des indices dans les facteurs vaut toujours exactement $k + (n - k) = n$.

### C. Exemples de Validation

**Exemple trivial (Convergence Absolue) :**
La série géométrique de terme général $u_n = \frac{(-1)^n}{2^n}$.
On a $|u_n| = \frac{1}{2^n} = (\frac{1}{2})^n$. Puisque $1/2 < 1$, la série géométrique $\sum (1/2)^n$ converge (elle vaut $\frac{1}{1 - 1/2} = 2$). Par conséquent, la série $\sum u_n$ est absolument convergente.

**Exemple complexe (Semi-convergence) :**
La série harmonique alternée $u_n = \frac{(-1)^n}{n}$ pour $n \ge 1$.
La série des valeurs absolues est $\sum \frac{1}{n}$, qui est la série harmonique (divergente vers $+\infty$). Elle ne converge donc pas absolument. Cependant, par le critère spécial des séries alternées (théorème de Leibniz, car $1/n \to 0$ en décroissant), la série $\sum \frac{(-1)^n}{n}$ converge vers $-\ln(2)$. Elle est donc strictement semi-convergente.

### D. Cas Pathologiques et Contre-exemples

**Le piège de Mertens (Divergence du Produit de Cauchy de séries semi-convergentes) :**
On pourrait naïvement espérer que si $\sum a_n$ converge et $\sum b_n$ converge, alors leur produit de Cauchy $\sum c_n$ converge vers le produit des sommes.
C'est **faux**. Prenons $a_n = b_n = \frac{(-1)^n}{\sqrt{n+1}}$. Ces deux séries convergent (critère alterné). Pourtant, nous prouverons en exercice que le terme général de leur produit de Cauchy $c_n$ ne tend même pas vers 0 ! Ainsi, sans la convergence absolue, le produit de Cauchy n'a aucune garantie algébrique.

## 3. Démonstrations pas-à-pas

### A. Théorème 1 : La convergence absolue implique la convergence

**Énoncé :** Soit $(u_n)$ une suite à valeurs dans $\mathbb{K}$ (complet). Si $\sum |u_n|$ converge, alors $\sum u_n$ converge.

**Démonstration détaillée  :**
1. La complétude du corps $\mathbb{K}$ implique que pour prouver la convergence de la série $\sum u_n$, il suffit de démontrer que la suite de ses sommes partielles $S_N = \sum_{k=0}^N u_k$ est une suite de Cauchy.
2. Soit $\epsilon \in \mathbb{R}_+^*$ fixé arbitrairement.
3. Par hypothèse, la série $\sum |u_n|$ converge. Ses sommes partielles $T_N = \sum_{k=0}^N |u_k|$ forment donc une suite convergente.
4. Toute suite convergente dans $\mathbb{R}$ est une suite de Cauchy. Par conséquent, pour la suite $(T_N)$, il existe un rang $N_0 \in \mathbb{N}$ tel que pour tous entiers $p \ge q \ge N_0$, on ait :
   $$|T_p - T_{q-1}| = T_p - T_{q-1} = \sum_{k=q}^p |u_k| < \epsilon$$
5. Considérons maintenant la différence des sommes partielles de la série d'origine $S_p - S_{q-1}$, pour ces mêmes $p \ge q \ge N_0$ :
   $$|S_p - S_{q-1}| = \left| \sum_{k=q}^p u_k \right|$$
6. D'après l'inégalité triangulaire généralisée dans $\mathbb{K}$, la norme (ou module) d'une somme est inférieure ou égale à la somme des normes :
   $$\left| \sum_{k=q}^p u_k \right| \le \sum_{k=q}^p |u_k|$$
7. En combinant les résultats de l'étape 4 et de l'étape 6, nous obtenons que pour tous $p \ge q \ge N_0$ :
   $$|S_p - S_{q-1}| \le \sum_{k=q}^p |u_k| < \epsilon$$
8. Ceci démontre rigoureusement que la suite $(S_N)$ vérifie le critère de Cauchy dans $\mathbb{K}$.
9. Puisque $\mathbb{K}$ est un espace complet, toute suite de Cauchy y est convergente. Donc la série $\sum u_n$ converge. $\blacksquare$

### B. Théorème 2 : Théorème de Mertens sur le Produit de Cauchy

**Énoncé :** Soient $\sum a_n$ et $\sum b_n$ deux séries réelles ou complexes. Si $\sum a_n$ converge absolument et $\sum b_n$ converge, alors leur produit de Cauchy $\sum c_n$ (avec $c_n = \sum_{k=0}^n a_k b_{n-k}$) converge, et on a :
$$\sum_{n=0}^\infty c_n = \left( \sum_{n=0}^\infty a_n \right) \times \left( \sum_{n=0}^\infty b_n \right)$$

**Démonstration détaillée  :**
1. Fixons les notations. Posons :
   $A_N = \sum_{n=0}^N a_n$, $A = \lim_{N\to\infty} A_N$
   $B_N = \sum_{n=0}^N b_n$, $B = \lim_{N\to\infty} B_N$
   $C_N = \sum_{n=0}^N c_n$
   Nous voulons prouver que $\lim_{N\to\infty} C_N = A \times B$.
2. Exprimons $C_N$ en développant sa définition :
   $C_N = \sum_{n=0}^N c_n = \sum_{n=0}^N \left( \sum_{k=0}^n a_k b_{n-k} \right)$.
3. Réorganisons la double somme en sommant selon les colonnes (interversion de sommes finies, toujours licite). Le couple d'indices $(n, k)$ vérifie $0 \le n \le N$ et $0 \le k \le n$, ce qui est équivalent à $0 \le k \le N$ et $k \le n \le N$.
   Ainsi, $C_N = \sum_{k=0}^N a_k \left( \sum_{n=k}^N b_{n-k} \right)$.
4. Dans la somme intérieure, effectuons le changement d'indice $j = n-k$. Lorsque $n$ varie de $k$ à $N$, $j$ varie de $0$ à $N-k$.
   $C_N = \sum_{k=0}^N a_k \left( \sum_{j=0}^{N-k} b_j \right) = \sum_{k=0}^N a_k B_{N-k}$.
5. Introduisons le reste partiel de la suite $(B_N)$ par rapport à sa limite $B$. Définissons $\beta_m = B_m - B$. Par hypothèse, $\lim_{m\to\infty} \beta_m = 0$. On peut alors écrire $B_{N-k} = B + \beta_{N-k}$.
6. Injectons cette décomposition dans $C_N$ :
   $C_N = \sum_{k=0}^N a_k (B + \beta_{N-k}) = B \sum_{k=0}^N a_k + \sum_{k=0}^N a_k \beta_{N-k}$.
   $C_N = B A_N + \sum_{k=0}^N a_k \beta_{N-k}$.
7. Puisque $\lim_{N\to\infty} B A_N = B \times A$, il suffit de démontrer que le terme de reste $R_N = \sum_{k=0}^N a_k \beta_{N-k}$ tend vers $0$ lorsque $N \to \infty$.
8. C'est ici que l'hypothèse de **convergence absolue** de $\sum a_n$ est fondamentale. Posons $M = \sum_{n=0}^\infty |a_n| < +\infty$.
   De plus, la suite $(\beta_n)$ convergeant vers $0$, elle est bornée. Il existe $K \in \mathbb{R}^+$ tel que $|\beta_n| \le K$ pour tout $n \in \mathbb{N}$.
9. Soit $\epsilon > 0$. Puisque $\lim_{n\to\infty} \beta_n = 0$, il existe un entier $N_1 \in \mathbb{N}$ tel que pour tout $n > N_1$, $|\beta_n| < \frac{\epsilon}{2M}$.
   Puisque $\sum |a_n|$ converge, son reste tend vers $0$. Il existe un entier $N_2 \in \mathbb{N}$ tel que pour tout $N > N_2$, $\sum_{k=N_2+1}^N |a_k| < \frac{\epsilon}{2K}$.
10. Prenons $N > N_1 + N_2$. Coupons la somme $R_N$ en deux parties (autour de l'indice $N - N_1$) :
    $|R_N| = \left| \sum_{k=0}^N a_k \beta_{N-k} \right| \le \sum_{k=0}^N |a_k| |\beta_{N-k}|$.
    $|R_N| \le \sum_{k=0}^{N-N_1-1} |a_k| |\beta_{N-k}| + \sum_{k=N-N_1}^N |a_k| |\beta_{N-k}|$.
11. Dans la première somme, on a $k \le N - N_1 - 1$, donc $N - k \ge N_1 + 1 > N_1$. Ainsi, $|\beta_{N-k}| < \frac{\epsilon}{2M}$.
    D'où : $\sum_{k=0}^{N-N_1-1} |a_k| |\beta_{N-k}| \le \frac{\epsilon}{2M} \sum_{k=0}^{N-N_1-1} |a_k| \le \frac{\epsilon}{2M} \sum_{k=0}^\infty |a_k| = \frac{\epsilon}{2M} M = \frac{\epsilon}{2}$.
12. Dans la seconde somme, on majore grossièrement $|\beta_{N-k}|$ par $K$. De plus, comme $N > N_1 + N_2$, on a $N - N_1 > N_2$.
    D'où : $\sum_{k=N-N_1}^N |a_k| |\beta_{N-k}| \le K \sum_{k=N-N_1}^N |a_k| \le K \sum_{k=N_2+1}^N |a_k| < K \frac{\epsilon}{2K} = \frac{\epsilon}{2}$.
13. En additionnant, on obtient que pour tout $N > N_1 + N_2$, $|R_N| < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$.
    Donc $\lim_{N\to\infty} R_N = 0$.
14. Par conséquent, $\lim_{N\to\infty} C_N = A B + 0 = A B$. Le théorème de Mertens est démontré. $\blacksquare$

## 4. Exercices d\'application et de concours
*Voir les fichiers séparés dans le répertoire `exos/` pour l'exhaustivité.*

## 5. Travaux pratiques et simulations algorithmiques

### Convolution de Réseaux Neuronaux et Signaux
Dans l'architecture mathématique des réseaux de neurones (particulièrement les CNN - *Convolutional Neural Networks* - pour l'audio 1D ou l'image 2D), l'opération clé est la convolution discrète entre le tenseur d'entrée et le noyau de convolution (le filtre d'apprentissage).

La définition du produit de Cauchy $c_n = \sum_{k=0}^n a_k b_{n-k}$ est **l'exacte formulation mathématique** de la convolution discrète $(a \ast b)[n]$.

La convergence de ce produit de Cauchy garantit un concept crucial en traitement du signal et en IA : le critère de stabilité **BIBO** (*Bounded-Input Bounded-Output*). Un filtre $h$ est BIBO-stable si, pour toute entrée bornée $x$, la sortie $y = h \ast x$ est également bornée. La théorie des séries démontre qu'un système discret, linéaire et invariant dans le temps est BIBO-stable **si et seulement si** la réponse impulsionnelle du filtre $h_n$ forme une série **absolument convergente** (c'est-à-dire $\sum_{n=-\infty}^\infty |h_n| < \infty$).
C'est précisément l'absolue convergence qui prévient les gradients explosifs dans les architectures de filtrage récursif ou les RNN de bas niveau.

## 6. Liens Sémantiques \& Maillage Obsidian
- **Concepts Précédents requis :** [[Jalon 14 (Suites réelles et complexes)]], [[Jalon-16]]
- **Concepts Futurs dépendants :** [[Jalon 23 (Séries entières)]], [[Jalon 80 (Transformée de Fourier dans L$^1$)]], [[Jalon 126 (Noyaux définis positifs)]]

---
uuid: "jalon-25"
title: "Formes bilinéaires, formes sesquilinieaires, produit scalaire et inégalité de Cauchy-Schwarz"
year: 1
trimester: 3
tags:
  - math/algebre-lineaire
  - ia/similarite
prev: "[[Jalon-24.md]]"
next: "[[Jalon 26 (Espaces euclidiens).md]]"
---

# Partie 1 : Intuition et Genèse


Historiquement, la notion de mesure, de distance et d'angle a d'abord émergé dans l'espace physique euclidien en dimension 2 et 3. Cependant, l'algèbre linéaire moderne, propulsée par les travaux de mathématiciens comme Peano et Banach, a nécessité une généralisation radicale : comment définir la "proximité" ou "l'orthogonalité" de deux objets abstraits, par exemple deux polynômes ou deux fonctions continues ? C'est ici qu'intervient la forme bilinéaire.
En tant que concept, la forme bilinéaire agit comme une passerelle entre l'algèbre pure (la linéarité) et la géométrie (la métrique). Imaginez une machine qui absorbe deux vecteurs et crache un nombre scalaire mesurant leur "degré d'interaction". Si ce nombre est nul, les vecteurs s'ignorent totalement (ils sont orthogonaux). Si le nombre est maximal (relativement à leurs tailles respectives), ils sont intimement liés (colinéaires). Ce mécanisme universel permet de projeter n'importe quel espace vectoriel, si abstrait soit-il, dans notre intuition géométrique la plus primale.

```latex
\begin{tikzpicture}[scale=1.5]
  \coordinate (O) at (0,0);
  \coordinate (U) at (3,1);
  \coordinate (V) at (1,2.5);
  \coordinate (P) at (1.5,0.5);

  \draw[->, thick, blue] (O) -- (U) node[right] {$\vec{u}$};
  \draw[->, thick, red] (O) -- (V) node[above left] {$\vec{v}$};
  \draw[->, thick, dashed, purple] (O) -- (P) node[below right] {$P_{\vec{u}}(\vec{v})$};
  \draw[dashed, thick, gray] (V) -- (P);

  \tkzMarkRightAngle[size=0.2,fill=gray!20](V,P,O);
\end{tikzpicture}
```

La magie s'opère réellement avec l'Inégalité de Cauchy-Schwarz. Découverte initialement par Augustin-Louis Cauchy pour des sommes finies en 1821, puis étendue aux intégrales par Viktor Bunyakovsky en 1859 et enfin formulée pour les espaces préhilbertiens par Hermann Amandus Schwarz en 1885, cette inégalité borne la valeur absolue de cette interaction. Elle stipule, avec une rigueur implacable, que "l'ombre géométrique" (la projection) d'un vecteur sur un autre ne pourra jamais excéder la longueur intrinsèque de ce vecteur.


# Partie 2 : Formalisation


Soit $\mathbb{K}$ un corps commutatif (généralement $\mathbb{R}$ ou $\mathbb{C}$). Soit $E$ un $\mathbb{K}$-espace vectoriel.

**Définition 1 : Forme bilinéaire**
Une application $\phi : E \times E \to \mathbb{K}$ est une forme bilinéaire si elle est linéaire par rapport à chacune de ses variables. C'est-à-dire, pour tout $x, y, z \in E$ et tout $\lambda, \mu \in \mathbb{K}$ :
1. Linéarité à gauche : $\phi(\lambda x + \mu y, z) = \lambda \phi(x, z) + \mu \phi(y, z)$
2. Linéarité à droite : $\phi(x, \lambda y + \mu z) = \lambda \phi(x, y) + \mu \phi(x, z)$

*Exemple canonique :* Sur $E = \mathbb{R}^n$, l'application $\phi(x, y) = \sum_{i=1}^n x_i y_i$ est une forme bilinéaire.
*Cas pathologique :* L'application nulle $\phi(x, y) = 0$ est bilinéaire, mais elle est complètement dégénérée et n'apporte aucune structure géométrique intéressante.

**Définition 2 : Forme symétrique et antisymétrique**
Une forme bilinéaire $\phi$ sur un $\mathbb{R}$-espace vectoriel est dite symétrique si $\forall (x, y) \in E^2, \phi(x, y) = \phi(y, x)$. Elle est dite antisymétrique si $\forall (x, y) \in E^2, \phi(x, y) = -\phi(y, x)$.

**Définition 3 : Forme sesquilinéaire (Cas complexe)**
Si $\mathbb{K} = \mathbb{C}$, on utilise des formes sesquilinéaires. L'application $\phi : E \times E \to \mathbb{C}$ est linéaire à droite et semi-linéaire à gauche :
$\phi(\lambda x + \mu y, z) = \overline{\lambda} \phi(x, z) + \overline{\mu} \phi(y, z)$ (convention française, semi-linéarité à gauche).

**Définition 4 : Produit Scalaire (Cas Réel)**
Un produit scalaire sur un $\mathbb{R}$-espace vectoriel $E$ est une forme bilinéaire $\langle \cdot, \cdot \rangle$ qui est :
1. **Symétrique :** $\langle x, y \rangle = \langle y, x \rangle$
2. **Positive :** $\forall x \in E, \langle x, x \rangle \ge 0$
3. **Définie :** $\forall x \in E, \langle x, x \rangle = 0 \implies x = 0_E$.

**Définition 5 : Espace Préhilbertien et Euclidien**
Un $\mathbb{R}$-espace vectoriel muni d'un produit scalaire est appelé un espace préhilbertien réel. S'il est de dimension finie, c'est un espace euclidien. S'il est de dimension infinie et complet pour la norme induite, c'est un espace de Hilbert.


# Partie 3 : Démonstrations pas-à-pas


**Théorème (Inégalité de Cauchy-Schwarz)**
Soit $(E, \langle \cdot, \cdot \rangle)$ un espace préhilbertien réel. Pour tout $(x, y) \in E^2$, on a :
\[ | \langle x, y \rangle | \le \sqrt{\langle x, x \rangle} \sqrt{\langle y, y \rangle} \]
soit $| \langle x, y \rangle | \le \|x\| \|y\|$.
L'égalité a lieu si et seulement si la famille $(x, y)$ est liée.

**Démonstration (Zéro Ellipse) :**
Fixons $x, y \in E$. Nous allons utiliser la positivité du produit scalaire sur des combinaisons linéaires de $x$ et $y$.
Si $x = 0_E$, alors par bilinéarité $\langle 0_E, y \rangle = \langle 0 \cdot 0_E, y \rangle = 0 \cdot \langle 0_E, y \rangle = 0$. De même $\|x\| = 0$. On a donc $0 \le 0 \times \|y\|$, l'inégalité est vérifiée et la famille $(0_E, y)$ est bien liée.

Supposons désormais $x \neq 0_E$. Considérons le vecteur paramétré $z(\lambda) = y - \lambda x$ pour un réel $\lambda \in \mathbb{R}$ quelconque.
Par définition d'un produit scalaire, la forme est positive. Donc pour tout $\lambda \in \mathbb{R}$ :
\[ \langle z(\lambda), z(\lambda) \rangle \ge 0 \]
Développons cette expression en utilisant la bilinéarité et la symétrie :
\[ \langle y - \lambda x, y - \lambda x \rangle = \langle y, y \rangle - \lambda \langle y, x \rangle - \lambda \langle x, y \rangle + \lambda^2 \langle x, x \rangle \]
Puisque le produit scalaire est symétrique ($\langle x, y \rangle = \langle y, x \rangle$), on obtient :
\[ \|x\|^2 \lambda^2 - 2 \langle x, y \rangle \lambda + \|y\|^2 \ge 0 \]
Soit $P(\lambda) = a\lambda^2 + b\lambda + c$ avec $a = \|x\|^2$, $b = -2\langle x, y \rangle$ et $c = \|y\|^2$.
Puisque $x \neq 0_E$, on a $a = \|x\|^2 > 0$ (car le produit scalaire est défini positif). $P(\lambda)$ est un trinôme du second degré à coefficients réels.
Puisque ce trinôme est positif ou nul pour tout $\lambda \in \mathbb{R}$, il ne peut pas admettre deux racines réelles distinctes, sinon il changerait de signe (il serait négatif entre les racines puisque $a > 0$).
Par conséquent, son discriminant réduit (ou discriminant classique) doit être inférieur ou égal à zéro.
Calculons le discriminant :
\[ \Delta = b^2 - 4ac = (-2\langle x, y \rangle)^2 - 4 \|x\|^2 \|y\|^2 \]
\[ \Delta = 4 \langle x, y \rangle^2 - 4 \|x\|^2 \|y\|^2 \]
Imposons $\Delta \le 0$ :
\[ 4 \langle x, y \rangle^2 - 4 \|x\|^2 \|y\|^2 \le 0 \]
En divisant par $4$ :
\[ \langle x, y \rangle^2 \le \|x\|^2 \|y\|^2 \]
Puisque la fonction racine carrée est croissante sur $\mathbb{R}_+$, on obtient :
\[ | \langle x, y \rangle | \le \|x\| \|y\| \]
Ceci achève la preuve de l'inégalité de Cauchy-Schwarz.

**Cas d'égalité :**
Supposons que l'égalité soit vérifiée : $| \langle x, y \rangle | = \|x\| \|y\|$. Alors $\Delta = 0$. Le trinôme $P(\lambda)$ admet une unique racine double $\lambda_0 \in \mathbb{R}$.
Cela signifie qu'il existe un $\lambda_0$ tel que $P(\lambda_0) = 0$, c'est-à-dire $\langle y - \lambda_0 x, y - \lambda_0 x \rangle = 0$.
Puisque le produit scalaire est défini, la seule façon qu'un vecteur ait une norme nulle est qu'il soit le vecteur nul :
\[ y - \lambda_0 x = 0_E \implies y = \lambda_0 x \]
Ceci démontre que la famille $(x, y)$ est liée, établissant complètement le théorème.

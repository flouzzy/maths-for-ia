# Exercice 10 : Égalité fondamentale des normes $\bigstar\bigstar\bigstar\bigstar\bigstar$
## Énoncé
Soit $H$ un espace de Hilbert et $T \in \mathcal{L}(H)$ un opérateur linéaire continu.
L'objectif de cet exercice est de démontrer la propriété de $C^*$-algèbre liant la norme de l'opérateur et la norme de son adjoint :
$$ \|T^* T\| = \|T\|^2 $$
Rappelons que la norme d'un opérateur linéaire borné est définie par $\|A\| = \sup_{\|x\|=1} \|Ax\|$.
1. Montrer l'inégalité de Cauchy-Schwarz généralisée pour les opérateurs : $\|T^* T\| \le \|T^*\| \|T\|$.
2. Démontrer, en utilisant le produit scalaire et l'inégalité de Cauchy-Schwarz vectorielle classique, que $\|T\|^2 \le \|T^* T\|$.
3. Montrer que $\|T^*\| = \|T\|$ et conclure sur l'égalité demandée.

## Correction
1. La norme d'un produit d'opérateurs continus est sous-multiplicative, car pour tout vecteur $x \in H$ de norme 1 :
$$ \|T^* T x\| \le \|T^*\| \cdot \|Tx\| \le \|T^*\| \cdot (\|T\| \cdot \|x\|) = \|T^*\| \|T\| $$
En prenant le supremum sur l'ensemble des vecteurs de la sphère unité, on obtient l'inégalité pour la norme d'opérateur :
$$ \|T^* T\| \le \|T^*\| \|T\| $$

2. Considérons le carré de la norme de l'opérateur $T$ :
$$ \|T\|^2 = \left( \sup_{\|x\|=1} \|Tx\| \right)^2 = \sup_{\|x\|=1} \|Tx\|^2 $$
Pour un vecteur arbitraire $x$ de norme 1, exprimons la norme au carré de l'image $Tx$ sous la forme d'un produit scalaire :
$$ \|Tx\|^2 = \langle Tx, Tx \rangle $$
Par définition de l'opérateur adjoint $T^*$, nous pouvons déplacer $T$ du premier argument du produit scalaire vers le second argument :
$$ \langle Tx, Tx \rangle = \langle x, T^*(Tx) \rangle = \langle x, (T^*T)x \rangle $$
Appliquons l'inégalité de Cauchy-Schwarz classique au produit scalaire des vecteurs $x$ et $(T^*T)x$ :
$$ \langle x, (T^*T)x \rangle \le \|x\| \cdot \|(T^*T)x\| $$
Puisque le vecteur $x$ a une norme égale à 1 par construction ($\|x\|=1$) :
$$ \le 1 \cdot \|(T^*T)x\| = \|(T^*T)x\| $$
Par définition de la norme d'opérateur subordonnée, nous avons l'inégalité fondamentale $\|Ay\| \le \|A\|\|y\|$. En l'appliquant avec l'opérateur $A = T^*T$ et le vecteur $y = x$ (toujours de norme 1) :
$$ \|(T^*T)x\| \le \|T^*T\| \cdot \|x\| = \|T^*T\| \cdot 1 = \|T^*T\| $$
En rassemblant cette chaîne d'inégalités pour un $x$ unitaire quelconque, nous avons établi rigoureusement que :
$$ \|Tx\|^2 \le \|T^*T\| $$
Comme cette borne supérieure ne dépend pas de $x$ (tant qu'il est sur la sphère unité), elle est valide pour le supremum lui-même. Par passage au supremum, on obtient :
$$ \sup_{\|x\|=1} \|Tx\|^2 \le \|T^*T\| \implies \|T\|^2 \le \|T^*T\| $$

3. Nous devons maintenant prouver que $\|T^*\| = \|T\|$.
En vertu de l'inégalité démontrée à l'étape 2 ( $\|T\|^2 \le \|T^*T\|$ ) combinée avec la sous-multiplicativité de l'étape 1 ( $\|T^*T\| \le \|T^*\|\|T\|$ ), nous formons la chaîne :
$$ \|T\|^2 \le \|T^*T\| \le \|T^*\| \|T\| $$
Si $T = 0$, la propriété $\|T^*\| = \|T\|$ est trivialement vraie.
Supposons donc que $T$ n'est pas l'opérateur nul, ce qui implique strictement que $\|T\| > 0$. On peut alors diviser l'inégalité totale par $\|T\|$ :
$$ \|T\| \le \|T^*\| $$
Comme l'opérateur adjoint est défini de manière parfaitement symétrique, cette inégalité mathématique est universellement valable pour n'importe quel opérateur linéaire continu, y compris pour l'opérateur $T^*$.
En remplaçant formellement $T$ par $T^*$ dans cette même inégalité générique, on obtient :
$$ \|T^*\| \le \|(T^*)^*\| $$
Or, par involution double, l'adjoint de l'adjoint est l'opérateur initial, c'est-à-dire $(T^*)^* = T$. L'inégalité devient donc :
$$ \|T^*\| \le \|T\| $$
Nous avons démontré simultanément que $\|T\| \le \|T^*\|$ et $\|T^*\| \le \|T\|$. La seule issue mathématique possible pour ces deux nombres réels est l'égalité stricte :
$$ \|T^*\| = \|T\| $$
Enfin, revenons à la chaîne d'inégalités du début de cette section :
$$ \|T\|^2 \le \|T^*T\| \le \|T^*\| \|T\| $$
Puisque nous venons de substituer $\|T^*\|$ par $\|T\|$, le terme le plus à droite devient exactement $\|T\| \cdot \|T\| = \|T\|^2$. La chaîne devient :
$$ \|T\|^2 \le \|T^*T\| \le \|T\|^2 $$
Pris en tenaille (théorème des gendarmes), le terme central n'a d'autre choix que d'être strictement égal aux limites encadrantes. L'égalité structurelle est formellement démontrée :
$$ \|T^*T\| = \|T\|^2 $$

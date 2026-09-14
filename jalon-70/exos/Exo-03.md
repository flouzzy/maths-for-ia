# Exercice 3 : Aire d'un parallélogramme par sections (★★☆☆☆)

**Énoncé :**
On considère la mesure de Lebesgue produit sur $\mathbb{R}^2$, notée $\lambda_2 = \lambda \otimes \lambda$.
Soit le parallélogramme $P$ délimité par les droites $y = 0$, $y = 1$, $y = x$, et $y = x - 2$.
En utilisant la méthode d'intégration par sections, calculer la mesure de $P$.

**Correction :**
1. L'ensemble $P$ est un borélien car délimité par des droites continues.
   Il est défini par les conditions : $0 \leq y \leq 1$ et $y \leq x \leq y + 2$.
2. Nous devons calculer $\lambda_2(P) = \int \lambda(P_x) \, dx$ ou $\int \lambda(P^y) \, dy$.
   Ici, l'intégration selon les sections en $y$ (horizontales) est beaucoup plus naturelle.
   Fixons $y \in \mathbb{R}$.
   - Si $y \notin [0,1]$, alors la section $P^y = \emptyset$, d'où $\lambda(P^y) = 0$.
   - Si $y \in [0,1]$, l'ensemble des $x$ vérifiant les conditions est $x \in [y, y+2]$.
   La section en $y$ est donc l'intervalle $P^y = [y, y+2]$.
3. Calculons la mesure (longueur) de cette section :
   Pour $y \in [0,1]$, $\lambda(P^y) = (y+2) - y = 2$.
4. D'après le théorème de la mesure produit (qui préfigure le théorème de Fubini-Tonelli) :
   $\lambda_2(P) = \int_{\mathbb{R}} \lambda(P^y) \, d\lambda(y) = \int_0^1 2 \, dy = [2y]_0^1 = 2 - 0 = 2$.
   L'aire du parallélogramme est bien 2 (base 2, hauteur 1).

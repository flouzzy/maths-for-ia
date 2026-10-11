# Exercice 7

\subsection*{Exercice 7 : Produit de variables absolument continues \quad $\bigstar\bigstar\bigstar\bigstar\star$}

**Énoncé :**
Soient $X$ et $Y$ deux variables aléatoires indépendantes de densités respectives $f_X$ et $f_Y$.
Montrer que la densité de probabilité de leur produit $Z = XY$ (en supposant $X > 0, Y > 0$) est donnée par :
$f_Z(z) = \int_{0}^{+\infty} f_X(x) f_Y\left(\frac{z}{x}\right) \frac{1}{x} dx \quad \text{pour } z > 0$

**Correction :**
1. La fonction de répartition de $Z$ pour $z > 0$ est $F_Z(z) = P(Z \le z) = P(XY \le z)$.
2. Puisque $X$ et $Y$ sont indépendantes et continues, leur densité conjointe est $f_{X,Y}(x,y) = f_X(x)f_Y(y)$.
3. On exprime la probabilité comme l'intégrale de la densité conjointe sur le domaine $D = \{(x,y) \in \mathbb{R}_+^2 \mid xy \le z\}$ :
   $F_Z(z) = \iint_{D} f_X(x)f_Y(y) dx dy = \int_{0}^{+\infty} \left( \int_{0}^{z/x} f_X(x)f_Y(y) dy \right) dx$.
4. On dérive $F_Z(z)$ par rapport à $z$ pour obtenir la densité $f_Z(z)$.
5. Par le théorème de dérivation sous le signe intégral (les hypothèses de domination étant supposées vérifiées ici), on dérive l'intégrale interne :
   $f_Z(z) = \frac{d}{dz} \int_{0}^{+\infty} f_X(x) \left( \int_{0}^{z/x} f_Y(y) dy \right) dx$.
6. La dérivée par rapport à $z$ de l'intégrale $\int_{0}^{z/x} f_Y(y) dy$ est $f_Y\left(\frac{z}{x}\right) \cdot \frac{\partial}{\partial z}\left(\frac{z}{x}\right)$.
7. La dérivée de $\frac{z}{x}$ par rapport à $z$ est $\frac{1}{x}$.
8. Ainsi, on obtient :
   $f_Z(z) = \int_{0}^{+\infty} f_X(x) f_Y\left(\frac{z}{x}\right) \frac{1}{x} dx$.
9. Cette formule s'applique pour déterminer la distribution de produits (par exemple pour la loi de Fisher, issue du ratio d'un produit).

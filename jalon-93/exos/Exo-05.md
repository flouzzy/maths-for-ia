# Exercice 05 : Variable de Rademacher et Marche Aléatoire
Difficulté : $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $X$ une variable de Rademacher, telle que $P(X = 1) = \frac{1}{2}$ et $P(X = -1) = \frac{1}{2}$.
1. Calculer la fonction caractéristique de $X$.
2. Soient $X_1, \dots, X_n$ i.i.d. de loi de Rademacher. On pose $S_n = \frac{1}{\sqrt{n}} \sum_{k=1}^n X_k$.
Calculer $\phi_{S_n}(t)$ et trouver sa limite quand $n \to +\infty$.

**Correction pas à pas :**
1. $\phi_X(t) = \mathbb{E}[e^{itX}] = \frac{1}{2} e^{it(1)} + \frac{1}{2} e^{it(-1)} = \frac{e^{it} + e^{-it}}{2} = \cos(t)$.
2. Par indépendance, la fonction caractéristique de la somme est le produit des fonctions caractéristiques.
   Et avec le facteur $\frac{1}{\sqrt{n}}$, on a :
   $\phi_{S_n}(t) = \left( \phi_X\left(\frac{t}{\sqrt{n}}\right) \right)^n = \left( \cos\left(\frac{t}{\sqrt{n}}\right) \right)^n$.
3. Pour trouver la limite quand $n \to +\infty$, passons au logarithme (pour un $n$ assez grand tel que le cosinus soit strictement positif) :
   $\ln(\phi_{S_n}(t)) = n \ln\left( \cos\left(\frac{t}{\sqrt{n}}\right) \right)$.
4. Faisons un développement limité en $u = \frac{t}{\sqrt{n}}$ au voisinage de 0.
   $\cos(u) = 1 - \frac{u^2}{2} + o(u^2)$.
   $\ln(1 + x) = x + o(x)$ pour $x \to 0$.
   Donc $\ln(\cos(u)) = \ln\left(1 - \frac{u^2}{2} + o(u^2)\right) = - \frac{u^2}{2} + o(u^2)$.
5. En remplaçant $u$ par $\frac{t}{\sqrt{n}}$ :
   $\ln(\phi_{S_n}(t)) = n \left( - \frac{t^2}{2n} + o\left(\frac{t^2}{n}\right) \right) = - \frac{t^2}{2} + o(1)$.
6. Quand $n \to +\infty$, $\ln(\phi_{S_n}(t)) \to - \frac{t^2}{2}$.
   Par continuité de l'exponentielle, $\phi_{S_n}(t) \to e^{-t^2/2}$.
7. On reconnaît la fonction caractéristique de la loi Normale $\mathcal{N}(0, 1)$. C'est une application directe du Théorème Central Limite.

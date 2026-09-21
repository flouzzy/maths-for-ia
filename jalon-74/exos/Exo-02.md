---
title: "Exercice 2 : Application des Inégalités"
difficulty: "★★☆☆☆"
---

# Exercice 2 : Application des Inégalités

**Niveau :** ★★☆☆☆

**Énoncé :**
Soit $f \in L^2([0,1])$ muni de la mesure de Lebesgue. Démontrer que $f \in L^1([0,1])$ et que $\|f\|_1 \le \|f\|_2$.

**Correction Détaillée :**
Nous devons appliquer l'inégalité de Cauchy-Schwarz (Hölder avec $p=q=2$).<br>On peut écrire $|f(x)| = |f(x)| \times 1$.<br>Soit $g(x) = 1$ pour tout $x \in [0,1]$. La fonction $g$ appartient à $L^2([0,1])$ et $\|g\|_2 = (\int_0^1 1^2 dx)^{1/2} = 1^{1/2} = 1$.<br>En appliquant Cauchy-Schwarz aux fonctions $|f|$ et $g$ sur le domaine $X = [0,1]$ :<br>$\int_0^1 |f(x) \times 1| dx \le \left( \int_0^1 |f(x)|^2 dx \right)^{1/2} \left( \int_0^1 1^2 dx \right)^{1/2}$.<br>Soit $\|f\|_1 \le \|f\|_2 \times 1 = \|f\|_2$.<br>Puisque $\|f\|_2$ est finie par hypothèse, $\|f\|_1$ l'est aussi, d'où $f \in L^1([0,1])$. Cela montre que sur un espace de mesure finie, les espaces $L^p$ s'emboîtent.

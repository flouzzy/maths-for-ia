# Exercice 02

**Difficulté :** $\bigstar\star\star\star\star$

**Énoncé :**
On lance un dé équilibré à 6 faces une infinité de fois. Soit $X_i$ le résultat du $i$-ème lancer.
Soit $Y_n = \frac{1}{n} \sum_{i=1}^n X_i^2$.
1. Exprimer $Y_n$ en fonction des résultats des lancers.
2. Montrer que $Y_n$ converge presque sûrement et calculer sa limite.

**Correction :**
1. $Y_n$ représente la moyenne empirique des carrés des résultats obtenus lors des $n$ premiers lancers.
2. Posons $Z_i = X_i^2$. Puisque les $X_i$ sont indépendants et de même loi, il en est de même pour les variables $(Z_i)$.
Calculons l'espérance de $Z_1$ :
$\mathbb{E}[Z_1] = \mathbb{E}[X_1^2] = \sum_{k=1}^6 k^2 \mathbb{P}(X_1 = k) = \frac{1}{6}(1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2) = \frac{1+4+9+16+25+36}{6} = \frac{91}{6}$.
La variable $Z_1$ prend des valeurs finies donc $\mathbb{E}[|Z_1|] = \frac{91}{6} < +\infty$.
D'après la Loi Forte des Grands Nombres appliquée à la suite $(Z_i)$, la moyenne empirique $\frac{1}{n}\sum_{i=1}^n Z_i$ converge presque sûrement vers $\mathbb{E}[Z_1]$.
Donc, $\lim_{n \to \infty} Y_n = \frac{91}{6}$ presque sûrement.

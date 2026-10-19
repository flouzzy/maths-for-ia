# Exercice 4 : Intégration de Monte-Carlo (1D)

$\bigstar\bigstar\star\star\star$

On souhaite évaluer numériquement l'intégrale $I = \int_0^1 e^{-x^2} dx$.
Soit $(U_n)_{n \geq 1}$ une suite de variables aléatoires I.I.D. suivant la loi uniforme sur $[0, 1]$.
On pose $Y_i = e^{-U_i^2}$ et $I_n = \frac{1}{n} \sum_{i=1}^n Y_i$.

1. Déterminer l'espérance $\mathbb{E}[Y_1]$.
2. En appliquant la loi forte des grands nombres, montrer que $I_n$ converge presque sûrement vers $I$.

**Correction détaillée :**

1. La variable $U_1$ suit la loi uniforme continue sur $[0, 1]$, dont la densité est $f(x) = 1$ pour $x \in [0, 1]$ et $0$ ailleurs.
   D'après le théorème de transfert, l'espérance de $Y_1 = e^{-U_1^2}$ est :
   $$ \mathbb{E}[Y_1] = \mathbb{E}[e^{-U_1^2}] = \int_{-\infty}^{+\infty} e^{-x^2} f(x) dx = \int_0^1 e^{-x^2} \times 1 dx = \int_0^1 e^{-x^2} dx = I $$
2. Les variables $Y_i = e^{-U_i^2}$ sont I.I.D. car elles sont des transformations déterministes identiques des variables I.I.D. $U_i$.
   De plus, pour tout $x \in [0, 1]$, $e^{-x^2} \in [1/e, 1]$, donc les $Y_i$ sont bornées et leur espérance est bien finie.
   On peut donc appliquer la loi forte des grands nombres à la suite $(Y_n)$ :
   $$ \frac{1}{n} \sum_{i=1}^n Y_i \xrightarrow{p.s.} \mathbb{E}[Y_1] $$
   Ce qui s'écrit exactement :
   $$ I_n \xrightarrow{p.s.} I $$
   C'est le principe fondamental de la méthode d'intégration de Monte-Carlo.

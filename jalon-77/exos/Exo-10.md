## Exercice 10 : Lemme d'Urysohn et approximation de compacts \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Le théorème de régularité des mesures de Borel-Lebesgue sur $\mathbb{R}^n$ stipule que pour tout ensemble mesurable $A$ et tout $\epsilon > 0$, il existe un fermé $F \subset A$ et un ouvert $U \supset A$ tels que $\mu(U \setminus F) < \epsilon$.
Utiliser ce résultat conjointement avec le lemme d'Urysohn (ou son équivalent métrique) pour prouver rigoureusement la densité de $C_c(\mathbb{R})$ dans $L^1(\mathbb{R})$ pour l'indicatrice $f = \mathbf{1}_A$, où $\mu(A) < \infty$.

**Correction :**
Soit $A \subset \mathbb{R}$ mesurable avec $\mu(A) < \infty$, et $\epsilon > 0$.
1. Par régularité de Lebesgue (approximations intérieures par des compacts), il existe un compact $K \subset A$ tel que $\mu(A \setminus K) < \frac{\epsilon}{2}$.
2. Par régularité (approximations extérieures), il existe un ouvert $U \supset K$ tel que $\mu(U \setminus K) < \frac{\epsilon}{2}$. Quitte à réduire $U$, on peut le supposer borné car $K$ l'est.
L'objectif est de lisser l'indicatrice entre $K$ et $U$.
Le lemme d'Urysohn pour les espaces métriques donne l'existence d'une fonction continue $g : \mathbb{R} \to [0,1]$ telle que :
$g(x) = 1$ pour tout $x \in K$,
$g(x) = 0$ pour tout $x \notin U$.
De plus, le support de $g$ est inclus dans l'adhérence de $U$. Comme $U$ est borné, le support est compact. Ainsi $g \in C_c(\mathbb{R})$.

Évaluons l'erreur en norme $L^1$ : $\| \mathbf{1}_A - g \|_1 = \int_{\mathbb{R}} |\mathbf{1}_A(x) - g(x)| dx$.
Découpons l'intégrale sur trois domaines : $K$, $U \setminus K$, et $U^c$.
- Sur $K$ : $\mathbf{1}_A(x) = 1$ (car $K \subset A$) et $g(x) = 1$. La différence est $0$.
- Sur $U^c$ : $\mathbf{1}_A(x)$ vaut $0$ (sauf sur $A \setminus U$, mais $A \setminus U \subset A \setminus K$ qui est de mesure petite) et $g(x) = 0$. Plus précisément, l'erreur est majorée par $\mu(A \setminus U) \le \mu(A \setminus K) < \frac{\epsilon}{2}$.
- Sur $U \setminus K$ : les fonctions $\mathbf{1}_A$ et $g$ sont à valeurs dans $[0,1]$, donc $|\mathbf{1}_A(x) - g(x)| \le 1$.
L'intégrale sur ce domaine est majorée par $\int_{U \setminus K} 1 \, dx = \mu(U \setminus K) < \frac{\epsilon}{2}$.

Par union disjointe, $\| \mathbf{1}_A - g \|_1 \le \mu(A \setminus K) + \mu(U \setminus K) < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$.
L'indicatrice d'un ensemble mesurable de mesure finie peut donc être approchée arbitrairement près par une fonction continue à support compact, ce qui est la pierre angulaire de la densité générale dans $L^1$.

# Exercice 10

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Preuve du contre-exemple p.s n'implique pas $L^p$

Rédigez la démonstration formelle du fait que la convergence presque sûre n'implique pas la convergence dans $L^p$ (ni même $L^1$). On exhibera un contre-exemple explicite et on calculera toutes les normes.

**Correction exhaustive :**
Nous devons fournir un exemple canonique illustrant la fuite de masse vers l'infini (concentration d'énergie sur un volume évanescent).
Considérons l'espace de probabilité $\Omega = ]0, 1]$ muni de la mesure de Borel-Lebesgue usuelle $\mathbb{P}$.
Définissons la suite de fonctions $X_n : \Omega \to \mathbb{R}$ par :
$$ X_n(\omega) = n \cdot \mathbf{1}_{]0, 1/n]}(\omega) $$
**1. Convergence presque sûre :**
Soit un événement élémentaire $\omega \in ]0, 1]$.
Parce que $\omega > 0$, et par la propriété archimédienne des réels, il existe un entier $N \ge 1$ tel que $\frac{1}{N} < \omega$.
Pour tout $n \ge N$, nous aurons $\frac{1}{n} \le \frac{1}{N} < \omega$.
Cela signifie que pour $n \ge N$, $\omega \notin ]0, 1/n]$, et donc par définition de la fonction indicatrice, $X_n(\omega) = 0$.
La suite numérique déterministe $X_n(\omega)$ devient stationnaire et égale à 0 pour tout indice $n \ge N$. Elle converge donc trivialement vers 0.
Puisque ceci est vrai pour **tout** $\omega \in ]0, 1]$, la convergence a lieu ponctuellement sur tout $\Omega$.
L'événement exceptionnel est l'ensemble vide, dont la probabilité est bien $0$.
Ainsi, $X_n \xrightarrow{p.s.} 0$.

**2. Non-convergence dans $L^1$ :**
Pour prouver la convergence $L^1$ vers 0, il faudrait que $\lim_{n \to \infty} \mathbb{E}[|X_n|] = 0$.
Procédons au calcul rigoureux de l'espérance pour un $n$ fixé, en utilisant l'intégrale de Lebesgue :
$$ \mathbb{E}[|X_n|] = \int_{\Omega} |X_n(\omega)| d\mathbb{P}(\omega) = \int_0^1 n \cdot \mathbf{1}_{]0, 1/n]}(\omega) d\omega $$
$$ \mathbb{E}[|X_n|] = n \int_0^{1/n} 1 d\omega = n \cdot \left[ \omega \right]_0^{1/n} = n \cdot \left( \frac{1}{n} - 0 \right) = n \cdot \frac{1}{n} = 1 $$
Pour tout indice $n \ge 1$, la masse fonctionnelle (l'aire sous la courbe) est constante et strictement égale à 1.
Par passage à la limite :
$$ \lim_{n \to \infty} \mathbb{E}[|X_n - 0|] = 1 \neq 0 $$
La suite ne converge donc absolument pas vers 0 dans la topologie des espaces $L^1$, établissant la démonstration définitive qu'une singularité géométrique empêche l'inversion limite/intégrale.

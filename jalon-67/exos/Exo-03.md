# Exercice 3 : Limite de suite d'intégrales $\bigstar\bigstar\star\star\star$

## Énoncé
Calculer $\lim_{n \to \infty} \int_0^n \left(1 - \frac{x}{n}\right)^n e^{x/2} dx$.

## Correction Détaillée
1. Posons $f_n(x) = \left(1 - \frac{x}{n}\right)^n e^{x/2} \mathbf{1}_{[0, n]}(x)$.
2. Les fonctions $f_n$ sont mesurables et positives sur $[0, \infty[$.
3. Montrons que la suite $(f_n)$ est croissante. Pour $x \in [0, n]$, étudions la fonction $y \mapsto y \ln(1 - x/y)$. Sa dérivée est positive, donc $(1 - x/n)^n$ croît avec $n$.
4. Déterminons la limite ponctuelle de $f_n(x)$ :
   $$ \left(1 - \frac{x}{n}\right)^n = \exp\left(n \ln\left(1 - \frac{x}{n}\right)\right) \xrightarrow{n \to \infty} \exp(n (-x/n)) = e^{-x} $$
   Donc $f_n(x) \xrightarrow{n \to \infty} f(x) = e^{-x} e^{x/2} \mathbf{1}_{[0, \infty[}(x) = e^{-x/2}$.
5. Comme $(f_n)$ est une suite de fonctions positives et croissantes, le TCM s'applique :
   $$ \lim_{n \to \infty} \int_0^\infty f_n(x) dx = \int_0^\infty f(x) dx $$
6. L'intégrale de la limite est :
   $$ \int_0^\infty e^{-x/2} dx = \left[-2e^{-x/2}\right]_0^\infty = 2 $$
7. La limite cherchée est donc $2$.

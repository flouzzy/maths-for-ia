# Exercice 02

**Difficulté :** $\bigstar\star\star\star\star$

**Énoncé :**
Soit $X_n$ une suite de variables aléatoires suivant une loi uniforme discrète sur $\{1, 2, \dots, n\}$.
Montrez que $X_n/n$ ne converge pas en probabilité vers $0$.

**Correction :**
Soit $\epsilon = \frac{1}{2}$. On cherche la probabilité que $|X_n/n - 0| > \frac{1}{2}$.
$$ \mathbb{P}\left(\frac{X_n}{n} > \frac{1}{2}\right) = \mathbb{P}\left(X_n > \frac{n}{2}\right) $$
Puisque $X_n$ est uniforme sur $\{1, \dots, n\}$, il y a $\lfloor n/2 \rfloor$ entiers strictement supérieurs à $n/2$ dans cet ensemble (ou $\lceil n/2 \rceil$ selon la parité, dans tous les cas, environ la moitié).
$$ \mathbb{P}\left(X_n > \frac{n}{2}\right) \approx \frac{1}{2} $$
En passant à la limite :
$$ \lim_{n \to \infty} \mathbb{P}\left(\left| \frac{X_n}{n} \right| > \frac{1}{2}\right) = \frac{1}{2} \neq 0 $$
Par conséquent, $X_n/n$ ne converge pas en probabilité vers $0$.

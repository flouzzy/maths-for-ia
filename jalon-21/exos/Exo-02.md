# Exercice 2 : Inversion limite et limite en l'infini
**Énoncé :**
On considère la suite de fonctions $g_n : ]0, +\infty[ \to \mathbb{R}$ définie par :
$$g_n(x) = \frac{n^2 x^2}{1 + n^3 x^3}$$
Montrer que $(g_n)$ converge uniformément vers la fonction nulle, et en déduire la limite de $\lim_{x \to +\infty} \lim_{n \to +\infty} g_n(x)$. Ce résultat nécessite de justifier avec une précision analytique absolue.

**Solution Rigoureuse :**
Fixons $x > 0$. On observe que :
$$g_n(x) \sim_{n \to +\infty} \frac{n^2 x^2}{n^3 x^3} = \frac{1}{nx} \xrightarrow[n \to +\infty]{} 0$$
La suite converge simplement vers la fonction nulle $g = 0$ sur $]0, +\infty[$.
Étudions la convergence uniforme. La dérivée est :
$$g_n'(x) = \frac{2n^2 x(1 + n^3 x^3) - n^2 x^2(3n^3 x^2)}{(1 + n^3 x^3)^2} = \frac{2n^2 x + 2n^5 x^4 - 3n^5 x^4}{(1 + n^3 x^3)^2} = \frac{nx(2n - n^4 x^3)}{(1 + n^3 x^3)^2}$$
La dérivée s'annule lorsque $2n = n^4 x^3$, soit $x^3 = \frac{2}{n^3}$, c'est-à-dire $x = \frac{\sqrt[3]{2}}{n}$.
La fonction $g_n$ est croissante sur $]0, \frac{\sqrt[3]{2}}{n}]$ et décroissante sur $[\frac{\sqrt[3]{2}}{n}, +\infty[$. Le maximum global est donc :
$$g_n\left(\frac{\sqrt[3]{2}}{n}\right) = \frac{n^2 \left(\frac{\sqrt[3]{2}}{n}\right)^2}{1 + n^3 \left(\frac{\sqrt[3]{2}}{n}\right)^3} = \frac{2^{2/3}}{1 + 2} = \frac{2^{2/3}}{3}$$
On constate avec stupeur que $\sup_{x \in ]0, +\infty[} |g_n(x)| = \frac{2^{2/3}}{3} \neq 0$.
La convergence **n'est pas uniforme** sur $]0, +\infty[$.
L'énoncé comportait un piège pédagogique : la convergence uniforme est fausse sur $]0, +\infty[$.
Cependant, pour appliquer l'inversion des limites (théorème de la double limite), il suffit d'avoir la convergence uniforme sur un voisinage de $+\infty$.
Soit $a > 0$. Pour $n$ assez grand, $\frac{\sqrt[3]{2}}{n} < a$, et le supremum sur $[a, +\infty[$ est $g_n(a)$, qui tend vers $0$.
Donc il y a convergence uniforme sur $[a, +\infty[$.
On peut alors appliquer le théorème d'inversion des limites :
$$\lim_{x \to +\infty} \lim_{n \to +\infty} g_n(x) = \lim_{x \to +\infty} 0 = 0$$
$$\lim_{n \to +\infty} \lim_{x \to +\infty} g_n(x) = \lim_{n \to +\infty} 0 = 0$$
L'égalité est bien vérifiée.

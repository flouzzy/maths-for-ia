# Exercice 4 : Transfert de dérivabilité et série de fonctions
**Énoncé :**
Étudier la suite de fonctions définie par $h_n(x) = \frac{\sin(nx)}{\sqrt{n}}$ sur $\mathbb{R}$.
Montrer que $h_n$ converge uniformément, mais que sa limite n'est pas dérivable. En déduire que le transfert de dérivabilité exige des hypothèses sur la suite des dérivées.

**Solution Rigoureuse :**
1. **Convergence de $(h_n)$ :**
Pour tout $x \in \mathbb{R}$ et tout $n \ge 1$, on a :
$$|h_n(x)| = \frac{|\sin(nx)|}{\sqrt{n}} \le \frac{1}{\sqrt{n}}$$
Donc $\sup_{x \in \mathbb{R}} |h_n(x)| \le \frac{1}{\sqrt{n}}$.
Puisque $\lim_{n \to +\infty} \frac{1}{\sqrt{n}} = 0$, la suite $(h_n)$ converge uniformément sur $\mathbb{R}$ vers la fonction constante $h = 0$.

2. **Étude des dérivées :**
La limite de $(h_n)$ est $h(x) = 0$, qui est de classe $\mathcal{C}^\infty$, donc infiniment dérivable avec $h'(x) = 0$.
Regardons la suite des dérivées :
$$h_n'(x) = \sqrt{n} \cos(nx)$$
Fixons par exemple $x = 0$. $h_n'(0) = \sqrt{n} \cos(0) = \sqrt{n}$.
On constate que $\lim_{n \to +\infty} h_n'(0) = +\infty$.
La suite des dérivées ne converge même pas simplement en $0$.
Cet exemple met en évidence une pathologie fondamentale : la convergence uniforme d'une suite de fonctions régulières vers une limite régulière ne garantit absolument pas le transfert des dérivées. Le théorème de dérivation exige la convergence uniforme de la **suite des dérivées** $(h_n')$, ce qui est gravement mis en défaut ici.

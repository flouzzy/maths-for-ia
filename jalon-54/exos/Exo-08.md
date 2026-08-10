## Exercice 8 : Non-compacité de la boule fermée en dimension infinie \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :** Soit $E$ l'espace des suites réelles de carré sommable, $\ell^2(\mathbb{N})$, muni de la norme $\|x\|_2 = \sqrt{\sum_{n=0}^\infty x_n^2}$. Démontrer que la boule unité fermée $\bar{B}(0, 1)$ n'est pas compacte, bien qu'étant fermée et bornée. (Théorème de Riesz).

**Correction Détaillée :**
Considérons la suite d'éléments $(e_n)_{n \in \mathbb{N}}$ de $E$ formant la base de Hilbert canonique, définie par $e_n = (0, \dots, 0, 1, 0, \dots)$ où le 1 est à la $n$-ième position.
La norme de chaque $e_n$ est $\|e_n\|_2 = 1$. Donc la suite $(e_n)$ est intégralement contenue dans la boule unité fermée $\bar{B}(0, 1)$.
Calculons la distance entre deux termes distincts $e_n$ et $e_m$ (pour $n \neq m$) :
$\|e_n - e_m\|_2^2 = \sum_{k=0}^\infty (e_{n,k} - e_{m,k})^2 = 1^2 + (-1)^2 = 2$.
Ainsi, pour tous $n \neq m$, $\|e_n - e_m\|_2 = \sqrt{2}$.
Supposons par l'absurde que $\bar{B}(0, 1)$ soit compacte. Alors la suite $(e_n)$ admettrait une sous-suite convergente $(e_{\phi(k)})_{k \in \mathbb{N}}$ convergeant vers un certain $l \in E$.
Si une suite converge, c'est une suite de Cauchy. Il devrait donc exister un rang $K$ tel que pour tous $p, q > K$, $\|e_{\phi(p)} - e_{\phi(q)}\|_2 < \frac{1}{2}$.
Mais pour $p \neq q$, l'injectivité stricte de l'extraction $\phi$ assure que $\phi(p) \neq \phi(q)$. Ainsi, la distance est invariablement $\|e_{\phi(p)} - e_{\phi(q)}\|_2 = \sqrt{2} \approx 1.414$, ce qui est strictement supérieur à $\frac{1}{2}$.
Ceci est une contradiction flagrante avec le fait d'être une suite de Cauchy. La suite $(e_n)$ ne possède donc aucune sous-suite convergente. La boule unité fermée n'est pas séquentiellement compacte.
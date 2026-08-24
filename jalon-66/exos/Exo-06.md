# Exercice 6 : Suite de fonctions simples approximantes \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Construire explicitement une suite de fonctions simples positives $(s_n)$ qui croît ponctuellement vers $f(x) = x^2$ sur $[0, 1]$.

**Correction :**
Ceci est la construction standard, dite 'découpage en tranches horizontales' dyadiques.
1. Pour chaque entier $n \ge 1$, on découpe l'axe des ordonnées (l'image de $f$) en $n 2^n$ intervalles de hauteur $1/2^n$.
2. Sur $[0,1]$, l'image de $f$ est $[0,1]$. On n'a donc besoin de découper que jusqu'à $1$.
3. On pose $s_n(x) = \sum_{k=0}^{2^n - 1} \frac{k}{2^n} \mathbf{1}_{\{x \mid \frac{k}{2^n} \le f(x) < \frac{k+1}{2^n}\}}(x)$.
4. Explicitons pour $f(x) = x^2$ : la condition $\frac{k}{2^n} \le x^2 < \frac{k+1}{2^n}$ devient $\sqrt{\frac{k}{2^n}} \le x < \sqrt{\frac{k+1}{2^n}}$.
5. Donc, $s_n(x) = \sum_{k=0}^{2^n - 1} \frac{k}{2^n} \mathbf{1}_{[\sqrt{\frac{k}{2^n}}, \sqrt{\frac{k+1}{2^n}}[}(x)$.
6. Par construction, $0 \le f(x) - s_n(x) \le \frac{1}{2^n}$ sur $[0,1]$, garantissant que $s_n \uparrow f$ uniformément, donc ponctuellement.

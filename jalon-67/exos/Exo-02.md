# Exercice 2 : Séries de fonctions positives

**Difficulté :** $\bigstar\star$

**Énoncé :**
Soit $(u_n)$ une suite de fonctions mesurables positives. Montrer que $\int (\sum u_n) d\mu = \sum \int u_n d\mu$.

**Correction :**
Soit $f_N = \sum_{n=0}^N u_n$. La positivité des $u_n$ implique que $f_N \leq f_{N+1}$. De plus $f_N \to f = \sum_{n=0}^\infty u_n$. Par Beppo Levi, $\int f d\mu = \lim_N \int f_N d\mu = \lim_N \sum_{n=0}^N \int u_n d\mu$ par linéarité sur une somme finie. La limite de la somme partielle est la série des intégrales. $\blacksquare$

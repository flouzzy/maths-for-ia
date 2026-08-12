# Exercice 8 : Non-contraction et espaces ultramétriques (Théorème de l'Application Rétractante p-adique)
**Niveau :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Un espace ultramétrique vérifie l'inégalité triangulaire forte : $d(x, z) \leq \max(d(x, y), d(y, z))$.
Soit un tel espace $(X, d)$ complet. Démontrer que si $f : X \to X$ satisfait strictement $d(f(x), f(y)) < d(x, y)$ pour $x \neq y$, et s'il existe une itération $x_n$ telle que $d(x_{n+1}, x_n) \to 0$, alors $f$ admet un point fixe unique. L'hypothèse contractante faible sans constante suffit grâce à l'ultramétricité.

**Démonstration pas à pas :**
1. L'unicité suit de la condition $d(f(x), f(y)) < d(x, y)$ (même preuve absurde qu'usuellement).
2. Vérifions que la suite $(x_n)$ est de Cauchy. Par l'inégalité forte, pour $m > n$ :
   $d(x_n, x_m) \leq \max_{n \leq i < m} d(x_i, x_{i+1})$.
   Comme $d(x_i, x_{i+1}) \to 0$, ce maximum devient arbitrairement petit pour $n$ grand.
3. Ainsi $(x_n)$ est de Cauchy dans un espace complet, donc converge vers $x^*$.
4. Par l'inégalité faible (qui implique la continuité), la limite est un point fixe.

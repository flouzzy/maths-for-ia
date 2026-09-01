# Exercice 7 : Comportement pathologique sans croissance

**Difficulté :** $\bigstar\star$

**Énoncé :**
Donner un exemple où $f_n \ge 0$, $f_n \to f$ presque partout, mais $\int f_n \not\to \int f$. Pourquoi le TCM échoue-t-il ?

**Correction :**
Prenons la bosse glissante : $f_n(x) = \mathbb{I}_{[n, n+1]}(x)$ sur $\mathbb{R}$. Pour tout $x \in \mathbb{R}$, $f_n(x) \to 0 = f(x)$. Mais $\int f_n(x) dx = 1$ pour tout $n$, et $\int f(x) dx = 0$. Le TCM requiert $f_n \le f_{n+1}$. Ici $\mathbb{I}_{[n, n+1]}$ n'est absolument pas incluse dans $\mathbb{I}_{[n+1, n+2]}$. La condition de monotonie fait défaut. $\blacksquare$

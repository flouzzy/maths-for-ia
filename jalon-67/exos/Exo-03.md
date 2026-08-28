# Exercice 3 : Application aux densités de probabilité ★★★★☆

**Énoncé :**
Soit $X$ une variable aléatoire positive admettant une densité $f$. Montrer par le théorème de convergence monotone que $\mathbb{E}[X] = \int_0^\infty \mathbb{P}(X > t) dt$.

**Correction :**
1. Par définition, $\mathbb{E}[X] = \int_0^\infty x f(x) dx$. On peut écrire $x = \int_0^x 1 dt$.
2. Ainsi $\mathbb{E}[X] = \int_0^\infty \left( \int_0^\infty \chi_{\{t < x\}}(t) dt \right) f(x) dx$.
3. La fonction $(t, x) \mapsto \chi_{\{t < x\}}(t) f(x)$ est positive et mesurable sur $\mathbb{R}^+ \times \mathbb{R}^+$.
4. On peut appliquer le théorème de Tonelli (qui repose fondamentalement sur Beppo Levi). On intervertit l'ordre d'intégration :
$\mathbb{E}[X] = \int_0^\infty \left( \int_0^\infty \chi_{\{t < x\}}(t) f(x) dx \right) dt$.
5. L'intégrale interne est $\int_t^\infty f(x) dx = \mathbb{P}(X > t)$.
6. Donc $\mathbb{E}[X] = \int_0^\infty \mathbb{P}(X > t) dt$.

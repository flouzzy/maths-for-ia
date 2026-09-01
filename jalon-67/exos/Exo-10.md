# Exercice 10 : Continuité de la transformée de Laplace

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $f \ge 0$ mesurable et $\mathcal{L}f(p) = \int_0^\infty f(t) e^{-pt} dt$. Montrer que $p \mapsto \mathcal{L}f(p)$ est continue si $f$ est intégrable.

**Correction :**
Si $p_n \to p$ en décroissant ($p_n \downarrow p$), alors $e^{-p_n t} \uparrow e^{-pt}$. Les fonctions $g_n(t) = f(t) e^{-p_n t}$ forment une suite croissante de fonctions positives, qui converge vers $g(t) = f(t) e^{-pt}$. Par le TCM, $\int g_n(t) dt \to \int g(t) dt$, donc $\mathcal{L}f(p_n) \to \mathcal{L}f(p)$. (Pour le cas croissant, on utilisera le théorème de convergence dominée dominé par $f(t)e^{-p_0 t}$). $\blacksquare$

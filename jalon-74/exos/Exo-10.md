---
title: "Exercice 10 : Application des Inégalités"
difficulty: "★★★★★"
---

# Exercice 10 : Application des Inégalités

**Niveau :** ★★★★★

**Énoncé :**
Démontrer que si $f \in L^1(\mathbb{R}) \cap L^\infty(\mathbb{R})$, alors $f \in L^p(\mathbb{R})$ pour tout $1 < p < \infty$ et $\lim_{p \to \infty} \|f\|_p = \|f\|_\infty$.

**Correction Détaillée :**
Pour $f \in L^1 \cap L^\infty$, notons $\|f\|_\infty$ son supremum essentiel.<br>Pour tout $p > 1$, on peut majorer l'intégrande $|f|^p = |f|^{p-1}|f| \le \|f\|_\infty^{p-1} |f|$ presque partout.<br>En intégrant : $\int |f|^p \le \|f\|_\infty^{p-1} \int |f|$.<br>Puisque $\int |f| = \|f\|_1 < \infty$ et $\|f\|_\infty < \infty$, l'intégrale est finie. Donc $f \in L^p$.<br>Prenons la puissance $1/p$ : $\|f\|_p \le \|f\|_\infty^{1 - 1/p} \|f\|_1^{1/p}$.<br>En passant à la limite supérieure $p \to \infty$, le membre de droite tend vers $\|f\|_\infty^1 \times \|f\|_1^0 = \|f\|_\infty$. Donc $\limsup_{p \to \infty} \|f\|_p \le \|f\|_\infty$.<br>Pour minorer, soit $0 < \epsilon < \|f\|_\infty$. L'ensemble $A_\epsilon = \{x : |f(x)| > \|f\|_\infty - \epsilon\}$ a une mesure strictement positive, $0 < \mu(A_\epsilon) < \infty$ (car $f \in L^1$).<br>$\int |f|^p \ge \int_{A_\epsilon} |f|^p \ge \int_{A_\epsilon} (\|f\|_\infty - \epsilon)^p = \mu(A_\epsilon) (\|f\|_\infty - \epsilon)^p$.<br>D'où $\|f\|_p \ge \mu(A_\epsilon)^{1/p} (\|f\|_\infty - \epsilon)$.<br>En passant à la limite inférieure $p \to \infty$, $\mu(A_\epsilon)^{1/p} \to 1$, donc $\liminf_{p \to \infty} \|f\|_p \ge \|f\|_\infty - \epsilon$.<br>Comme ceci est vrai pour tout $\epsilon > 0$, $\liminf \|f\|_p \ge \|f\|_\infty$.<br>Les limites inf et sup coïncidant, la limite existe et vaut $\|f\|_\infty.

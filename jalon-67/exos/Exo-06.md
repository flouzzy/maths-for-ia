# Exercice 6 : Fonction $\Gamma$ d'Euler \quad $\bigstar$$\bigstar$$\bigstar$$\bigstar$$\star$

**Énoncé :**
Évaluer $\lim_{n \to \infty} \int_0^n (1 - x/n)^n x^{z-1} dx$.

**Correction Détaillée :**
1. La fonction $f_n(x) = (1 - x/n)^n x^{z-1} \mathbf{1}_{[0,n]}$ est croissante et converge vers $e^{-x} x^{z-1}$. Par Beppo Levi, on obtient $\Gamma(z)$.
2. Le théorème de convergence monotone est au coeur de la justification formelle.

---
title: "Exercice 10 : TCM"
difficulty: "★★★★★"
---
# Exercice 10 : Construction de la transformée de Fourier

**Niveau :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Pour approcher $\int_{-\infty}^{+\infty} e^{-x^2/2} dx$, on utilise $f_n(x) = e^{-x^2/2} \mathbf{1}_{[-n, n]}(x)$. L'utilisation du TCM est-elle valide ici ? Le prouver rigoureusement.

**Correction détaillée :**
1. La fonction indicatrice $\mathbf{1}_{[-n, n]}(x)$ est une suite croissante d'ensembles.
2. Comme $e^{-x^2/2} > 0$, le produit $f_n(x)$ forme bien une suite croissante de fonctions positives, convergeant ponctuellement vers $f(x) = e^{-x^2/2}$.
3. Le Théorème de Convergence Monotone de Beppo-Levi s'applique pleinement.
4. Ainsi $\lim_{n \to \infty} \int_{-n}^n e^{-x^2/2} dx = \int_{-\infty}^{+\infty} e^{-x^2/2} dx = \sqrt{2\pi}$ (Intégrale de Gauss).
5. C'est l'argument fondamental pour définir les intégrales impropres de fonctions positives de Riemann comme des intégrales de Lebesgue sur des ensembles non bornés.

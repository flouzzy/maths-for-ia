\subsection*{Exercice 2 : Parité et nature de la transformée de Fourier \quad $\bigstar\bigstar\star\star\star$}

Soit $f \in L^1(\mathbb{R})$ une fonction à valeurs réelles.
Montrer que :
**1.** Si $f$ est paire, alors sa transformée de Fourier $\hat{f}$ est une fonction à valeurs réelles et paire.
**2.** Si $f$ est impaire, alors sa transformée de Fourier $\hat{f}$ est une fonction imaginaire pure et impaire.

---
**Correction :**

**1. Cas $f$ paire :**
Par définition, $\hat{f}(\xi) = \int_{-\infty}^{+\infty} f(t)e^{-i\xi t} \, dt$.
On utilise la formule d'Euler : $e^{-i\xi t} = \cos(-\xi t) + i\sin(-\xi t) = \cos(\xi t) - i\sin(\xi t)$.
Donc $\hat{f}(\xi) = \int_{-\infty}^{+\infty} f(t)\cos(\xi t) \, dt - i \int_{-\infty}^{+\infty} f(t)\sin(\xi t) \, dt$.
Puisque $f$ est paire, la fonction $t \mapsto f(t)\sin(\xi t)$ est impaire (produit d'une paire par une impaire). Sur l'intervalle symétrique $\mathbb{R}$, son intégrale est nulle.
Ainsi, $\hat{f}(\xi) = \int_{-\infty}^{+\infty} f(t)\cos(\xi t) \, dt$.
L'expression sous l'intégrale est réelle, donc $\hat{f}(\xi) \in \mathbb{R}$.
De plus, la fonction $\cos$ étant paire, $\cos(-\xi t) = \cos(\xi t)$, d'où $\hat{f}(-\xi) = \hat{f}(\xi)$. $\hat{f}$ est donc paire.

**2. Cas $f$ impaire :**
Avec la même décomposition :
$$ \hat{f}(\xi) = \int_{-\infty}^{+\infty} f(t)\cos(\xi t) \, dt - i \int_{-\infty}^{+\infty} f(t)\sin(\xi t) \, dt $$
Ici, $f$ est impaire, donc $t \mapsto f(t)\cos(\xi t)$ est impaire. Son intégrale sur $\mathbb{R}$ est nulle.
Ainsi, $\hat{f}(\xi) = -i \int_{-\infty}^{+\infty} f(t)\sin(\xi t) \, dt$.
L'intégrale est réelle, donc $\hat{f}(\xi)$ est imaginaire pure.
De plus, $\sin(-\xi t) = -\sin(\xi t)$, donc $\hat{f}(-\xi) = -i \int_{-\infty}^{+\infty} f(t)(-\sin(\xi t)) \, dt = i \int_{-\infty}^{+\infty} f(t)\sin(\xi t) \, dt = -\hat{f}(\xi)$. $\hat{f}$ est donc impaire.

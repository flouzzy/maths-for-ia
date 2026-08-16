---
title: "Exercice 9 : Propriété discriminatoire (Théorème de Cybenko)"
difficulty: $\bigstar\bigstar\bigstar\bigstar\bigstar$
---

# Exercice 9 : Propriété discriminatoire (Théorème de Cybenko)

## Énoncé

Prouvez qu'une fonction d'activation $\sigma$ est discriminatoire si, pour toute mesure de probabilité signée $\mu$ sur $I_n = [0, 1]^n$, l'hypothèse :
$$\forall w, b, \quad \int_{I_n} \sigma(w^T x + b) d\mu(x) = 0$$
implique $\mu = 0$.
Utilisez une activation continue bornée vérifiant $\lim_{t\to-\infty}\sigma(t)=0$ et $\lim_{t\to+\infty}\sigma(t)=1$.

## Correction Rigoureuse

**Étape 1 : Limites avec l'activation sigmoïdale**
Soit un vecteur unitaire $\omega \in \mathbb{R}^n$ et deux réels $c, \theta$. Posons $w = \lambda \omega$ et $b = -\lambda c + \theta$.
L'intégrale devient : $\int_{I_n} \sigma(\lambda (\omega^T x - c) + \theta) d\mu(x) = 0$.

**Étape 2 : Passage à la limite $\lambda \to +\infty$**
Pour $x$ tel que $\omega^T x > c$, le terme $\lambda(\omega^T x - c) \to +\infty$, donc la sigmoïde tend vers 1.
Pour $x$ tel que $\omega^T x < c$, la sigmoïde tend vers 0.
Par le Théorème de Convergence Dominée de Lebesgue (car $\sigma$ est bornée et $\mu$ est finie) :
$$ \lim_{\lambda \to \infty} \int_{I_n} \dots = \int_{I_n \cap \{\omega^T x > c\}} 1 \, d\mu(x) + \int_{I_n \cap \{\omega^T x = c\}} \sigma(\theta) \, d\mu(x) = 0 $$

**Étape 3 : Élimination du plan singulier**
En faisant tendre $\theta \to -\infty$, le terme $\sigma(\theta) \to 0$. L'intégrale sur le plan $\{\omega^T x = c\}$ s'annule.
On déduit que pour tout $\omega$ et tout $c$, la mesure $\mu$ des demi-espaces stricts $H_{\omega, c} = \{x \in I_n : \omega^T x > c\}$ est nulle : $\mu(H_{\omega, c}) = 0$.

**Étape 4 : Conclusion par la transformée de Fourier**
Puisque la mesure signée $\mu$ annule tous les demi-espaces, elle annule par intersection toutes les hyperboîtes (les rectangles $n$-dimensionnels). Les hyperboîtes engendrant la tribu borélienne de $I_n$, la mesure $\mu$ s'annule sur tout borélien.
Ainsi, $\mu \equiv 0$. La fonction $\sigma$ est donc discriminatoire, validant l'hypothèse de base de Hahn-Banach de la preuve de Cybenko. $\blacksquare$

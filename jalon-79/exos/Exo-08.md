---
title: "Exercice 8 : Redressement double alternance"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 8 : Redressement double alternance $|\sin(t)|$

**Niveau :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Soit $f(t) = |\sin(t)|$, fonction $\pi$-périodique. On l'étudie comme $2\pi$-périodique.
1. Calculer les coefficients de Fourier de $f$.
2. Évaluer $\sum_{p=1}^\infty \frac{1}{(4p^2-1)^2}$ par Parseval et comparer avec l'exercice précédent.

## Correction Détaillée

1. **Coefficients :**
La fonction est paire, $b_n = 0$.
$a_0 = \frac{1}{\pi} \int_{-\pi}^\pi |\sin(t)| dt = \frac{4}{\pi}$.
$a_n = \frac{2}{\pi} \int_0^\pi \sin(t)\cos(nt) dt$.
D'après l'exercice 7, pour $n=2p$, $\int_0^\pi \sin(t)\cos(2pt) dt = \frac{-2}{4p^2-1}$.
Donc $a_{2p} = \frac{-4}{\pi(4p^2-1)}$. Pour $n$ impair, $a_{2p+1}=0$.

2. **Parseval :**
Énergie : $\|f\|_{L^2}^2 = \frac{1}{2\pi} \int_{-\pi}^\pi \sin^2(t) dt = \frac{1}{2}$.
Parseval : $\frac{a_0^2}{4} + \frac{1}{2} \sum_{p=1}^\infty a_{2p}^2 = \frac{1}{2}$.
$\frac{4}{\pi^2} + \frac{1}{2} \sum_{p=1}^\infty \frac{16}{\pi^2(4p^2-1)^2} = \frac{1}{2}$.
$\frac{8}{\pi^2} \sum_{p=1}^\infty \frac{1}{(4p^2-1)^2} = \frac{1}{2} - \frac{4}{\pi^2}$.
$\sum_{p=1}^\infty \frac{1}{(4p^2-1)^2} = \frac{\pi^2}{16} - \frac{1}{2}$.
On retrouve heureusement le même résultat fondamental !

---
title: "Masse fuyante (Pathologie non monotone)"
difficulty: $\bigstar\bigstar\bigstar\bigstar\star$
---
# Masse fuyante (Pathologie non monotone)
**Énoncé :**
Soit $f_n(x) = n^2 x e^{-n x}$ sur $\mathbb{R}^+$. Étudier la convergence ponctuelle, calculer l'intégrale et voir pourquoi le TCM échoue.

**Correction :**
1. Pour $x > 0$, $\lim_{n \to \infty} n^2 x e^{-n x} = 0$ par croissance comparée. Pour $x=0$, $f_n(0) = 0$. Donc $f_n \to 0$ ponctuellement.
2. $\int_0^{+\infty} \lim f_n = 0$.
3. Calculons $\int_0^{+\infty} n^2 x e^{-n x} dx$.
   Par IPP : $u=x, v' = n^2 e^{-nx} \implies u'=1, v = -n e^{-nx}$.
   $\int f_n = \left[ -n x e^{-nx} \right]_0^{+\infty} + \int_0^{+\infty} n e^{-nx} dx = 0 + \left[ -e^{-nx} \right]_0^{+\infty} = 1$.
4. On a $\lim \int f_n = 1 \neq 0$.
5. Le TCM ne s'applique pas car la suite $f_n$ n'est pas croissante (pour un $x$ donné, elle croît puis décroît vers 0). La masse "glisse" vers 0 et se concentre.

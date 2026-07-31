---
title: "Exercice 8 : Étude qualitative sans résolution explicite"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 8 : Étude qualitative sans résolution explicite

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit l'équation $y' = -y + \sin(t)$. Montrer qu'il existe une unique solution périodique, et que toute solution de l'équation s'en rapproche lorsque $t \to +\infty$.

**Correction détaillée :**
1. **Résolution de l'équation :**
   Équation homogène $y' + y = 0 \implies y_H(t) = C e^{-t}$.
   Solution particulière pour le second membre trigonométrique (cf Exo 5) : on cherche $z_P$ pour $z' + z = e^{it}$.
   $z_P(t) = A e^{it} \implies A(i+1)e^{it} = e^{it} \implies A = \frac{1}{1+i} = \frac{1-i}{2}$.
   $z_P(t) = \frac{1-i}{2} (\cos t + i \sin t) = \frac{1}{2}(\cos t + \sin t) + i \frac{1}{2}(\sin t - \cos t)$.
   Comme on a un second membre $\sin(t) = \Im(e^{it})$, on prend la partie imaginaire : $y_P(t) = \frac{1}{2}(\sin t - \cos t)$.
2. **Solution générale :**
   $y(t) = C e^{-t} + \frac{1}{2}(\sin t - \cos t)$.
3. **Recherche de solution périodique :**
   La fonction $y_P(t) = \frac{1}{2}(\sin t - \cos t)$ est $2\pi$-périodique.
   Si $C \neq 0$, le terme $C e^{-t}$ n'est pas périodique (il est strictement monotone). La seule solution périodique s'obtient pour $C = 0$. Il existe donc bien une unique solution périodique.
4. **Comportement asymptotique :**
   Pour toute solution avec une condition initiale donnant une constante $C$, on a :
   $y(t) - y_P(t) = C e^{-t}$.
   Or, $\lim_{t \to +\infty} C e^{-t} = 0$.
   Donc la différence entre n'importe quelle solution et la solution périodique tend vers $0$. Toute solution "s'accroche" asymptotiquement à l'orbite périodique. C'est un phénomène classique de relaxation dans les systèmes dynamiques (attracteur).

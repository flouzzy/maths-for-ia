---
title: "Exercice 3 : Équation avec coefficient variable"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exercice 3 : Équation avec coefficient variable

**Difficulté :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
Résoudre sur $\mathbb{R}$ l'équation différentielle suivante :
$$y'(t) - 2t y(t) = 1$$

**Correction détaillée :**
1. **Équation homogène associée :**
   L'équation $(H)$ est $y'(t) - 2t y(t) = 0$. La fonction $a(t) = -2t$ a pour primitive $A(t) = -t^2$.
   Les solutions homogènes sont $y_H(t) = C e^{t^2}$, avec $C \in \mathbb{R}$.
2. **Recherche d'une solution particulière :**
   On pose $y_P(t) = C(t) e^{t^2}$. En injectant dans l'équation, l'astuce de la variation de la constante donne directement :
   $$C'(t) e^{t^2} = 1 \implies C'(t) = e^{-t^2}$$
3. **Expression intégrale :**
   La fonction $t \mapsto e^{-t^2}$ n'admet pas de primitive s'exprimant à l'aide des fonctions usuelles élémentaires. On l'écrit donc sous forme intégrale.
   $C(t) = \int_0^t e^{-s^2} ds$.
   (On reconnaît la fonction d'erreur, à un facteur près, liée à la loi normale en probabilités).
4. **Solution générale :**
   La solution particulière est $y_P(t) = e^{t^2} \int_0^t e^{-s^2} ds$.
   La solution générale sur $\mathbb{R}$ s'écrit :
   $$y(t) = \left( C + \int_0^t e^{-s^2} ds \right) e^{t^2}, \quad C \in \mathbb{R}$$

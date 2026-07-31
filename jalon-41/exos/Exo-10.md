---
title: "Exercice 10 : Équation de Riccati"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 10 : Équation de Riccati

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit l'équation de Riccati $(E) : y' = y^2 + 1 - t^2$.
1. Vérifier que $y_0(t) = t$ est une solution particulière évidente.
2. Déterminer la solution générale en posant $y(t) = y_0(t) + \frac{1}{z(t)}$.

**Correction détaillée :**
1. **Solution évidente :**
   Soit $y_0(t) = t$. Sa dérivée est $y_0'(t) = 1$.
   En calculant le second membre : $y_0(t)^2 + 1 - t^2 = t^2 + 1 - t^2 = 1$.
   On a bien $y_0'(t) = 1$, donc $y_0$ est solution de $(E)$.
2. **Changement de fonction :**
   Soit $y$ une autre solution (on suppose qu'elle ne croise pas $y_0$). On pose $z(t) = \frac{1}{y(t) - t}$, soit $y(t) = t + \frac{1}{z(t)}$.
   La dérivée de $y$ est $y'(t) = 1 - \frac{z'(t)}{z(t)^2}$.
3. **Injection dans (E) :**
   On remplace $y$ et $y'$ dans l'équation :
   $$1 - \frac{z'}{z^2} = \left( t + \frac{1}{z} \right)^2 + 1 - t^2$$
   $$1 - \frac{z'}{z^2} = t^2 + \frac{2t}{z} + \frac{1}{z^2} + 1 - t^2$$
   $$1 - \frac{z'}{z^2} = \frac{2t}{z} + \frac{1}{z^2} + 1$$
   On soustrait $1$ des deux côtés :
   $$-\frac{z'}{z^2} = \frac{2t}{z} + \frac{1}{z^2}$$
4. **Réduction à une équation linéaire :**
   On multiplie toute l'équation par $-z^2$ (on sait que $z \neq 0$) :
   $$z'(t) = -2t z(t) - 1 \iff z'(t) + 2t z(t) = -1$$
   C'est une équation différentielle linéaire du premier ordre pour $z$.
5. **Résolution pour z :**
   - Équation homogène $z' + 2tz = 0 \implies z_H(t) = C e^{-t^2}$.
   - Variation de la constante : $z_P(t) = C(t) e^{-t^2} \implies C'(t)e^{-t^2} = -1 \implies C'(t) = -e^{t^2}$.
   $C(t) = -\int_0^t e^{s^2} ds$.
   $z(t) = \left( C - \int_0^t e^{s^2} ds \right) e^{-t^2}$.
6. **Solution pour y :**
   $y(t) = t + \frac{e^{t^2}}{C - \int_0^t e^{s^2} ds}$.

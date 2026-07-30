---
uuid: "jalon-40-exo-08"
title: "Exercice 8 : Calcul d'une intégrale délicate par paramètre"
difficulty: "$\star\star\star\star\star$"
---

# Exercice 8 : Calcul d'une intégrale délicate par paramètre ($\star\star\star\star\star$)

Calculer $\int_0^1 \frac{t-1}{\ln(t)} \mathrm{d}t$ en posant $F(x) = \int_0^1 \frac{t^x-1}{\ln(t)} \mathrm{d}t$.

**Correction détaillée :**
1. Identifions la régularité. Pour $x > -1$, on a justifié dans le cours que $F$ est bien définie et dérivable.
2. $F'(x) = \int_0^1 t^x \mathrm{d}t = \frac{1}{x+1}$.
3. Par intégration, $F(x) = \ln(x+1) + C$.
4. L'évaluation en $x=0$ donne $F(0) = \int_0^1 0 \mathrm{d}t = 0$. Donc $C = 0$ et $F(x) = \ln(x+1)$.
5. L'intégrale demandée correspond à la valeur pour $x=1$, soit $F(1) = \ln(2)$. La démonstration est totale, stricte, par dérivation sous le signe intégral avec théorème de Leibniz bien vérifié.

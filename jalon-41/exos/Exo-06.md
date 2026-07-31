---
title: "Exercice 6 : Équation de Bernoulli (réduction au premier ordre linéaire)"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 6 : Équation de Bernoulli (réduction au premier ordre linéaire)

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Résoudre sur $]0, +\infty[$ l'équation différentielle non linéaire :
$$y'(t) + \frac{1}{t} y(t) = y(t)^2$$
On cherchera des solutions ne s'annulant pas.

**Correction détaillée :**
1. **Changement de variable de Bernoulli :**
   C'est une équation de Bernoulli avec exposant $\alpha = 2$. L'astuce standard est de diviser par $y^2$ (licite car $y$ ne s'annule pas) :
   $$\frac{y'(t)}{y(t)^2} + \frac{1}{t} \frac{1}{y(t)} = 1$$
2. **Nouvelle fonction inconnue :**
   On pose $z(t) = \frac{1}{y(t)} = y(t)^{-1}$.
   Sa dérivée est $z'(t) = -\frac{y'(t)}{y(t)^2}$.
   En multipliant la première équation par $-1$, on obtient :
   $$-\frac{y'(t)}{y(t)^2} - \frac{1}{t} \frac{1}{y(t)} = -1$$
   Ce qui se réécrit comme une équation linéaire du premier ordre pour $z$ :
   $$z'(t) - \frac{1}{t} z(t) = -1$$
3. **Résolution pour z :**
   - Équation homogène : $z' - \frac{1}{t} z = 0 \implies z_H(t) = C t$.
   - Solution particulière par variation de la constante : $z_P(t) = C(t)t \implies C'(t)t = -1 \implies C'(t) = -1/t \implies C(t) = -\ln(t)$. Donc $z_P(t) = -t\ln(t)$.
   - Solution générale pour $z$ : $z(t) = Ct - t\ln(t) = t(C - \ln(t))$, avec $C \in \mathbb{R}$.
4. **Retour à y :**
   Sachant que $y(t) = \frac{1}{z(t)}$, la solution est :
   $$y(t) = \frac{1}{t(C - \ln(t))}$$
   L'intervalle maximal de définition d'une telle solution dépend de $C$, pour que $C - \ln(t) \neq 0$.

---
title: "Exercice 8 : Application des Inégalités"
difficulty: "★★★★★"
---

# Exercice 8 : Application des Inégalités

**Niveau :** ★★★★★

**Énoncé :**
Soit $f$ mesurable positive. Montrer que la fonction $p \mapsto \ln(\int f^p d\mu)$ est convexe sur l'ensemble où l'intégrale est finie (Application de Hölder).

**Correction Détaillée :**
Soit $p_0, p_1$ dans l'ensemble où l'intégrale est finie, et $\lambda \in ]0, 1[$. Posons $p_\lambda = (1-\lambda)p_0 + \lambda p_1$.<br>Nous voulons évaluer $\int f^{p_\lambda} = \int f^{(1-\lambda)p_0} f^{\lambda p_1}$.<br>Appliquons Hölder avec les exposants conjugués $u = \frac{1}{1-\lambda}$ et $v = \frac{1}{\lambda}$ (on a bien $1/u + 1/v = 1-\lambda + \lambda = 1$).<br>$\int f^{p_\lambda} \le \left( \int (f^{(1-\lambda)p_0})^{\frac{1}{1-\lambda}} \right)^{1-\lambda} \left( \int (f^{\lambda p_1})^{\frac{1}{\lambda}} \right)^{\lambda}$<br>$\int f^{p_\lambda} \le \left( \int f^{p_0} \right)^{1-\lambda} \left( \int f^{p_1} \right)^{\lambda}$.<br>En appliquant le logarithme naturel (strictement croissant) aux deux membres :<br>$\ln\left(\int f^{p_\lambda}\right) \le \ln\left( \left( \int f^{p_0} \right)^{1-\lambda} \left( \int f^{p_1} \right)^{\lambda} \right)$<br>$\ln\left(\int f^{p_\lambda}\right) \le (1-\lambda)\ln\left(\int f^{p_0}\right) + \lambda\ln\left(\int f^{p_1}\right)$.<br>Ce qui est exactement la définition de la convexité de la fonction $p \mapsto \ln(\int f^p d\mu)$.

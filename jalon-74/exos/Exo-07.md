---
title: "Exercice 7 : Application des Inégalités"
difficulty: "★★★★★"
---

# Exercice 7 : Application des Inégalités

**Niveau :** ★★★★★

**Énoncé :**
Utiliser Minkowski pour montrer que l'espace $L^p$ muni de sa norme est un espace normé (vérifier l'axiome de séparation et l'homogénéité).

**Correction Détaillée :**
Pour que $(L^p, \|\cdot\|_p)$ soit un espace vectoriel normé, il faut vérifier trois axiomes.<br>1. Séparation : $\|f\|_p = 0 \iff \int |f|^p = 0$. Comme l'intégrale d'une fonction positive n'est nulle que si la fonction est nulle presque partout, $f = 0$ p.p. C'est l'intérêt du quotient de l'espace $\mathcal{L}^p$ par la relation d'équivalence $f \sim g$ ssi $f = g$ p.p.<br>2. Homogénéité absolue : $\|\lambda f\|_p = (\int |\lambda f|^p)^{1/p} = (\int |\lambda|^p |f|^p)^{1/p} = (|\lambda|^p \int |f|^p)^{1/p} = |\lambda| \|f\|_p$.<br>3. Inégalité triangulaire : C'est exactement le théorème de Minkowski, $\|f+g\|_p \le \|f\|_p + \|g\|_p$.<br>Les trois axiomes sont vérifiés, l'espace $L^p$ (au sens du quotient) est bien un espace vectoriel normé.

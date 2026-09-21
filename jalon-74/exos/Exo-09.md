---
title: "Exercice 9 : Application des Inégalités"
difficulty: "★★★★★"
---

# Exercice 9 : Application des Inégalités

**Niveau :** ★★★★★

**Énoncé :**
Optimisation : Dans le cas de l'algorithme k-Means, montrer formellement par l'inégalité de Jensen que l'assignation d'un point au centroïde le plus proche minimise l'erreur quadratique sous une affectation de type distribution de probabilité molle.

**Correction Détaillée :**
L'erreur k-Means pour un point $x$ sous des probabilités d'affectation $q(k)$ telles que $\sum q(k) = 1$ est $\mathbb{E}_{k \sim q} [\|x - \mu_k\|^2] = \sum_k q(k) \|x - \mu_k\|^2$.<br>On cherche à minimiser cette quantité sur toutes les distributions $q$.<br>Soit $k^* = \arg\min_k \|x - \mu_k\|^2$.<br>Pour toute distribution $q$, comme $\|x - \mu_{k^*}\|^2 \le \|x - \mu_k\|^2$ pour tout $k$, on a par sommation (linéarité) :<br>$\sum_k q(k) \|x - \mu_{k^*}\|^2 \le \sum_k q(k) \|x - \mu_k\|^2$.<br>Comme $\sum_k q(k) = 1$, le terme de gauche vaut $\|x - \mu_{k^*}\|^2$.<br>Donc $\min_k \|x - \mu_k\|^2 \le \sum_k q(k) \|x - \mu_k\|^2$.<br>La borne inférieure est atteinte précisément par la distribution déterministe $q(k) = 1$ si $k=k^*$, et $0$ sinon.<br>Bien que ce soit un cas trivial d'optimisation linéaire sur un simplexe (qui est convexe), cela illustre comment des espérances (Jensen) sur des choix discrets forcent des solutions de type Dirac (Hard-assignement).

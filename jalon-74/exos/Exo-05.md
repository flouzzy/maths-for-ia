---
title: "Exercice 5 : Application des Inégalités"
difficulty: "★★★★☆"
---

# Exercice 5 : Application des Inégalités

**Niveau :** ★★★★☆

**Énoncé :**
Démontrer que sur un espace probabilisé, la norme $L^p$ d'une variable aléatoire $X$ est une fonction croissante de $p$ : $\|X\|_p \le \|X\|_q$ pour $1 \le p \le q$.

**Correction Détaillée :**
On souhaite montrer que $\left(\int |X|^p dP\right)^{1/p} \le \left(\int |X|^q dP\right)^{1/q}$ sachant $\int 1 dP = 1$.<br>Considérons la fonction $\phi(t) = |t|^{q/p}$. Comme $q/p \ge 1$, sa dérivée seconde contient un facteur $\frac{q}{p}(\frac{q}{p}-1) \ge 0$, donc $\phi$ est convexe sur $\mathbb{R}$.<br>Appliquons l'inégalité de Jensen à la variable aléatoire $Y = |X|^p$ avec la fonction $\phi$ :<br>$\phi(\mathbb{E}[Y]) \le \mathbb{E}[\phi(Y)]$.<br>Ceci se traduit par : $(\mathbb{E}[|X|^p])^{q/p} \le \mathbb{E}[(|X|^p)^{q/p}] = \mathbb{E}[|X|^q]$.<br>En prenant la puissance $1/q$ des deux côtés, on obtient :<br>$(\mathbb{E}[|X|^p])^{1/p} \le (\mathbb{E}[|X|^q])^{1/q}$.<br>Soit exactement $\|X\|_p \le \|X\|_q$.<br>Note : ce résultat nécessite que la mesure totale soit 1 (ou finie avec ajustement).

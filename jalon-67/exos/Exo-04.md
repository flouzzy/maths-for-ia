---
title: "Exercice 4 : TCM"
difficulty: "★★☆☆☆"
---
# Exercice 4 : Indice de Gini et TCM

**Niveau :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
Dans un modèle de répartition des richesses, on étudie une suite de densités croissantes $f_n(x) = \frac{n}{n+1} x^{n-1} \mathbf{1}_{[0,1]}(x)$. Que dire de la limite de l'intégrale vs l'intégrale de la limite ?

**Correction détaillée :**
1. Étudions la limite ponctuelle de $f_n(x)$. Pour $x \in [0, 1[$, $x^{n-1} \to 0$, donc $f(x) = 0$. Pour $x=1$, $f_n(1) = \frac{n}{n+1} \to 1$. La limite p.p. est la fonction nulle, d'intégrale $0$.
2. Calculons $\int_0^1 f_n(x) dx = \frac{n}{n+1} \left[\frac{x^n}{n}\right]_0^1 = \frac{1}{n+1}$.
3. La limite des intégrales est $\lim_{n \to \infty} \frac{1}{n+1} = 0$.
4. On a bien égalité $0=0$. Pourquoi Beppo-Levi ne s'applique-t-il pas directement pour le prouver ? Parce que la suite n'est pas croissante p.p ! En effet $f_2(x) = \frac{2}{3}x$ et $f_3(x) = \frac{3}{4}x^2$. Pour $x=1/2$, $f_2(1/2)=1/3 > f_3(1/2)=3/16$. L'égalité ici est fortuite par rapport aux hypothèses du TCM.

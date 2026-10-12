# Exercice 5 : Variables aléatoires et indépendance

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soient $X$ et $Y$ deux variables aléatoires indépendantes qui suivent toutes les deux une loi de Bernoulli de paramètre $p = \frac{1}{2}$.
Considérons une nouvelle variable aléatoire $Z$ définie par $Z = |X - Y|$.
1. Déterminer la loi de probabilité de la variable $Z$.
2. Les variables aléatoires $X$ et $Z$ sont-elles indépendantes ? Démontrez rigoureusement votre réponse.

---
**Correction détaillée :**

**Question 1 : Loi de $Z$**
Les variables $X$ et $Y$ sont indépendantes et de loi $\mathcal{B}(1/2)$. Leurs valeurs possibles sont $\{0, 1\}$.
L'univers du couple $(X,Y)$ possède 4 issues équiprobables (probabilité $1/4$ pour chacune, par indépendance).
Calculons la valeur de $Z = |X - Y|$ pour chaque issue :
- Si $X = 0, Y = 0$, alors $Z = |0 - 0| = 0$. (Probabilité $1/4$)
- Si $X = 1, Y = 0$, alors $Z = |1 - 0| = 1$. (Probabilité $1/4$)
- Si $X = 0, Y = 1$, alors $Z = |0 - 1| = 1$. (Probabilité $1/4$)
- Si $X = 1, Y = 1$, alors $Z = |1 - 1| = 0$. (Probabilité $1/4$)

Pour déterminer la loi de $Z$, sommons les probabilités pour chaque valeur possible :
- $\mathbb{P}(Z = 0) = \mathbb{P}(X=0, Y=0) + \mathbb{P}(X=1, Y=1) = \frac{1}{4} + \frac{1}{4} = \frac{1}{2}$
- $\mathbb{P}(Z = 1) = \mathbb{P}(X=1, Y=0) + \mathbb{P}(X=0, Y=1) = \frac{1}{4} + \frac{1}{4} = \frac{1}{2}$
Ainsi, $Z$ suit également une loi de Bernoulli de paramètre $p = \frac{1}{2}$.

**Question 2 : Indépendance de $X$ et $Z$**
Pour que deux variables aléatoires discrètes $X$ et $Z$ soient indépendantes, il faut que pour toutes valeurs $x, z$, on ait $\mathbb{P}(X=x, Z=z) = \mathbb{P}(X=x) \times \mathbb{P}(Z=z)$.
Testons avec $X = 0$ et $Z = 0$.
- Probabilités marginales : $\mathbb{P}(X=0) = \frac{1}{2}$ et $\mathbb{P}(Z=0) = \frac{1}{2}$.
- Leur produit : $\mathbb{P}(X=0) \times \mathbb{P}(Z=0) = \frac{1}{4}$.
Maintenant, calculons la probabilité conjointe $\mathbb{P}(X=0 \text{ et } Z=0)$.
L'événement $\{X=0 \text{ et } Z=0\}$ se produit si et seulement si $X=0$ et $|X-Y|=0$, ce qui implique $X=0$ et $Y=0$.
Or, nous savons que $\mathbb{P}(X=0 \text{ et } Y=0) = \frac{1}{4}$.
Ainsi, $\mathbb{P}(X=0, Z=0) = \frac{1}{4}$.
Vérifions les autres combinaisons :
- $\mathbb{P}(X=0, Z=1) = \mathbb{P}(X=0 \text{ et } Y=1) = \frac{1}{4} = \mathbb{P}(X=0)\mathbb{P}(Z=1)$
- $\mathbb{P}(X=1, Z=0) = \mathbb{P}(X=1 \text{ et } Y=1) = \frac{1}{4} = \mathbb{P}(X=1)\mathbb{P}(Z=0)$
- $\mathbb{P}(X=1, Z=1) = \mathbb{P}(X=1 \text{ et } Y=0) = \frac{1}{4} = \mathbb{P}(X=1)\mathbb{P}(Z=1)$

Dans tous les cas possibles, la relation de factorisation tient.
Par conséquent, bien que $Z$ ait été construite de manière déterministe à partir de $X$ (et de $Y$), les variables aléatoires $X$ et $Z$ sont parfaitement indépendantes ! (Ce résultat est une propriété remarquable liée à la symétrie de la loi uniforme sur le groupe additif modulo 2). $\blacksquare$

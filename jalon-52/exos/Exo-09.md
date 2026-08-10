---
title: "Continuité sur le produit cartésien"
difficulty: $\bigstar\bigstar\bigstar\bigstar\bigstar$
---

# Exercice 09 : Continuité sur le produit cartésien
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soient $X, Y, Z$ trois espaces topologiques. Soit $f : Z \to X \times Y$ une application définie par $f(z) = (f_1(z), f_2(z))$, où $f_1 : Z \to X$ et $f_2 : Z \to Y$. L'espace $X \times Y$ est muni de la topologie produit.
Montrer que $f$ est continue si et seulement si ses composantes $f_1$ et $f_2$ sont continues.

**Correction Détaillée :**
1. **Rappel :** La topologie produit sur $X \times Y$ a pour prébase les ensembles de la forme $U \times Y$ et $X \times V$ avec $U$ ouvert de $X$ et $V$ ouvert de $Y$. Les projections $\pi_1(x,y)=x$ et $\pi_2(x,y)=y$ sont continues par construction.

2. **Sens ($\implies$) :** Si $f$ est continue, alors $f_1 = \pi_1 \circ f$ est la composée de deux applications continues, donc $f_1$ est continue. De même, $f_2 = \pi_2 \circ f$ est continue.

3. **Sens ($\impliedby$) :** Supposons $f_1$ et $f_2$ continues.
Soit $W$ un ouvert sous-basique de la topologie produit. On peut prendre $W = U \times Y$ (un cas symétrique s'applique pour $X \times V$).
L'image réciproque par $f$ est :
$$ f^{-1}(U \times Y) = \{ z \in Z \mid f_1(z) \in U \text{ et } f_2(z) \in Y \} = f_1^{-1}(U) \cap f_2^{-1}(Y) = f_1^{-1}(U) \cap Z = f_1^{-1}(U) $$
Puisque $f_1$ est continue et $U$ est ouvert dans $X$, $f_1^{-1}(U)$ est ouvert dans $Z$.
La pré-image de tout ouvert sous-basique étant un ouvert, on conclut classiquement que $f$ est continue sur l'espace produit (l'image réciproque d'une intersection finie d'ouverts sous-basiques et d'une union d'intersections est ouverte).

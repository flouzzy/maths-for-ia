\subsection*{Exercice 4 : Produit de variables de Rademacher \quad $\bigstar\bigstar\star\star\star$}

Soient $X$ et $Y$ deux variables aléatoires indépendantes suivant la loi de Rademacher, c'est-à-dire $\mathbb{P}(X = 1) = \mathbb{P}(X = -1) = 1/2$. On pose $Z = XY$.
1. Déterminer la loi de $Z$.
2. Les variables $X$ et $Z$ sont-elles indépendantes ?

**Correction :**
1. Loi de $Z$ :
   - $Z = 1$ s'il y a un nombre pair de signes négatifs, soit $(X=1, Y=1)$ ou $(X=-1, Y=-1)$.
   - $\mathbb{P}(Z = 1) = \mathbb{P}(X=1)\mathbb{P}(Y=1) + \mathbb{P}(X=-1)\mathbb{P}(Y=-1) = (1/2)(1/2) + (1/2)(1/2) = 1/2$.
   - $Z = -1$ s'il y a un seul signe négatif. $\mathbb{P}(Z = -1) = 1 - \mathbb{P}(Z=1) = 1/2$.
   - Donc $Z$ suit également une loi de Rademacher.
2. Indépendance de $X$ et $Z$ :
   - On doit vérifier si $\mathbb{P}(X=i, Z=j) = \mathbb{P}(X=i)\mathbb{P}(Z=j)$ pour tous $i, j \in \{-1, 1\}$.
   - Prenons $i = 1$ et $j = 1$. $\mathbb{P}(X=1, Z=1) = \mathbb{P}(X=1, Y=1) = 1/4$.
   - D'autre part, $\mathbb{P}(X=1)\mathbb{P}(Z=1) = (1/2) \times (1/2) = 1/4$.
   - En vérifiant pour toutes les combinaisons, on trouve l'égalité partout. $X$ et $Z$ sont indépendantes.
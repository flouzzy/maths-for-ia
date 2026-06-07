# Exercice 1 : Calcul de la fonction de répartition empirique
**Énoncé :** Soit un échantillon de 5 observations réelles $S = (1.2, 3.4, 1.2, 5.0, 2.8)$. Calculer et tracer la fonction de répartition empirique $F_n(t)$ associée à cet échantillon.

**Correction Détaillée :**
* *Analyse de l'énoncé :* La fonction de répartition empirique $F_n(t)$ est définie comme la proportion d'observations de l'échantillon qui sont inférieures ou égales à $t$.
* *Résolution pas-à-pas :*
  1. On ordonne d'abord l'échantillon par ordre croissant : $S_{trié} = (1.2, 1.2, 2.8, 3.4, 5.0)$. La taille de l'échantillon est $n=5$.
  2. Par définition, $F_n(t) = \frac{1}{n} \sum_{i=1}^n \mathbb{I}_{Z_i \le t}$.
  3. Calculons $F_n(t)$ pour les différents intervalles réels définis par les valeurs de l'échantillon :
     - Pour $t < 1.2$ : aucune observation n'est inférieure ou égale à $t$.
       $$F_n(t) = \frac{0}{5} = 0$$
     - Pour $1.2 \le t < 2.8$ : seules les deux premières observations (1.2 et 1.2) sont inférieures ou égales à $t$.
       $$F_n(t) = \frac{2}{5} = 0.4$$
     - Pour $2.8 \le t < 3.4$ : trois observations sont inférieures ou égales à $t$.
       $$F_n(t) = \frac{3}{5} = 0.6$$
     - Pour $3.4 \le t < 5.0$ : quatre observations sont inférieures ou égales à $t$.
       $$F_n(t) = \frac{4}{5} = 0.8$$
     - Pour $t \ge 5.0$ : toutes les cinq observations sont inférieures ou égales à $t$.
       $$F_n(t) = \frac{5}{5} = 1$$
  4. Le tracé de $F_n(t)$ est donc une fonction en escalier, continue à droite et avec des limites à gauche, possédant des sauts aux points d'observation (un saut de 0.4 en 1.2, et des sauts de 0.2 en 2.8, 3.4, et 5.0).

# Exercice 2 : Rectangle mesurable pathologique (★★☆☆☆)

**Énoncé :**
Sur $\mathbb{R}^2$, on considère la tribu produit $\mathcal{F} = \mathcal{P}(\mathbb{R}) \otimes \{\emptyset, \mathbb{R}\}$, où $\mathcal{P}(\mathbb{R})$ est l'ensemble des parties de $\mathbb{R}$.
1. Décrire exactement les ensembles qui appartiennent à cette tribu produit $\mathcal{F}$.
2. Le disque $D = \{(x,y) \in \mathbb{R}^2 \mid x^2+y^2 < 1\}$ appartient-il à $\mathcal{F}$ ?

**Correction :**
1. Par définition, les rectangles mesurables de cet espace produit sont de la forme $A_1 \times A_2$ avec $A_1 \in \mathcal{P}(\mathbb{R})$ (donc $A_1$ est une partie quelconque de $\mathbb{R}$) et $A_2 \in \{\emptyset, \mathbb{R}\}$.
   - Si $A_2 = \emptyset$, alors $A_1 \times A_2 = \emptyset$.
   - Si $A_2 = \mathbb{R}$, alors $A_1 \times \mathbb{R} = \{(x,y) \mid x \in A_1, y \in \mathbb{R}\}$.
   La classe des rectangles générateurs est $\mathcal{R} = \{\emptyset\} \cup \{A \times \mathbb{R} \mid A \subset \mathbb{R}\}$.
   Il se trouve que cette classe $\mathcal{R}$ est déjà une tribu !
   Vérifions-le :
   - $\emptyset \in \mathcal{R}$.
   - Stable par complémentaire : le complémentaire de $A \times \mathbb{R}$ dans $\mathbb{R}^2$ est $A^c \times \mathbb{R}$, qui est bien dans $\mathcal{R}$ car $A^c \subset \mathbb{R}$.
   - Stable par union dénombrable : $\bigcup_n (A_n \times \mathbb{R}) = (\bigcup_n A_n) \times \mathbb{R}$, qui est bien dans $\mathcal{R}$.
   Par conséquent, la tribu engendrée est la classe elle-même : $\mathcal{F} = \{A \times \mathbb{R} \mid A \subset \mathbb{R}\}$. Les ensembles mesurables sont des "bandes verticales" (infinies en $y$).
2. Le disque $D$ n'est pas une "bande verticale" infinie en $y$. Par exemple, le point $(0, 0) \in D$, donc la section en $x=0$ de $D$ est $]-1, 1[$. Mais pour un ensemble de la tribu $\mathcal{F}$, ses sections (non vides) selon $y$ doivent être égales à $\mathbb{R}$. Or $]-1, 1[ \neq \mathbb{R}$.
   Par conséquent, le disque $D$ n'appartient pas à la tribu produit $\mathcal{F}$.

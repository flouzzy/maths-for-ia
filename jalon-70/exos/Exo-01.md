# Exercice 1 : Section d'un triangle mesurable (★☆☆☆☆)

**Énoncé :**
Dans le plan $\mathbb{R}^2$ muni de sa tribu borélienne $\mathcal{B}(\mathbb{R}^2)$, on considère le triangle $T = \{(x, y) \in \mathbb{R}^2 \mid 0 \leq x \leq 1, 0 \leq y \leq 2x\}$.
1. Montrer que $T$ est un borélien.
2. Pour un $x \in \mathbb{R}$ fixé, déterminer explicitement la section $T_x = \{y \in \mathbb{R} \mid (x,y) \in T\}$.
3. Pour un $y \in \mathbb{R}$ fixé, déterminer explicitement la section $T^y = \{x \in \mathbb{R} \mid (x,y) \in T\}$.

**Correction :**
1. L'ensemble $T$ s'écrit comme l'intersection de trois demi-plans : $T = \{x \geq 0\} \cap \{x \leq 1\} \cap \{2x - y \geq 0\}$. Les applications $(x,y) \mapsto x$ et $(x,y) \mapsto 2x-y$ étant continues de $\mathbb{R}^2$ dans $\mathbb{R}$, les images réciproques d'intervalles fermés sont des fermés de $\mathbb{R}^2$. $T$, étant une intersection finie de fermés, est un fermé. Or tout fermé de $\mathbb{R}^2$ est un borélien, donc $T \in \mathcal{B}(\mathbb{R}^2)$.
2. Fixons $x \in \mathbb{R}$. Par définition, on cherche les $y$ tels que $0 \leq x \leq 1$ et $0 \leq y \leq 2x$.
   - Si $x \notin [0,1]$, alors la condition $0 \leq x \leq 1$ est violée, donc $T_x = \emptyset$.
   - Si $x \in [0,1]$, alors la condition sur $y$ donne $T_x = [0, 2x]$.
   Dans tous les cas, $T_x$ est bien un borélien de $\mathbb{R}$ (intervalle ou ensemble vide).
3. Fixons $y \in \mathbb{R}$. On cherche les $x$ tels que $0 \leq x \leq 1$ et $0 \leq y \leq 2x$, ce qui équivaut à $x \geq y/2$.
   - Si $y < 0$, les $x$ doivent vérifier $0 \leq x \leq 1$ (car $x \geq y/2$ est automatique si $x \geq 0$), donc $T^y = [0,1]$.
   *(Correction : attention, si $y<0$, la condition $0 \leq y \leq 2x$ force $y \geq 0$, or $y<0$, c'est impossible. Donc $T^y = \emptyset$.)*
   Reprenons : il faut $y \geq 0$ ET $y/2 \leq x \leq 1$.
   - Si $y < 0$ ou $y > 2$ (car si $x \leq 1$, $2x \leq 2$), $T^y = \emptyset$.
   - Si $y \in [0, 2]$, alors $T^y = [\frac{y}{2}, 1]$.
   Dans tous les cas, $T^y$ est un borélien de $\mathbb{R}$.

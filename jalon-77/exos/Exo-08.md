# Exercice 8 : Produit scalaire dans $L^2$ et régularisation $\star\star\star\star\star$

**Énoncé :**
Montrer que si $f \in L^2(\mathbb{R})$ vérifie $\int_{\mathbb{R}} f(x)\varphi(x) \, dx = 0$ pour tout $\varphi \in C_c^\infty(\mathbb{R})$, alors $f = 0$ presque partout.

**Correction détaillée :**
Cette preuve souligne l'importance des fonctions tests (l'espace $\mathcal{D}(\mathbb{R})$) pour "lire" les éléments de $L^2$.
1. Soit $f \in L^2(\mathbb{R})$ satisfaisant l'hypothèse de l'énoncé. On note $\langle u, v \rangle_{L^2} = \int_{\mathbb{R}} u(x)v(x) \, dx$ le produit scalaire sur $L^2(\mathbb{R})$ (fonctions à valeurs réelles).
L'hypothèse indique que $f$ est orthogonale à tous les sous-espaces engendrés par les fonctions tests : $\langle f, \varphi \rangle_{L^2} = 0$, $\forall \varphi \in C_c^\infty(\mathbb{R})$.
2. Par le théorème fondamental, $C_c^\infty(\mathbb{R})$ est un sous-espace dense dans l'espace de Hilbert $L^2(\mathbb{R})$.
3. Rappel d'un résultat général sur les espaces de Hilbert : Soit $H$ un espace de Hilbert et $V$ un sous-espace vectoriel de $H$. L'orthogonal $V^\perp$ se réduit au vecteur nul $\{0\}$ si et seulement si $V$ est dense dans $H$.
4. Ici, posons $H = L^2(\mathbb{R})$ et $V = C_c^\infty(\mathbb{R})$.
Comme $V$ est dense dans $H$ par théorème d'approximation, $V^\perp = \{0\}$.
5. L'hypothèse de l'exercice affirme précisément que $f \in V^\perp$.
On déduit immédiatement que $f = 0$ en tant qu'élément de $L^2(\mathbb{R})$.
Par définition des espaces $L^p$, l'élément nul est la classe d'équivalence des fonctions nulles presque partout. Donc $f = 0$ presque partout. $\blacksquare$

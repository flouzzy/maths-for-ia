## Exercice 3 : La section d'un mesurable \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $E = \{ (x,y) \in [0,1]^2 \mid x^2 + y^2 \le 1 \}$.
Montrer que $E \in \mathcal{B}(\mathbb{R}) \otimes \mathcal{B}(\mathbb{R})$ et décrire formellement la section $E_x$ pour $x \in \mathbb{R}$.

**Correction :**
1. La fonction $f(x,y) = x^2 + y^2$ est continue sur $\mathbb{R}^2$, donc mesurable par rapport à $\mathcal{B}(\mathbb{R}^2)$.
2. L'ensemble $E = f^{-1}([0, 1]) \cap ([0,1] \times [0,1])$ est l'intersection de deux fermés, donc un borélien de $\mathbb{R}^2$. On rappelle que $\mathcal{B}(\mathbb{R}^2) = \mathcal{B}(\mathbb{R}) \otimes \mathcal{B}(\mathbb{R})$.
3. Pour un $x \in \mathbb{R}$ fixé :
   - Si $x \notin [0, 1]$, alors $E_x = \emptyset$.
   - Si $x \in [0, 1]$, alors on cherche les $y \in [0, 1]$ tels que $y^2 \le 1 - x^2$. Comme $y \ge 0$, on obtient $0 \le y \le \sqrt{1 - x^2}$.
   - Donc $E_x = [0, \sqrt{1 - x^2}]$.

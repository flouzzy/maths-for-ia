# Exercice 5 : Équivalence des normes en dimension finie
$\bigstar$\bigstar$\bigstar\star\star$

**Énoncé :**
Rappeler la preuve que sur $\mathbb{R}^n$, la norme $\| \cdot \|_1$ et la norme $\| \cdot \|_2$ sont équivalentes. L'identité entre ces deux espaces normés est-elle continue ?

**Correction Détaillée :**
1. Soit $x \in \mathbb{R}^n$. $\|x\|_2 = (\sum x_i^2)^{1/2} \le (\sum x_i^2 + \sum_{i \neq j} |x_i||x_j|)^{1/2} = \sum |x_i| = \|x\|_1$.
2. Par Cauchy-Schwarz, $\|x\|_1 = \sum 1 \cdot |x_i| \le (\sum 1^2)^{1/2} (\sum x_i^2)^{1/2} = \sqrt{n} \|x\|_2$.
3. Donc $\|x\|_2 \le \|x\|_1 \le \sqrt{n} \|x\|_2$. Les normes sont équivalentes.
4. L'application identité de $(\mathbb{R}^n, \|\cdot\|_1)$ vers $(\mathbb{R}^n, \|\cdot\|_2)$ est donc continue, de norme au plus 1.

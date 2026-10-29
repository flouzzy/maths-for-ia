# Exercice 3 : Limite Simple de Formes Linéaires Continues
$\bigstar\bigstar\star\star\star$
**Énoncé :**
Soit $E$ un espace de Banach et $(f_n)_{n \in \mathbb{N}}$ une suite de formes linéaires continues sur $E$.
On suppose que pour tout $x \in E$, la suite $(f_n(x))_{n \in \mathbb{N}}$ converge dans $\mathbb{K}$ vers une limite notée $f(x)$.
Démontrer que la forme linéaire limite $f$ est continue.

**Correction :**
1. Linéarité de $f$ :
   Pour tous $x, y \in E$ et $\lambda \in \mathbb{K}$,
   $f(\lambda x + y) = \lim_{n \to \infty} f_n(\lambda x + y) = \lim_{n \to \infty} (\lambda f_n(x) + f_n(y)) = \lambda f(x) + f(y)$.
   Donc $f$ est bien une forme linéaire.
2. Bornitude ponctuelle :
   Pour tout $x \in E$, la suite $(f_n(x))$ est convergente, donc elle est bornée.
   Il existe $M_x > 0$ tel que $\forall n, |f_n(x)| \le M_x$.
3. Application de Banach-Steinhaus :
   $E$ est de Banach. Les $f_n$ sont continues et ponctuellement bornées.
   Donc il existe $M > 0$ tel que $\forall n, \|f_n\| \le M$.
4. Continuité de $f$ :
   Soit $x \in E$ tel que $\|x\| \le 1$.
   Pour tout $n$, $|f_n(x)| \le \|f_n\| \|x\| \le M \|x\|$.
   En passant à la limite quand $n \to \infty$, $|f(x)| \le M \|x\|$.
   Ceci prouve que $f$ est bornée sur la boule unité fermée, donc continue, et $\|f\| \le M$.
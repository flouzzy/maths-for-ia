## Exercice 4 : Distance induite par une fonction continue croissante \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $(X, d)$ un espace métrique. On pose $d'(x, y) = \frac{d(x, y)}{1 + d(x, y)}$.
Montrer que $d'$ est une distance sur $X$.

**Correction :**
La fonction $f(t) = \frac{t}{1+t} = 1 - \frac{1}{1+t}$ est strictement croissante sur $\mathbb{R}_+$.
1. **Séparation :**
   $d'(x,y) = 0 \iff \frac{d(x,y)}{1+d(x,y)} = 0 \iff d(x,y) = 0 \iff x = y$.
2. **Symétrie :**
   L'expression dépend uniquement de $d(x,y)$, qui est symétrique, donc $d'(x,y) = d'(y,x)$.
3. **Inégalité triangulaire :**
   Pour $x,y,z \in X$, notons $a=d(x,y)$, $b=d(y,z)$ et $c=d(x,z)$. On sait que $c \le a+b$.
   Puisque $f$ est croissante, $f(c) \le f(a+b)$.
   $f(a+b) = \frac{a+b}{1+a+b} = \frac{a}{1+a+b} + \frac{b}{1+a+b}$.
   Comme $1+a+b \ge 1+a$ et $1+a+b \ge 1+b$ (car $a,b \ge 0$), on a :
   $\frac{a}{1+a+b} \le \frac{a}{1+a}$ et $\frac{b}{1+a+b} \le \frac{b}{1+b}$.
   En sommant, $f(a+b) \le \frac{a}{1+a} + \frac{b}{1+b} = f(a) + f(b)$.
   Donc $f(c) \le f(a) + f(b)$, ce qui équivaut à $d'(x,z) \le d'(x,y) + d'(y,z)$. $\blacksquare$

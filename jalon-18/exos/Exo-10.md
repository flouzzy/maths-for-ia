# Exercice 10 : La fonction de Thomae : un défi à la continuité

En tant que Professeur Émérite, je vous propose un exercice qui mettra à l'épreuve votre compréhension la plus fine de la notion de continuité. La fonction que nous allons étudier, souvent appelée fonction de Thomae ou fonction du popcorn, est un exemple canonique en analyse réelle, réputé pour ses propriétés de continuité singulières.

---

### Énoncé théorique précis

Soit $f: \mathbb{R} \to \mathbb{R}$ la fonction définie comme suit :
$$ f(x) = \begin{cases} 0 & \text{si } x \in \mathbb{R} \setminus \mathbb{Q} \text{ (c'est-à-dire } x \text{ est irrationnel) ou } x=0 \\ 1/q & \text{si } x = p/q \text{ est un nombre rationnel non nul, où } p \in \mathbb{Z}, q \in \mathbb{N}^* \text{, et } p/q \text{ est écrit sous forme irréductible (c'est-à-dire } \text{pgcd}(p,q)=1 \text{ et } q>0) \end{cases} $$

Par exemple, $f(\sqrt{2}) = 0$, $f(0) = 0$, $f(1/2) = 1/2$, $f(3/4) = 1/4$, $f(6/8) = f(3/4) = 1/4$, $f(5) = f(5/1) = 1/1 = 1$.

**Questions :**

1.  Démontrer que la fonction $f$ est discontinue en tout point $x_0 \in \mathbb{Q}^*$ (c'est-à-dire en tout nombre rationnel non nul).
2.  Démontrer que la fonction $f$ est continue en tout point $x_0 \in \mathbb{R} \setminus \mathbb{Q}$ (c'est-à-dire en tout nombre irrationnel).
3.  Démontrer que la fonction $f$ est continue en $x_0 = 0$.

---

### Corrigé exhaustif

Nous allons aborder chaque question avec la rigueur nécessaire, en utilisant les définitions formelles de la continuité et de la discontinuité.

#### 1. Discontinuité en tout point $x_0 \in \mathbb{Q}^*$

Soit $x_0 \in \mathbb{Q}^*$. Par définition, $x_0$ peut s'écrire sous la forme $p_0/q_0$ où $p_0 \in \mathbb{Z}^*$, $q_0 \in \mathbb{N}^*$, et $\text{pgcd}(p_0,q_0)=1$.
D'après la définition de la fonction $f$, nous avons $f(x_0) = 1/q_0$. Puisque $q_0 \ge 1$, il s'ensuit que $f(x_0) > 0$.

Pour démontrer la discontinuité de $f$ en $x_0$, nous allons utiliser la caractérisation séquentielle de la continuité. Une fonction $f$ est discontinue en $x_0$ s'il existe une suite $(x_n)_{n \in \mathbb{N}}$ telle que $x_n \to x_0$ mais $f(x_n) \not\to f(x_0)$.

Nous savons que l'ensemble des nombres irrationnels est dense dans $\mathbb{R}$. Cela signifie que pour tout $x_0 \in \mathbb{R}$ et pour tout $\delta > 0$, l'intervalle $(x_0 - \delta, x_0 + \delta)$ contient au moins un nombre irrationnel. Par conséquent, nous pouvons construire une suite $(x_n)_{n \in \mathbb{N}}$ de nombres irrationnels telle que $x_n \to x_0$.

Pour chaque terme $x_n$ de cette suite, puisque $x_n$ est irrationnel, la définition de $f$ nous donne $f(x_n) = 0$.
Calculons la limite de $f(x_n)$ lorsque $n \to \infty$:
$$ \lim_{n \to \infty} f(x_n) = \lim_{n \to \infty} 0 = 0 $$
Cependant, nous avons $f(x_0) = 1/q_0$. Puisque $x_0 \in \mathbb{Q}^*$, $p_0 \neq 0$, et $q_0 \ge 1$, donc $1/q_0 > 0$.
Ainsi, $\lim_{n \to \infty} f(x_n) = 0 \neq 1/q_0 = f(x_0)$.

Puisque nous avons trouvé une suite $(x_n)$ convergeant vers $x_0$ telle que la suite $(f(x_n))$ ne converge pas vers $f(x_0)$, nous concluons que la fonction $f$ est discontinue en tout point $x_0 \in \mathbb{Q}^*$.

#### 2. Continuité en tout point $x_0 \in \mathbb{R} \setminus \mathbb{Q}$

Soit $x_0 \in \mathbb{R} \setminus \mathbb{Q}$ (c'est-à-dire $x_0$ est un nombre irrationnel).
D'après la définition de la fonction $f$, nous avons $f(x_0) = 0$.

Pour démontrer la continuité de $f$ en $x_0$, nous allons utiliser la définition $\epsilon-\delta$. Nous devons montrer que pour tout $\epsilon > 0$, il existe un $\delta > 0$ tel que pour tout $x \in \mathbb{R}$, si $|x - x_0| < \delta$, alors $|f(x) - f(x_0)| < \epsilon$.
Puisque $f(x_0)=0$, cela revient à montrer que $|f(x)| < \epsilon$.

Soit $\epsilon > 0$ donné.
Nous devons trouver un $\delta > 0$.
L'idée est de s'assurer que si $x$ est proche de $x_0$, alors $f(x)$ est petit.
Si $x$ est irrationnel, alors $f(x) = 0$, et $|f(x)| = 0 < \epsilon$ est toujours vrai.
Si $x$ est rationnel, $x = p/q$ sous forme irréductible ($p \in \mathbb{Z}^*$, $q \in \mathbb{N}^*$), alors $f(x) = 1/q$. Pour que $|f(x)| < \epsilon$, il faut que $1/q < \epsilon$, ce qui est équivalent à $q > 1/\epsilon$.

Choisissons un entier naturel $N$ tel que $N > 1/\epsilon$. (Par exemple, $N = \lfloor 1/\epsilon \rfloor + 1$ si $\epsilon > 0$).
Considérons l'ensemble $S_N$ des nombres rationnels $p/q$ (sous forme irréductible) dont le dénominateur $q$ est inférieur ou égal à $N$.
$$ S_N = \{ p/q \in \mathbb{Q} \mid p \in \mathbb{Z}^*, q \in \{1, 2, \dots, N\}, \text{pgcd}(p,q)=1 \} $$
Nous allons restreindre notre recherche de $x$ à un intervalle borné autour de $x_0$, par exemple $(x_0-1, x_0+1)$.
Considérons l'ensemble $K_N = S_N \cap (x_0-1, x_0+1)$.
Pour chaque $q \in \{1, 2, \dots, N\}$, il n'y a qu'un nombre fini d'entiers $p$ tels que $x_0-1 < p/q < x_0+1$, c'est-à-dire $q(x_0-1) < p < q(x_0+1)$.
Par conséquent, l'ensemble $K_N$ est un ensemble fini de nombres rationnels.

Puisque $x_0$ est irrationnel, $x_0$ n'appartient à aucun ensemble de nombres rationnels, et donc $x_0 \notin K_N$.
Soit $K_N = \{r_1, r_2, \dots, r_M\}$ les éléments de $K_N$.
Définissons $\delta$ comme la plus petite distance entre $x_0$ et les éléments de $K_N$:
$$ \delta = \min \{ |x_0 - r_j| \mid r_j \in K_N \} $$
Puisque $x_0 \notin K_N$, toutes les distances $|x_0 - r_j|$ sont strictement positives. Par conséquent, $\delta > 0$.
Nous pouvons également nous assurer que $\delta \le 1$ en prenant $\delta = \min(1, \min \{ |x_0 - r_j| \mid r_j \in K_N \})$.

Maintenant, considérons un $x \in \mathbb{R}$ tel que $|x - x_0| < \delta$. Nous devons montrer que $|f(x)| < \epsilon$.

*   **Cas 1 : $x$ est irrationnel.**
    Dans ce cas, $f(x) = 0$. Donc $|f(x)| = 0 < \epsilon$. La condition est satisfaite.

*   **Cas 2 : $x$ est rationnel.**
    Soit $x = p/q$ sous forme irréductible ($p \in \mathbb{Z}^*$, $q \in \mathbb{N}^*$).
    Puisque $|x - x_0| < \delta$ et $\delta \le 1$, nous avons $|x - x_0| < 1$, ce qui implique $x \in (x_0-1, x_0+1)$.
    Par la construction de $\delta$, $x$ ne peut pas être un élément de $K_N$.
    Puisque $x \in (x_0-1, x_0+1)$ et $x \notin K_N$, cela signifie que $x$ n'est pas dans $S_N$.
    Si $x \notin S_N$, cela signifie que le dénominateur $q$ de $x$ (sous forme irréductible) doit être strictement supérieur à $N$.
    Donc, $q > N$.
    Alors, $f(x) = 1/q$. Puisque $q > N$, nous avons $1/q < 1/N$.
    Par notre choix de $N$, nous avons $N > 1/\epsilon$, ce qui implique $1/N < \epsilon$.
    Par conséquent, $f(x) < 1/N < \epsilon$.
    Ainsi, $|f(x)| < \epsilon$.

Dans les deux cas, nous avons montré que si $|x - x_0| < \delta$, alors $|f(x) - f(x_0)| < \epsilon$.
Par la définition $\epsilon-\delta$, la fonction $f$ est continue en tout point $x_0 \in \mathbb{R} \setminus \mathbb{Q}$.

#### 3. Continuité en $x_0 = 0$

Le point $x_0=0$ est un cas particulier de nombre rationnel. Cependant, la définition de $f$ spécifie explicitement $f(0)=0$.
Nous allons démontrer la continuité de $f$ en $x_0=0$ en utilisant la définition $\epsilon-\delta$.
Nous devons montrer que pour tout $\epsilon > 0$, il existe un $\delta > 0$ tel que pour tout $x \in \mathbb{R}$, si $|x - 0| < \delta$, c'est-à-dire $|x| < \delta$, alors $|f(x) - f(0)| < \epsilon$.
Puisque $f(0)=0$, cela revient à montrer que $|f(x)| < \epsilon$.

Soit $\epsilon > 0$ donné.
Nous devons trouver un $\delta > 0$.
L'argumentation est très similaire à celle utilisée pour les points irrationnels.
Choisissons un entier naturel $N$ tel que $N > 1/\epsilon$.
Considérons l'ensemble $S_N$ des nombres rationnels $p/q$ (sous forme irréductible) dont le dénominateur $q$ est inférieur ou égal à $N$.
$$ S_N = \{ p/q \in \mathbb{Q} \mid p \in \mathbb{Z}^*, q \in \{1, 2, \dots, N\}, \text{pgcd}(p,q)=1 \} $$
Notez que $0 \notin S_N$ car $p \in \mathbb{Z}^*$.
Considérons l'ensemble $K_N = S_N \cap (-1, 1)$. Cet ensemble est fini.
Soit $K_N = \{r_1, r_2, \dots, r_M\}$ les éléments de $K_N$.
Définissons $\delta$ comme la plus petite distance entre $0$ et les éléments de $K_N$:
$$ \delta = \min \{ |0 - r_j| \mid r_j \in K_N \} = \min \{ |r_j| \mid r_j \in K_N \} $$
Puisque $0 \notin K_N$, toutes les distances $|r_j|$ sont strictement positives. Par conséquent, $\delta > 0$.
Nous pouvons également nous assurer que $\delta \le 1$ en prenant $\delta = \min(1, \min \{ |r_j| \mid r_j \in K_N \})$.

Maintenant, considérons un $x \in \mathbb{R}$ tel que $|x| < \delta$. Nous devons montrer que $|f(x)| < \epsilon$.

*   **Cas 1 : $x$ est irrationnel ou $x=0$.**
    Dans ce cas, $f(x) = 0$. Donc $|f(x)| = 0 < \epsilon$. La condition est satisfaite.

*   **Cas 2 : $x$ est rationnel et $x \neq 0$.**
    Soit $x = p/q$ sous forme irréductible ($p \in \mathbb{Z}^*$, $q \in \mathbb{N}^*$).
    Puisque $|x| < \delta$ et $\delta \le 1$, nous avons $|x| < 1$, ce qui implique $x \in (-1, 1)$.
    Par la construction de $\delta$, $x$ ne peut pas être un élément de $K_N$.
    Puisque $x \in (-1, 1)$ et $x \notin K_N$, cela signifie que $x$ n'est pas dans $S_N$.
    Si $x \notin S_N$, cela signifie que le dénominateur $q$ de $x$ (sous forme irréductible) doit être strictement supérieur à $N$.
    Donc, $q > N$.
    Alors, $f(x) = 1/q$. Puisque $q > N$, nous avons $1/q < 1/N$.
    Par notre choix de $N$, nous avons $N > 1/\epsilon$, ce qui implique $1/N < \epsilon$.
    Par conséquent, $f(x) < 1/N < \epsilon$.
    Ainsi, $|f(x)| < \epsilon$.

Dans les deux cas, nous avons montré que si $|x - 0| < \delta$, alors $|f(x) - f(0)| < \epsilon$.
Par la définition $\epsilon-\delta$, la fonction $f$ est continue en $x_0 = 0$.

---

**Conclusion générale :** La fonction de Thomae est un exemple fascinant d'une fonction qui est continue en tous les points irrationnels et en $0$, mais discontinue en tous les points rationnels non nuls. Elle illustre de manière frappante la complexité de la notion de continuité et la différence fondamentale entre la densité des rationnels et des irrationnels sur la droite réelle.
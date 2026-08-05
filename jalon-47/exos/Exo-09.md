# Hessienne de la fonction Log-Sum-Exp

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $f : \mathbb{R}^n \to \mathbb{R}$ définie par $f(x) = \log\left(\sum_{i=1}^n e^{x_i}\right)$.
Cette fonction (Log-Sum-Exp) est fondamentale en machine learning.
1. Calculez son gradient $\nabla f(x)$.
2. Calculez sa Hessienne $H_f(x)$.
3. Montrez que $H_f(x)$ est semi-définie positive. Que cela signifie-t-il pour $f$ ?

**Correction mathématique détaillée :**

1. **Calcul du gradient :**
   Soit $S(x) = \sum_{j=1}^n e^{x_j}$. Alors $f(x) = \log(S(x))$.
   $\frac{\partial f}{\partial x_i} = \frac{1}{S(x)} \frac{\partial S}{\partial x_i} = \frac{e^{x_i}}{\sum_{j=1}^n e^{x_j}}$.
   Notons $p_i(x) = \frac{e^{x_i}}{\sum e^{x_j}}$. On remarque que $p(x) \in \mathbb{R}^n$ est le vecteur de la transformation softmax.
   $\nabla f(x) = p(x)$.

2. **Calcul de la Hessienne :**
   Il faut dériver $p_i(x)$ par rapport à $x_j$.
   - **Si $i = j$ :**
     $$\frac{\partial p_i}{\partial x_i} = \frac{e^{x_i} S(x) - e^{x_i} e^{x_i}}{S(x)^2} = p_i(x) - p_i(x)^2 = p_i(x)(1 - p_i(x))$$
   - **Si $i \neq j$ :**
     $$\frac{\partial p_i}{\partial x_j} = \frac{0 \cdot S(x) - e^{x_i} e^{x_j}}{S(x)^2} = - p_i(x) p_j(x)$$
   Sous forme matricielle, $H_f(x) = \text{Diag}(p(x)) - p(x)p(x)^T$.

3. **Caractère semi-défini positif :**
   Pour tout vecteur $v \in \mathbb{R}^n$, la forme quadratique associée est $v^T H_f(x) v$.
   $$v^T H_f(x) v = \sum_{i=1}^n p_i v_i^2 - (p^T v)^2$$
   Puisque les $p_i$ sont positifs et $\sum p_i = 1$, on peut voir cela comme une espérance sous la loi discrète $P$.
   $\sum p_i v_i^2 = \mathbb{E}[V^2]$ et $(p^T v)^2 = (\mathbb{E}[V])^2$.
   Donc $v^T H_f(x) v = \text{Var}(V)$.
   La variance d'une variable aléatoire étant toujours positive ou nulle, $H_f(x)$ est semi-définie positive pour tout $x$.
   Par conséquent, la fonction Log-Sum-Exp est globale convexe.

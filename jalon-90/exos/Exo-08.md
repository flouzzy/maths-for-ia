# Exercice 8 : Lien subtil entre L1 et probabilité avec condition de domination
$\bigstar\bigstar\bigstar\bigstar\star$


Soit $(X_n)$ une suite de variables aléatoires convergeant en probabilité vers une variable $X$. On suppose qu'il existe une variable aléatoire $Y \geq 0$ telle que pour tout $n$, $|X_n| \leq Y$ avec $\mathbb{E}[Y] < \infty$.
À l'aide d'une adaptation du théorème de convergence dominée, démontrez pas-à-pas que $X_n \xrightarrow{L^1} X$.

**Correction :**
1. On veut montrer que $\lim_{n\to\infty} \mathbb{E}[|X_n - X|] = 0$.
2. Posons $Z_n = |X_n - X|$. L'hypothèse $|X_n| \leq Y$ implique $|X| \leq Y$ (puisque les inégalités se préservent par limite en probabilité). L'inégalité triangulaire donne $Z_n \leq |X_n| + |X| \leq 2Y$.
3. Fixons un petit $\epsilon > 0$. On découpe l'espérance selon que $Z_n$ est grand ou petit :
$$ \mathbb{E}[Z_n] = \mathbb{E}[Z_n \mathbf{1}_{Z_n \leq \epsilon}] + \mathbb{E}[Z_n \mathbf{1}_{Z_n > \epsilon}] $$
4. Le premier terme est trivialement majoré :
$$ \mathbb{E}[Z_n \mathbf{1}_{Z_n \leq \epsilon}] \leq \epsilon \cdot \mathbb{P}(Z_n \leq \epsilon) \leq \epsilon $$
5. Pour le deuxième terme, on applique la majoration absolue par la variable dominante $Y$ :
$$ \mathbb{E}[Z_n \mathbf{1}_{Z_n > \epsilon}] \leq \mathbb{E}[2Y \mathbf{1}_{Z_n > \epsilon}] $$
6. Nous faisons face à l'espérance d'une variable positive. Nous définissons l'application qui à un événement associe l'intégrale de $Y$. Puisque $\mathbb{E}[Y] < \infty$, la mesure $\nu(A) = \int_A 2Y d\mathbb{P}$ est finie et absolument continue par rapport à $\mathbb{P}$. Ainsi, si $\mathbb{P}(A_n) \to 0$, alors $\nu(A_n) \to 0$.
7. L'événement considéré est $A_n = \{Z_n > \epsilon\}$. Or, l'hypothèse de l'exercice est que $X_n$ converge en probabilité vers $X$, donc $\lim_{n \to \infty} \mathbb{P}(Z_n > \epsilon) = 0$.
8. Ainsi $\lim_{n\to\infty}\mathbb{E}[2Y \mathbf{1}_{Z_n > \epsilon}] = 0$.
9. En combinant : $\limsup \mathbb{E}[Z_n] \leq \epsilon + 0$. Et ce, pour tout $\epsilon > 0$. On conclut que la limite est nulle, et la convergence $L^1$ est acquise.

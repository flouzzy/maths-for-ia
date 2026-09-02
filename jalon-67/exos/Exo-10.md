# Exo 10 : Équivalence de la mesurabilité ($\bigstar$\bigstar$\bigstar$\bigstar$\bigstar$)

## Énoncé
Soit $f : X \to [0, +\infty]$ une fonction. On définit $\mathcal{E}^+$ comme l'ensemble des fonctions étagées positives.
On définit $I_{sup}(f) = \sup \{ \int \varphi \, d\mu \mid \varphi \in \mathcal{E}^+, \varphi \le f \}$.
Le TCM stipule que si $f_n$ sont mesurables croissantes vers $f$, $\lim \int f_n = I_{sup}(f)$.
Montrer en utilisant le TCM que pour qu'une fonction soit Lebesgue-intégrable par rapport à une tribu, il est **nécessaire et suffisant** qu'elle soit la limite croissante d'une suite de fonctions étagées.

## Correction Détaillée
**Étape 1 : Condition Suffisante**
Soit $(s_n)$ une suite de fonctions étagées mesurables positives (donc $s_n \in \mathcal{E}^+$) et croissantes telles que $s_n(x) \to f(x)$.
La limite simple d'une suite de fonctions mesurables est mesurable (vu au Jalon 65). Comme $s_n$ sont mesurables, la limite $f$ l'est.
Le théorème de Beppo Levi garantit que $I_{sup}(f) = \lim \int s_n \, d\mu$.
La fonction $f$ vérifie ainsi parfaitement les critères de la théorie de Lebesgue.

**Étape 2 : Condition Nécessaire**
Soit $f$ une fonction mesurable à valeurs dans $[0, +\infty]$. Il faut construire explicitement une suite d'étagées croissantes vers $f$.
Définissons pour chaque entier $n \ge 1$ la partition de $[0, n]$ en $n 2^n$ intervalles de longueur $\frac{1}{2^n}$.
Pour $k$ de $0$ à $n 2^n - 1$, posons $E_{n,k} = \{ x \in X \mid \frac{k}{2^n} \le f(x) < \frac{k+1}{2^n} \}$.
Posons $F_n = \{x \in X \mid f(x) \ge n \}$.
Ces ensembles sont mesurables car $f$ est mesurable.
Définissons la fonction étagée :
$$ s_n(x) = \sum_{k=0}^{n 2^n - 1} \frac{k}{2^n} \mathbf{1}_{E_{n,k}}(x) + n \mathbf{1}_{F_n}(x) $$

**Étape 3 : Preuve de la convergence de $s_n$**
Fixons $x$.
- Si $f(x) = +\infty$, pour tout $n$, $f(x) \ge n$, donc $x \in F_n$, d'où $s_n(x) = n \to +\infty = f(x)$.
- Si $f(x) < +\infty$, il existe $N$ tel que $N > f(x)$. Pour tout $n \ge N$, $x \notin F_n$. $x$ appartiendra à l'un des sous-intervalles $E_{n,k}$, tel que $|f(x) - \frac{k}{2^n}| < \frac{1}{2^n}$.
Par conséquent, $0 \le f(x) - s_n(x) < \frac{1}{2^n}$. Lorsque $n \to \infty$, $s_n(x) \to f(x)$.

**Étape 4 : Croissance de la suite**
Passer de $n$ à $n+1$ revient à diviser chaque intervalle $[\frac{k}{2^n}, \frac{k+1}{2^n}[$ en deux intervalles de longueur moitié.
La valeur de $s_{n+1}(x)$ prendra soit la valeur $\frac{k}{2^n}$ (moitié gauche), soit $\frac{k+0.5}{2^n}$ (moitié droite).
Dans les deux cas, $s_{n+1}(x) \ge s_n(x) = \frac{k}{2^n}$. Sur l'ensemble $F_n$, le découpage est affine, assurant également que $s_{n+1}(x) \ge s_n(x)$.
La suite $(s_n)$ est donc une suite de fonctions étagées positives croissantes convergeant simplement vers $f$. C'est cette construction qui fonde la légitimité du TCM.

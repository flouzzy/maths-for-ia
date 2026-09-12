## L'ensemble des points de convergence \quad $\bigstar\bigstar\bigstar\star\star$

Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables sur $(X, \mathcal{F})$.
Montrez que l'ensemble de convergence $E = \{x \in X \mid \lim_{n \to \infty} f_n(x) \text{ existe dans } \mathbb{R}\}$ est un ensemble mesurable ($E \in \mathcal{F}$).

### Correction Détaillée

Une suite $(u_n)$ converge dans $\mathbb{R}$ si et seulement si c'est une suite de Cauchy.
Nous allons traduire le critère de Cauchy en une formule logique purement dénombrable pour utiliser les axiomes de la tribu.
La suite $(f_n(x))$ est de Cauchy si :
$$ \forall \varepsilon > 0, \exists N \in \mathbb{N}, \forall p, q \ge N, |f_p(x) - f_q(x)| \le \varepsilon $$

Pour éviter la non-dénombrabilité du quantificateur $\forall \varepsilon > 0$, on se restreint aux rationnels ou simplement aux $\varepsilon_k = \frac{1}{k}$ avec $k \in \mathbb{N}^*$. L'équivalence logique devient :
$$ x \in E \iff \forall k \ge 1, \exists N \in \mathbb{N}, \forall p \ge N, \forall q \ge N, |f_p(x) - f_q(x)| < \frac{1}{k} $$

Traduisons méticuleusement cela en termes d'ensembles :
- Le "pour tout $p \ge N, q \ge N$" devient une intersection dénombrable : $\bigcap_{p, q \ge N}$
- L'expression $|f_p(x) - f_q(x)| < \frac{1}{k}$ décrit un ensemble mesurable car $f_p, f_q$ sont mesurables et leur différence l'est. Notons cet ensemble $A_{p,q,k} = (f_p - f_q)^{-1}(]-\frac{1}{k}, \frac{1}{k}[) \in \mathcal{F}$.
- Le "il existe $N$" devient une union dénombrable : $\bigcup_{N \in \mathbb{N}}$
- Le "pour tout $k \ge 1$" devient une intersection dénombrable : $\bigcap_{k \ge 1}$

On synthétise :
$$ E = \bigcap_{k=1}^{\infty} \bigcup_{N=0}^{\infty} \bigcap_{p=N}^{\infty} \bigcap_{q=N}^{\infty} \left\{ x \in X \mid |f_p(x) - f_q(x)| < \frac{1}{k} \right\} $$

Puisque les tribus sont stables par intersection dénombrable et union dénombrable, cette vaste combinaison d'ensembles mesurables reste mesurable. Donc $E \in \mathcal{F}$.

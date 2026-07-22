# Exercice 4 : Comportement sur le bord du disque de convergence

**Énoncé :**
Déterminer le rayon de convergence $R$ de la série entière $\sum_{n \geq 1} \frac{z^n}{n}$. Étudier ensuite rigoureusement la nature de la convergence sur le bord du disque (pour $|z| = R$).

**Correction détaillée :**
1. **Calcul de $R$ :**
Soit $a_n = 1/n$. Appliquons le quotient de d'Alembert :
$$ \left| \frac{a_{n+1}}{a_n} \right| = \frac{n}{n+1} $$
Lorsque $n \to \infty$, la limite est clairement $L = 1$. Le rayon de convergence est donc $R = 1/1 = 1$.
Le disque ouvert de convergence est l'ensemble des $z \in \mathbb{C}$ tels que $|z| < 1$.

2. **Analyse sur la frontière $|z| = 1$ :**
Soit $z$ un nombre complexe de module $1$. Il peut s'écrire sous forme trigonométrique $z = e^{i\theta}$ avec $\theta \in [0, 2\pi[$.
- Cas $z = 1$ ($\theta = 0$) : La série s'évalue en $\sum_{n \geq 1} \frac{1^n}{n} = \sum_{n \geq 1} \frac{1}{n}$. C'est l'archétype de la série harmonique. L'intégrale de comparaison $\int_{1}^{N} dx/x = \ln(N)$ diverge vers l'infini, donc la série harmonique est divergente.
- Cas $z \neq 1$ ($\theta \in ]0, 2\pi[$) : La série est $\sum_{n \geq 1} \frac{e^{in\theta}}{n}$.
Nous mobilisons le critère de Dirichlet (ou transformation d'Abel). La suite $\alpha_n = 1/n$ est à termes positifs, décroissante et tend vers zéro.
Il reste à borner les sommes partielles de l'exponentielle complexe. Soit $S_N = \sum_{k=1}^N e^{ik\theta}$. C'est une somme de termes d'une suite géométrique de raison $q = e^{i\theta} \neq 1$.
$$ S_N = e^{i\theta} \frac{1 - e^{iN\theta}}{1 - e^{i\theta}} $$
Majorons rigoureusement le module de $S_N$ :
$$ |S_N| = \left| e^{i\theta} \right| \cdot \frac{\left| 1 - e^{iN\theta} \right|}{\left| 1 - e^{i\theta} \right|} \leq 1 \cdot \frac{1 + \left| e^{iN\theta} \right|}{\left| 1 - e^{i\theta} \right|} = \frac{2}{\left| 1 - e^{i\theta} \right|} $$
Puisque $\theta \not\equiv 0 \pmod{2\pi}$, le dénominateur est non nul, la quantité $\frac{2}{|1 - e^{i\theta}|}$ est une constante fixée $M(\theta)$ indépendante de $N$. La suite des sommes partielles est formellement bornée.
Les hypothèses de la règle d'Abel-Dirichlet étant pleinement satisfaites, la série $\sum \frac{e^{in\theta}}{n}$ est convergente.
Conclusion : Sur le cercle unité $|z|=1$, la série diverge uniquement au pôle réel $z=1$, et converge conditionnellement (mais non absolument, car la série des modules est l'harmonique divergente) en tout autre point.

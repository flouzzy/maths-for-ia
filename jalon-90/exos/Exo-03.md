# Exercice 03

**Difficulté :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
(Le phénomène de la "bosse qui s'échappe").
Soit une suite de variables aléatoires $(Y_n)_{n \ge 1}$ vérifiant :
$$ \mathbb{P}(Y_n = \sqrt{n}) = \frac{1}{n} \quad \text{et} \quad \mathbb{P}(Y_n = 0) = 1 - \frac{1}{n} $$
1. Montrez que $Y_n \xrightarrow{\mathbb{P}} 0$.
2. Calculez $\mathbb{E}[|Y_n|^2]$ et déduisez-en si la suite converge dans $L^2(\Omega)$.

**Correction :**

**1. Convergence en probabilité :**
Nous devons évaluer $\mathbb{P}(|Y_n - 0| > \varepsilon)$ pour un $\varepsilon > 0$ fixé.
La variable $Y_n$ ne prend que les valeurs $0$ et $\sqrt{n}$.
Pour tout $\varepsilon > 0$, dès que $n$ est suffisamment grand pour que $\sqrt{n} > \varepsilon$ (c'est-à-dire $n > \varepsilon^2$), l'événement $\{|Y_n| > \varepsilon\}$ coïncide exactement avec l'événement $\{Y_n = \sqrt{n}\}$.
Ainsi, pour $n > \varepsilon^2$ :
$$ \mathbb{P}(|Y_n| > \varepsilon) = \mathbb{P}(Y_n = \sqrt{n}) = \frac{1}{n} $$
En passant à la limite lorsque $n \to \infty$ :
$$ \lim_{n \to \infty} \mathbb{P}(|Y_n| > \varepsilon) = \lim_{n \to \infty} \frac{1}{n} = 0 $$
La suite $(Y_n)$ converge donc en probabilité vers $0$.

**2. Étude de la convergence dans $L^2$ :**
Pour étudier la convergence dans l'espace de Hilbert $L^2$, nous devons analyser la limite de l'espérance quadratique $\mathbb{E}[|Y_n - 0|^2]$.
Calculons explicitement l'espérance du carré de $Y_n$ en appliquant la définition de l'espérance pour une variable discrète :
$$ \mathbb{E}[Y_n^2] = (\sqrt{n})^2 \cdot \mathbb{P}(Y_n = \sqrt{n}) + 0^2 \cdot \mathbb{P}(Y_n = 0) $$
$$ \mathbb{E}[Y_n^2] = n \cdot \frac{1}{n} + 0 = 1 $$
Nous observons que pour tout entier $n \ge 1$, $\mathbb{E}[Y_n^2] = 1$.
Par conséquent :
$$ \lim_{n \to \infty} \mathbb{E}[|Y_n - 0|^2] = \lim_{n \to \infty} 1 = 1 \neq 0 $$
La distance $L^2$ entre $Y_n$ et la limite prétendue $0$ ne tend pas vers zéro. La suite $(Y_n)$ **ne converge pas** dans $L^2(\Omega)$.

*Remarque géométrique :* Cet exemple est canonique. Bien que la "largeur" de la masse de probabilité déviante diminue (probabilité $1/n$ tendant vers $0$), la "hauteur" de cette masse (la pénalité quadratique de valeur $n$) augmente suffisamment rapidement pour compenser exactement la diminution de probabilité, empêchant la queue de distribution de s'évanouir en moyenne quadratique.

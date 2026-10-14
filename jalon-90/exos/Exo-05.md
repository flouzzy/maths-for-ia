\subsection*{Exercice 5 : Somme de variables convergentes \quad $\bigstar\bigstar\bigstar\star\star$}

Montrer que si $X_n \xrightarrow{\mathbb{P}} X$ et $Y_n \xrightarrow{\mathbb{P}} Y$, alors $X_n + Y_n \xrightarrow{\mathbb{P}} X + Y$.

**Correction :**
Soit $\varepsilon > 0$. Nous cherchons à évaluer $\mathbb{P}(|(X_n + Y_n) - (X + Y)| > \varepsilon)$.
D'après l'inégalité triangulaire :
$|(X_n + Y_n) - (X + Y)| = |(X_n - X) + (Y_n - Y)| \le |X_n - X| + |Y_n - Y|$.
Ainsi, si la somme $|X_n - X| + |Y_n - Y|$ est strictement supérieure à $\varepsilon$, alors l'un au moins des deux termes doit être strictement supérieur à $\varepsilon / 2$.
Ceci se traduit par l'inclusion d'événements suivante :
$\{|(X_n + Y_n) - (X + Y)| > \varepsilon\} \subset \{|X_n - X| > \varepsilon / 2\} \cup \{|Y_n - Y| > \varepsilon / 2\}$.
En utilisant la sous-additivité des probabilités :
$\mathbb{P}(|(X_n + Y_n) - (X + Y)| > \varepsilon) \le \mathbb{P}(|X_n - X| > \varepsilon / 2) + \mathbb{P}(|Y_n - Y| > \varepsilon / 2)$.
Puisque $X_n \xrightarrow{\mathbb{P}} X$ et $Y_n \xrightarrow{\mathbb{P}} Y$, on a :
$\lim_{n \to \infty} \mathbb{P}(|X_n - X| > \varepsilon / 2) = 0$ et $\lim_{n \to \infty} \mathbb{P}(|Y_n - Y| > \varepsilon / 2) = 0$.
Par somme de limites, le membre de droite tend vers 0, ce qui conclut la preuve par le théorème des gendarmes.
$X_n + Y_n \xrightarrow{\mathbb{P}} X + Y$.

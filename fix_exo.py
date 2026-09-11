# Fix Exo 04
f = "jalon-67/exos/Exo-04.md"
with open(f, "r") as file:
    content = file.read()
content = content.replace(
    r"Les $f_n$ sont continues (donc mesurables) et positives sur $\mathbb{R}^+$.",
    r"Les fonctions $x \mapsto (1 + \frac{x}{n})^n e^{-2x}$ sont continues, et $\mathbf{1}_{[0, n]}$ est étagée mesurable, donc les $f_n$ sont mesurables et positives sur $\mathbb{R}^+$."
)
with open(f, "w") as file:
    file.write(content)

# Fix Exo 10
f = "jalon-67/exos/Exo-10.md"
with open(f, "r") as file:
    content = file.read()
content = content.replace(
    r"Par définition, $T = \sum_{n=1}^\infty n \mathbf{1}_{\{T=n\}}$. Son espérance est $\mathbb{E}[T] = \int_{\Omega} T d\mathbb{P}$.",
    r"La variable aléatoire prend ses valeurs dans $\mathbb{N}^* \cup \{\infty\}$. On peut l'écrire sous la forme $T = \sum_{n=1}^\infty n \mathbf{1}_{\{T=n\}} + \infty \mathbf{1}_{\{T=\infty\}}$. Son espérance est $\mathbb{E}[T] = \int_{\Omega} T d\mathbb{P}$."
)
with open(f, "w") as file:
    file.write(content)

```yaml
title: "Le Théorème des Intervalles Emboîtés (Version Simplifiée)"
difficulty: 4
tags: [Intervalles Emboîtés, Axiome de la Borne Supérieure, Suite, Convergence, Nombres Réels]
```
## Énoncé de l'Exercice 09

Soit une suite d'intervalles fermés et bornés de nombres réels $(I_n)_{n \in \mathbb{N}}$, où chaque intervalle $I_n$ est de la forme $[a_n, b_n]$ avec $a_n, b_n \in \mathbb{R}$ et $a_n \le b_n$.

On suppose que cette suite satisfait les deux conditions suivantes :
1.  **Emboîtement** : Pour tout entier naturel $n \in \mathbb{N}$, l'intervalle $I_{n+1}$ est inclus dans l'intervalle $I_n$. Formellement, $\forall n \in \mathbb{N}, [a_{n+1}, b_{n+1}] \subseteq [a_n, b_n]$.
2.  **Longueurs tendant vers zéro** : La longueur des intervalles tend vers zéro lorsque $n$ tend vers l'infini. Formellement, $\lim_{n \to \infty} (b_n - a_n) = 0$.

Démontrer qu'il existe un unique nombre réel $c \in \mathbb{R}$ tel que l'intersection de tous les intervalles de la suite est le singleton $\{c\}$.
Formellement :
$$ \bigcap_{n \in \mathbb{N}} I_n = \{c\} $$

Votre démonstration doit utiliser l'axiome de la borne supérieure ainsi que la propriété d'Archimède (ou une de ses conséquences, comme la convergence des suites de Cauchy).

### Axiome de la Borne Supérieure Rappelé :

Tout sous-ensemble non vide de $\mathbb{R}$ qui est majoré admet une borne supérieure dans $\mathbb{R}$.

### Propriété d'Archimède Rappelée (ou une de ses conséquences) :

Pour tout nombre réel $\varepsilon > 0$, il existe un entier naturel $N \in \mathbb{N}$ tel que $1/N < \varepsilon$.

---
---
title: "Exo 03 : Non-universalité des activations polynomiales"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exo 03 : Non-universalité des activations polynomiales

## Énoncé formel
Démontrer algébriquement que si la fonction d'activation est le polynôme $\sigma(t) = t^2$, le réseau à une couche cachée ne peut pas approcher la fonction $\sin(x)$ sur $[-\pi, \pi]$ avec une précision arbitraire, quel que soit le nombre de neurones $N$.

---

## Démonstration et correction pas à pas
Considérons $\Sigma = \{ \sum_{i=1}^N \alpha_i \sigma(w_i x + b_i) \}$. Si $\sigma(t) = t^2$, alors $\sigma(w_i x + b_i) = w_i^2 x^2 + 2w_i b_i x + b_i^2$.\nChaque neurone calcule donc un polynôme de degré au plus 2. Une combinaison linéaire quelconque de tels polynômes, $\sum_{i=1}^N \alpha_i (w_i^2 x^2 + 2w_i b_i x + b_i^2)$, reste invariablement un polynôme de degré au maximum 2. \nAinsi, l'espace des fonctions générées par ce réseau, $\Sigma$, est exactement l'espace vectoriel des polynômes de degré $\le 2$, c'est-à-dire l'espace engendré par $\{1, x, x^2\}$.\n\nSupposons qu'il soit possible d'approcher $\sin(x)$ avec une erreur $\|\sin(x) - p(x)\|_{\infty} < \epsilon$ pour tout $\epsilon > 0$, où $p$ est de degré $\le 2$.\nLa fonction $\sin(x)$ possède 4 racines sur $[-\pi, \pi]$ (à savoir $-\pi, 0, \pi$). Cependant, un polynôme non nul de degré au plus 2 ne peut avoir plus de 2 racines. Par conséquent, il est topologiquement impossible qu'une limite uniforme d'un espace de dimension 3 de polynômes converge vers $\sin(x)$ (dont la dérivée 3ème n'est pas nulle, contrairement aux polynômes de degré 2). La distance minimale entre $\sin(x)$ et le sous-espace fermé des polynômes de degré $\le 2$ est strictement positive. Le réseau n'est donc pas un approximateur universel.

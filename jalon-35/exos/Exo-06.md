# Exercice 6 : ★★★

**Énoncé :**
Image réciproque d'un ouvert par une application continue.

**Correction (Zéro Ellipse) :**
Soient $E, F$ deux espaces normés et $f : E \to F$ une application continue. Montrer par caractérisation séquentielle que pour tout ouvert $V$ de $F$, $U = f^{-1}(V) = \{x \in E \mid f(x) \in V\}$ est un ouvert de $E$.

Soit $(x_n)_{n \in \mathbb{N}}$ une suite de $E$ convergeant vers $x \in U$.
Puisque $x \in f^{-1}(V)$, nous avons $f(x) \in V$.
L'application $f$ étant continue au point $x$, la convergence de la suite $x_n \to x$ implique la convergence des images : $f(x_n) \to f(x)$.
Posons $y_n = f(x_n)$ et $y = f(x)$. Nous avons donc une suite $(y_n)_{n \in \mathbb{N}}$ de $F$ convergeant vers $y \in V$.
Puisque $V$ est un ouvert de $F$, par caractérisation séquentielle, il existe un rang $N \in \mathbb{N}$ tel que pour tout $n \ge N$, $y_n \in V$.
Cela se réécrit : pour tout $n \ge N$, $f(x_n) \in V$.
Par définition de l'image réciproque, cela équivaut à : pour tout $n \ge N$, $x_n \in f^{-1}(V) = U$.
Nous avons prouvé qu'à partir d'un certain rang, les termes de la suite entrent définitivement dans $U$. Donc $f^{-1}(V)$ est ouvert. $\blacksquare$

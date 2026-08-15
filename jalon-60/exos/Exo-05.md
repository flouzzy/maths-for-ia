---
title: "Exo 05 : Continuité des opérateurs fonctionnels"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exo 05 : Continuité des opérateurs fonctionnels

## Énoncé formel
Considérons un sous-espace vectoriel $S \subset C([0,1])$. Démontrer que si $S$ est dense dans $C([0,1])$ pour la norme uniforme, alors pour toute forme linéaire continue $L \in C([0,1])^*$, si $L(f) = 0$ pour tout $f \in S$, alors nécessairement $L = 0$ (c'est le socle du théorème de Cybenko).

---

## Démonstration et correction pas à pas
Soit $L : C([0,1]) \to \mathbb{R}$ une forme linéaire continue. Par hypothèse de continuité topologique, pour toute fonction $f \in C([0,1])$ et toute suite $(f_n)_{n \ge 0} \subset C([0,1])$ telle que $\|f_n - f\|_\infty \to 0$, on a $\lim_{n \to \infty} L(f_n) = L(f)$.\n\nSupposons que $S$ est dense dans $C([0,1])$. Cela signifie que pour toute fonction $f \in C([0,1])$, il existe une suite $(f_n)_{n \ge 0}$ d'éléments de $S$ telle que $\lim_{n \to \infty} \|f_n - f\|_\infty = 0$.\n\nPar hypothèse, $L$ s'annule sur $S$. Donc pour chaque $n$, $f_n \in S \implies L(f_n) = 0$.\nEn combinant avec la continuité de $L$, on obtient :\n$$L(f) = L\left(\lim_{n \to \infty} f_n\right) = \lim_{n \to \infty} L(f_n) = \lim_{n \to \infty} 0 = 0$$\n\nPuisque ce résultat est vrai pour un $f$ quelconque de $C([0,1])$, l'opérateur $L$ envoie toute fonction de l'espace sur $0$. Par conséquent, l'opérateur est nul, $L = 0$. C'est le théorème de Hahn-Banach sous-jacent qui affirme réciproquement que si $S$ n'était pas dense, une telle forme linéaire non nulle existerait.

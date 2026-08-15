---
title: "Exo 04 : Approximation par réseaux ReLU"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exo 04 : Approximation par réseaux ReLU

## Énoncé formel
Soit la fonction d'activation ReLU définie par $\sigma(x) = \max(0, x)$. Construire explicitement avec des neurones ReLU une fonction 'chapeau' $h(x)$ telle que $h(x) = 0$ pour $x \le -1$ et $x \ge 1$, et $h(0) = 1$, de manière affine par morceaux.

---

## Démonstration et correction pas à pas
Pour construire la fonction chapeau, analysons les pentes successives. La fonction $h(x)$ vérifie :\n- De $-\infty$ à $-1$, la pente est $0$.\n- De $-1$ à $0$, la pente passe de $0$ à $1$. L'incrément de pente est de $+1$ en $x = -1$.\n- De $0$ à $1$, la pente passe de $1$ à $-1$. L'incrément de pente est de $-2$ en $x = 0$.\n- De $1$ à $+\infty$, la pente repasse à $0$. L'incrément de pente est de $+1$ en $x = 1$.\n\nLa fonction ReLU $\sigma(x)$ est exactement le mécanisme permettant d'introduire un incrément de pente de $+1$ au point $x=0$. Par translation, $\sigma(x - c)$ introduit un incrément de pente de $+1$ au point $c$.\nEn cumulant ces incréments de pente, nous formons la combinaison linéaire suivante :\n$$h(x) = \sigma(x + 1) - 2\sigma(x) + \sigma(x - 1)$$\n\nVérifions cela :\n- Pour $x \le -1$ : toutes les ReLU sont nulles, $h(x) = 0$.\n- Pour $x \in [-1, 0]$ : $x+1 > 0$ mais les autres arguments sont $\le 0$. Ainsi $h(x) = (x+1) - 0 + 0 = x+1$. À $x=0$, $h(0) = 1$.\n- Pour $x \in [0, 1]$ : $x+1 > 0$, $x > 0$, mais $x-1 \le 0$. Ainsi $h(x) = (x+1) - 2(x) = 1 - x$. À $x=1$, $h(1) = 0$.\n- Pour $x \ge 1$ : tous les arguments sont $> 0$. $h(x) = (x+1) - 2x + (x-1) = 0$.\n\nNous avons donc construit algébriquement une fonction chapeau (fonction affine par morceaux à support compact) en utilisant 3 neurones ReLU dans une seule couche cachée.

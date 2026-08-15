---
title: "Exo 10 : Équivalence de la séparabilité de Hahn-Banach"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exo 10 : Équivalence de la séparabilité de Hahn-Banach

## Énoncé formel
Dans la preuve du théorème de l'approximation universelle, l'utilisation du théorème de Hahn-Banach est l'étape cardinale. Redémontrez explicitement le fait suivant : Dans un espace normé $E$, si $F$ est un sous-espace fermé de $E$ et $x_0 \notin F$, il existe une forme linéaire continue $L \in E^*$ telle que $L_{|F} = 0$ et $L(x_0) = \delta > 0$, où $\delta = d(x_0, F)$.

---

## Démonstration et correction pas à pas
Ce théorème de séparation géométrique découle directement de la forme analytique de Hahn-Banach. Posons $E = C(K, \mathbb{R})$. Soit $F = \overline{\Sigma_n(\sigma)}$ l'adhérence de l'espace généré par le réseau de neurones. Par hypothèse $x_0 \notin F$ et puisque $F$ est fermé, la distance $\delta = \inf_{y \in F} \|x_0 - y\|$ est strictement positive.\nConsidérons le sous-espace $G$ engendré par $F$ et $x_0$, c'est-à-dire $G = F \oplus \mathbb{R}x_0$. Tout élément de $G$ s'écrit de manière unique $z = y + t x_0$ avec $y \in F$ et $t \in \mathbb{R}$.\nDéfinissons une forme linéaire locale $f_0$ sur $G$ par $f_0(y + t x_0) = t \delta$.\nPour montrer que $f_0$ est continue sur $G$, il faut évaluer sa norme subordonnée. Si $t=0$, $f_0(y)=0$. Si $t \neq 0$ :\n$$ \|y + t x_0\| = |t| \| \frac{y}{t} + x_0 \| $$\nComme $-y/t \in F$, on a $\|x_0 - (-y/t)\| \ge d(x_0, F) = \delta$.\nDonc $\|y + t x_0\| \ge |t| \delta = |f_0(y + t x_0)|$. Ceci montre que pour tout $z \in G$, $|f_0(z)| \le 1 \cdot \|z\|$, donc $f_0$ est une forme linéaire bornée de norme $\|f_0\| \le 1$ sur le sous-espace $G$.\nPar le théorème de Hahn-Banach, cette fonctionnelle linéaire $f_0$ continue sur le sous-espace $G$ peut être prolongée en une forme linéaire continue $L$ sur tout l'espace $E$, sans augmentation de la norme (donc $\|L\| = \|f_0\| \le 1$).\nPar construction de ce prolongement, nous avons bien $L(y) = 0$ pour tout $y \in F$ (puisqu'ici $t=0$), et $L(x_0) = 1 \cdot \delta = \delta > 0$. \nAinsi, c'est cette forme $L$ qui est envoyée par le théorème de représentation de Riesz sur la mesure $\mu$, annulant l'intégrale du réseau de neurones et permettant de boucler la preuve par l'absurde d'universalité.
